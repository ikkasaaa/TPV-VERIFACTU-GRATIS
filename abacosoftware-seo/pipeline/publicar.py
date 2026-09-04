#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escribir una pagina sin machacar una viva del cliente sin querer.

Los generadores hacian open(..., "w") a pelo. El pipeline trabaja sobre el
arbol real de la web, asi que dar de alta una clave en SECTORES_* con el nombre
de una pagina que ya existe la sobrescribe entera y en silencio. Y las paginas
de sector mas flojas, que son justo las que se quieren mejorar, son paginas
vivas del cliente: el fallo estaba apuntando a lo que mas dolia.

Ya paso una vez en el otro dominio, donde casi se llevo por delante
'descargar-tpv-gratis.html', que es la pagina de descargas. Alli se arreglo
desviando a _propuestas/. Aqui faltaba.

Sobrescribir una pagina viva no es malo: hace falta, es como se profundiza una
pagina floja. Lo que no puede es pasar sin que nadie lo haya dicho. Asi que la
regla es que la sustitucion se declara:

    SECTORES = {
      "negocio_libreria.asp": {..., "sustituye": True},   # la mejoro a sabiendas
      "negocio_kiosko.asp":   {...},                      # pagina nueva
    }

Y con eso, cuatro casos:

    no existe                        -> se escribe.                  nueva
    existe y la hizo el pipeline     -> se reescribe.                regenerada
    existe, es del cliente, declarada-> se reescribe.                sustituida
    existe, es del cliente, sin decir-> va a _propuestas/ y se avisa. propuesta

Como se sabe cual hizo el pipeline: por el manifiesto '_generadas.txt' que se
lleva en el propio directorio de salida. Se penso primero en marcar el HTML con
un comentario, y es mala idea: estas paginas son ASP clasico y '<%@ LANGUAGE %>'
tiene que ir en la primerisima linea del fichero. Cualquier cosa delante lo
rompe. El manifiesto no toca los bytes de ninguna pagina.
"""
import os

MANIFIESTO = "_generadas.txt"
PROPUESTAS = "_propuestas"


def _manifiesto(out):
    p = os.path.join(out, MANIFIESTO)
    if not os.path.exists(p):
        return set()
    with open(p, encoding="utf-8") as fh:
        # Las lineas de '#' son la cabecera explicativa. Sin saltarlas, cada
        # pasada las leia como si fueran nombres de pagina y las volvia a
        # escribir debajo de la cabecera nueva, duplicandola sin parar.
        return {l.strip() for l in fh if l.strip() and not l.startswith("#")}


def _anotar(out, fichero):
    ya = _manifiesto(out)
    if fichero in ya:
        return
    ya.add(fichero)
    with open(os.path.join(out, MANIFIESTO), "w", encoding="utf-8") as fh:
        fh.write("# Paginas que ha creado el pipeline. No editar a mano.\n")
        fh.write("# Sirve para distinguirlas de las vivas del cliente y no\n")
        fh.write("# sobrescribir estas ultimas sin haberlo declarado.\n")
        for f in sorted(ya):
            fh.write(f + "\n")


def publicar(out, fichero, html, sustituye=False):
    """Escribe la pagina donde toque. Devuelve el estado, uno de cuatro."""
    destino = os.path.join(out, fichero)
    nuestras = _manifiesto(out)

    if not os.path.exists(destino):
        estado = "nueva"
    elif fichero in nuestras:
        estado = "regenerada"
    elif sustituye:
        estado = "sustituida"
    else:
        estado = "propuesta"

    if estado == "propuesta":
        # No se toca la viva. La propuesta se deja al lado para comparar.
        destino = os.path.join(out, PROPUESTAS, fichero)

    os.makedirs(os.path.dirname(destino) or ".", exist_ok=True)
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write(html)
    if estado != "propuesta":
        _anotar(out, fichero)
    return estado


class Cuenta:
    """Lleva la cuenta y avisa al final. Un print por pagina no lo lee nadie."""

    def __init__(self):
        self.estados = {}

    def __call__(self, out, fichero, html, sustituye=False):
        e = publicar(out, fichero, html, sustituye)
        self.estados.setdefault(e, []).append(fichero)
        return e

    def total(self):
        return sum(len(v) for v in self.estados.values())

    def resumen(self, prefijo="  "):
        L = []
        for e in ("nueva", "regenerada", "sustituida", "propuesta"):
            if self.estados.get(e):
                L.append("%s%-11s %d" % (prefijo, e + ":", len(self.estados[e])))
        prop = self.estados.get("propuesta") or []
        if prop:
            L.append("")
            L.append("%s!! %d pagina(s) ya existen en la web viva y no se han tocado."
                     % (prefijo, len(prop)))
            L.append("%s   La version nueva esta en %s/. Si la sustitucion es"
                     % (prefijo, PROPUESTAS))
            L.append("%s   querida, pon \"sustituye\": True en su ficha de contenido."
                     % prefijo)
            for f in prop:
                L.append("%s     %s" % (prefijo, f))
        return "\n".join(L)

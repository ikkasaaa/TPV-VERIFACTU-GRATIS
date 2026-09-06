#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorta los <title> que Google cortaria en la SERP (>65 caracteres).

Se ejecuta al final del pipeline, despues de que todos los generadores hayan
escrito sus paginas. Mantiene og:title y twitter:title sincronizados.

El recorte por palabras deja a veces la frase colgando de una preposicion o un
articulo ("... sin Cerrar al"). Esa comprobacion es la parte que de verdad
importa: un titulo cortado a mitad se ve peor que uno largo.
"""
import os, re

import sitio, marcado as M

OUT = sitio.salida()
MAX = 65
MIN = 22

SUFIJOS = (" | Caja 5", " | Ábaco Software", " | Abaco Software", " - Caja 5", " | Caja5")
COLGANTE = re.compile(r"\b(al|el|la|lo|los|las|de|del|en|con|sin|por|para|y|o|a|un|una|"
                      r"que|su|sus|es|se|te|le|mi|tu|más|mas|como|desde|hasta|entre)$", re.I)
# Finales que parecen colgantes y no lo son: "explicado una a una" acaba en
# articulo, pero es una locucion entera. Sin esto, cada build avisaba de un
# colgante que no existia.
LOCUCIONES = ("una a una", "uno a uno", "paso a paso", "cara a cara")


def colgante(t):
    return bool(COLGANTE.search(t)) and not t.lower().endswith(LOCUCIONES)

# titulos que el recorte automatico deja mal y se resuelven a mano
MANUALES = {
    "como-hacer-un-inventario-tienda.asp": "Cómo Hacer el Inventario de una Tienda sin Cerrar",
    "guia-abrir-tienda-de-ropa.asp": "Cómo Abrir una Tienda de Ropa en España: Guía y TPV",
    "impresoras-tickets-y-lectores-compatibles.asp": "Impresoras y Lectores Compatibles con Caja 5",
    "ley-antifraude-tpv.asp": "Ley Antifraude 11/2021 en el Software TPV",
    "alternativa-tpv-suscripcion.asp": "Alternativa Española al TPV por Suscripción",
    "app_etiquetas_ql5.asp": "Etiquetas con Código de Barras: App QL5",
}


def acortar(t):
    """Devuelve un titulo <=65 car. sin cortar a mitad de idea."""
    if len(t) <= MAX:
        return t
    # 1) quitar el sufijo de marca
    for s in SUFIJOS:
        if len(t) > MAX and t.endswith(s):
            t = t[: -len(s)].rstrip(" |-·")
    # 2) quedarse con la primera parte antes de un separador fuerte
    if len(t) > MAX:
        for sep in (" | ", " · ", " - "):
            if sep in t:
                cand = t.split(sep)[0].strip()
                if MIN < len(cand) <= MAX:
                    return cand
    # 3) podar enumeraciones "A, B y C" -> "A"
    if len(t) > MAX:
        m = re.match(r"^(.*?),\s*[^,]+\s+y\s+[^,]+$", t)
        if m and MIN < len(m.group(1)) <= MAX:
            t = m.group(1)
    # 4) cortar por palabra y limpiar finales colgantes
    while len(t) > MAX and " " in t:
        t = t[: t.rfind(" ")].rstrip(" ,;:|-·")
    while colgante(t) and " " in t:
        t = t[: t.rfind(" ")].rstrip(" ,;:|-·")
    return t


def main():
    n = colgantes = 0
    largos = []
    for f in sitio.paginas(OUT):
        b = os.path.basename(f)
        s = M.leer(f)
        t = M.titulo(s)
        if not t:
            continue
        nuevo = MANUALES.get(b) or (acortar(t) if len(t) > MAX else t)
        if nuevo != t and MIN <= len(nuevo) <= MAX:
            M.escribir(f, M.poner_title(s, nuevo))
            t = nuevo
            n += 1
        # verificacion sobre lo que queda escrito
        if len(t) > MAX:
            largos.append(b)
        if colgante(t):
            colgantes += 1
    print(f"titulos recortados: {n} | quedan >{MAX}: {len(largos)} | finales colgantes: {colgantes}")
    if largos:
        print("  revisar a mano:", ", ".join(largos[:6]))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Encuentra ficheros que no deberian estar publicados en la web.

Uso: python3 limpieza_raiz.py <dir-web> [--aplicar] [--bloquear]

Sin --aplicar solo informa. Con --aplicar los mueve a _retirados/ dentro del
mismo directorio, para que se puedan recuperar si alguno hacia falta.

Con --bloquear anade ademas al web.config una regla que devuelve 404 para cada
uno. Hace falta porque retirarlos del ZIP no los borra del servidor: el cliente
sube la web y los que ya estaban siguen ahi, servibles, hasta que alguien entre
por FTP. El web.config viaja con la subida, asi que el bloqueo entra solo. Es un
parche, no el arreglo: al final hay que borrarlos, y por eso el informe termina
con la lista de lo que hay que borrar a mano.

Que busca y por que:

  COPIA      Ficheros de respaldo dejados al lado del original ("Copia de X",
             "X - 09-10-2023", "XNO"). IIS protege 'global.asa' por su nombre
             exacto; una copia llamada 'Copia de global.asa' NO esta protegida
             y su codigo VBScript se puede servir como texto plano.
  BINARIO    Ejecutables sueltos. En un dominio cuyo negocio es "descarga
             nuestro programa", un .exe que nadie anuncia es justo lo que
             marcan los antivirus y la reputacion del navegador.
  ESCRITORIO Accesos directos de Windows (.lnk) subidos por error.
  PRUEBA     Restos de comprobaciones ("test.txt" con 'hello world').
  CARPETA    Directorios enteros de respaldo ("archivojs/copias/"). Recorre el
             arbol completo, no solo la raiz: la primera version de este script
             solo miraba el directorio de arriba y se dejo una carpeta entera.

Ninguno de estos ficheros aparece enlazado desde el sitio, asi que retirarlos
no rompe ninguna ruta. Aun asi el script lo comprueba antes de mover nada.
"""
import os, re, shutil, sys

REGLAS = [
    # Ojo con el sufijo "NO": sin distinguir mayusculas, 'NO\.asp' casa con
    # 'negocio_segunda_maNO.asp', que es una pagina real. Lo que separa el
    # descarte del contenido son las mayusculas, asi que esa regla va aparte,
    # sin el (?i), y distingue 'medNO.asp' de 'mano.asp'.
    ("COPIA",      re.compile(r"(?i)(^copia de |^copy of |_old\b|\.bak$|"
                              r"\d{2}-\d{2}-\d{4}|~$)")),
    ("COPIA",      re.compile(r"NO\.(asp|html)$")),
    ("BINARIO",    re.compile(r"(?i)\.(exe|msi|bat|cmd|dll|zip|rar)$")),
    ("ESCRITORIO", re.compile(r"(?i)\.(lnk|url|ini)$")),
    # "prueba_gratis.css" no es un resto de desarrollo: "prueba gratis" es como
    # se llama el producto en castellano. La regla lo excluye a proposito.
    ("PRUEBA",     re.compile(r"(?i)^(test|prueba|tmp|temp)(?!_?grat)[._-]?")),
]

DIR_RESPALDO = re.compile(r"(?i)^(copias?|backups?|old|bak|tmp|temp|pruebas?)$")

# Lo que si debe seguir publicado aunque encaje en una regla.
SALVAR = {"global.asa", "web.config", "robots.txt", "sitemap.xml"}


def clasificar(nombre):
    if nombre in SALVAR:
        return None
    for etiqueta, pat in REGLAS:
        if pat.search(nombre):
            return etiqueta
    return None


def enlazado(rel, base):
    """¿Alguna pagina del sitio enlaza a esto? Si lo hace, no se toca.

    Para un directorio se busca la RUTA ('archivojs/copias'), no el nombre
    suelto: 'copias' sale en el texto corriente de cualquier web en castellano
    y daba un falso positivo desde una pagina que hablaba de copias de
    seguridad.
    """
    es_dir = rel.endswith("/")
    nombre = rel.rstrip("/").replace(os.sep, "/") if es_dir \
        else os.path.basename(rel.rstrip("/"))
    aguja = nombre.replace(" ", "%20")
    for raiz, dirs, ficheros in os.walk(base):
        dirs[:] = [d for d in dirs if d != "_retirados"]
        for f in ficheros:
            ruta = os.path.join(raiz, f)
            if os.path.relpath(ruta, base) == rel:
                continue      # nombrarse a si mismo no es un enlace entrante
            if not f.lower().endswith((".asp", ".html", ".htm", ".css", ".js")):
                continue
            try:
                s = open(ruta, encoding="latin-1").read()
            except OSError:
                continue
            if nombre in s or aguja in s:
                return os.path.relpath(ruta, base)
    return None


_ESPECIALES = set(r".^$*+?()[]{}|\\")


def _patron(ruta, es_dir=False):
    """Patron de IIS para una ruta. No vale re.escape: el motor no es Python.

    Dos cosas que re.escape hacia mal aqui, y las dos se veian en el fichero
    que mas importa de todos:

    - El espacio. re.escape lo dejaba como '\\ ', pero el navegador pide
      'Copia%20de%20global.asa', no 'Copia de global.asa'. La regla no habria
      disparado nunca, justo en el unico fichero del lote que expone codigo.
      Se acepta cualquiera de las dos formas.
    - El directorio. '^archivojs/copias$' bloquea la carpeta y deja servible
      todo lo de dentro, que es lo que se queria bloquear. Se le anade el
      subarbol.
    """
    fuera = []
    for c in ruta:
        if c == " ":
            fuera.append("(?: |%20)")
        elif c in _ESPECIALES:
            fuera.append("\\" + c)
        else:
            fuera.append(c)
    return "^" + "".join(fuera) + ("(?:/.*)?$" if es_dir else "$")


def reglas_bloqueo(rutas):
    """Reglas de IIS que devuelven 404 para cada ruta. Devuelve (xml, cuantas).

    Retirar un fichero del ZIP no lo borra del servidor: el cliente sube la web
    y los que ya estaban siguen ahi, servibles, hasta que alguien entre por FTP
    y los borre a mano. Estas reglas viajan dentro del web.config, o sea con la
    propia subida, y cierran el acceso sin depender de que nadie haga nada.

    Va por ruta exacta y NO por extension, y esa decision tiene una razon con
    nombre: la demo del producto es 'eutpv.exe' y esta enlazada desde todas las
    paginas. Un '<add fileExtension=".exe" allowed="false" />' habria devuelto
    404 en el boton de descargar, que es la conversion principal del sitio.
    """
    fuera = []
    for rel in sorted(rutas):
        es_dir = rel.endswith("/")
        ruta = rel.rstrip("/").replace(os.sep, "/")
        patron = _patron(ruta, es_dir)
        fuera.append("""
                <rule name="404 %s" stopProcessing="true">
                    <match url="%s" />
                    <action type="CustomResponse" statusCode="404"
                            statusReason="Not Found" statusDescription="Not Found" />
                </rule>""" % (ruta, patron))
    return "".join(fuera), len(fuera)


def bloquear(base, rutas):
    """Mete las reglas en el web.config. Idempotente por regla."""
    p = os.path.join(base, "web.config")
    if not os.path.exists(p):
        print("  no hay web.config en", base, "- no se puede bloquear")
        return 0
    with open(p, encoding="utf-8", errors="replace") as fh:
        s = fh.read()
    nuevas = [r for r in rutas
              if 'name="404 %s"' % r.rstrip("/").replace(os.sep, "/") not in s]
    if not nuevas:
        return 0
    xml, n = reglas_bloqueo(nuevas)
    if "<rules>" not in s:
        print("  el web.config no tiene <rules>: no se toca")
        return 0
    s = s.replace("<rules>", "<rules>" + xml, 1)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(s)
    return n


def escanear(base):
    hallazgos = []
    for raiz, dirs, ficheros in os.walk(base):
        dirs[:] = [d for d in dirs if d != "_retirados"]
        for d in sorted(dirs):
            if DIR_RESPALDO.match(d):
                rel = os.path.relpath(os.path.join(raiz, d), base)
                n_f = sum(len(f) for _, _, f in os.walk(os.path.join(raiz, d)))
                hallazgos.append(("CARPETA", rel + "/", n_f))
        for n in sorted(ficheros):
            rel = os.path.relpath(os.path.join(raiz, n), base)
            # lo que ya cae dentro de una carpeta de respaldo no se cuenta dos veces
            if any(DIR_RESPALDO.match(p) for p in rel.split(os.sep)[:-1]):
                continue
            et = clasificar(n)
            if et:
                hallazgos.append((et, rel, os.path.getsize(os.path.join(raiz, n))))
    return hallazgos


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    aplicar = "--aplicar" in sys.argv
    con_bloqueo = "--bloquear" in sys.argv

    hallazgos = escanear(base)
    if not hallazgos:
        print("  la raiz esta limpia")
        return 0

    print(f"  ficheros que no deberian estar publicados: {len(hallazgos)}\n")
    movidos = 0
    sueltos = []
    for et, n, tam in hallazgos:
        ref = enlazado(n, base)
        print(f"   {et:10} {n}   ({tam} bytes)")
        if ref:
            print(f"              enlazado desde {ref}: NO se toca")
            continue
        sueltos.append(n)
        if aplicar:
            destino = os.path.join(base, "_retirados", os.path.dirname(n))
            os.makedirs(destino, exist_ok=True)
            shutil.move(os.path.join(base, n.rstrip("/")),
                        os.path.join(destino, os.path.basename(n.rstrip("/"))))
            movidos += 1

    if aplicar:
        print(f"\n  movidos a _retirados/: {movidos}")
    else:
        print("\n  (informe solamente; usa --aplicar para retirarlos)")

    if con_bloqueo:
        print(f"  reglas 404 anadidas al web.config: {bloquear(base, sueltos)}")
    else:
        print("  (usa --bloquear para cerrarlos tambien en el servidor)")

    # Retirarlos del ZIP no los borra de produccion, y el bloqueo tampoco: solo
    # los hace inalcanzables. Alguien tiene que entrar por FTP.
    if sueltos:
        print("\n  BORRAR A MANO EN EL SERVIDOR (el ZIP no los borra):")
        for n in sueltos:
            print("   ", n)
    return 0


if __name__ == "__main__":
    sys.exit(main())

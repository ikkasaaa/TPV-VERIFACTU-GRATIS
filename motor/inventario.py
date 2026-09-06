#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrae el inventario de un sitio a un TSV: slug, titulo, H1, palabras.

Uso: python3 inventario.py <dir-web> <etiqueta-sitio> > inventario.tsv

Existe porque el arbol construido de abacosoftware vive en un directorio
temporal que desaparece al cerrar la sesion. El TSV que genera esto si se
guarda en el repositorio, y es lo que consume el agrupador de keywords.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate, marcado as M                               # noqa: E402

CABECERA = "sitio\tslug\ttitulo\th1\tpalabras"


def fila(sitio, ruta):
    s = M.leer(ruta)
    # el tabulador y el salto de linea rompen el TSV; un titulo puede llevar cualquier cosa
    limpio = lambda x: x.replace("\t", " ").replace("\n", " ")
    return "\t".join((sitio, os.path.basename(ruta), limpio(M.titulo(s)), limpio(M.h1(s)),
                      str(len(M.texto_visible(s).split()))))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    base = sys.argv[1]
    sitio = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(base.rstrip("/"))
    print(CABECERA)
    for f in gate.paginas(base):
        try:
            print(fila(sitio, f))
        except OSError:
            continue
    return 0


if __name__ == "__main__":
    sys.exit(main())

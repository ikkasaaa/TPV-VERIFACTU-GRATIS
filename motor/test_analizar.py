#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas de la lectura de keywords e inventarios."""
import os, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analizar_clusters as A                            # noqa: E402
from prueba import Suite, correr                         # noqa: E402

S = Suite("analizar_clusters")


def fichero(texto, suf=".csv"):
    p = tempfile.mktemp(suffix=suf)
    open(p, "w", encoding="utf-8").write(texto)
    return p


@S.caso("numero entiende millares y decimales en formato español e ingles")
def _():
    casos = {"1.234": 1234, "1.234,5": 1234.5, "12,3": 12.3, "12.3": 12.3, "1,234": 1234,
             "2.800": 2800, "5%": 5, " 7 ": 7, "1.234.567": 1234567, "0,45": 0.45, "": None,
             "n/a": None}
    for txt, esperado in casos.items():
        assert A.numero(txt) == esperado, f"{txt!r} -> {A.numero(txt)!r}, esperaba {esperado!r}"


@S.caso("una exportacion de Search Console en español se lee con sus metricas")
def _():
    p = fichero("Consulta;Clics;Impresiones;CTR;Posición media\n"
                "software tpv madrid;12;2.800;0,43%;8,4\n"
                "tpv zapateria;3;150;2%;12,1\n")
    kws = A.leer_keywords(p)
    assert [k for k, _ in kws] == ["software tpv madrid", "tpv zapateria"], kws
    assert kws[0][1]["impresiones"] == 2800 and kws[0][1]["posicion"] == 8.4, kws[0][1]


@S.caso("una lista a pelo sin cabecera se lee entera, primera linea incluida")
def _():
    p = fichero("tpv floristeria\ntpv mascotas\n", ".txt")
    assert [k for k, _ in A.leer_keywords(p)] == ["tpv floristeria", "tpv mascotas"]


@S.caso("un fichero con BOM y tabuladores (Semrush) tambien se lee")
def _():
    p = fichero("﻿Keyword\tVolume\tKeyword Difficulty\nverifactu gratis\t2900\t12\n", ".tsv")
    kws = A.leer_keywords(p)
    assert kws == [("verifactu gratis", {"volumen": 2900, "dificultad": 12})], kws


@S.caso("modo keywords encuentra el hueco de Madrid y no lo tapa con la pagina de instrumentos")
def _():
    inv = fichero("sitio\tslug\ttitulo\th1\tpalabras\n"
                  "c5\ttpv-instrumentos-musica-madrid.html\tTPV Instrumentos Música Madrid\t\t\n"
                  "c5\ttpv-zapateria.html\tTPV para Zapaterías\t\t\n", ".tsv")
    kw = fichero("query,impressions\nsoftware tpv madrid,2800\ntpv zapateria tallas,90\n")
    filas = A.cruzar(A.leer_keywords(kw), A.leer_inventarios([inv]))
    estados = {sorted(g)[0]: len(casan) for _, g, casan, _ in filas}
    assert estados["software tpv madrid"] == 0, estados
    assert estados["tpv zapateria tallas"] == 1, estados


if __name__ == "__main__":
    sys.exit(correr(S))

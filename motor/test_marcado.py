#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas de lectura y escritura de marcado."""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import marcado as M                                      # noqa: E402
from prueba import Suite, correr                         # noqa: E402

S = Suite("marcado")

PAGINA = """<%
Response.CharSet = "utf-8"
%>
<html><head>
<title>Zapater&iacute;as &amp; Calzado
   | Caja 5</title>
<meta name="description" content="Una descripci&oacute;n">
<meta property="og:title" content="Viejo">
<meta name="twitter:title" content='Viejo'>
<link rel="canonical" href="https://www.ejemplo.com/z.asp">
<style>h1{color:red}</style>
<script type="application/ld+json">{"@type": "FAQPage", "mainEntity": []}</script>
<script type="application/ld+json">{esto no es json}</script>
</head><body>
<!--#include virtual="/menu_nav.asp"-->
<h1 class="hero">Zapater&iacute;as <span>con tallas</span></h1>
<p>Texto   visible.</p>
<script>var oculto = "no visible";</script>
</body></html>"""


@S.caso("el titulo sale en texto plano, con entidades resueltas y sin saltos")
def _():
    assert M.titulo(PAGINA) == "Zapaterías & Calzado | Caja 5", M.titulo(PAGINA)


@S.caso("el H1 se lee sin etiquetas interiores y se cuenta sin confundirlo con CSS")
def _():
    assert M.h1(PAGINA) == "Zapaterías con tallas", M.h1(PAGINA)
    assert M.h1s(PAGINA) == 1, "el h1{} del <style> no es un encabezado"
    assert M.h1s(PAGINA + "<h1>Otro</h1>") == 2


@S.caso("meta y canonical se leen con comillas dobles o simples")
def _():
    assert M.meta(PAGINA, "description") == "Una descripción"
    assert M.meta(PAGINA, "twitter:title") == "Viejo"
    assert M.canonical(PAGINA) == "https://www.ejemplo.com/z.asp"


@S.caso("texto_visible ignora ASP, script, style, comentarios y etiquetas")
def _():
    t = M.texto_visible(PAGINA)
    assert "texto visible." in t and "zapaterías con tallas" in t, t
    assert "oculto" not in t and "charset" not in t and "menu_nav" not in t, t
    assert "color:red" not in t


@S.caso("poner_title cambia el <title> y sus espejos og/twitter, y nada mas")
def _():
    s = M.poner_title(PAGINA, "Nuevo")
    assert M.titulo(s) == "Nuevo"
    assert M.meta(s, "og:title") == "Nuevo" and M.meta(s, "twitter:title") == "Nuevo"
    assert M.meta(s, "description") == "Una descripción", "ha tocado la description"
    assert s.count("<title>") == 1


@S.caso("poner_meta no inventa una meta que no existe")
def _():
    assert M.poner_meta(PAGINA, "og:description", "x") == PAGINA


@S.caso("bloques_ld devuelve None para el JSON roto en vez de reventar")
def _():
    bl = M.bloques_ld(PAGINA)
    assert len(bl) == 2 and bl[0][2]["@type"] == "FAQPage" and bl[1][2] is None


@S.caso("breadcrumb_ld construye URLs absolutas sin barras dobles")
def _():
    ld = M.breadcrumb_ld([("Inicio", "/"), ("Sectores", "/tpv_negocios.asp"), ("Z", "z.asp")],
                         "https://www.ejemplo.com/")
    items = [i["item"] for i in ld["itemListElement"]]
    assert items == ["https://www.ejemplo.com/", "https://www.ejemplo.com/tpv_negocios.asp",
                     "https://www.ejemplo.com/z.asp"], items


@S.caso("ld() sangra todas las lineas con el prefijo pedido")
def _():
    b = M.ld({"a": 1}, sangria="\t")
    assert all(l.startswith("\t") for l in b.splitlines()), b


@S.caso("esc escapa lo justo para un atributo")
def _():
    assert M.esc('a "b" & <c>') == "a &quot;b&quot; &amp; &lt;c&gt;"


if __name__ == "__main__":
    sys.exit(correr(S))

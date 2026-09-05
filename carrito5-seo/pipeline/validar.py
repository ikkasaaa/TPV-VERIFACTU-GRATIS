#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoria de las paginas generadas de carrito5.com.

Uso: python3 validar.py <dir-salida> [<fichero-urls-vivas>]

Comprueba, por pagina: title (25-60 caracteres para que Google no lo corte),
description (hasta 155), un solo H1, canonical, OpenGraph, JSON-LD que parsea,
FAQPage coherente con las FAQ visibles, y que cada enlace interno apunte a una
pagina generada o a una URL viva del inventario. Ademas busca restos de
escritura de IA (rayas em) y el dato falso del «50 tickets al mes».

Sale con codigo 1 si hay errores. Los avisos (title largo, description larga)
no hacen fallar: se listan para revisarlos.
"""
import glob, html, json, os, re, sys

ERRORES, AVISOS = [], []


def err(f, m):
    ERRORES.append(f"  !! {os.path.basename(f)}: {m}")


def aviso(f, m):
    AVISOS.append(f"  ?  {os.path.basename(f)}: {m}")


def vivas(fichero):
    if not fichero or not os.path.exists(fichero):
        return set()
    return {re.sub(r"^https?://(www\.)?carrito5\.com/", "", l.strip())
            for l in open(fichero, encoding="utf-8") if l.strip()}


def texto_visible(s):
    t = re.sub(r"<script.*?</script>", "", s, flags=re.S | re.I)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S | re.I)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def validar(f, existentes):
    s = open(f, encoding="utf-8").read()
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    t = html.unescape(t.group(1)).strip() if t else ""
    if not t:
        err(f, "sin <title>")
    elif len(t) > 60:
        aviso(f, f"title de {len(t)} caracteres: «{t}»")
    elif len(t) < 25:
        aviso(f, f"title corto ({len(t)})")

    d = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
    d = html.unescape(d.group(1)).strip() if d else ""
    if not d:
        err(f, "sin description")
    elif len(d) > 155:
        aviso(f, f"description de {len(d)} caracteres")

    if len(re.findall(r"<h1\b", s, re.I)) != 1:
        err(f, f"{len(re.findall(r'<h1', s, re.I))} H1")
    if 'rel="canonical"' not in s:
        err(f, "sin canonical")
    if 'property="og:title"' not in s:
        err(f, "sin OpenGraph")

    tipos = []
    for m in re.findall(r'<script type="application/ld\+json">\n(.*?)\n</script>', s, re.S):
        try:
            o = json.loads(m)
            tipos.append(o.get("@type"))
        except json.JSONDecodeError as e:
            err(f, f"JSON-LD invalido: {e}")
    if "BreadcrumbList" not in tipos:
        err(f, "sin BreadcrumbList")
    if "Organization" not in tipos:
        err(f, "sin Organization (@id estable para GEO)")

    # FAQ visibles = FAQ del schema
    faq_vis = len(re.findall(r'<div class="c5-faq">', s))
    faq_ld = 0
    for m in re.findall(r'<script type="application/ld\+json">\n(.*?)\n</script>', s, re.S):
        try:
            o = json.loads(m)
            if o.get("@type") == "FAQPage":
                faq_ld = len(o.get("mainEntity", []))
        except json.JSONDecodeError:
            pass
    if faq_vis != faq_ld:
        err(f, f"FAQ visibles {faq_vis} != FAQ en schema {faq_ld}")

    # enlaces internos
    for h in re.findall(r'href="([^"#]+)"', s):
        if h.startswith(("http", "mailto:", "tel:", "//")):
            continue
        if h.endswith((".css", ".js", ".png", ".jpg", ".svg", ".ico", ".webp")):
            continue
        destino = h.split("?")[0].lstrip("/")
        if destino in ("",):
            continue
        if destino not in existentes and "blog/" + destino not in existentes:
            err(f, f"enlace a pagina inexistente: {destino}")

    vis = texto_visible(s)
    if "—" in vis:
        err(f, f"{vis.count('—')} rayas em en el texto visible")
    if re.search(r"50\s+(tickets|al mes)", vis):
        err(f, "dato falso del plan gratuito: 50 tickets al mes")
    palabras = len(vis.split())
    if palabras < 600:
        aviso(f, f"solo {palabras} palabras visibles")
    return palabras


def main():
    if len(sys.argv) < 2:
        print("uso: validar.py <dir-salida> [<fichero-urls-vivas>]")
        return 2
    salida = sys.argv[1]
    vivas_f = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inventario", "urls_descubiertas.txt")
    ficheros = sorted(glob.glob(os.path.join(salida, "*.html"))
                      + [f for f in glob.glob(os.path.join(salida, "blog", "*.html"))
                         if not os.path.basename(f).startswith("_")])
    existentes = vivas(vivas_f) | {"index.html", "blog.html"}
    for f in ficheros:
        rel = os.path.relpath(f, salida).replace(os.sep, "/")
        existentes.add(rel)
        existentes.add(os.path.basename(f))
    total = 0
    for f in ficheros:
        total += validar(f, existentes)
    print(f"  paginas validadas : {len(ficheros)}")
    print(f"  palabras visibles : {total:,}".replace(",", "."))
    print(f"  errores           : {len(ERRORES)}")
    print(f"  avisos            : {len(AVISOS)}")
    for l in ERRORES + AVISOS:
        print(l)
    return 1 if ERRORES else 0


if __name__ == "__main__":
    sys.exit(main())

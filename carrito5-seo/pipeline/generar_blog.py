#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador del blog de carrito5.com.

Uso: python3 generar_blog.py <dir-salida> [<modulo> ...]

Sin modulos, carga todos los contenido/blog_*.py. Cada modulo expone un dict
en mayusculas {slug: dict(...)} con los campos que pide plantilla_blog.articulo.

Escribe:
  <dir-salida>/blog/<slug>.html            un fichero por post
  <dir-salida>/blog/calendario-editorial.tsv  fecha, slug, titulo, para
  <dir-salida>/blog/_indice-fragmento.html    tarjetas para pegar en blog.html

El filtro anti-plantilla del motor compara los posts entre si y contra las
paginas ya generadas en <dir-salida>. Un post que se parezca demasiado a otro
no se escribe.
"""
import glob, importlib, os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))), "motor"))

import plantilla_blog as B   # noqa: E402
import gate                  # noqa: E402


def construir(slug, d):
    return B.articulo(
        slug=slug, title=d["title"], description=d["desc"], keywords=d["kw"],
        h1=d["h1"], sub=d["sub"], publicado=d["publicado"], para=d["para"],
        resumen=d.get("resumen"), cuerpo=d["cuerpo"], cierre=d["cierre"],
        faqs=d.get("faqs", []), faq_titulo=d.get("faq_titulo", "Preguntas que nos hacen sobre esto"),
        relacionadas=d.get("relacionadas", []), modificado=d.get("modificado"))


def main():
    if len(sys.argv) < 2:
        print("uso: generar_blog.py <dir-salida> [<modulo>...]")
        return 2
    out = sys.argv[1]
    mods = sys.argv[2:]
    if not mods:
        base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "contenido")
        mods = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(base, "blog_*.py")))

    todo = {}
    for m in mods:
        mod = importlib.import_module(f"contenido.{m}")
        for attr in dir(mod):
            v = getattr(mod, attr)
            if attr.isupper() and isinstance(v, dict) and not attr.startswith("_"):
                for slug, d in v.items():
                    if slug in todo:
                        print(f"  !! slug repetido: {slug} ({m})")
                    todo[slug] = d

    bdir = os.path.join(out, "blog")
    os.makedirs(bdir, exist_ok=True)
    paginas = {f"{slug}.html": construir(slug, d) for slug, d in todo.items()}

    previas = glob.glob(os.path.join(out, "*.html")) + [
        p for p in glob.glob(os.path.join(bdir, "*.html")) if os.path.basename(p) not in paginas]
    malos = gate.filtrar(paginas, previas)

    n = 0
    for f, html_ in paginas.items():
        if f in malos:
            continue
        open(os.path.join(bdir, f), "w", encoding="utf-8").write(html_)
        n += 1

    # calendario e indice, en orden de publicacion
    orden = sorted(todo.items(), key=lambda kv: kv[1]["publicado"])
    with open(os.path.join(bdir, "calendario-editorial.tsv"), "w", encoding="utf-8") as fh:
        fh.write("publicar\tslug\ttitulo\tpara\n")
        for slug, d in orden:
            fh.write(f"{d['publicado']}\tblog/{slug}.html\t{d['title']}\t{d['para']}\n")
    with open(os.path.join(bdir, "_indice-fragmento.html"), "w", encoding="utf-8") as fh:
        fh.write("<!-- Tarjetas para blog.html, de mas reciente a mas antiguo -->\n")
        for slug, d in reversed(orden):
            fh.write(f'<a href="/blog/{slug}.html" class="c5-satellite-card">{d["h1"]}'
                     f'<small>{B.P.fecha_legible(d["publicado"])} &middot; {d["para"]}</small></a>\n')

    print(f"  posts escritos {n} / {len(paginas)}   rechazados {len(malos)}")
    print(f"  calendario: {orden[0][1]['publicado']} a {orden[-1][1]['publicado']}" if orden else "")
    return 0


if __name__ == "__main__":
    sys.exit(main())

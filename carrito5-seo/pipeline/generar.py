#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador de paginas de carrito5.com.

Uso: python3 generar.py <dir-salida> <modulo> [<modulo> ...]

Cada modulo de contenido/ expone dicts en mayusculas {fichero: datos}. Dos
filtros deciden que llega al disco:

  1. Lo que YA EXISTE en la web viva no se sobrescribe: va a _propuestas/ para
     que el cliente compare. La lista de paginas vivas sale del inventario
     (inventario/urls_descubiertas.txt), no de una lista escrita a mano que se
     queda vieja: hubo un intento que iba a machacar descargar-tpv-gratis.html,
     la pagina de descargas, porque nadie la habia apuntado.
  2. El filtro de similitud del motor: lo que se parezca demasiado a otra
     pagina, nueva o ya publicada, no se escribe.
"""
import glob, importlib, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))       # carrito5-seo/
sys.path.insert(0, RAIZ)
sys.path.insert(0, os.path.join(os.path.dirname(RAIZ), "motor"))
import gate, plantilla as P                                               # noqa: E402

INVENTARIO = os.path.join(RAIZ, "inventario", "urls_descubiertas.txt")
# Paginas vivas que el inventario (reconstruido desde el buscador, un suelo) no
# recoge pero de las que hay constancia directa.
VIVAS_EXTRA = {"descargar-tpv-gratis.html", "sectores-y-negocios.html",
               "software-tpv-comercio-local.html", "verifactu-gratis.html",
               "index.html", "tpv-tienda-ropa.html", "tpv-zapateria.html"}


def vivas():
    """Nombres de fichero de la raiz de carrito5.com que existen hoy."""
    out = set(VIVAS_EXTRA)
    if os.path.exists(INVENTARIO):
        for l in open(INVENTARIO, encoding="utf-8"):
            ruta = l.strip().split("carrito5.com/", 1)[-1]
            if ruta and "/" not in ruta:
                out.add(ruta)
    return out


def cargar(modulos):
    todo = {}
    for m in modulos:
        mod = importlib.import_module(f"contenido.{m}")
        for attr in dir(mod):
            v = getattr(mod, attr)
            if attr.isupper() and isinstance(v, dict) and not attr.startswith("_"):
                todo.update(v)
    return todo


def construir(fichero, d):
    return P.pagina(
        fichero=fichero,
        title=d["title"], description=d["desc"], keywords=d["kw"],
        h1=d["h1"], sub=d["sub"], badge=d["badge"], trail=d["trail"],
        bloques=d["bloques"], faqs=d["faqs"],
        faq_titulo=d.get("faq_titulo", f"Preguntas frecuentes sobre {d['crumb'].lower()}"),
        aside=d["aside"], satelites=d.get("satelites", []), cta=d["cta"],
        extra_ld=d.get("extra_ld"))


def main():
    if len(sys.argv) < 3:
        print("uso: generar.py <dir-salida> <modulo>...")
        return 2
    out, mods = sys.argv[1], sys.argv[2:]
    os.makedirs(out, exist_ok=True)
    paginas = {f: construir(f, d) for f, d in cargar(mods).items()}

    existen = vivas()
    propuestas = {f: h for f, h in paginas.items() if f in existen}
    paginas = {f: h for f, h in paginas.items() if f not in existen}
    if propuestas:
        pdir = os.path.join(out, "_propuestas")
        os.makedirs(pdir, exist_ok=True)
        for f, h in propuestas.items():
            open(os.path.join(pdir, f), "w", encoding="utf-8").write(h)
        print(f"  {len(propuestas)} propuestas en _propuestas/ (esas paginas ya existen en la web viva):")
        print("   ", ", ".join(sorted(propuestas)))

    previas = [p for p in glob.glob(os.path.join(out, "*.html")) if os.path.basename(p) not in paginas]
    malos = gate.filtrar(paginas, previas)
    for f, html in paginas.items():
        if f not in malos:
            open(os.path.join(out, f), "w", encoding="utf-8").write(html)
    print(f"  publicadas {len(paginas) - len(malos)} / {len(paginas)}   rechazadas {len(malos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

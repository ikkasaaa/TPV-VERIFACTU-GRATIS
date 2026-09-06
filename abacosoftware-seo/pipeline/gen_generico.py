#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador generico para paginas escritas a mano, con filtro de similitud.

Uso: python3 gen_generico.py <modulo> [<modulo> ...]

Cada modulo de contenido/ expone un dict cuyo nombre empieza por uno de los
prefijos de HUBS (ABRIR_1, OPERATIVA_2, NORMATIVA_1...). El prefijo decide el
hub del que cuelga la pagina y el texto de la tarjeta lateral.
"""
import glob, importlib, os, sys

import sitio, gate, maqueta as Q, plantilla as P

OUT = "site"

HUBS = {
    "ABRIR": ("Abrir un negocio", "/abrir-un-negocio.asp",
              ("Empieza con el catálogo montado",
               "Te ayudamos a dar de alta tu catálogo inicial antes de abrir, para que el primer ticket ya salga con todo bajo control.")),
    "OPERATIVA": ("Operativa diaria del TPV", "/operativa-tpv.asp",
                  ("Pruébalo con tu propio catálogo",
                   "La demo es completa y no pide tarjeta. Media hora con tus artículos reales te dice más que cualquier folleto.")),
    "NORMATIVA": ("Normativa y obligaciones", "/normativa-comercio.asp",
                  ("Caja 5 ya está adaptado",
                   "Facturas simplificadas con QR reglamentario y registro encadenado. Licencia de 333 € en pago único.")),
}
PIE = (f"<strong>{sitio.PRECIO} pago único</strong> para PC. Sin cuota obligatoria ni comisión por venta. "
       f"<strong>{sitio.TEL}</strong>.")
CTA = ("¿Hablamos de tu caso?",
       "Llámanos antes de comprar nada. Te decimos qué necesitas de verdad y qué te puedes ahorrar.")


def construir(fichero, d, hub_nom, hub_url, aside):
    return P.pagina(
        fichero=fichero,
        title=d["title"][:65], description=d["desc"][:165], keywords=d["kw"],
        h1=d["h1"], subtitulo=d["sub"],
        badge=f'<i class="fa-solid {d["icono"]}"></i> {d["crumb"].upper()}',
        trail=[("Inicio", "/"), (hub_nom, hub_url), (d["crumb"], "/" + fichero)],
        cuerpo=Q.dos_columnas(Q.bloques(d["bloques"]), Q.aside(*aside, Q.boton_wa(), PIE)),
        faqs=d["faqs"], faq_titulo=d.get("faq_titulo", f"Preguntas frecuentes sobre {d['nom']}"),
        cta=d.get("cta", CTA), links=d["rel"])


def cargar(modulos):
    """{fichero: datos} de todos los modulos, y el prefijo de hub del ultimo."""
    todo, prefijo = {}, "ABRIR"
    for m in modulos:
        mod = importlib.import_module(m)
        for a in dir(mod):
            if a.split("_")[0] in HUBS:
                prefijo = a.split("_")[0]
                todo.update(getattr(mod, a))
    return todo, prefijo


def main():
    mods = sys.argv[1:]
    if not mods:
        print("uso: gen_generico.py <modulo>...")
        return 2
    todo, prefijo = cargar(mods)
    hub_nom, hub_url, aside = HUBS[prefijo]
    paginas = {f: construir(f, d, hub_nom, hub_url, aside) for f, d in todo.items()}

    # filtro de similitud: entre las nuevas y contra lo ya publicado del mismo cluster
    pat = "abrir-*.asp" if prefijo == "ABRIR" else "*.asp"
    previas = [f for f in glob.glob(os.path.join(OUT, pat)) if os.path.basename(f) not in paginas]
    malos = gate.filtrar(paginas, previas)

    for f, html in paginas.items():
        if f not in malos:
            open(os.path.join(OUT, f), "w", encoding="utf-8").write(html)
    print(f"\n  publicadas {len(paginas) - len(malos)} / {len(paginas)}   rechazadas {len(malos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las paginas de sector a partir de los modulos contenido/sectores_N.py.

Uso: python3 gen_sectores.py <dir-salida> [<modulo> ...]   (por defecto sectores_1)

La maqueta es comun, como en cualquier web; la prosa de cada pagina esta
escrita para su sector y no se comparte entre paginas.
"""
import importlib, os, sys

import sitio, maqueta as Q, plantilla as P

OUT = sitio.salida()
MODULOS = sys.argv[2:] or ["sectores_1"]

ASIDE = ("Pruébalo con tu catálogo",
         "La demo es completa y no pide tarjeta. Mete veinte referencias reales de tu tienda y comprueba si te encaja antes de pagar nada.")
PIE = (f"<strong>{sitio.PRECIO} pago único</strong> para PC, sin cuota obligatoria ni comisión por venta. "
       f"O llámanos al <strong>{sitio.TEL}</strong>.")
WA_MSG = "Hola,%20pregunto%20por%20el%20TPV%20para%20mi%20tienda"


def construir(fichero, d):
    return P.pagina(
        fichero=fichero, title=d["title"], description=d["desc"], keywords=d["kw"],
        h1=d["h1"], subtitulo=d["sub"],
        badge=f'<i class="fa-solid {d["icono"]}"></i> ESPECIALIZADO EN {d["nombre"].upper()}',
        trail=[("Inicio", "/"), ("Sectores y negocios", "/tpv_negocios.asp"), (d["crumb"], "/" + fichero)],
        cuerpo=Q.dos_columnas(Q.bloques(d["bloques"]),
                              Q.aside(*ASIDE, Q.boton_wa(mensaje=WA_MSG), PIE)),
        faqs=d["faqs"], faq_titulo=f"Preguntas frecuentes sobre el TPV para {d['nombre'].lower()}",
        cta=(f"¿Te encaja para tu {d['crumb'].lower().rstrip('s')}?",
             "Descarga la demo y pruébala con tus propias referencias. Si vemos que no te sirve, te lo diremos."),
        links=d["rel"])


def main():
    total = 0
    for mod in MODULOS:
        m = importlib.import_module(mod)
        data = next((getattr(m, a) for a in dir(m) if a.startswith("SECTORES")), None)
        if not data:
            print("  !! sin datos en", mod)
            continue
        for fichero, d in data.items():
            open(os.path.join(OUT, fichero), "w", encoding="utf-8").write(construir(fichero, d))
        total += len(data)
        print(f"  {mod}: {len(data)} paginas")
    print("total generadas:", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())

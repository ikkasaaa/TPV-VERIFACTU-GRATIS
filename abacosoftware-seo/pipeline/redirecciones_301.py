#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Redirecciones 301 de paginas canibalizadas. GENERADO por canibalizacion.py.

No editar a mano: se regenera. Para cambiar una decision, cambia el criterio
en canibalizacion.py y vuelve a ejecutarlo, para que quede razonado.

Solo estan aqui los grupos SEGURO, donde los slugs son variantes del mismo y no
hay juicio editorial que hacer. Los REVISAR, SEPARAR y CRUZADO se quedan fuera a
proposito: ver informes/canibalizacion.txt.
"""

# origen -> destino
REDIRECCIONES = {
    "guia-abrir-tienda-de-ropa.asp":               "abrir-tienda-de-ropa.asp",
    "index.html":                                  "index.asp",
    "negocio_antiguedad.asp":                      "negocio_antiguedades.asp",
    "negocio_souvenirs_tienda.asp":                "negocio_souvenirs.asp",
    "tpv_consultas_desde_web_med.asp":             "tpv_consultas_desde_web.asp",
}

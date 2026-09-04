#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Redirecciones 301 de paginas canibalizadas. GENERADO por canibalizacion.py.

No editar a mano: se regenera. Para cambiar una decision, cambia el criterio
en canibalizacion.py y vuelve a ejecutarlo, para que quede razonado.

Aqui hay dos cosas y solo dos:

  - Los grupos SEGURO, donde los slugs son variantes del mismo y no hay juicio
    editorial que hacer.
  - Los RESCATES: URLs que existieron y hoy dan 404.

Los REVISAR, TITULO, SEPARAR y CRUZADO se quedan fuera a proposito. Entre dos
paginas que responden 200 las dos no se redirige: eso se resuelve
diferenciandolas, con enlazado interno contextual y con su canonical. Ver
informes/canibalizacion.txt.
"""

# origen -> destino
REDIRECCIONES = {
    "guia-abrir-tienda-de-ropa.asp":               "abrir-tienda-de-ropa.asp",
    "index.html":                                  "index.asp",
    "negocio_antiguedad.asp":                      "negocio_antiguedades.asp",
    "negocio_souvenirs_tienda.asp":                "negocio_souvenirs.asp",
    "prueba_gratis.asp":                           "tpv_pedir_caja5_gratis.asp",
    "tpv_consultas_desde_web_med.asp":             "tpv_consultas_desde_web.asp",
}

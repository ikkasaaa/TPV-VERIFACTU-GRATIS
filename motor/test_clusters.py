#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas del agrupador. Cada caso salio de un fallo real.

Uso: python3 test_clusters.py        (o python3 test.py para todas las suites)
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import clusters as C                                    # noqa: E402
from prueba import Suite, correr                        # noqa: E402

S = Suite("clusters")


def agrupa(textos):
    """Devuelve el conjunto de grupos como conjuntos de claves."""
    grupos, _ = C.agrupar({str(i): t for i, t in enumerate(textos)})
    return [{int(k) for k in g} for g in grupos]


def juntos(textos, a, b):
    return any({a, b} <= g for g in agrupa(textos))


@S.caso("el par singular/plural de instrumentos es duplicado y debe agruparse")
def _():
    t = ["tpv-tienda-instrumentos-musica.html Software TPV para Tiendas de Instrumentos de Música",
         "tpv-tiendas-instrumentos-musica.html Software TPV Gratis para Tiendas de Instrumentos Musica | Carr…",
         "tpv-floristeria.html TPV para Floristerías"]
    assert juntos(t, 0, 1), "no agrupa el singular/plural"
    assert not juntos(t, 0, 2), "agrupa instrumentos con floristeria"


@S.caso("dos competidores distintos NO son el mismo grupo")
def _():
    t = ["catinfog-vs-caja5.asp Catinfog vs Caja5: alternativa y comparativa",
         "gesio-vs-caja5.asp Gesio vs Caja5: alternativa y comparativa",
         "glop-vs-caja5.asp Glop vs Caja5: alternativa y comparativa"]
    assert not juntos(t, 0, 1), "junta Catinfog con Gesio"


@S.caso("la coletilla de marca no une paginas de sectores distintos")
def _():
    t = ["tpv-floristeria.html TPV Floristeria Gratis | Carrito5 Software VeriFactu",
         "tpv-tienda-mascotas.html TPV Tienda Mascotas Gratis | Carrito5 Software VeriFactu",
         "tpv-tienda-deportes.html TPV Tienda Deportes Gratis | Carrito5 Software VeriFactu"]
    assert not juntos(t, 0, 1), "une floristeria con mascotas por la marca"


@S.caso("el tramo util tras la barra SI cuenta")
def _():
    assert C.sin_marca(
        "Software TPV para Tiendas de Ropa y Moda | Gestión de Tallas y Colores"
    ).endswith("Colores"), "se ha comido contenido real"


@S.caso("colapsar sinonimos no puede borrar el tema fiscal")
def _():
    # 16 paginas de verifactu entre 130: si la frecuencia se midiera despues de
    # aplicar familias, "verifactu" saldria como generica y desapareceria.
    t = [f"verifactu-{i}.asp VeriFactu tema {i}" for i in range(16)]
    t += [f"negocio_{i}.asp Sector numero {i}" for i in range(114)]
    assert "verifactu" not in C.genericas(t), "verifactu se ha marcado como generica"


@S.caso("fruteria y carniceria son negocios distintos")
def _():
    t = ["negocio_fruteria.asp TPV para fruterias", "negocio_carniceria.asp TPV para carnicerias"]
    assert not juntos(t, 0, 1), "fusiona dos sectores de alimentacion distintos"


@S.caso("zapateria y calzado son lo mismo")
def _():
    t = ["tpv-zapateria.html TPV para zapaterias con tallas",
         "programa-calzado.html Programa para tiendas de calzado con tallas"]
    assert juntos(t, 0, 1), "no reconoce zapateria = calzado"


@S.caso("una pagina mas especifica NO cubre una busqueda generica")
def _():
    kw = C.nucleo("software tpv madrid")
    especifica = C.nucleo("tpv-instrumentos-musica-madrid.html TPV Instrumentos Música Madrid")
    assert not C.cubre(kw, especifica), "la pagina de instrumentos tapa el hueco de Madrid"


@S.caso("una pagina general SI cubre una busqueda de cola larga")
def _():
    kw = C.nucleo("tpv zapateria tallas anchas")
    general = C.nucleo("tpv-zapateria.html TPV para Zapaterías")
    assert C.cubre(kw, general), "la pagina general no cubre su cola larga"


@S.caso("el detalle comercial del titulo no acota el tema de la pagina")
def _():
    # El tema sale del slug. Si se mezclara el titulo, "Gestion de Tallas y
    # Colores" contaria como acotacion y la pagina dejaria de cubrir su propia
    # busqueda principal.
    kw = C.nucleo("tpv tienda de ropa")
    assert C.cubre(kw, C.nucleo("tpv-tienda-ropa.html")), "la pagina de ropa no cubre 'tpv tienda de ropa'"
    con_titulo = C.nucleo("tpv-tienda-ropa.html Software TPV para Tiendas de "
                          "Ropa y Moda | Gestion de Tallas y Colores")
    assert not C.cubre(kw, con_titulo), \
        "el caso que motivo separar slug de titulo ya no se reproduce"


@S.caso("la etiqueta de un grupo no cae en 'generico' porque su primer miembro este vacio")
def _():
    # Antes: `a or b if c else d` se leia como `(a or b) if c else d`, y un
    # grupo cuyo primer nucleo estuviera vacio salia como "generico" aunque el
    # resto de miembros compartieran palabras.
    nuc = {"a": frozenset(), "b": frozenset({"joyeria"}), "c": frozenset({"joyeria"})}
    assert C.etiqueta(["a", "b", "c"], nuc) == "joyeria", C.etiqueta(["a", "b", "c"], nuc)
    assert C.etiqueta(["a"], nuc) == "generico"


if __name__ == "__main__":
    sys.exit(correr(S))

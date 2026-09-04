#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas del agrupador. Cada caso salio de un fallo real de esta sesion.

Uso: python3 test_clusters.py
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import clusters as C


def agrupa(textos):
    """Devuelve el conjunto de grupos como conjuntos de claves."""
    items = {str(i): t for i, t in enumerate(textos)}
    grupos, _ = C.agrupar(items)
    return [{int(k) for k in g} for g in grupos]


def juntos(textos, a, b):
    return any({a, b} <= g for g in agrupa(textos))


CASOS = []


def caso(nombre):
    def deco(f):
        CASOS.append((nombre, f))
        return f
    return deco


@caso("el par singular/plural de instrumentos es duplicado y debe agruparse")
def _():
    t = ["tpv-tienda-instrumentos-musica.html Software TPV para Tiendas de Instrumentos de Música",
         "tpv-tiendas-instrumentos-musica.html Software TPV Gratis para Tiendas de Instrumentos Musica | Carr…",
         "tpv-floristeria.html TPV para Floristerías"]
    assert juntos(t, 0, 1), "no agrupa el singular/plural"
    assert not juntos(t, 0, 2), "agrupa instrumentos con floristeria"


@caso("dos competidores distintos NO son el mismo grupo")
def _():
    t = ["catinfog-vs-caja5.asp Catinfog vs Caja5: alternativa y comparativa",
         "gesio-vs-caja5.asp Gesio vs Caja5: alternativa y comparativa",
         "glop-vs-caja5.asp Glop vs Caja5: alternativa y comparativa"]
    assert not juntos(t, 0, 1), "junta Catinfog con Gesio"


@caso("la coletilla de marca no une paginas de sectores distintos")
def _():
    t = ["tpv-floristeria.html TPV Floristeria Gratis | Carrito5 Software VeriFactu",
         "tpv-tienda-mascotas.html TPV Tienda Mascotas Gratis | Carrito5 Software VeriFactu",
         "tpv-tienda-deportes.html TPV Tienda Deportes Gratis | Carrito5 Software VeriFactu"]
    assert not juntos(t, 0, 1), "une floristeria con mascotas por la marca"


@caso("el tramo util tras la barra SI cuenta")
def _():
    assert C.sin_marca(
        "Software TPV para Tiendas de Ropa y Moda | Gestión de Tallas y Colores"
    ).endswith("Colores"), "se ha comido contenido real"


@caso("colapsar sinonimos no puede borrar el tema fiscal")
def _():
    # 16 paginas de verifactu entre 130: si la frecuencia se midiera despues de
    # aplicar familias, "verifactu" saldria como generica y desapareceria.
    t = [f"verifactu-{i}.asp VeriFactu tema {i}" for i in range(16)]
    t += [f"negocio_{i}.asp Sector numero {i}" for i in range(114)]
    ex = C.genericas(t)
    assert "verifactu" not in ex, "verifactu se ha marcado como generica"


@caso("fruteria y carniceria son negocios distintos")
def _():
    t = ["negocio_fruteria.asp TPV para fruterias", "negocio_carniceria.asp TPV para carnicerias"]
    assert not juntos(t, 0, 1), "fusiona dos sectores de alimentacion distintos"


@caso("zapateria y calzado son lo mismo")
def _():
    t = ["tpv-zapateria.html TPV para zapaterias con tallas",
         "programa-calzado.html Programa para tiendas de calzado con tallas"]
    assert juntos(t, 0, 1), "no reconoce zapateria = calzado"


@caso("una pagina mas especifica NO cubre una busqueda generica")
def _():
    kw = C.nucleo("software tpv madrid")
    especifica = C.nucleo("tpv-instrumentos-musica-madrid.html TPV Instrumentos Música Madrid")
    assert not C.cubre(kw, especifica), "la pagina de instrumentos tapa el hueco de Madrid"


@caso("una pagina general SI cubre una busqueda de cola larga")
def _():
    kw = C.nucleo("tpv zapateria tallas anchas")
    general = C.nucleo("tpv-zapateria.html TPV para Zapaterías")
    assert C.cubre(kw, general), "la pagina general no cubre su cola larga"


@caso("el detalle comercial del titulo no acota el tema de la pagina")
def _():
    # El tema sale del slug. Si se mezclara el titulo, "Gestion de Tallas y
    # Colores" contaria como acotacion y la pagina dejaria de cubrir su propia
    # busqueda principal.
    kw = C.nucleo("tpv tienda de ropa")
    slug = C.nucleo("tpv-tienda-ropa.html")
    assert C.cubre(kw, slug), "la pagina de ropa no cubre 'tpv tienda de ropa'"
    con_titulo = C.nucleo("tpv-tienda-ropa.html Software TPV para Tiendas de "
                          "Ropa y Moda | Gestion de Tallas y Colores")
    assert not C.cubre(kw, con_titulo), \
        "el caso que motivo separar slug de titulo ya no se reproduce"

@caso("dos dominios sobre el mismo negocio se agrupan pese al titulo largo")
def _():
    # La prueba de arriba fija el principio; esta fija que modo_paginas lo
    # cumple, que es donde no se cumplia. El titulo de abaco anade "arreglos de
    # ropa", y pegado al slug bajaba el parecido de 1,000 a 0,333, por debajo
    # del umbral: el informe no veia competir a dos paginas del mismo dueno
    # sobre el mismo negocio. Salio de tres casos reales comprobados en Google.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import analizar_clusters as A
    paginas = [
        ("abacosoftware", "negocio_lavanderia.asp",
         "Software TPV para Lavanderias, Tintorerias y Arreglos de Ropa"),
        ("carrito5", "tpv-lavanderia-tintoreria.html",
         "TPV para lavanderia y tintoreria | Carrito5"),
    ]
    grupos, _ = C.agrupar(A.items_de_paginas(paginas))
    assert len(grupos) == 1, \
        "las dos paginas de lavanderia no se agrupan: el titulo vuelve a acotar"


@caso("la union recupera lo que cada criterio por separado deja fuera")
def _():
    # Ninguno de los dos criterios ve todo, y fallan por lados distintos:
    #
    #   solo el slug lo ve   lavanderia: los slugs coinciden, pero al titulo de
    #                        abaco le sobran "arreglos" y "ropa" y lo separan.
    #   solo el titulo lo ve colchoneria/muebles: los slugs no comparten nada,
    #                        pero llevan el MISMO titulo, escrito por una
    #                        persona, que es la senal mas dura que hay.
    #
    # Medido sobre los inventarios reales: el slug solo gana 42 paginas y
    # pierde 12. Por eso la lista buena es la union.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import analizar_clusters as A
    mismo = "Software TPV para Mueblerias, Colchonerias y Decoracion"
    paginas = [
        ("abacosoftware", "negocio_lavanderia.asp",
         "Software TPV para Lavanderias, Tintorerias y Arreglos de Ropa"),
        ("carrito5", "tpv-lavanderia-tintoreria.html", "TPV lavanderia"),
        ("abacosoftware", "negocio_colchoneria.asp", mismo),
        ("abacosoftware", "negocio_muebles.asp", mismo),
    ]

    def pares(grupos):
        return {frozenset(g) for g in grupos if len(g) > 1}

    por_slug, _ = C.agrupar(A.items_de_paginas(paginas))
    por_tit, _ = C.agrupar({f"{s}|{sl}": f"{sl} {C.sin_marca(ti)}"
                            for s, sl, ti in paginas})
    unidos = pares(C.unir(por_slug, por_tit))

    assert len(pares(por_slug)) == 1, "el caso ya no distingue: el slug ve %d pares" % len(pares(por_slug))
    assert len(pares(por_tit)) == 1, "el caso ya no distingue: el titulo ve %d pares" % len(pares(por_tit))
    assert pares(por_slug) != pares(por_tit), "los dos criterios ven el mismo par"
    assert unidos == pares(por_slug) | pares(por_tit), \
        "la union no recupera los dos pares: %s" % sorted(map(sorted, unidos))


def main():
    fallos = 0
    for nombre, f in CASOS:
        try:
            f()
            print(f"   ok  {nombre}")
        except AssertionError as e:
            fallos += 1
            print(f"   !!  {nombre}\n         {e}")
    print(f"\n  {len(CASOS) - fallos} / {len(CASOS)} pasan")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
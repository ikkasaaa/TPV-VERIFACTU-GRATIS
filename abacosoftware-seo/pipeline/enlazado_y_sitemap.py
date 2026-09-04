#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Malla de enlazado interno, sitemap y redirecciones 301."""
import re, os, sys, glob, datetime, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from redirecciones_301 import REDIRECCIONES
except ImportError:                  # aun no se ha corrido canibalizacion.py
    REDIRECCIONES = {"index.html": "index.asp",
                     "negocio_antiguedad.asp": "negocio_antiguedades.asp"}

OUT = sys.argv[1] if len(sys.argv) > 1 else "site"
BASE = "https://www.abacosoftware.com"
HOY = datetime.date.today().isoformat()

NUEVOS_HUBS = [
    ("/funciones-tpv.asp", "Funciones del TPV", "fa-list-check",
     "Matriz de tallas, stock, fidelización, vales y rebajas"),
    ("/comparativas-tpv.asp", "Comparativas de TPV", "fa-scale-balanced",
     "Caja 5 frente a Stockagile, Glop, SimplyGest, Square…"),
    ("/hardware-tpv-compatible.asp", "Hardware compatible", "fa-plug",
     "Impresora, lector, cajón y equipo: qué comprar"),
    ("/preguntas-frecuentes-tpv.asp", "Preguntas frecuentes", "fa-circle-question",
     "Precio, VeriFactu, migración y soporte sin marketing"),
    ("/normativa-comercio.asp", "Normativa del comercio", "fa-scale-balanced",
     "VeriFactu, ticketBAI, factura electrónica y sanciones"),
    ("/abrir-un-negocio.asp", "Cómo abrir un negocio", "fa-store",
     "Guías por sector: inversión, trámites y errores"),
    ("/operativa-tpv.asp", "Operativa diaria del TPV", "fa-list-check",
     "Devoluciones, precios, cierres, informes"),
]

# Enlaces contextuales: sector -> paginas de funcion que de verdad usa ese oficio.
#
# Antes habia once sectores aqui y los otros ochenta y ocho caian en GENERICO, o
# sea que recibian los tres mismos enlaces. Dos problemas, y el segundo es peor:
#
#   1. Ochenta y ocho paginas con el bloque identico son una plantilla, y este
#      bloque va al pie de la pagina de sector, donde mas se nota.
#   2. GENERICO encabeza con "matriz de tallas y colores", que es de ropa y
#      calzado. Una fruteria, una ferreteria o una cerrajeria lo recibian igual,
#      enlazando a una funcion que su lector no usa.
#
# Y hay una razon de fondo: cuando dos paginas compiten por la misma busqueda,
# el enlazado contextual es una de las dos formas de diferenciarlas sin
# redirigir ninguna. Si las dos reciben los mismos tres enlaces, se parecen mas,
# no menos. Por eso los pares que salen en informes/canibalizacion.txt llevan
# aqui juegos distintos a proposito: animales/petshop, colchoneria/muebles,
# complementos/decoracion, cosmetica/perfumeria, instrumentos/musica,
# infantil/puericultura, lenceria/merceria y calzado/calzado_infantil.
POR_SECTOR = {
    # --- ropa, calzado y complementos: talla y color mandan
    "moda": ["matriz-tallas-y-colores", "rebajas-y-promociones-tpv", "vales-y-tarjetas-regalo-tpv"],
    "calzado": ["matriz-tallas-y-colores", "control-de-stock-multialmacen", "rebajas-y-promociones-tpv"],
    "calzado_infantil": ["matriz-tallas-y-colores", "programa-fidelizacion-puntos", "gestion-de-proveedores-y-pedidos"],
    "tallas_grandes": ["matriz-tallas-y-colores", "control-de-stock-multialmacen", "vales-y-tarjetas-regalo-tpv"],
    "lenceria": ["matriz-tallas-y-colores", "control-de-stock-multialmacen", "etiquetas-codigo-de-barras-tpv"],
    "ropa_laboral": ["matriz-tallas-y-colores", "gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen"],
    "uniformes": ["matriz-tallas-y-colores", "gestion-de-proveedores-y-pedidos", "inventario-con-pda-lector-codigo-barras"],
    "ropa_regional": ["matriz-tallas-y-colores", "vales-y-tarjetas-regalo-tpv", "gestion-de-proveedores-y-pedidos"],
    "flamenca": ["matriz-tallas-y-colores", "vales-y-tarjetas-regalo-tpv", "rebajas-y-promociones-tpv"],
    "novias": ["matriz-tallas-y-colores", "gestion-de-proveedores-y-pedidos", "programa-fidelizacion-puntos"],
    "comunion": ["matriz-tallas-y-colores", "gestion-de-proveedores-y-pedidos", "vales-y-tarjetas-regalo-tpv"],
    "infantil": ["matriz-tallas-y-colores", "rebajas-y-promociones-tpv", "control-de-stock-multialmacen"],
    "puericultura": ["gestion-de-proveedores-y-pedidos", "vales-y-tarjetas-regalo-tpv", "control-de-stock-multialmacen"],
    "sombreros": ["matriz-tallas-y-colores", "etiquetas-codigo-de-barras-tpv", "rebajas-y-promociones-tpv"],
    "complementos": ["etiquetas-codigo-de-barras-tpv", "rebajas-y-promociones-tpv", "control-de-stock-multialmacen"],
    "maletas": ["control-de-stock-multialmacen", "etiquetas-codigo-de-barras-tpv", "gestion-de-proveedores-y-pedidos"],
    "bisuteria": ["etiquetas-codigo-de-barras-tpv", "inventario-con-pda-lector-codigo-barras", "rebajas-y-promociones-tpv"],
    "merceria": ["inventario-con-pda-lector-codigo-barras", "etiquetas-codigo-de-barras-tpv", "gestion-de-proveedores-y-pedidos"],
    "merceria_creativa": ["inventario-con-pda-lector-codigo-barras", "programa-fidelizacion-puntos", "rebajas-y-promociones-tpv"],
    "textil_hogar": ["control-de-stock-multialmacen", "rebajas-y-promociones-tpv", "gestion-de-proveedores-y-pedidos"],
    "alfombras": ["control-de-stock-multialmacen", "gestion-de-proveedores-y-pedidos", "etiquetas-codigo-de-barras-tpv"],

    # --- articulo de valor y pieza pequena: etiqueta e inventario
    "joyeria": ["etiquetas-codigo-de-barras-tpv", "inventario-con-pda-lector-codigo-barras", "vales-y-tarjetas-regalo-tpv"],
    "relojeria": ["etiquetas-codigo-de-barras-tpv", "gestion-de-proveedores-y-pedidos", "arqueo-de-caja-cierre-diario"],
    "compro_oro": ["arqueo-de-caja-cierre-diario", "inventario-con-pda-lector-codigo-barras", "etiquetas-codigo-de-barras-tpv"],
    "oro": ["arqueo-de-caja-cierre-diario", "etiquetas-codigo-de-barras-tpv", "gestion-de-proveedores-y-pedidos"],
    "optica": ["gestion-de-proveedores-y-pedidos", "programa-fidelizacion-puntos", "etiquetas-codigo-de-barras-tpv"],
    "gafas_sol": ["etiquetas-codigo-de-barras-tpv", "rebajas-y-promociones-tpv", "control-de-stock-multialmacen"],
    "fotografia": ["gestion-de-proveedores-y-pedidos", "etiquetas-codigo-de-barras-tpv", "control-de-stock-multialmacen"],

    # --- alimentacion: caja diaria y proveedor
    "alimentacion": ["arqueo-de-caja-cierre-diario", "gestion-de-proveedores-y-pedidos", "etiquetas-codigo-de-barras-tpv"],
    "fruteria": ["arqueo-de-caja-cierre-diario", "gestion-de-proveedores-y-pedidos", "tpv-sin-internet-modo-offline"],
    "carniceria": ["etiquetas-codigo-de-barras-tpv", "arqueo-de-caja-cierre-diario", "gestion-de-proveedores-y-pedidos"],
    "pescaderia": ["etiquetas-codigo-de-barras-tpv", "arqueo-de-caja-cierre-diario", "tpv-sin-internet-modo-offline"],
    "panaderia": ["arqueo-de-caja-cierre-diario", "tpv-sin-internet-modo-offline", "programa-fidelizacion-puntos"],
    "supermercado": ["inventario-con-pda-lector-codigo-barras", "control-de-stock-multialmacen", "arqueo-de-caja-cierre-diario"],
    "estanco": ["arqueo-de-caja-cierre-diario", "control-de-stock-multialmacen", "tpv-sin-internet-modo-offline"],
    "quiosco": ["arqueo-de-caja-cierre-diario", "tpv-sin-internet-modo-offline", "gestion-de-proveedores-y-pedidos"],

    # --- salud y bienestar: ficha de cliente y repeticion de compra
    "herboristeria": ["gestion-de-proveedores-y-pedidos", "programa-fidelizacion-puntos", "etiquetas-codigo-de-barras-tpv"],
    "herbodietetica": ["programa-fidelizacion-puntos", "control-de-stock-multialmacen", "gestion-de-proveedores-y-pedidos"],
    "parafarmacia": ["gestion-de-proveedores-y-pedidos", "inventario-con-pda-lector-codigo-barras", "programa-fidelizacion-puntos"],
    "ortopedia": ["gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen", "etiquetas-codigo-de-barras-tpv"],
    "suplementacion": ["programa-fidelizacion-puntos", "gestion-de-proveedores-y-pedidos", "rebajas-y-promociones-tpv"],
    "cosmetica": ["gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen", "etiquetas-codigo-de-barras-tpv"],
    "cosmetica_natural": ["programa-fidelizacion-puntos", "gestion-de-proveedores-y-pedidos", "etiquetas-codigo-de-barras-tpv"],
    "perfumeria": ["programa-fidelizacion-puntos", "vales-y-tarjetas-regalo-tpv", "rebajas-y-promociones-tpv"],
    "estetica": ["programa-fidelizacion-puntos", "vales-y-tarjetas-regalo-tpv", "arqueo-de-caja-cierre-diario"],
    "peluqueria": ["programa-fidelizacion-puntos", "arqueo-de-caja-cierre-diario", "vales-y-tarjetas-regalo-tpv"],
    "peluqueria_canina": ["programa-fidelizacion-puntos", "arqueo-de-caja-cierre-diario", "gestion-de-proveedores-y-pedidos"],
    "gimnasio": ["programa-fidelizacion-puntos", "arqueo-de-caja-cierre-diario", "tpv-sin-internet-modo-offline"],

    # --- animales
    "animales": ["gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen", "programa-fidelizacion-puntos"],
    "petshop": ["etiquetas-codigo-de-barras-tpv", "rebajas-y-promociones-tpv", "inventario-con-pda-lector-codigo-barras"],
    "acuarios": ["gestion-de-proveedores-y-pedidos", "etiquetas-codigo-de-barras-tpv", "control-de-stock-multialmacen"],
    "hipica": ["control-de-stock-multialmacen", "gestion-de-proveedores-y-pedidos", "matriz-tallas-y-colores"],

    # --- hogar, mueble y decoracion
    "muebles": ["gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen", "vales-y-tarjetas-regalo-tpv"],
    "colchoneria": ["gestion-de-proveedores-y-pedidos", "arqueo-de-caja-cierre-diario", "rebajas-y-promociones-tpv"],
    "decoracion": ["rebajas-y-promociones-tpv", "vales-y-tarjetas-regalo-tpv", "gestion-de-proveedores-y-pedidos"],
    "lamparas": ["gestion-de-proveedores-y-pedidos", "etiquetas-codigo-de-barras-tpv", "control-de-stock-multialmacen"],
    "enmarcacion": ["gestion-de-proveedores-y-pedidos", "arqueo-de-caja-cierre-diario", "control-de-stock-multialmacen"],
    "pinturas": ["gestion-de-proveedores-y-pedidos", "etiquetas-codigo-de-barras-tpv", "inventario-con-pda-lector-codigo-barras"],
    "electrodomesticos": ["gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen", "etiquetas-codigo-de-barras-tpv"],

    # --- ferreteria, oficio y taller
    "ferreteria": ["inventario-con-pda-lector-codigo-barras", "gestion-de-proveedores-y-pedidos", "etiquetas-codigo-de-barras-tpv"],
    "cerrajeria": ["arqueo-de-caja-cierre-diario", "gestion-de-proveedores-y-pedidos", "tpv-sin-internet-modo-offline"],
    "repuestos": ["inventario-con-pda-lector-codigo-barras", "control-de-stock-multialmacen", "gestion-de-proveedores-y-pedidos"],
    "reparaciones": ["arqueo-de-caja-cierre-diario", "gestion-de-proveedores-y-pedidos", "tpv-sin-internet-modo-offline"],
    "telefonia": ["control-de-stock-multialmacen", "etiquetas-codigo-de-barras-tpv", "programa-fidelizacion-puntos"],
    "telefonia_sat": ["arqueo-de-caja-cierre-diario", "inventario-con-pda-lector-codigo-barras", "gestion-de-proveedores-y-pedidos"],
    "informatica": ["control-de-stock-multialmacen", "gestion-de-proveedores-y-pedidos", "inventario-con-pda-lector-codigo-barras"],
    "lavanderia": ["arqueo-de-caja-cierre-diario", "programa-fidelizacion-puntos", "tpv-sin-internet-modo-offline"],

    # --- ocio, cultura y coleccion
    "libreria": ["inventario-con-pda-lector-codigo-barras", "gestion-de-proveedores-y-pedidos", "programa-fidelizacion-puntos"],
    "papeleria": ["etiquetas-codigo-de-barras-tpv", "gestion-de-proveedores-y-pedidos", "arqueo-de-caja-cierre-diario"],
    "comics": ["inventario-con-pda-lector-codigo-barras", "programa-fidelizacion-puntos", "gestion-de-proveedores-y-pedidos"],
    "juegos_mesa": ["control-de-stock-multialmacen", "vales-y-tarjetas-regalo-tpv", "programa-fidelizacion-puntos"],
    "jugueteria": ["vales-y-tarjetas-regalo-tpv", "rebajas-y-promociones-tpv", "control-de-stock-multialmacen"],
    "modelismo": ["inventario-con-pda-lector-codigo-barras", "gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen"],
    "bellas_artes": ["gestion-de-proveedores-y-pedidos", "inventario-con-pda-lector-codigo-barras", "etiquetas-codigo-de-barras-tpv"],
    "instrumentos": ["control-de-stock-multialmacen", "gestion-de-proveedores-y-pedidos", "etiquetas-codigo-de-barras-tpv"],
    "musica": ["inventario-con-pda-lector-codigo-barras", "programa-fidelizacion-puntos", "rebajas-y-promociones-tpv"],
    "vinilos": ["inventario-con-pda-lector-codigo-barras", "etiquetas-codigo-de-barras-tpv", "programa-fidelizacion-puntos"],
    "antiguedades": ["etiquetas-codigo-de-barras-tpv", "inventario-con-pda-lector-codigo-barras", "arqueo-de-caja-cierre-diario"],
    "segunda_mano": ["etiquetas-codigo-de-barras-tpv", "arqueo-de-caja-cierre-diario", "inventario-con-pda-lector-codigo-barras"],
    # Compite con segunda_mano en el informe, asi que lleva juego distinto.
    "vintage_segundamano": ["inventario-con-pda-lector-codigo-barras", "rebajas-y-promociones-tpv", "control-de-stock-multialmacen"],
    "souvenirs": ["arqueo-de-caja-cierre-diario", "tpv-sin-internet-modo-offline", "rebajas-y-promociones-tpv"],
    "fiestas_disfraces": ["control-de-stock-multialmacen", "rebajas-y-promociones-tpv", "arqueo-de-caja-cierre-diario"],
    "disfraces": ["matriz-tallas-y-colores", "control-de-stock-multialmacen", "rebajas-y-promociones-tpv"],
    "floristeria": ["arqueo-de-caja-cierre-diario", "gestion-de-proveedores-y-pedidos", "tpv-sin-internet-modo-offline"],

    # --- deporte y movilidad
    "deportes": ["matriz-tallas-y-colores", "control-de-stock-multialmacen", "rebajas-y-promociones-tpv"],
    "padel": ["control-de-stock-multialmacen", "programa-fidelizacion-puntos", "gestion-de-proveedores-y-pedidos"],
    "montana": ["matriz-tallas-y-colores", "gestion-de-proveedores-y-pedidos", "inventario-con-pda-lector-codigo-barras"],
    "bicicletas": ["gestion-de-proveedores-y-pedidos", "arqueo-de-caja-cierre-diario", "control-de-stock-multialmacen"],
    "skate": ["control-de-stock-multialmacen", "rebajas-y-promociones-tpv", "etiquetas-codigo-de-barras-tpv"],
    "motos_boutique": ["matriz-tallas-y-colores", "gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen"],
    "armeria": ["inventario-con-pda-lector-codigo-barras", "gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen"],

    # --- resto
    "articulos_eroticos": ["control-de-stock-multialmacen", "etiquetas-codigo-de-barras-tpv", "arqueo-de-caja-cierre-diario"],
    "sexshop": ["rebajas-y-promociones-tpv", "programa-fidelizacion-puntos", "control-de-stock-multialmacen"],
    "vapeo": ["control-de-stock-multialmacen", "programa-fidelizacion-puntos", "gestion-de-proveedores-y-pedidos"],
    "distribuidor": ["gestion-de-proveedores-y-pedidos", "control-de-stock-multialmacen", "inventario-con-pda-lector-codigo-barras"],
}
GENERICO = ["matriz-tallas-y-colores", "control-de-stock-multialmacen",
            "etiquetas-codigo-de-barras-tpv", "tpv-sin-internet-modo-offline"]

TITULOS = {
    "matriz-tallas-y-colores": "Matriz de tallas y colores",
    "control-de-stock-multialmacen": "Control de stock multialmacén",
    "programa-fidelizacion-puntos": "Programa de puntos y fidelización",
    "tpv-sin-internet-modo-offline": "TPV que funciona sin internet",
    "etiquetas-codigo-de-barras-tpv": "Etiquetas con código de barras",
    "inventario-con-pda-lector-codigo-barras": "Inventario con PDA o lector",
    "vales-y-tarjetas-regalo-tpv": "Vales y tarjetas regalo",
    "rebajas-y-promociones-tpv": "Rebajas y promociones",
    "arqueo-de-caja-cierre-diario": "Arqueo de caja y cierre diario",
    "gestion-de-proveedores-y-pedidos": "Proveedores y pedidos de compra",
}

NO_INDEX = {
    "conexion.asp", "conexion_visitas.asp", "menu_nav.asp", "footer_comun.asp",
    "tpv_consultas_desde_web_med.asp", "tpv_consultas_desde_web_medNO.asp",
    "tpv_consultas_desde_web_med -09-10-2023.asp", "vercarrito.asp", "carrito5.asp",
    "descargar.asp", "comprar_tpv.asp", "recuento5.asp", "negocio_antiguedad.asp",
    "resolucion_litigios.asp", "index.html", "Condiciones.htm",
}
PRIORIDAD = {
    "index.asp": ("1.0", "daily"), "caja5_pc.asp": ("0.9", "weekly"),
    "caja5_nube.asp": ("0.9", "weekly"), "tpv_negocios.asp": ("0.9", "weekly"),
    "verifactu-tpv.asp": ("0.9", "weekly"), "comparativas-tpv.asp": ("0.9", "weekly"),
    "funciones-tpv.asp": ("0.9", "weekly"), "preguntas-frecuentes-tpv.asp": ("0.8", "weekly"),
    "hardware-tpv-compatible.asp": ("0.8", "weekly"),
}


def leer(p):
    return open(p, encoding="utf-8").read()


def escribir(p, s):
    open(p, "w", encoding="utf-8").write(s)


# ------------------------------------------------- 1. menu: nuevos hubs
def menu():
    p = os.path.join(OUT, "menu_nav.asp")
    s = leer(p)
    if "funciones-tpv.asp" in s:
        return 0
    items = "".join(f"""
								<a href="{u}" class="mega-item">
									<div class="mega-item-icon"><i class="fa-solid {ic}"></i></div>
									<div class="mega-item-text">
										<strong>{t}</strong>
										<small>{d}</small>
									</div>
								</a>""" for u, t, ic, d in NUEVOS_HUBS)
    bloque = f"""
							<div class="dropdown-header">RECURSOS Y COMPARATIVAS</div>{items}
"""
    # insertar en la segunda columna del mega-menu de guias
    m = re.search(r'(<div class="dropdown-header">EQUIPAMIENTO Y GUÍAS RETAIL</div>)', s)
    if not m:
        return 0
    s = s[:m.start()] + bloque + "\n\t\t\t\t\t\t\t" + s[m.start():]
    escribir(p, s)
    return 1


# --------------------------------- 2. hub de sectores: recuperar huerfanas
def hub_sectores():
    p = os.path.join(OUT, "tpv_negocios.asp")
    s = leer(p)
    todas = {os.path.basename(f) for f in glob.glob(os.path.join(OUT, "negocio_*.asp"))}
    # Enlazar una pagina que redirige es tirar un enlace interno: el usuario
    # y el robot acaban en otra. Se quitan todas las que tengan 301, no solo
    # la de antiguedades que estaba a mano.
    todas -= set(REDIRECCIONES)
    enlazadas = set(re.findall(r"negocio_[a-z_]+\.asp", s))
    faltan = sorted(todas - enlazadas)
    if not faltan:
        return 0

    def bonito(fn):
        t = fn.replace("negocio_", "").replace(".asp", "").replace("_", " ")
        return t[:1].upper() + t[1:]

    cards = "".join(f"""
					<a href="/{fn}" class="card-sector-editorial" data-keywords="{bonito(fn).lower()}">
						<div>
							<div class="card-header-sector">
								<div class="card-icon-box"><i class="fa-solid fa-store"></i></div>
								<div><h4 class="card-title-sector">{bonito(fn)}</h4></div>
							</div>
						</div>
					</a>""" for fn in faltan)

    bloque = f"""
			<!-- GRUPO: OTROS SECTORES ESPECIALIZADOS -->
			<div class="categoria-bloque" data-category="cat-otros">
				<div class="categoria-titulo-editorial">
					<span>Otros sectores y especialidades</span>
					<small>[ {len(faltan)} ESPECIALIDADES ]</small>
				</div>
				<div class="grid-sectores-editorial">{cards}
				</div>
			</div>
"""
    m = None
    for m in re.finditer(r'</div>\s*</div>\s*</section>', s):
        pass  # nos quedamos con la ultima
    if not m:
        return 0
    s = s[:m.start()] + bloque + "\n\t\t" + s[m.start():]
    escribir(p, s)
    return len(faltan)


# ----------------------------- 3. enlaces contextuales sector -> funciones
def enlaces_contextuales():
    n = 0
    for f in sorted(glob.glob(os.path.join(OUT, "negocio_*.asp"))):
        s = leer(f)
        if "bloque-funciones-rel" in s:
            continue
        base = os.path.basename(f)
        # Clave exacta y no "la primera que sea subcadena". Con once sectores
        # daba igual; con noventa y tres no: 'calzado' es subcadena de
        # 'calzado_infantil', y lo mismo pasa con merceria/merceria_creativa,
        # telefonia/telefonia_sat, cosmetica/cosmetica_natural y
        # souvenirs/souvenirs_tienda. Buscando por subcadena, la pagina mas
        # especifica se llevaba los enlaces de la generica, que es justo el par
        # que hay que diferenciar.
        exacta = base[len("negocio_"):-len(".asp")] if base.startswith("negocio_") \
            and base.endswith(".asp") else ""
        if exacta in POR_SECTOR:
            clave = exacta
        else:                       # sectores que aun no estan en el mapa
            clave = next((k for k in sorted(POR_SECTOR, key=len, reverse=True)
                          if k in base), None)
        slugs = POR_SECTOR.get(clave, GENERICO)[:3]
        if len(slugs) < 3:
            slugs = slugs + [g for g in GENERICO if g not in slugs][:3 - len(slugs)]
        lis = "".join(
            f'\n\t\t\t\t\t<li style="padding:9px 0; border-bottom:1px solid #e9e4db;">'
            f'<a href="/{sl}.asp" style="color:#8c2d19; font-weight:600; text-decoration:none;">'
            f'<i class="fa-solid fa-angle-right" style="margin-right:7px;"></i>{TITULOS[sl]}</a></li>'
            for sl in slugs)
        bloque = f"""
	<section class="bloque-funciones-rel" style="padding:40px 0; background:#faf8f4; border-top:1px solid #e9e4db;">
		<div class="container">
			<h2 style="font-size:22px; font-weight:800; color:#1e293b; margin-top:0; margin-bottom:12px;">Funciones del TPV que más se usan en este sector</h2>
			<ul style="list-style:none; padding:0; margin:0; column-count:2; column-gap:34px;">{lis}
				<li style="padding:9px 0; border-bottom:1px solid #e9e4db;"><a href="/comparativas-tpv.asp" style="color:#8c2d19; font-weight:600; text-decoration:none;"><i class="fa-solid fa-angle-right" style="margin-right:7px;"></i>Comparativas con otros TPV</a></li>
				<li style="padding:9px 0; border-bottom:1px solid #e9e4db;"><a href="/preguntas-frecuentes-tpv.asp" style="color:#8c2d19; font-weight:600; text-decoration:none;"><i class="fa-solid fa-angle-right" style="margin-right:7px;"></i>Preguntas frecuentes sobre TPV</a></li>
			</ul>
		</div>
	</section>
"""
        i = s.find('<section class="cta-final-abaco"')
        if i < 0:
            i = s.find("<footer")
        if i < 0:
            continue
        escribir(f, s[:i] + bloque + "\n\t" + s[i:])
        n += 1
    return n


# ------------------------------------------------------------- 4. sitemap
def sitemap():
    urls = []
    for f in sorted(glob.glob(os.path.join(OUT, "*.asp"))):
        b = os.path.basename(f)
        if b in NO_INDEX or b.startswith(("conexion", "index__")):
            continue
        s = leer(f)
        if re.search(r'<meta[^>]+name="robots"[^>]+noindex', s, re.I):
            continue
        # respetar canonical hacia otra pagina
        m = re.search(r'<link rel="canonical" href="([^"]+)"', s)
        if m and not m.group(1).rstrip("/").endswith(b) and m.group(1).rstrip("/") != BASE:
            continue
        pri, chg = PRIORIDAD.get(b, ("0.7", "monthly"))
        loc = BASE + "/" if b == "index.asp" else BASE + "/" + b
        urls.append((loc, pri, chg))

    cuerpo = "".join(
        f"\n  <url>\n    <loc>{u}</loc>\n    <lastmod>{HOY}</lastmod>"
        f"\n    <changefreq>{c}</changefreq>\n    <priority>{p}</priority>\n  </url>"
        for u, p, c in urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           + cuerpo + "\n</urlset>\n")
    escribir(os.path.join(OUT, "sitemap.xml"), xml)
    for extra in ("sitemap2.xml", "sitemapMALO.xml"):
        q = os.path.join(OUT, extra)
        if os.path.exists(q):
            os.remove(q)
    return len(urls)


# --------------------------------------------------------- 5. web.config 301
def redirecciones():
    """301 de las paginas canibalizadas, desde la tabla de redirecciones_301.py.

    Idempotente por regla, no por bloque: la version anterior comprobaba si
    existia la regla de index.html y, si estaba, no anadia ninguna mas. Eso
    dejaba el sitio congelado en las dos primeras redirecciones, asi que
    cualquier canibalizacion resuelta despues no llegaba nunca al web.config.
    """
    p = os.path.join(OUT, "web.config")
    s = leer(p)
    nuevas = []
    for origen, destino in sorted(REDIRECCIONES.items()):
        # Un solo patron para escribir la regla y para detectar si ya esta. Con
        # dos expresiones distintas se escapaba de mas al escribir: salia
        # '^index\\.html$', que en regex de IIS es 'barra invertida y luego
        # cualquier caracter', asi que la regla no llegaba a redirigir nunca y
        # ademas la deteccion fallaba y la duplicaba en cada pasada.
        patron = "^" + origen.replace(".", r"\.") + "$"
        if 'url="%s"' % patron in s:
            continue                                   # ya esta, no duplicar
        # index.asp es la raiz: redirigir a /index.asp dejaria dos URLs para
        # la portada, que es justo lo que este 301 viene a cerrar.
        url = "/" if destino == "index.asp" else "/" + destino
        nuevas.append("""
                <rule name="301 %s" stopProcessing="true">
                    <match url="%s" />
                    <action type="Redirect" url="%s" redirectType="Permanent" />
                </rule>""" % (origen, patron, url))
    if not nuevas:
        return 0
    s = s.replace("            <rules>", "            <rules>" + "".join(nuevas), 1)
    escribir(p, s)
    return len(nuevas)


if __name__ == "__main__":
    print("menu (hubs nuevos)      :", menu())
    print("huerfanas recuperadas   :", hub_sectores())
    print("paginas con enlaces ctx :", enlaces_contextuales())
    print("URLs en sitemap         :", sitemap())
    print("redirecciones 301       :", redirecciones())

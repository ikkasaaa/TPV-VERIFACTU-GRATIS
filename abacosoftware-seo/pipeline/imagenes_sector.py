#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Una imagen social propia por pagina de sector, en vez de una para las 99.

Uso:
  python3 imagenes_sector.py --prompts [inv.tsv]     lista para generar
  python3 imagenes_sector.py --aplicar <dir-web>     mete las etiquetas
  python3 imagenes_sector.py --faltan <dir-img>      que imagenes no estan

El problema: seo_tech.py pone la misma og:image en todo el sitio
('/img/og-caja5-tpv.png'). Las 99 paginas de sector se ven identicas al
compartirse en WhatsApp, en Twitter o en un chat, que es donde ese enlace se
juega el clic. Una imagen del sector propio es lo que diferencia una de otra.

Por que hay una escena escrita para cada sector y no una plantilla con el
nombre cambiado: 99 fotos del mismo mostrador con distinto genero al fondo son
la version visual de la plantilla que motor/gate.py rechaza, y encima se nota
mas, porque una foto se juzga de un vistazo. Una libreria no se parece a una
pescaderia. Si el sector no esta en la tabla se avisa y no se inventa: mejor
que le falte imagen a que le sobre una generica.

Las imagenes no se generan desde aqui. El modo ilimitado de Higgsfield es un
boton de su interfaz web y no llega al conector, asi que generarlas por API
gastaria creditos. Este script escribe los prompts para pegarlos alli, y luego
coloca los ficheros que salgan.

Convenciones de las imagenes que espera:

  ruta     /img/sectores/<slug-sin-negocio_>.jpg
  tamano   1200x630 (lo que piden Open Graph y las tarjetas de Twitter)
  peso     por debajo de 150 kB, que va en el <head> de una pagina que carga

Sin caras, sin texto y sin logotipos, y esto no es estetica. Texto en una
imagen generada sale con faltas y en un idioma que no es el suyo; un logotipo
inventado sobre el mostrador de un cliente es una marca que no existe; y una
cara reconocible en la ficha comercial de un negocio real es un problema de
derecho de imagen que no hace falta tener.
"""
import os
import re
import signal
import sys

# Misma razon que en motor/analizar_clusters.py: sin esto, cortar la salida
# con "| head" revienta con BrokenPipeError en vez de terminar en silencio,
# que es lo que hace cualquier orden de Unix.
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass                              # Windows no tiene SIGPIPE

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from redirecciones_301 import REDIRECCIONES
except ImportError:
    REDIRECCIONES = {}

BASE = "https://www.abacosoftware.com"
RUTA = "/img/sectores"

# El nombre castellano del sector NO entra aqui: "a small independent Spanish
# tienda de acuarios" mezcla los dos idiomas en la misma frase y el modelo lo
# lee peor. La escena ya dice que tienda es (unos acuarios retroiluminados no
# son otra cosa), y el nombre en castellano se usa donde toca, que es el alt.
MARCO = ("Interior of a small independent Spanish retail shop, photographed from the "
         "customer side of the counter in warm natural daylight. {escena} On the "
         "counter, a modern point-of-sale setup: a plain touchscreen monitor "
         "angled away from camera, a small receipt printer and a barcode scanner. "
         "Realistic documentary retail photography, shallow depth of field, soft "
         "shadows, muted warm palette, eye level, 3:2 crop. No people and no "
         "faces. No text, no lettering, no signage, no numbers, no brand names "
         "and no logos anywhere in the frame, and nothing legible on the screen.")

# slug -> (que es en castellano, escena propia del sector, para el alt y el prompt)
ESCENAS = {
 "acuarios": ("tienda de acuarios", "Backlit glass aquarium tanks along the wall, water plants, bags of substrate and small pumps on a shelf."),
 "alfombras": ("tienda de alfombras", "Rolled and stacked rugs leaning against the wall, one large kilim unrolled across the floor."),
 "alimentacion": ("tienda de alimentacion", "Shelves of tins and dry goods, a crate of vegetables, a scale at the end of the counter."),
 "animales": ("tienda de animales", "Sacks of pet feed stacked low, collars and leads on a rack, a wall of small accessories."),
 "antiguedades": ("tienda de antiguedades", "Crowded shelves of old porcelain, brass lamps and framed prints, a marble-topped side table."),
 "armeria": ("armeria", "Locked glass cabinets with hunting gear, boxes of cartridges, camouflage jackets on a rail."),
 "articulos_eroticos": ("tienda de articulos eroticos", "Discreet dark shelving with plain boxed products, soft low lighting, a curtained back area."),
 "bellas_artes": ("tienda de bellas artes", "Racks of stretched canvases, jars of brushes, tubes of oil paint in open trays."),
 "bicicletas": ("tienda de bicicletas", "Bicycles hanging from a wall rack, a repair stand with tools, boxed helmets on a shelf."),
 "bisuteria": ("tienda de bisuteria", "Trays of costume jewellery under a glass counter, earring stands, a small mirror."),
 "calzado": ("zapateria", "Wall shelving of boxed and displayed shoes, a low fitting bench with a shoehorn, a floor mirror."),
 "calzado_infantil": ("zapateria infantil", "Small colourful shoes on low shelves, a child-height fitting bench, a foot measuring gauge."),
 "carniceria": ("carniceria", "Refrigerated glass display of cuts and sausages, a butcher block, knives on a magnetic strip."),
 "cerrajeria": ("cerrajeria", "Wall of blank keys on hooks, a key-cutting machine, boxed locks and cylinders behind."),
 "colchoneria": ("colchoneria", "Mattresses stacked and stood on edge, folded pillows and quilts on a shelf, a bed base display."),
 "comics": ("tienda de comics", "Spinner racks and long boxes of comics, shelves of graphic novels, small figures in blister packs."),
 "complementos": ("tienda de complementos", "Handbags on wall pegs, scarves folded in a basket, belts hanging in a row."),
 "compro_oro": ("compro oro", "Precision scale on the counter, a loupe and small tray, a secure glass cabinet behind."),
 "comunion": ("tienda de comunion", "White communion dresses and small suits on a rail, candles and rosaries in a display case."),
 "cosmetica": ("tienda de cosmetica", "Shelves of skincare bottles and jars in neat rows, a small mirror and tester tray."),
 "cosmetica_natural": ("tienda de cosmetica natural", "Amber glass bottles and paper-wrapped soaps on raw wood shelving, dried herbs in jars."),
 "decoracion": ("tienda de decoracion", "Ceramic vases and candle holders on shelves, framed prints, folded throws in a basket."),
 "deportes": ("tienda de deportes", "Racks of technical sportswear, boxed trainers, balls in a wire bin."),
 "disfraces": ("tienda de disfraces", "Costumes crowded on a rail, masks and wigs on a wall, hats stacked on a shelf."),
 "electrodomesticos": ("tienda de electrodomesticos", "Row of white goods along the wall, small appliances boxed on shelves, a demonstration unit."),
 "enmarcacion": ("tienda de enmarcacion", "Sample frame corners on a wall board, sheets of mount board, a mitre cutter on the workbench."),
 "estanco": ("estanco", "Cabinet of packaged goods behind the counter, a lottery display, a rack of newspapers."),
 "estetica": ("centro de estetica", "Reception desk with product shelving, a treatment room glimpsed through an open door, folded towels."),
 "ferreteria": ("ferreteria", "Dense wooden shelving and small drawers of screws and fittings, tools hanging on a pegboard."),
 "fiestas_disfraces": ("tienda de fiestas y disfraces", "Party balloons in bunches, paper tableware in stacks, costumes on a rail behind."),
 "flamenca": ("tienda de moda flamenca", "Ruffled flamenco dresses on a rail, shawls folded on a shelf, hair flowers in open boxes."),
 "floristeria": ("floristeria", "Buckets of cut flowers on the floor, foliage in tall containers, a roll of wrapping paper and ribbon."),
 "fotografia": ("tienda de fotografia", "Cameras and lenses in a glass cabinet, tripods standing in a corner, photo paper boxes."),
 "fruteria": ("fruteria", "Sloped crates of fruit and vegetables, a hanging scale, brown paper bags on a spike."),
 "gafas_sol": ("tienda de gafas de sol", "Rotating sunglasses displays, a mirror on the counter, cases in a small tray."),
 "gimnasio": ("gimnasio", "Reception desk with a turnstile behind, weights racked in the room beyond, folded towels and a drinks fridge."),
 "herbodietetica": ("herbodietetica", "Shelves of supplement tubs and boxed infusions, glass jars of dried herbs, a small scale."),
 "herboristeria": ("herboristeria", "Wall of labelled glass jars with dried herbs, paper bags, a brass scale on the counter."),
 "hipica": ("tienda hipica", "Saddles on stands, bridles hanging in a row, riding boots and helmets on a shelf."),
 "infantil": ("tienda infantil", "Small garments on low rails, soft toys on a shelf, folded blankets in a basket."),
 "informatica": ("tienda de informatica", "Boxed components on shelving, a workbench with an open tower case, cables coiled on hooks."),
 "instrumentos": ("tienda de instrumentos musicales", "Acoustic guitars hanging on the wall, a digital piano, sheet music in a rack."),
 "joyeria": ("joyeria", "Lit glass cabinets of rings and chains, velvet display busts, a loupe on the counter."),
 "juegos_mesa": ("tienda de juegos de mesa", "Shelves of boxed board games spine out, a demo table with a game set up, dice in a bowl."),
 "jugueteria": ("jugueteria", "Bright shelving of boxed toys, a bin of soft toys, board games stacked high."),
 "lamparas": ("tienda de lamparas", "Pendant lamps hung at different heights and lit, table lamps on a shelf, bulbs boxed below."),
 "lavanderia": ("lavanderia", "Row of industrial washers and dryers, folding table with stacked linen, detergent bottles on a shelf."),
 "lenceria": ("tienda de lenceria", "Delicate garments on padded hangers, folded sets in shallow drawers, a fitting-room curtain."),
 "libreria": ("libreria", "Floor-to-ceiling wooden bookshelves, a display table of face-out books, a rolling ladder."),
 "maletas": ("tienda de maletas", "Hard-shell suitcases stacked by size, backpacks on wall hooks, travel accessories in a tray."),
 "merceria": ("merceria", "Wall of thread spools by colour, buttons in small drawers, ribbon rolls on a rack."),
 "merceria_creativa": ("merceria creativa", "Yarn in open cubbies by colour, knitting needles in a jar, pattern books on a table."),
 "moda": ("tienda de ropa", "Rails of hanging garments and folded knitwear on a table, a fitting-room curtain, a potted plant."),
 "modelismo": ("tienda de modelismo", "Boxed scale kits on shelves, small paint pots in racks, tweezers and a cutting mat on the bench."),
 "montana": ("tienda de montana", "Rucksacks on wall hooks, technical jackets on a rail, boots and coiled climbing rope."),
 "motos_boutique": ("boutique de moto", "Helmets on a lit shelf, leather jackets on a rail, gloves and boots in a display case."),
 "muebles": ("tienda de muebles", "Room set with a sofa and side table, chairs stacked at the back, fabric swatch book on the counter."),
 "musica": ("tienda de musica", "Guitars on the wall, an amplifier stack, vinyl records in flip bins."),
 "novias": ("tienda de novias", "White bridal gowns in protective covers on a rail, a full-length mirror, a veil on a stand."),
 "optica": ("optica", "Wall panels of spectacle frames, a fitting mirror on the counter, a lens measuring device."),
 "ortopedia": ("ortopedia", "Supports and braces on wall hooks, a walking frame and crutches, boxed insoles on a shelf."),
 "padel": ("tienda de padel", "Padel rackets on a wall display, tubes of balls stacked, grip tape and bags on a shelf."),
 "panaderia": ("panaderia", "Glass display of rustic loaves and pastries, wooden bread shelving and baskets behind."),
 "papeleria": ("papeleria", "Notebooks and folders on shelves, pens in counter displays, reams of paper stacked below."),
 "parafarmacia": ("parafarmacia", "White shelving of boxed health and skincare products, a small consultation corner."),
 "peluqueria": ("peluqueria", "Styling chairs at mirrors, a washbasin unit, product bottles lined on a shelf."),
 "peluqueria_canina": ("peluqueria canina", "Stainless grooming table with an arm, clippers and brushes in a tray, a bathing tub behind."),
 "perfumeria": ("perfumeria", "Glass shelves of boxed fragrance, tester bottles on a mirrored tray, soft lighting."),
 "pescaderia": ("pescaderia", "Crushed-ice display of whole fish and shellfish, a filleting board, a hanging scale."),
 "pinturas": ("tienda de pinturas", "Paint tins stacked by size, a colour fan deck open on the counter, a tinting machine, rollers and brushes."),
 "puericultura": ("tienda de puericultura", "Prams and car seats on display, cots at the back, small boxed accessories on a shelf."),
 "quiosco": ("quiosco", "Newspaper and magazine racks facing out, sweets in a counter display, a small fridge of drinks."),
 "relojeria": ("relojeria", "Watches on cushions in a lit glass cabinet, a workbench with a loupe and tiny tools, straps in a drawer."),
 "reparaciones": ("taller de reparaciones", "Workbench with a device opened up, small tools laid out, labelled parts drawers behind."),
 "repuestos": ("tienda de repuestos", "Metal shelving of boxed spare parts, a parts catalogue on the counter, bins of small fittings."),
 "ropa_laboral": ("tienda de ropa laboral", "Workwear and hi-vis jackets on rails, safety boots on a shelf, helmets and gloves boxed."),
 "ropa_regional": ("tienda de ropa regional", "Traditional Spanish regional garments on a rail, embroidered shawls folded, hair combs in a case."),
 "segunda_mano": ("tienda de segunda mano", "Mixed second-hand goods on shelves, a rail of used clothing, books and small appliances."),
 "sexshop": ("sexshop", "Discreet dark shelving with plain boxed products, low warm lighting, a curtained back area."),
 "skate": ("tienda de skate", "Skateboard decks mounted on the wall, wheels and trucks in boxes, trainers on a shelf."),
 "sombreros": ("sombrereria", "Hats on wooden blocks and wall pegs, a hat box stack, a brim-measuring tape on the counter."),
 "souvenirs": ("tienda de souvenirs", "Postcard spinner, small ceramic and magnet displays, printed tote bags on a rack."),
 "supermercado": ("supermercado", "Aisle of stocked shelves receding, a chilled cabinet, wire baskets stacked by the counter."),
 "suplementacion": ("tienda de suplementacion", "Tubs of protein powder in rows, boxed bars in a display, a shaker bottle on the counter."),
 "tallas_grandes": ("tienda de tallas grandes", "Rails of garments in generous sizes, a spacious fitting room with a curtain, a full-length mirror."),
 "telefonia": ("tienda de telefonia", "Phone accessories on pegboard, cases in a rack, a small repair bench at the back."),
 "textil_hogar": ("tienda de textil hogar", "Folded towels and bed linen stacked by colour, curtain fabric rolls stood on end."),
 "uniformes": ("tienda de uniformes", "School and work uniforms on rails by size, embroidered badges in a tray, folded polos stacked."),
 "vapeo": ("tienda de vapeo", "Devices in a lit glass cabinet, bottles of liquid on shelves by colour, coils boxed in a tray."),
 "vinilos": ("tienda de vinilos", "Flip bins of vinyl records, a turntable on the counter, album sleeves displayed on the wall."),
}

# Paginas que no son de sector aunque empiecen por negocio_, o que redirigen.
NO_SECTOR = {"distribuidor", "consulta", "gestion_clientes"}

# Sinonimos: comparten sector, asi que comparten imagen. No se genera dos veces
# la misma foto para dos paginas que hablan del mismo negocio.
ALIAS = {
    "antiguedad": "antiguedades",
    "oro": "compro_oro",
    "petshop": "animales",
    "telefonia_sat": "telefonia",
    "vintage_segundamano": "segunda_mano",
    "fiestas_disfraces": "disfraces",
    "souvenirs_tienda": "souvenirs",
    "herboristeria": "herbodietetica",
}


def sectores(inventario):
    """[(slug_pagina, clave_imagen)] de las paginas de sector que siguen vivas."""
    out = []
    with open(inventario, encoding="utf-8") as fh:
        fh.readline()
        for linea in fh:
            c = linea.rstrip("\n").split("\t")
            if len(c) < 2 or not c[1].startswith("negocio_"):
                continue
            pagina = c[1]
            if pagina in REDIRECCIONES:      # ya no existe, redirige a otra
                continue
            clave = pagina[len("negocio_"):].replace(".asp", "")
            if clave in NO_SECTOR:
                continue
            out.append((pagina, ALIAS.get(clave, clave)))
    return sorted(set(out))


def prompt(clave):
    sitio, escena = ESCENAS[clave]
    return MARCO.format(escena=escena), sitio


def alt(clave):
    sitio = ESCENAS[clave][0]
    return "Mostrador de una %s con un TPV en funcionamiento" % sitio


def listar(inventario):
    pares = sectores(inventario)
    vistos, faltan, filas = set(), [], []
    for pagina, clave in pares:
        if clave not in ESCENAS:
            faltan.append((pagina, clave))
            continue
        if clave in vistos:
            continue
        vistos.add(clave)
        p, _ = prompt(clave)
        filas.append((clave, pagina, p))
    return filas, faltan, pares


def _meta(clave):
    url = "%s%s/%s.jpg" % (BASE, RUTA, clave)
    return url


def poner_og(texto, clave):
    """Devuelve (texto, cambiado). Idempotente: dos pasadas dejan lo mismo."""
    url = _meta(clave)
    if url in texto:
        return texto, False
    hecho = False
    for prop, attr in (("og:image", "property"), ("twitter:image", "name")):
        rx = re.compile(r'<meta\s+%s=["\']%s["\']\s+content=["\'][^"\']*["\']\s*/?>'
                        % (attr, prop), re.I)
        nueva = '<meta %s="%s" content="%s">' % (attr, prop, url)
        if rx.search(texto):
            texto = rx.sub(nueva, texto, count=1)
        elif "<head>" in texto:
            texto = texto.replace("<head>", "<head>\n\t" + nueva, 1)
        else:
            continue
        hecho = True
    return texto, hecho


def aplicar_dir(web, inventario):
    cambiadas, sin_imagen = 0, []
    for pagina, clave in sectores(inventario):
        if clave not in ESCENAS:
            sin_imagen.append(pagina)
            continue
        p = os.path.join(web, pagina)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8", errors="replace") as fh:
            s = fh.read()
        s2, hecho = poner_og(s, clave)
        if hecho:
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(s2)
            cambiadas += 1
    return cambiadas, sin_imagen


AQUI = os.path.dirname(os.path.abspath(__file__))
INV = os.path.join(AQUI, "..", "..", "inventarios", "abacosoftware.tsv")


if __name__ == "__main__":
    if "--prompts" in sys.argv:
        filas, faltan, pares = listar(INV)
        print("# %d paginas de sector -> %d imagenes distintas" % (len(pares), len(filas)))
        print("# %s/<clave>.jpg  |  1200x630  |  <150 kB" % RUTA)
        print("# El modo ilimitado es un boton de la web de Higgsfield: no llega")
        print("# al conector, asi que estos prompts se pegan alli, no se generan aqui.")
        print()
        for i, (clave, pagina, p) in enumerate(filas, 1):
            print("## %d. %s  ->  %s.jpg   (%s)" % (i, pagina, clave, ESCENAS[clave][0]))
            print(p)
            print('alt: "%s"' % alt(clave))
            print()
        if faltan:
            print("# SIN ESCENA ESCRITA, no se generan (anadir a ESCENAS):")
            for pagina, clave in faltan:
                print("#   %-34s %s" % (pagina, clave))
    elif "--faltan" in sys.argv:
        i = sys.argv.index("--faltan")
        carpeta = sys.argv[i + 1] if len(sys.argv) > i + 1 else "img/sectores"
        filas, faltan, _ = listar(INV)
        sin = [c for c, _, _ in filas
               if not os.path.exists(os.path.join(carpeta, c + ".jpg"))]
        print("esperadas %d | estan %d | faltan %d"
              % (len(filas), len(filas) - len(sin), len(sin)))
        for c in sin:
            print("  ", c + ".jpg")
    elif "--aplicar" in sys.argv:
        i = sys.argv.index("--aplicar")
        web = sys.argv[i + 1] if len(sys.argv) > i + 1 else "site"
        n, sin = aplicar_dir(web, INV)
        print("paginas con og:image de sector:", n)
        if sin:
            print("sin escena escrita:", len(sin))
    else:
        print(__doc__.split("\n\n")[1].strip())

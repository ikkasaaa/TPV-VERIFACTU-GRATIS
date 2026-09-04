#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resuelve la canibalizacion: dos paginas propias peleando por la misma busqueda.

Uso:
  python3 canibalizacion.py <inv.tsv> [<inv.tsv> ...]        informe
  python3 canibalizacion.py <inv.tsv> [...] --escribir       + genera el modulo
                                                               de redirecciones

El agrupador de motor/ dice que dos paginas hablan de lo mismo. Eso NO basta
para fusionarlas, y esa distincion es todo este fichero.

motor/README.md ya lo avisa: fruteria y carniceria no se fusionan aunque las
dos sean alimentacion, porque son paginas distintas con clientes distintos. El
agrupador esta afinado para no separar de mas, asi que junta de mas. Aplicar un
301 a cada grupo que devuelve seria tirar paginas buenas.

Asi que aqui cada grupo cae en uno de cuatro cajones, y solo el primero se
aplica solo:

  SEGURO    Los slugs son variantes del mismo: plural ('negocio_antiguedad' /
            'negocio_antiguedades'), sufijo ('..._telefonia' / '..._telefonia_sat')
            o extension ('index.asp' / 'index.html'). No hay juicio editorial
            que hacer: sobra una. 301 a la ganadora.

  TITULO    Lo que seria REVISAR, pero las paginas llevan el MISMO <title>,
            byte a byte. Eso ya no es una conjetura del agrupador: el titulo lo
            escribio una persona, y escribir el mismo para dos paginas es
            decir que sirven lo mismo. La canibalizacion esta confirmada; lo
            que queda por decidir es el remedio, porque puede ser fusionarlas o
            puede ser que los negocios si sean distintos y lo que este mal sea
            el titulo. Lo que no puede quedarse es como esta: dos paginas vivas
            compitiendo en la misma busqueda con el mismo titulo.

  REVISAR   Misma familia de pagina, pero negocios distintos ('colchoneria' /
            'muebles'). El agrupador los unio por vecindad semantica. Fusionar
            aqui es una decision de negocio, no tecnica: puede que sean dos
            clientes distintos. Se informa y no se toca.

  SEPARAR   Distinta etapa del embudo: 'abrir-tienda-electrodomesticos' es una
            guia para quien monta la tienda y 'negocio_electrodomesticos' es la
            ficha del TPV para quien ya la tiene. Comparten palabras y no
            compiten. Nunca se fusionan: se enlazan entre si.

  CRUZADO   Las paginas son de dominios distintos. Un 301 aqui regala un
            dominio entero al otro, y los dos son del mismo dueno pero son dos
            negocios. Decision del cliente, no del pipeline.

Criterio de ganadora dentro de un grupo SEGURO. Primero manda YA_DECIDIDO, o
sea lo que el web.config del sitio ya redirige: si el criterio automatico saliera
al reves, las dos reglas juntas serian un bucle de redireccion en produccion.
Despues, en este orden y sin empates posibles: mas palabras, luego slug con
guiones antes que con guion bajo (es la forma moderna del sitio), luego slug mas
corto, luego alfabetico. Tiene que ser determinista: las dos cuentas que trabajan
en este repositorio lo calculan por separado y deben llegar al mismo resultado
sin hablarse.

Sin exportacion de Search Console no se puede usar el unico criterio que de
verdad manda, que es cual de las dos ya recibe trafico. Cuando la haya, gana la
que tenga clics y esto pasa a ser el desempate.
"""
import difflib
import os
import re
import signal
import sys

# Igual que en motor/analizar_clusters.py: sin esto, cortar la salida con
# "| head" revienta con BrokenPipeError en vez de terminar en silencio.
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (AttributeError, ValueError):
    pass                              # Windows no tiene SIGPIPE

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "motor"))
import clusters as C                                          # noqa: E402

# Paginas de sistema: no son contenido y no compiten por nada.
NO_CONTENIDO = {
    "conexion.asp", "conexion_visitas.asp", "menu_nav.asp", "footer_comun.asp",
    "contenido_copyr-footer.html", "vercarrito.asp", "carrito5.asp",
    "info_asp.aspx", "ventas.aspx",
}

# Familia = para que sirve la pagina. Dos familias distintas son dos etapas del
# embudo, y esas nunca se fusionan.
FAMILIAS = [
    (re.compile(r"^blog/"),                    "articulo"),
    (re.compile(r"^(abrir|guia-abrir)[-_]"),   "guia"),
    (re.compile(r"^negocio[-_]"),              "sector"),
    (re.compile(r"^tpv[-_](tienda|negocio)"),  "sector"),
    (re.compile(r"^app[-_]"),                  "producto"),
    (re.compile(r"^index\b"),                  "portada"),
]

PREFIJOS = ("negocio_", "negocio-", "tpv-tienda-", "tpv_tienda_", "tpv-", "tpv_",
            "abrir-", "abrir_", "guia-abrir-", "app_", "app-")

# Redirecciones que YA estan en el web.config que genera enlazado_y_sitemap.py,
# o sea vivas en el sitio. Mandan sobre el criterio de abajo.
#
# No es una preferencia de estilo: 'negocio_antiguedad' y 'negocio_antiguedades'
# tienen las dos 992 palabras, asi que cualquier desempate automatico es
# arbitrario, y si sale al reves que el web.config las dos reglas juntas son un
# bucle de redireccion en produccion. Ante un empate, manda lo que ya se envio.
YA_DECIDIDO = {
    "negocio_antiguedad.asp": "negocio_antiguedades.asp",
    "index.html": "index.asp",
}

# URLs que existieron en produccion y hoy devuelven 404. Un 301 aqui no quita
# nada a nadie: recupera los enlaces y el historial que apuntan a una direccion
# muerta y los lleva a la pagina que hace ese trabajo ahora.
#
# No salen del analisis y no pueden salir, precisamente porque ya no existen:
# si no estan en el arbol, no estan en el inventario. Se anotan a mano cuando
# aparecen en el log del servidor o en Search Console como 404 con enlaces
# entrantes.
#
# Es el unico caso en el que una 301 se escribe por decision y no por hallazgo.
# Entre dos paginas que las dos responden 200 no se redirige: eso se resuelve
# diferenciandolas, con enlazado interno y con su canonical.
RESCATES = {
    "prueba_gratis.asp": "tpv_pedir_caja5_gratis.asp",
}


def familia(slug):
    s = slug.lower()
    for rx, nombre in FAMILIAS:
        if rx.search(s):
            return nombre
    return "generica"


def raiz_slug(slug):
    """Slug sin carpeta, sin extension y sin el prefijo de familia."""
    s = slug.lower().rsplit("/", 1)[-1]
    s = re.sub(r"\.(asp|aspx|html?|php)$", "", s)
    for p in PREFIJOS:
        if s.startswith(p):
            s = s[len(p):]
            break
    return re.sub(r"[-_]+", " ", s).strip()


def _palabras(r):
    return [C.singular(p) for p in r.split() if p]


def variante(a, b):
    """True si los dos slugs son la misma cosa escrita de otra forma."""
    if a == b:
        return True
    pa, pb = _palabras(a), _palabras(b)
    if pa == pb:                                   # singular / plural
        return True
    corto, largo = sorted((pa, pb), key=len)
    if corto and largo[:len(corto)] == corto:      # '..._telefonia_sat'
        return True
    return difflib.SequenceMatcher(None, a, b).ratio() >= 0.86


def clasificar(paginas):
    """Veredicto de un subgrupo de UN SOLO dominio.

    Antes esto miraba lo primero si habia mas de un dominio y devolvia CRUZADO,
    y era un error: una sola pagina del otro dominio envenenaba el grupo entero
    y escondia un duplicado interno evidente. 'index.asp' e 'index.html', que
    son la misma portada y ya llevan un 301 vivo, acababan clasificadas como
    "decide el cliente" solo porque la portada de carrito5 caia en el grupo.

    Son dos problemas independientes en el mismo grupo: uno se arregla con un
    301 hoy y el otro es una decision de negocio. Asi que el grupo se parte por
    dominio y cada parte tiene su veredicto.
    """
    if len({familia(p[1]) for p in paginas}) > 1:
        return "SEPARAR"
    raices = [raiz_slug(p[1]) for p in paginas]
    # Todas contra la primera: el grupo ya es una componente conexa.
    if all(variante(raices[0], r) for r in raices[1:]):
        return "SEGURO"
    if titulo_repetido(paginas):
        return "TITULO"
    return "REVISAR"


def titulo_repetido(paginas):
    """True si dos paginas del grupo llevan exactamente el mismo <title>.

    Es la senal mas dura que hay aqui, y no sale del agrupador sino de una
    persona: el parecido semantico es una medida con umbral y esto es una
    igualdad. Quien escribio la web puso el mismo titulo a las dos paginas, o
    sea que para el sirven lo mismo. En la SERP se ve todavia peor, porque el
    usuario ve dos resultados con el mismo texto.
    """
    vistos = set()
    for _, _, titulo, _ in paginas:
        t = " ".join(titulo.split()).lower()
        if not t:
            continue
        if t in vistos:
            return True
        vistos.add(t)
    return False


def ganadora(paginas):
    """Determinista a proposito: las dos cuentas deben calcular lo mismo."""
    bases = {p[1].rsplit("/", 1)[-1]: p for p in paginas}
    for origen, destino in YA_DECIDIDO.items():
        if origen in bases and destino in bases:
            return bases[destino]                  # manda el sitio, no el criterio
    def clave(p):
        _, slug, _, palabras = p
        base = slug.rsplit("/", 1)[-1]
        # -1 deja las no medibles al final sin reventar la comparacion.
        return (-(palabras if palabras is not None else -1),
                "_" in base, len(base), base)
    return sorted(paginas, key=clave)[0]


def leer(rutas):
    out = []
    for r in rutas:
        with open(r, encoding="utf-8") as fh:
            fh.readline()
            for linea in fh:
                c = linea.rstrip("\n").split("\t")
                if len(c) < 5:
                    continue
                sitio, slug, titulo = c[0], c[1], c[2]
                if slug.rsplit("/", 1)[-1] in NO_CONTENIDO:
                    continue
                # Ojo: columna vacia NO es "pagina vacia". El inventario de
                # carrito5 se reconstruyo del indice de busqueda porque el
                # proxy bloquea el dominio, asi que no trae recuento. Tratarlo
                # como cero descartaba el dominio entero y con el las
                # canibalizaciones cruzadas, que son las que mas duelen.
                bruto = c[4].strip()
                if bruto == "":
                    palabras = None                       # no medible
                else:
                    try:
                        palabras = int(bruto)
                    except ValueError:
                        palabras = None
                    if palabras == 0:                     # medido y vacio
                        continue
                out.append((sitio, slug, titulo, palabras))
    return out


ORDEN = {"SEGURO": 0, "TITULO": 1, "REVISAR": 2, "SEPARAR": 3, "CRUZADO": 4}


def analizar(rutas):
    paginas = leer(rutas)
    indice = {p[1] + "\x00" + p[0]: p for p in paginas}
    # El tema de una pagina es su SLUG, no su titulo. Es la trampa nº 5 de
    # motor/README.md y aqui la tenia yo viva: pegarle el titulo al slug mete
    # el detalle comercial en el nucleo, la cobertura asimetrica lee ese
    # detalle como acotacion, y dos paginas que hablan de lo mismo dejan de
    # agruparse. Medido con lavanderia: por slug se parecen 1,000 y con el
    # titulo pegado 0,333, por debajo del umbral de 0,50.
    #
    # El titulo no se pierde: entra por titulo_repetido(), que es igualdad
    # exacta y no similitud, y ahi si es la senal mas dura del analisis.
    grupos, nuc = C.agrupar({k: v[1] for k, v in indice.items()})

    salida = []
    for claves in grupos:
        if len(claves) < 2:
            continue
        pgs = sorted((indice[k] for k in claves), key=lambda p: p[1])
        etiq = C.etiqueta(claves, nuc)

        # Un grupo puede llevar dos problemas distintos a la vez, y se arreglan
        # de forma distinta, asi que se informan por separado: el duplicado
        # dentro de un dominio se cierra con un 301 hoy, y la competencia entre
        # los dos dominios la decide el cliente. Mezclarlos escondia el
        # primero: bastaba una pagina de carrito5 en el grupo para que
        # 'index.asp' e 'index.html', que son la misma portada, salieran como
        # "decide el cliente".
        por_dominio = {}
        for p in pgs:
            por_dominio.setdefault(p[0], []).append(p)

        for sitio in sorted(por_dominio):
            sub = por_dominio[sitio]
            if len(sub) >= 2:
                salida.append((etiq, clasificar(sub), sub))
        if len(por_dominio) > 1:
            salida.append((etiq, "CRUZADO", pgs))

    salida.sort(key=lambda x: (ORDEN[x[1]], x[0]))
    return salida


CABECERA = {
    "SEGURO":  ("SE FUSIONAN — sobra una pagina, 301 a la ganadora",
                "Los slugs son variantes del mismo. No hay decision editorial."),
    "TITULO":  ("CONFIRMADA — las dos paginas llevan el mismo <title>",
                "No es el agrupador: el titulo lo escribio una persona, igual en las dos."),
    "REVISAR": ("HAY QUE DECIDIR — negocios parecidos, no identicos",
                "El agrupador los unio por vecindad. Fusionar es decision de negocio."),
    "SEPARAR": ("NO SE TOCAN — distinta etapa del embudo",
                "Comparten palabras pero no compiten. Enlazarlas entre si."),
    "CRUZADO": ("DECIDE EL CLIENTE — dominios distintos",
                "Un 301 aqui regala un dominio al otro. Los dos son suyos."),
}


def titulos_repetidos_sueltos(rutas, grupos):
    """Paginas con el mismo <title> que NO salen en ningun grupo de arriba.

    El agrupador mira el tema, asi que dos paginas de temas distintos con el
    mismo titulo se le escapan, y ese caso no es menor: normalmente significa
    que alguien copio una pagina para hacer otra y se dejo el titulo puesto.
    En la SERP el usuario ve dos resultados con el mismo texto sin que las
    paginas tengan nada que ver.
    """
    en_grupo = {p[1] for _, _, pgs in grupos for p in pgs}
    por_titulo = {}
    for sitio, slug, titulo, _ in leer(rutas):
        t = " ".join(titulo.split()).lower()
        if t:
            por_titulo.setdefault(t, []).append((sitio, slug))
    fuera = []
    for t, pgs in sorted(por_titulo.items()):
        if len(pgs) < 2:
            continue
        if all(s in en_grupo for _, s in pgs):
            continue                      # ya sale arriba, no se repite
        fuera.append((pgs[0][0], t, pgs))
    return fuera


def informe(grupos):
    L = []
    tot = {k: 0 for k in CABECERA}
    for _, tipo, _ in grupos:
        tot[tipo] += 1
    L.append("CANIBALIZACION")
    L.append("  grupos con mas de una pagina: %d" % len(grupos))
    for t in ("SEGURO", "TITULO", "REVISAR", "SEPARAR", "CRUZADO"):
        L.append("    %-8s %3d" % (t, tot[t]))
    L.append("")

    actual = None
    for etiq, tipo, pgs in grupos:
        if tipo != actual:
            actual = tipo
            tit, sub = CABECERA[tipo]
            L.append("")
            L.append("%s  %s" % (tipo, tit))
            L.append("   %s" % sub)
            L.append("")
        gana = ganadora(pgs) if tipo == "SEGURO" else None
        # El titulo repetido se marca siempre, aunque el veredicto sea otro.
        # Si un grupo es CRUZADO porque entra una pagina del otro dominio, el
        # que dos paginas de este lleven el mismo titulo no deja de ser cierto,
        # y sin marcarlo se perdia dentro del cajon de "decide el cliente".
        marca_t = "   !! mismo <title>" if titulo_repetido(pgs) else ""
        L.append("   [%s]%s" % (etiq, marca_t))
        for sitio, slug, titulo, palabras in pgs:
            marca = "  <- GANA" if gana and slug == gana[1] else ""
            cuenta = "    ? pal" if palabras is None else "%5d pal" % palabras
            L.append("      %-12s %-46s %s%s" % (sitio, slug, cuenta, marca))
        L.append("")
    return "\n".join(L)


PLANTILLA = '''#!/usr/bin/env python3
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
%s}
'''


def escribir_modulo(grupos, destino):
    pares = []
    for _, tipo, pgs in grupos:
        if tipo != "SEGURO":
            continue
        # Red de seguridad, no comprobacion defensiva de adorno: editando este
        # fichero deje de mirar el dominio dentro de clasificar() y el informe
        # empezo a dar por SEGURO pares como negocio_bicicletas.asp con
        # tpv-tienda-bicicletas.html. Eso escrito en el web.config es un 301 de
        # un dominio del cliente al otro, o sea regalarle un dominio entero al
        # otro. No lo vi leyendo la salida; lo vio una comprobacion como esta.
        dominios = {p[0] for p in pgs}
        if len(dominios) > 1:
            raise SystemExit(
                "ABORTADO: el grupo SEGURO %r tiene paginas de %s. Un 301 entre\n"
                "dominios distintos no se escribe nunca desde aqui." %
                (pgs[0][1], " y ".join(sorted(dominios))))
        gana = ganadora(pgs)
        for sitio, slug, _, _ in pgs:
            if slug != gana[1]:
                pares.append((slug, gana[1]))
    pares.extend(RESCATES.items())
    pares.sort()
    cuerpo = "".join('    %-46s %s,\n' % ('"%s":' % o, '"%s"' % d) for o, d in pares)
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write(PLANTILLA % cuerpo)
    return len(pares)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--escribir"]
    if not args:
        print(__doc__.split("\n\n")[1].strip())
        sys.exit(1)
    g = analizar(args)
    print(informe(g))
    sueltos = titulos_repetidos_sueltos(args, g)
    if sueltos:
        print("")
        print("TITULO  EL MISMO <title> FUERA DE TODO GRUPO")
        print("   Temas distintos y titulo igual: alguien copio una pagina y se")
        print("   dejo el titulo. Se arregla escribiendo el que le toca.")
        print("")
        for _, titulo, pgs in sueltos:
            print("   \"%s\"" % titulo)
            for sitio, slug in pgs:
                print("      %-12s %s" % (sitio, slug))
            print("")
    if "--escribir" in sys.argv:
        d = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "redirecciones_301.py")
        print("redirecciones escritas en %s: %d" % (os.path.basename(d),
                                                    escribir_modulo(g, d)))

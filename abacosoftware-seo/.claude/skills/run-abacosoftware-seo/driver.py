#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Driver del pipeline SEO de abacosoftware.com.

Un solo punto de entrada para construir, verificar y previsualizar el sitio.
No hace falta IIS: `preview` resuelve los includes ASP y sirve el HTML resultante
para poder abrirlo en Chromium y hacerle una captura.

    python3 driver.py build    --base <dir-web>      genera todas las paginas
    python3 driver.py gate     --base <dir-web>      filtro de similitud
    python3 driver.py validate --base <dir-web>      auditoria SEO
    python3 driver.py preview  --base <dir-web> --page negocio_ferreteria.asp
    python3 driver.py stats    --base <dir-web>
    python3 driver.py audit    --base <dir-web> [--original <dir>]   calidad: titulos, longitud, enlazado
    python3 driver.py package  --base <dir-web> --out sitio.zip
    python3 driver.py smoke                          build+gate+validate sobre una web sintetica

`--base` es el directorio con la web (el ZIP del cliente descomprimido).
El pipeline modifica ese directorio in situ: trabaja siempre sobre una copia.

`smoke` no necesita la web del cliente: monta en un temporal los cuatro
ficheros que el pipeline espera encontrar, construye encima y pasa gate y
validate. Es la forma de saber que un cambio en los generadores no ha roto
nada antes de tocar material real.
"""
import argparse, functools, glob, http.server, os, shutil, socketserver, subprocess, sys, tempfile, threading

RAIZ = os.path.dirname(os.path.realpath(__file__))
UNIT = os.path.abspath(os.path.join(RAIZ, "..", "..", ".."))       # abacosoftware-seo/
PIPE = os.path.join(UNIT, "pipeline")
CONT = os.path.join(UNIT, "contenido")
sys.path.insert(0, PIPE)
import sitio                                              # noqa: E402  (deja motor/ en sys.path)
import consola, gate, marcado as M                        # noqa: E402

consola.tuberias()

CHROME_GLOB = "/opt/pw-browsers/chromium*/chrome-linux/chrome"
MAX_TITLE, MAX_DESC = 65, 165


# ----------------------------------------------------------------- utilidades
def correr(script, *args, cwd=None):
    """Ejecuta un script del pipeline con el cwd que espera.

    Los modulos del directorio de trabajo son enlaces simbolicos, y Python
    resuelve el enlace para fijar sys.path[0], que acaba apuntando al destino
    real en lugar de al temporal. Por eso hay que forzar PYTHONPATH.
    """
    env = dict(os.environ, PYTHONPATH=cwd or "")
    r = subprocess.run([sys.executable, script, *args], cwd=cwd,
                       capture_output=True, text=True, env=env)
    if r.returncode != 0:
        print(f"  !! fallo {os.path.basename(script)}:\n{r.stderr[-1200:]}")
    return r.stdout.strip()


def entorno(base):
    """Los scripts del pipeline esperan './site' como directorio de salida.

    Se monta un directorio de trabajo temporal con enlaces simbolicos a los
    modulos y un 'site' que apunta al directorio base real.
    """
    tmp = tempfile.mkdtemp(prefix="abaco-pipe-")
    for f in glob.glob(os.path.join(PIPE, "*.py")) + glob.glob(os.path.join(CONT, "*.py")):
        os.symlink(f, os.path.join(tmp, os.path.basename(f)))
    os.symlink(os.path.join(UNIT, "plantilla.py"), os.path.join(tmp, "plantilla.py"))
    os.symlink(os.path.abspath(base), os.path.join(tmp, "site"))
    return tmp


def ultima_linea(texto):
    return ([l for l in texto.splitlines() if l.strip()] or [""])[-1]


# --------------------------------------------------------------------- build
GENERADORES = [
    ("gen_sectores.py", ["site", "sectores_1", "sectores_2", "sectores_3"]),
    ("gen_funciones.py", ["site"]),
    ("gen_verifactu.py", ["site"]),
    ("gen_faq_hub.py", ["site"]),
    ("gen_generico.py", ["abrir_1", "abrir_2", "operativa_1", "operativa_2", "vs_1", "vs_2", "normativa_1"]),
    ("gen_hubs2.py", []),
]


def cmd_build(a):
    tmp = entorno(a.base)
    try:
        print("== capa tecnica ==")
        print(" ", correr(os.path.join(tmp, "seo_tech.py"), "site", cwd=tmp)[:200])
        print("== generadores de contenido ==")
        for script, args in GENERADORES:
            out = correr(os.path.join(tmp, script), *args, cwd=tmp)
            print(f"  {script:22} {ultima_linea(out)[:90]}")
        print("== limpieza y metadatos ==")
        correr(os.path.join(tmp, "limpiar_copy.py"), "site", cwd=tmp)
        print(" ", correr(os.path.join(tmp, "fix_metadatos.py"), "site", cwd=tmp)[:160])
        print(" ", correr(os.path.join(tmp, "recortar_titulos.py"), "site", cwd=tmp)[:200])
        print("== enlazado y sitemap ==")
        print(" ", correr(os.path.join(tmp, "enlazado_y_sitemap.py"), "site", cwd=tmp)[:300])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return cmd_stats(a)


# ---------------------------------------------------------------------- gate
def cmd_gate(a):
    fs = sitio.paginas(a.base)
    if a.original:
        viejas = {os.path.basename(f) for f in glob.glob(os.path.join(a.original, "*.asp"))}
        fs = [f for f in fs if os.path.basename(f) not in viejas]
    return 1 if gate.informe(fs) else 0


# ------------------------------------------------------------------ validate
def auditar(fichero):
    """Lista de defectos SEO de una pagina. Vacia si esta bien."""
    s, b = M.leer(fichero), os.path.basename(fichero)
    t, d = M.titulo(s), M.meta(s, "description")
    fallos = []
    if not t:
        fallos.append("sin title")
    elif len(t) > MAX_TITLE:
        fallos.append(f"title > {MAX_TITLE}")
    if not d:
        fallos.append("sin description")
    elif len(d) > MAX_DESC:
        fallos.append(f"desc > {MAX_DESC}")
    if not M.canonical(s):
        fallos.append("sin canonical")
    if not M.meta(s, "og:title"):
        fallos.append("sin og")
    lds = M.bloques_ld(s)
    if any(obj is None for _, _, obj in lds):
        fallos.append("LD roto")
    if b != "index.asp" and not any(obj and obj.get("@type") == "BreadcrumbList" for _, _, obj in lds):
        fallos.append("sin breadcrumb")
    if M.h1s(s) != 1:
        fallos.append("H1 != 1")
    return fallos, sum(len(obj.get("mainEntity", [])) for _, _, obj in lds
                       if obj and obj.get("@type") == "FAQPage")


def cmd_validate(a):
    fs = sitio.paginas(a.base)
    por_tipo, faqs = {}, 0
    for f in fs:
        fallos, n = auditar(f)
        faqs += n
        for k in fallos:
            por_tipo.setdefault(k, []).append(os.path.basename(f))
    print(f"  paginas: {len(fs)}   preguntas con schema FAQ: {faqs}")
    total = 0
    for k in ("sin title", "sin description", "sin canonical", "sin og", "sin breadcrumb",
              "H1 != 1", f"title > {MAX_TITLE}", f"desc > {MAX_DESC}", "LD roto"):
        v = por_tipo.get(k, [])
        total += len(v)
        print(f"   {'!!' if v else 'ok'} {k:16} {len(v):4}  {', '.join(v[:4])}")
    sm = os.path.join(a.base, "sitemap.xml")
    if os.path.exists(sm):
        urls = M.leer(sm).count("<loc>")
        faltan = [u for u in __import__("re").findall(r"<loc>" + sitio.BASE + r"/([^<]*)</loc>", M.leer(sm))
                  if u and not os.path.exists(os.path.join(a.base, u))]
        print(f"   {'!!' if faltan else 'ok'} sitemap: {urls} URLs, {len(faltan)} apuntan a ficheros inexistentes")
        total += len(faltan)
    return 1 if total else 0


# ------------------------------------------------------------------- preview
INC = __import__("re").compile(r'<!--#include\s+virtual="([^"]+)"\s*-->')


def resolver_asp(base, fichero, profundidad=0):
    """Resuelve includes ASP y elimina el codigo <% %> para poder ver el HTML."""
    ruta = os.path.join(base, fichero.lstrip("/"))
    if not os.path.exists(ruta) or profundidad > 4:
        return ""
    s = INC.sub(lambda m: resolver_asp(base, m.group(1), profundidad + 1), M.leer(ruta))
    return __import__("re").sub(r"<%.*?%>", "", s, flags=16)


def cmd_preview(a):
    chrome = sorted(glob.glob(CHROME_GLOB))
    if not chrome:
        print("  !! no encuentro chromium en", CHROME_GLOB)
        return 1
    salida = os.path.abspath(a.out or "preview.png")
    destino = os.path.join(a.base, "__preview__.html")     # dentro de la web: css/js/img resuelven
    try:
        M.escribir(destino, resolver_asp(a.base, a.page))
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=a.base)
        socketserver.TCPServer.allow_reuse_address = True
        srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        url = f"http://127.0.0.1:{srv.server_address[1]}/__preview__.html"
        print(f"  sirviendo {a.page} en {url}")
        r = subprocess.run([chrome[-1], "--headless", "--disable-gpu", "--no-sandbox",
                            "--hide-scrollbars", f"--window-size={a.width},{a.height}",
                            f"--screenshot={salida}", "--virtual-time-budget=6000", url],
                           capture_output=True, text=True, timeout=120)
        srv.shutdown()
        if not os.path.exists(salida):
            print("  !! chromium no genero captura:\n", r.stderr[-800:])
            return 1
        print(f"  captura: {salida}  ({os.path.getsize(salida)//1024} KB)")
        return 0
    finally:
        if os.path.exists(destino):
            os.remove(destino)


# --------------------------------------------------------------------- stats
def cmd_stats(a):
    fs = sitio.paginas(a.base)
    total = sum(len(M.texto_visible(M.leer(f)).split()) for f in fs)
    sm = os.path.join(a.base, "sitemap.xml")
    urls = M.leer(sm).count("<loc>") if os.path.exists(sm) else 0
    print(f"  paginas indexables : {len(fs)}")
    print(f"  palabras visibles  : {total:,}".replace(",", "."))
    print(f"  URLs en sitemap    : {urls}")
    return 0


# ------------------------------------------------------------------- package
def cmd_package(a):
    out = os.path.abspath(a.out or "sitio.zip")
    if os.path.exists(out):
        os.remove(out)
    r = subprocess.run(["zip", "-q", "-r", "-X", out, ".",
                        "-x", "*.DS_Store", "Thumbs.db", "*/Thumbs.db", "__preview__.html"],
                       cwd=a.base, capture_output=True, text=True)
    if r.returncode != 0:
        print("  !! zip fallo:", r.stderr[-400:])
        return 1
    print(f"  {out}  ({os.path.getsize(out)//1024//1024} MB)")
    return 0


# --------------------------------------------------------------------- audit
def cmd_audit(a):
    """Lo que validate no mira: paginas cortas, titulos y descriptions que se
    parecen entre si, coletillas repetidas, enlazado entrante y enlaces rotos.
    Informa; no falla. Con --original se limita a las paginas nuevas."""
    import collections, itertools, re
    fs = sitio.paginas(a.base)
    if a.original:
        viejas = {os.path.basename(f) for f in glob.glob(os.path.join(a.original, "*.asp"))}
        fs = [f for f in fs if os.path.basename(f) not in viejas]
    todas = {os.path.basename(f) for f in sitio.paginas(a.base)}
    # La web real tiene 198 paginas que en una construccion parcial (smoke) no
    # estan: el inventario del repositorio cuenta como existente.
    inv = os.path.join(os.path.dirname(UNIT), "inventarios", "abacosoftware.tsv")
    if os.path.exists(inv):
        todas |= {l.split("\t")[1] for l in M.leer(inv).splitlines()[1:] if "\t" in l}
    d = {}
    for f in fs:
        s = M.leer(f)
        lds = [o for _, _, o in M.bloques_ld(s) if o]
        d[os.path.basename(f)] = dict(
            t=M.titulo(s), desc=M.meta(s, "description"), n=len(M.texto_visible(s).split()),
            faqs=sum(len(o.get("mainEntity", [])) for o in lds if o.get("@type") == "FAQPage"),
            enlaces=set(re.findall(r'href="/?([a-z0-9_\-]+\.asp)', s)))
    if not d:
        print("  nada que auditar")
        return 0
    voc = lambda t: frozenset(re.findall(r"[a-záéíóúüñ0-9]+", t.lower()))
    print(f"  paginas auditadas: {len(d)}\n")
    print("  mas cortas (palabras visibles, el menu y el pie suman unas 250):")
    for b, x in sorted(d.items(), key=lambda kv: kv[1]["n"])[:8]:
        print(f"   {x['n']:5}  faqs={x['faqs']:2}  {b}")
    for campo, etiqueta, umbral in (("t", "titulos", 0.6), ("desc", "descriptions", 0.45)):
        sims = sorted(((gate.jaccard(voc(d[x][campo]), voc(d[y][campo])), x, y)
                       for x, y in itertools.combinations(d, 2)), reverse=True)
        malos = [s for s in sims if s[0] >= umbral]
        media = sum(s[0] for s in sims) / len(sims) if sims else 0
        print(f"\n  {'!!' if malos else 'ok'} {etiqueta}: media {media:.2f}, "
              f"{len(malos)} pares con {umbral} o mas")
        for j, x, y in malos[:5]:
            print(f"     {j:.2f}  {x} <-> {y}\n           {d[x][campo][:80]}\n           {d[y][campo][:80]}")
    for etiqueta, corte in (("cierres de description repetidos", lambda t: " ".join(t.lower().split()[-4:])),
                            ("arranques de title repetidos (3 palabras)", lambda t: " ".join(t.lower().split()[:3]))):
        campo = "desc" if "description" in etiqueta else "t"
        rep = [(c, n) for c, n in collections.Counter(corte(x[campo]) for x in d.values()).most_common(5) if n > 2]
        # informativo: "como abrir una" x9 es la intencion de las guias, no una plantilla
        print(f"\n  {'--' if rep else 'ok'} {etiqueta}: {len(rep)}")
        for c, n in rep:
            print(f"     {n}x  {c}")
    largos = [(b, len(x["t"]), len(x["desc"])) for b, x in d.items() if len(x["t"]) > 60 or len(x["desc"]) > 158]
    print(f"\n  {'!!' if largos else 'ok'} title > 60 o description > 158 (Google corta ahi): {len(largos)}")
    for b, lt, ld in sorted(largos)[:8]:
        print(f"     title={lt} desc={ld}  {b}")
    entrantes = collections.Counter(e for b, x in d.items() for e in x["enlaces"] if e in d and e != b)
    solas = [b for b in sorted(d) if entrantes[b] <= 1]
    print(f"\n  {'!!' if solas else 'ok'} con un enlace entrante o ninguno desde las demas: {len(solas)}")
    for b in solas[:10]:
        print(f"     {entrantes[b]}  {b}")
    rotos = collections.Counter(e for x in d.values() for e in x["enlaces"] if e not in todas)
    print(f"\n  {'!!' if rotos else 'ok'} enlaces a .asp que no existen en la web: {len(rotos)}")
    for e, n in rotos.most_common(10):
        print(f"     {n}x  {e}")
    return 0


# --------------------------------------------------------------------- smoke
SINTETICO = {
    "index.asp": """<!DOCTYPE html><html lang="es"><head><title>Caja 5 TPV | Ábaco Software</title>
<meta name="description" content="Portada sintética para probar el pipeline.">
<link rel="canonical" href="https://www.abacosoftware.com/"></head>
<body><div id="menu-contenedor"><!--#include virtual="/menu_nav.asp"--></div>
<h1>Portada</h1><p>Texto de portada.</p></body></html>""",
    "menu_nav.asp": """<nav><div class="dropdown-header">EQUIPAMIENTO Y GUÍAS RETAIL</div>
<a href="/tpv_negocios.asp">Sectores</a></nav>""",
    "tpv_negocios.asp": """<!DOCTYPE html><html lang="es"><head><title>TPV por sector | Caja 5</title>
<meta name="description" content="Hub sintético de sectores."><link rel="canonical" href="https://www.abacosoftware.com/tpv_negocios.asp"></head>
<body><h1>Sectores</h1><section><div class="container"><div class="row"><a href="/negocio_moda.asp">Moda</a></div></div></section></body></html>""",
    "web.config": """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <rewrite>
            <rules>
            </rules>
        </rewrite>
    </system.webServer>
</configuration>""",
}


def cmd_smoke(a):
    base = tempfile.mkdtemp(prefix="abaco-smoke-")
    for n, s in SINTETICO.items():
        M.escribir(os.path.join(base, n), s)
    orig = tempfile.mkdtemp(prefix="abaco-smoke-orig-")
    for n in SINTETICO:
        M.escribir(os.path.join(orig, n), SINTETICO[n])
    a.base, a.original = base, orig
    try:
        print(f"== smoke: web sintetica en {base} ==")
        cmd_build(a)
        print("== gate (solo paginas nuevas) ==")
        g = cmd_gate(a)
        print("== validate ==")
        v = cmd_validate(a)
        print("== audit ==")
        cmd_audit(a)
        print(f"\n  smoke {'OK' if not (g or v) else 'FALLA'}: gate={g} validate={v}")
        return 1 if (g or v) else 0
    finally:
        if a.keep:
            print(f"  (se conserva {base})")
        else:
            shutil.rmtree(base, ignore_errors=True)
        shutil.rmtree(orig, ignore_errors=True)


CMDS = {"build": cmd_build, "gate": cmd_gate, "validate": cmd_validate, "audit": cmd_audit,
        "preview": cmd_preview, "stats": cmd_stats, "package": cmd_package, "smoke": cmd_smoke}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=CMDS)
    ap.add_argument("--base", help="directorio de la web (obligatorio salvo en smoke)")
    ap.add_argument("--original", help="directorio de la web sin tocar (para gate)")
    ap.add_argument("--page", default="index.asp", help="pagina a previsualizar")
    ap.add_argument("--out", help="fichero de salida (captura o zip)")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=1600)
    ap.add_argument("--keep", action="store_true", help="smoke: no borrar la web sintetica al acabar")
    a = ap.parse_args()
    if a.cmd != "smoke" and not (a.base and os.path.isdir(a.base)):
        print("  !! --base no es un directorio:", a.base)
        return 2
    return CMDS[a.cmd](a) or 0


if __name__ == "__main__":
    sys.exit(main())

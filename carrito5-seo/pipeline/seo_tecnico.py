#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capa tecnica SEO de carrito5.com: redirecciones, robots, sitemap y llms.txt.

Uso: python3 seo_tecnico.py <dir-salida> [<fichero-urls-vivas>]

Escribe en <dir-salida>:

  web.config      reglas 301 para IIS (el sitio sirve pg/*.asp, asi que es IIS).
                  Si el servidor ya tiene web.config, se copia solo el bloque
                  <rewrite> dentro de <system.webServer>.
  .htaccess       las mismas reglas por si el hosting fuera Apache.
  robots.txt      permite todo, declara el sitemap y no bloquea a los
                  rastreadores de los motores generativos.
  sitemap.xml     URLs vivas (inventario) + paginas generadas, sin las que
                  se redirigen y sin las que no deben indexarse.
  llms.txt        indice en Markdown para motores generativos (llmstxt.org):
                  quien es Carrito5, que hace, y las paginas que responden a
                  cada pregunta, con su descripcion.

Las decisiones de redireccion vienen de INFORME_CARRITO5.md:
  - singular/plural de instrumentos: se queda la singular (titulo con tilde).
  - tpv_gratis_verifactu_bonito.html: prueba publicada; compite con
    verifactu-gratis.html.
  - dos esquemas de URL de ciudad en Zaragoza y Malaga: se queda tpv-<ciudad>.
"""
import glob, html, os, re, sys
from datetime import date

DOMINIO = "https://www.carrito5.com"

# origen -> destino (rutas relativas a la raiz del sitio)
REDIRECCIONES = {
    "tpv-tiendas-instrumentos-musica.html": "tpv-tienda-instrumentos-musica.html",
    "tpv_gratis_verifactu_bonito.html": "verifactu-gratis.html",
    "software-tpv-zaragoza-centro-delicias.html": "tpv-zaragoza.html",
    "software-tpv-malaga-larios-centro.html": "tpv-malaga.html",
    "index.html": "",   # portada canonica en /
}

# Paginas que existen pero no deben ir al sitemap (legales, sin valor de busqueda)
NO_SITEMAP = {"pg/terminos.asp", "pg/condiciones.asp"}

# prioridad y frecuencia por patron de URL; el primero que casa gana
PRIORIDAD = [
    (r"^$", ("1.0", "weekly")),
    (r"^descargar-tpv-gratis\.html$", ("0.9", "weekly")),
    (r"^verifactu-gratis\.html$", ("0.9", "weekly")),
    (r"^mejor-tpv-gratis-2026\.html$", ("0.9", "weekly")),
    (r"^tpv-madrid\.html$", ("0.8", "monthly")),
    (r"^(sectores-y-negocios|software-tpv-comercio-local|sobre-carrito5|tallas-y-colores)\.html$", ("0.8", "monthly")),
    (r"^(verifactu|ley-|factura-|programa-caja|tpv-gratis-autonomos)", ("0.8", "monthly")),
    (r"^(tpv-|software-tpv-|programa-)", ("0.7", "monthly")),
    (r"^blog", ("0.6", "monthly")),
    (r"^preguntas-frecuentes", ("0.6", "monthly")),
]


def prioridad(ruta):
    for pat, v in PRIORIDAD:
        if re.search(pat, ruta):
            return v
    return ("0.5", "monthly")


def urls_vivas(fichero):
    if not fichero or not os.path.exists(fichero):
        return []
    out = []
    for l in open(fichero, encoding="utf-8"):
        l = l.strip()
        if not l:
            continue
        out.append(re.sub(r"^https?://(www\.)?carrito5\.com/", "", l))
    return out


def paginas_generadas(salida):
    out = []
    for p in glob.glob(os.path.join(salida, "*.html")):
        out.append(os.path.basename(p))
    for p in glob.glob(os.path.join(salida, "blog", "*.html")):
        if not os.path.basename(p).startswith("_"):
            out.append("blog/" + os.path.basename(p))
    return out


def meta(fichero):
    """title y description de una pagina generada, para el llms.txt."""
    try:
        s = open(fichero, encoding="utf-8").read()
    except OSError:
        return "", ""
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
    return (html.unescape(t.group(1)).strip() if t else "",
            html.unescape(d.group(1)).strip() if d else "")


# ------------------------------------------------------------------ web.config
def web_config():
    reglas = []
    for i, (o, d) in enumerate(REDIRECCIONES.items()):
        reglas.append(f"""        <rule name="301-{i:02d}-{re.sub(r'[^a-z0-9]', '-', o.lower())}" stopProcessing="true">
          <match url="^{re.escape(o)}$" />
          <action type="Redirect" url="{DOMINIO}/{d}" redirectType="Permanent" />
        </rule>""")
    reglas_txt = "\n".join(reglas)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!--
  Redirecciones 301 de carrito5.com. Generado por carrito5-seo/pipeline/seo_tecnico.py.
  Si el servidor ya tiene un web.config, copiar solo el bloque <rewrite> dentro
  de <system.webServer>. Requiere el modulo URL Rewrite de IIS.
-->
<configuration>
  <system.webServer>
    <rewrite>
      <rules>
        <rule name="www-y-https" stopProcessing="true">
          <match url="(.*)" />
          <conditions logicalGrouping="MatchAny">
            <add input="{{HTTPS}}" pattern="off" />
            <add input="{{HTTP_HOST}}" pattern="^carrito5\\.com$" />
          </conditions>
          <action type="Redirect" url="{DOMINIO}/{{R:1}}" redirectType="Permanent" />
        </rule>
{reglas_txt}
      </rules>
    </rewrite>
  </system.webServer>
</configuration>
"""


def htaccess():
    lineas = ["# Redirecciones 301 de carrito5.com (equivalente Apache del web.config)",
              "RewriteEngine On",
              "RewriteCond %{HTTPS} off [OR]",
              "RewriteCond %{HTTP_HOST} ^carrito5\\.com$ [NC]",
              f"RewriteRule ^(.*)$ {DOMINIO}/$1 [R=301,L]"]
    for o, d in REDIRECCIONES.items():
        lineas.append(f"RewriteRule ^{re.escape(o)}$ {DOMINIO}/{d} [R=301,L]")
    return "\n".join(lineas) + "\n"


# ------------------------------------------------------------------ robots.txt
def robots():
    return f"""# carrito5.com
User-agent: *
Allow: /
Disallow: /_propuestas/
Disallow: /_retirados/

# Rastreadores de motores generativos: se permiten a proposito. Queremos que
# ChatGPT, Perplexity, Gemini y Claude puedan citar estas paginas.
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: {DOMINIO}/sitemap.xml
"""


# ------------------------------------------------------------------ sitemap
def sitemap(rutas):
    hoy = date.today().isoformat()
    items = []
    for r in sorted(set(rutas), key=lambda x: (prioridad(x)[0] != "1.0", x)):
        p, f = prioridad(r)
        items.append(f"  <url>\n    <loc>{DOMINIO}/{r}</loc>\n    <lastmod>{hoy}</lastmod>"
                     f"\n    <changefreq>{f}</changefreq>\n    <priority>{p}</priority>\n  </url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(items) + "\n</urlset>\n")


# ------------------------------------------------------------------ llms.txt
SECCIONES_LLMS = [
    ("Empezar", ["", "descargar-tpv-gratis.html", "sobre-carrito5.html", "mejor-tpv-gratis-2026.html",
                 "software-tpv-comercio-local.html", "tpv-gratis-autonomos.html",
                 "programa-caja-registradora-gratis.html"]),
    ("VeriFactu y normativa", ["verifactu-gratis.html", "verifactu-entrada-en-vigor.html",
                               "verifactu-autonomos.html", "verifactu-aeat-descargar.html",
                               "ley-crea-y-crece-facturacion.html", "verifactu-ley-antifraude-rd1007-2023.html",
                               "verifactu-sin-conexion-internet-offline.html", "factura-simplificada-ticket.html",
                               "preguntas-frecuentes-verifactu-ley-antifraude.html"]),
    ("Funciones", ["tallas-y-colores.html", "preguntas-frecuentes-operativa-caja-tienda.html",
                   "blog/como-hacer-arqueo-de-caja-cierre-z.html"]),
    ("Ciudades", ["tpv-madrid.html", "software-tpv-barcelona.html", "software-tpv-valencia.html",
                  "software-tpv-sevilla-centro-tetuan.html", "tpv-malaga.html",
                  "software-tpv-bilbao-gran-via-casco-viejo.html", "tpv-zaragoza.html",
                  "tpv-palma-de-mallorca.html", "tpv-alicante.html", "tpv-murcia.html", "tpv-vigo.html",
                  "software-tpv-sabadell-terrassa.html"]),
]


def llms(rutas, salida, titulos_vivos):
    """titulos_vivos: {ruta: titulo} del inventario, para las paginas que no
    se han generado aqui y de las que solo conocemos el titulo."""
    def linea(r):
        t, d = meta(os.path.join(salida, r)) if r else ("", "")
        if not t:
            t = titulos_vivos.get(r, r) if r else "Carrito5: software TPV gratis para Windows, adaptado a VeriFactu"
        t = re.sub(r"\s*[|·-]\s*Carr.*$", "", t).strip()
        url = f"{DOMINIO}/{r}"
        return f"- [{t}]({url})" + (f": {d}" if d else "")

    usadas = set()
    out = [f"# Carrito5",
           "",
           "> Carrito5 es un programa TPV (punto de venta) gratuito para Windows, hecho en España por "
           "Ábaco Infoelectrónica S.L. (Jaén), fabricante de software de caja para comercio desde hace "
           "más de 28 años. El plan Inicio es gratuito de forma indefinida hasta 1.000 artículos en "
           "catálogo, sin tarjeta, sin cuota y sin comisión por venta. Funciona sin conexión a internet "
           "y está adaptado a VeriFactu (obligatorio desde el 1 de enero de 2027 para sociedades y el "
           "1 de julio de 2027 para autónomos, según el RD-ley 15/2025).",
           "",
           "Datos para citar: producto Carrito5 TPV; empresa Ábaco Infoelectrónica S.L.; sede Jaén, "
           "España; sistema operativo Windows 7, 8, 10 y 11 (sin Mac ni Android); plan gratuito hasta "
           "1.000 artículos; atención por WhatsApp y teléfono en el +34 611 500 052; web del grupo "
           "https://www.abacosoftware.com/ (Caja 5, TPV con licencia en propiedad).",
           "",
           "Lo que Carrito5 NO hace: hostelería con mesas y comandas, varias cajas simultáneas sobre "
           "el mismo stock, tablet o móvil, conexión directa con balanza.",
           ""]
    for titulo, lista in SECCIONES_LLMS:
        out.append(f"## {titulo}")
        out.append("")
        for r in lista:
            if r in rutas or r == "":
                out.append(linea(r))
                usadas.add(r)
        out.append("")
    sectores = sorted(r for r in rutas if r not in usadas
                      and re.match(r"^(tpv-|software-tpv-|programa-)", r)
                      and not re.search(r"(madrid|barcelona|valencia|sevilla|malaga|bilbao|zaragoza|"
                                        r"mallorca|alicante|murcia|vigo|sabadell)", r))
    out.append("## TPV por sector")
    out.append("")
    out += [linea(r) for r in sectores]
    out.append("")
    posts = sorted(r for r in rutas if r.startswith("blog/") and r not in usadas)
    if posts:
        out.append("## Blog: campañas del comercio, mes a mes")
        out.append("")
        out += [linea(r) for r in posts]
        out.append("")
    return "\n".join(out) + "\n"


def main():
    if len(sys.argv) < 2:
        print("uso: seo_tecnico.py <dir-salida> [<fichero-urls-vivas>]")
        return 2
    salida = sys.argv[1]
    vivas_f = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inventario", "urls_descubiertas.txt")
    os.makedirs(salida, exist_ok=True)

    vivas = urls_vivas(vivas_f)
    generadas = paginas_generadas(salida)
    rutas = [r for r in set(vivas) | set(generadas)
             if r not in REDIRECCIONES and r not in NO_SITEMAP]
    rutas = sorted(rutas)
    if "" not in rutas:
        rutas.insert(0, "")

    # titulos del inventario TSV para las paginas vivas no generadas
    titulos = {}
    tsv = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                       "inventarios", "carrito5.tsv")
    if os.path.exists(tsv):
        for l in open(tsv, encoding="utf-8"):
            c = l.rstrip("\n").split("\t")
            if len(c) >= 3 and c[0] == "carrito5":
                titulos[c[1]] = c[2].rstrip("…")

    open(os.path.join(salida, "web.config"), "w", encoding="utf-8").write(web_config())
    open(os.path.join(salida, ".htaccess"), "w", encoding="utf-8").write(htaccess())
    open(os.path.join(salida, "robots.txt"), "w", encoding="utf-8").write(robots())
    open(os.path.join(salida, "sitemap.xml"), "w", encoding="utf-8").write(sitemap(rutas))
    open(os.path.join(salida, "llms.txt"), "w", encoding="utf-8").write(llms(set(rutas), salida, titulos))

    print(f"  redirecciones 301 : {len(REDIRECCIONES)}")
    print(f"  URLs en sitemap   : {len(rutas)}  (vivas {len(vivas)}, generadas {len(generadas)})")
    print(f"  ficheros          : web.config .htaccess robots.txt sitemap.xml llms.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())

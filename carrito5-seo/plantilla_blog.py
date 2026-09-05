#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Plantilla de articulo del blog de carrito5.com.

Reutiliza el CSS, la cabecera, el pie y la entidad de plantilla.py, y añade lo
propio de un articulo: fecha de publicacion visible, schema Article con
datePublished y dateModified, miga Inicio > Blog > articulo, y un cierre
comercial que cada post escribe a su manera (no hay bloque de venta comun: el
gate lo detectaria y, peor, el lector tambien).

Los articulos viven en /blog/<slug>.html, un nivel por debajo de la raiz, asi
que todos los enlaces del NAV y del PIE se pasan a rutas absolutas.
"""
import re

import plantilla as P

DOMINIO = P.DOMINIO


def absolutos(html_):
    """href="x.html" -> href="/x.html" (deja http, mailto, tel, # y ya absolutos)."""
    return re.sub(r'href="(?!https?:|mailto:|tel:|#|/)([^"]+)"', r'href="/\1"', html_)


NAV = absolutos(P.NAV)
PIE = absolutos(P.PIE)

CSS_BLOG = """
.c5-art-hero{background:linear-gradient(160deg,#1e1b4b 0%,var(--c5-slate) 60%);color:#e2e8f0;padding:38px 0 40px}
.c5-art-hero h1{color:#fff;font-size:clamp(1.7rem,3.6vw,2.4rem);line-height:1.15;font-weight:800;margin:10px 0 12px;max-width:26ch}
.c5-art-hero p.sub{font-size:1.04rem;color:#cbd5e1;max-width:64ch;margin:0}
.c5-art-meta{font-size:.84rem;color:#94a3b8;margin-top:16px;display:flex;gap:14px;flex-wrap:wrap}
.c5-art-meta strong{color:#e2e8f0}
.c5-art{max-width:760px}
.c5-art h2{font-size:1.5rem;font-weight:800;margin:32px 0 12px}
.c5-art h3{font-size:1.12rem;font-weight:700;margin:22px 0 8px}
.c5-art p{margin:0 0 14px}
.c5-art blockquote{margin:18px 0;padding:14px 18px;border-left:4px solid var(--c5-azul);background:var(--c5-fondo);font-size:.98rem}
.c5-cierre{background:#fff7fb;border:1px solid #f0c6d8;border-radius:12px;padding:22px 24px;margin:34px 0 10px}
.c5-cierre h2{margin-top:0;font-size:1.3rem}
.c5-cierre .c5-btn-main{margin-top:8px}
.c5-fecha-pub{display:inline-block;background:rgba(56,189,248,.15);border:1px solid rgba(56,189,248,.45);color:#bae6fd;
  font-size:.74rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:5px 12px;border-radius:20px}
"""


def cuerpo_html(cuerpo):
    """cuerpo: lista de (h2, [parrafos o bloques html], [bullets] | None).
    Un parrafo que empiece por <h3, <table, <ol, <ul, <blockquote o <div se
    emite tal cual."""
    out = []
    for t, ps, *extra in cuerpo:
        if t:
            out.append(f"<h2>{t}</h2>")
        for p in ps:
            if p.lstrip().startswith(("<h3", "<table", "<ol", "<ul", "<blockquote", "<div")):
                out.append(p)
            else:
                out.append(f"<p>{p}</p>")
        if extra and extra[0]:
            out.append('<ul class="c5-lista">' + "".join(f"<li>{x}</li>" for x in extra[0]) + "</ul>")
    return "\n".join(out)


def articulo(slug, title, description, keywords, h1, sub, publicado, para, resumen,
             cuerpo, cierre, faqs, faq_titulo, relacionadas, modificado=None):
    """Genera /blog/<slug>.html.

    publicado:    'AAAA-MM-DD' fecha de publicacion (visible y en Article).
    para:         a quien va dirigido, en una frase corta ('Papelerías y librerías').
    resumen:      lista de 1-3 parrafos de respuesta directa.
    cierre:       (titulo, [parrafos], texto_boton, url_boton) escrito por el post.
    relacionadas: [(texto, url, descripcion)] con URLs absolutas o de raiz.
    """
    canon = f"{DOMINIO}/blog/{slug}.html"
    modificado = modificado or publicado
    trail = [("Inicio", "/"), ("Blog", "/blog.html"), (h1, f"/blog/{slug}.html")]
    migas = ' &rsaquo; '.join([f'<a href="{u}">{n}</a>' for n, u in trail[:-1]] + [f"<span>{trail[-1][0]}</span>"])

    art = {"@context": "https://schema.org", "@type": "Article", "@id": canon + "#article",
           "headline": h1, "description": description, "inLanguage": "es-ES",
           "datePublished": publicado, "dateModified": modificado,
           "author": {"@id": DOMINIO + "/#organization"},
           "publisher": {"@id": DOMINIO + "/#organization"},
           "image": P.OG, "mainEntityOfPage": canon, "url": canon,
           "isPartOf": {"@type": "Blog", "@id": DOMINIO + "/blog.html#blog", "name": "Blog de Carrito5",
                        "url": DOMINIO + "/blog.html"},
           "about": {"@type": "Thing", "name": para}}
    lds = P.ld(P.ORG_LD) + P.ld({"@context": "https://schema.org", "@type": "BreadcrumbList",
                                  "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n,
                                                       "item": DOMINIO + u}
                                                      for i, (n, u) in enumerate(trail)]})
    lds += P.ld(art)
    if faqs:
        lds += P.ld(P.faq_ld(faqs))

    c_t, c_ps, c_btn, c_url = cierre
    cierre_html = (f'<div class="c5-cierre"><h2>{c_t}</h2>' + "".join(f"<p>{p}</p>" for p in c_ps)
                   + f'<a href="{c_url}" class="c5-btn-main">{c_btn}</a></div>')

    rel = [(t, (u if u.startswith(("http", "/")) else "/" + u), d) for t, u, d in relacionadas]
    rel_html = P.satelites_html(rel, "Páginas relacionadas").replace('href="', 'href="') if rel else ""
    # satelites_html hace lstrip('/') a las urls; se restaura la barra
    rel_html = re.sub(r'href="(?!https?:|/)', 'href="/', rel_html)

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{P.esc(title)}</title>
<meta name="description" content="{P.esc(description)}">
<meta name="keywords" content="{P.esc(keywords)}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="{canon}">
<meta property="og:site_name" content="{P.MARCA} TPV">
<meta property="og:type" content="article">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{P.esc(title)}">
<meta property="og:description" content="{P.esc(description)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{P.OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta property="article:published_time" content="{publicado}">
<meta property="article:modified_time" content="{modificado}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{P.esc(title)}">
<meta name="twitter:description" content="{P.esc(description)}">
<meta name="twitter:image" content="{P.OG}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<style>{P.CSS}{CSS_BLOG}</style>
{lds}</head>
<body>
{NAV}
<main>
<section class="c5-art-hero">
  <div class="c5-wrap">
    <div class="c5-migas">{migas}</div>
    <span class="c5-fecha-pub">Publicado el {P.fecha_legible(publicado)}</span>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
    <div class="c5-art-meta"><span>Para: <strong>{para}</strong></span><span>Por: <strong>Carrito5</strong></span></div>
  </div>
</section>

<section class="c5-seccion">
  <div class="c5-wrap c5-cols">
    <div class="c5-art">
{P.resumen_html(resumen)}
{cuerpo_html(cuerpo)}
{cierre_html}
    </div>
    <aside class="c5-aside">
      <h3>Carrito5, TPV gratis para Windows</h3>
      <p>Plan Inicio sin cuota ni tarjeta hasta 1.000 artículos. Tallas y colores, clientes con devoluciones, códigos de barras y etiquetas. Adaptado a VeriFactu.</p>
      <a href="/descargar-tpv-gratis.html" class="c5-btn-main">Descargar gratis</a>
      <a href="{P.WA}" class="c5-btn-wa">Preguntar por WhatsApp</a>
      <p style="margin:12px 0 0;font-size:.82rem">O llama al <strong>{P.TEL}</strong>. Te atiende una persona en España.</p>
    </aside>
  </div>
</section>

{rel_html}
{P.faq_html(faqs, faq_titulo)}
</main>
{PIE}
</body>
</html>
"""

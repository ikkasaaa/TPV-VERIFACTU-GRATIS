#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lectura y escritura de marcado HTML/ASP, compartida por los dos sitios.

Todo lo que aqui vive estaba copiado en seis ficheros distintos, cada uno con
su propia expresion regular para el <title>, su propio "quita etiquetas" y su
propio escape de atributos. Cuando una de las copias se corregia, las otras
cinco no. Ahora hay una.

Dos familias de funciones:

  Leer      texto_visible, vocabulario, titulo, h1, meta, bloques_ld
  Escribir  poner_title, poner_meta, esc, ld, faq_ld, breadcrumb_ld

Regla que respetan todas las de escritura: reciben y devuelven marcado tal
cual esta en el fichero. No re-escapan lo que ya venia escapado, porque un
"&amp;" que pasa dos veces por esc() acaba como "&amp;amp;" en la SERP.
"""
import html, json, re

_ASP = re.compile(r"<%.*?%>", re.S)
_OCULTO = re.compile(r"<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->", re.S | re.I)
_ETIQUETA = re.compile(r"<[^>]+>")
_BLANCO = re.compile(r"\s+")
_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
_H1 = re.compile(r"<h1(?:\s[^>]*)?>(.*?)</h1>", re.S | re.I)
_LD = re.compile(r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>', re.S | re.I)


# ------------------------------------------------------------------- leer
def leer(ruta):
    with open(ruta, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def escribir(ruta, s):
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(s)


def plano(fragmento):
    """Texto de un trozo de marcado: sin ASP, etiquetas ni entidades, un espacio
    entre palabras. Conserva mayusculas: sirve para titulos y H1."""
    t = _OCULTO.sub(" ", _ASP.sub("", fragmento))
    return _BLANCO.sub(" ", html.unescape(_ETIQUETA.sub(" ", t))).strip()


def texto_visible(marcado):
    """Lo que lee el usuario, en minusculas. Es la base del filtro anti-plantilla."""
    return plano(marcado).lower()


def vocabulario(marcado):
    """Conjunto de palabras visibles. Lo que compara el gate."""
    return frozenset(texto_visible(marcado).split())


def jaccard(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def titulo(s):
    m = _TITLE.search(s)
    return plano(m.group(1)) if m else ""


def h1(s):
    """Texto del primer H1. Ver h1s() para contarlos."""
    m = _H1.search(s)
    return plano(m.group(1)) if m else ""


def h1s(s):
    """Numero de H1 en el marcado, ignorando los que esten dentro de <style> o
    <script> (un selector CSS 'h1{...}' no es un encabezado)."""
    return len(re.findall(r"<h1[\s>]", _OCULTO.sub(" ", s), re.I))


def meta(s, nombre):
    """Contenido de <meta name|property="nombre" content="...">, en texto plano."""
    m = re.search(_meta_pat(nombre), s, re.S | re.I)
    return plano(m.group(2)) if m else ""


def canonical(s):
    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', s, re.I)
    return m.group(1).strip() if m else ""


def bloques_ld(s):
    """[(inicio, fin, objeto|None)] de cada <script type="application/ld+json">.
    objeto es None cuando el JSON no parsea: eso es un fallo que hay que ver."""
    out = []
    for m in _LD.finditer(s):
        try:
            obj = json.loads(m.group(1))
        except ValueError:
            obj = None
        out.append((m.start(), m.end(), obj))
    return out


# --------------------------------------------------------------- escribir
def _meta_pat(nombre):
    return (r'(<meta\s+(?:name|property)=["\']' + re.escape(nombre)
            + r'["\']\s+content=["\'])(.*?)(["\'])')


def poner_meta(s, nombre, valor):
    """Sustituye el content de una <meta> existente. Si no existe, no la crea:
    decidir donde va una meta nueva es cosa de quien conoce la plantilla."""
    return re.sub(_meta_pat(nombre), lambda m: m.group(1) + valor + m.group(3), s,
                  count=1, flags=re.S | re.I)


ESPEJOS_TITLE = ("og:title", "twitter:title")
ESPEJOS_DESC = ("og:description", "twitter:description")


def poner_title(s, nuevo):
    """Cambia el <title> y sus espejos (og:title, twitter:title) a la vez.

    Si se cambia uno solo, la tarjeta de WhatsApp o de Twitter sigue enseñando
    el titulo viejo meses despues del recorte. Ha pasado.
    """
    s = _TITLE.sub(lambda m: m.group(0)[:m.start(1) - m.start()] + nuevo + "</title>", s, count=1)
    for p in ESPEJOS_TITLE:
        s = poner_meta(s, p, nuevo)
    return s


def poner_description(s, nueva):
    for p in ("description",) + ESPEJOS_DESC:
        s = poner_meta(s, p, nueva)
    return s


def esc(t):
    """Escape para valores de atributo y texto. No lo apliques dos veces."""
    return (t.replace("&", "&amp;").replace('"', "&quot;")
             .replace("<", "&lt;").replace(">", "&gt;"))


def ld(obj, sangria=""):
    """Bloque <script type="application/ld+json"> listo para el <head>.
    sangria: prefijo de cada linea (abacosoftware usa tabuladores)."""
    cuerpo = json.dumps(obj, ensure_ascii=False, indent=2).replace("\n", "\n" + sangria)
    return (f'{sangria}<script type="application/ld+json">\n{sangria}{cuerpo}'
            f"\n{sangria}</script>\n")


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in faqs]}


def breadcrumb_ld(trail, base):
    """trail: [(nombre, url relativa)]. base: dominio con esquema, sin barra final."""
    base = base.rstrip("/")
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n,
                                 "item": base + "/" + u.lstrip("/")}
                                for i, (n, u) in enumerate(trail)]}

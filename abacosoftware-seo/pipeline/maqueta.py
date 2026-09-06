# -*- coding: utf-8 -*-
"""Piezas HTML comunes a los generadores de abacosoftware.com.

Cada generador tenia su propia copia del parrafo, la lista con el check, la
tarjeta lateral y la rejilla de tarjetas: seis versiones del mismo estilo en
linea, que divergian un pixel cada vez que alguien tocaba una. Ahora la
maqueta es una y lo que cambia entre generadores es solo el texto.

Nada de aqui pone texto visible propio salvo lo que se le pasa: el filtro
anti-plantilla mide texto visible y estas piezas no deben sumar palabras
compartidas entre paginas.
"""
import sitio

P = 'style="font-size:15.5px; line-height:1.8; color:#3f3f46;"'
H2 = 'style="font-size:25px; font-weight:800; color:#1e293b; margin-top:34px;"'
LI = 'style="padding:10px 0; border-bottom:1px solid #f0ebe2; font-size:14.6px; line-height:1.65;"'
BTN_SEC = ('style="display:block; text-align:center; background:#ffffff; color:#8c2d19; '
           'border:2px solid #8c2d19; border-radius:6px; font-weight:700; font-size:15px; '
           'padding:11px 18px; text-decoration:none;"')
S5 = "\n\t\t\t\t\t"


def icono(nombre):
    return f'<i class="fa-solid {nombre}" style="color:#8c2d19; margin-right:9px;"></i>'


def parrafos(ps, sangria=S5):
    return "".join(f"{sangria}<p {P}>{p}</p>" for p in ps)


def lista(xs, ico="fa-check", sangria=S5):
    if not xs:
        return ""
    return (f'{sangria}<ul style="list-style:none; padding:0; margin:18px 0;">'
            + "".join(f"{sangria}\t<li {LI}>{icono(ico)}{x}</li>" for x in xs)
            + f"{sangria}</ul>")


def bloque(titulo, ps, xs=None, ico="fa-check"):
    return f"{S5}<h2 {H2}>{titulo}</h2>{parrafos(ps)}{lista(xs, ico)}"


def bloques(bs, ico="fa-check"):
    """bs: [(titulo, [parrafos]) | (titulo, [parrafos], [lista])]."""
    return "".join(bloque(t, ps, extra[0] if extra else None, ico) for t, ps, *extra in bs)


def boton_wa(texto="Preguntar por WhatsApp", mensaje=""):
    href = sitio.WA + (f"?text={mensaje}" if mensaje else "")
    return f'<a href="{href}" {BTN_SEC}><i class="fa-brands fa-whatsapp"></i> {texto}</a>'


def boton_tel():
    return f'<a href="{sitio.TEL_HREF}" {BTN_SEC}><i class="fa-solid fa-phone"></i> {sitio.TEL}</a>'


def aside(titulo, texto, boton, pie):
    """Tarjeta lateral pegajosa: titulo, texto, demo, un segundo boton y una nota al pie."""
    return f"""
					<div style="background:#faf8f4; border:1.5px solid #e4dfd5; border-radius:10px; padding:24px; position:sticky; top:20px;">
						<h3 style="font-size:18px; font-weight:800; color:#1e293b; margin-top:0;">{titulo}</h3>
						<p style="font-size:14px; line-height:1.7; color:#52525b;">{texto}</p>
						<a href="{sitio.DEMO}" class="btn-hero-primary" style="display:block; text-align:center; margin-bottom:10px;"><i class="fa-solid fa-download"></i> Descargar demo</a>
						{boton}
						<hr style="border-color:#e4dfd5; margin:18px 0;">
						<p style="font-size:13px; color:#71717a; margin:0;">{pie}</p>
					</div>"""


def dos_columnas(principal, lateral, padding="48px 0 40px"):
    return f"""
	<section style="padding:{padding}; background:#ffffff;">
		<div class="container">
			<div class="row">
				<div class="col-md-8">{principal}
				</div>
				<div class="col-md-4">{lateral}
				</div>
			</div>
		</div>
	</section>
"""


def intro(ps, ancho=880, padding="46px 0 26px"):
    return f"""
	<section style="padding:{padding}; background:#ffffff;">
		<div class="container"><div style="max-width:{ancho}px;">{parrafos(ps, "")}</div></div>
	</section>
"""


def tarjetas(items):
    """items: [(url, titulo, texto)]."""
    return "".join(f"""
				<div class="col-md-4 col-sm-6" style="margin-bottom:22px;">
					<div style="background:#ffffff; border:1.5px solid #e4dfd5; border-radius:9px; padding:22px; height:100%;">
						<h3 style="font-size:17px; font-weight:800; margin-top:0; margin-bottom:9px; line-height:1.35;">
							<a href="{u}" style="color:#8c2d19; text-decoration:none;">{t}</a></h3>
						<p style="font-size:13.8px; line-height:1.65; color:#52525b; margin:0;">{d}</p>
					</div>
				</div>""" for u, t, d in items)


def seccion_tarjetas(nombre, items):
    return f"""
	<section style="padding:42px 0; background:#faf8f4; border-top:1px solid #e9e4db;">
		<div class="container">
			<h2 style="font-size:25px; font-weight:800; color:#1e293b; margin-top:0; margin-bottom:20px;">{nombre}</h2>
			<div class="row">{tarjetas(items)}
			</div>
		</div>
	</section>
"""

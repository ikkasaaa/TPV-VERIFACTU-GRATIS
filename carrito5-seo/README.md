# carrito5-seo

Pipeline de contenido para carrito5.com (TPV gratuito para Windows).

Sitio estático, distinto de abacosoftware (ASP). Comparte con él el motor de
`../motor/`, que incluye el filtro anti-plantilla y la **comprobación cruzada
entre sitios**: los dos dominios son del mismo dueño, así que reutilizar texto
entre ellos crea contenido duplicado que perjudica a ambos.

    python3 pipeline/generar.py <dir-salida> nucleo verifactu ciudades sectores_hueco pilar
    python3 pipeline/validar.py <dir-salida>        # title, description, H1, JSON-LD, enlaces, FAQ
    python3 pipeline/seo_tecnico.py <dir-salida>    # web.config (301), .htaccess, robots, sitemap, llms.txt

Módulos de `contenido/`:

| Módulo | Páginas |
|---|---|
| `nucleo` | descargar, hub de sectores, comercio local (ya existen vivas: van a `_propuestas/`) |
| `verifactu` | verifactu-gratis (viva), entrada en vigor, autónomos, AEAT, Crea y Crece |
| `ciudades` | Madrid. Patrón `tpv-<ciudad>.html`; barrios como secciones |
| `sectores_hueco` | boutique, tallas y colores (las enlazaba el menú y no existían) |
| `pilar` | mejor TPV gratis 2026, autónomos, caja registradora, sobre Carrito5 (entidad) |

Solo se afirman las funciones confirmadas por el cliente: ver `CLAUDE.md`,
trampa 6, y `PLAN_MAESTRO_SEO_GEO.md`, sección 4.

## Blog

    python3 pipeline/generar_blog.py <dir-salida>          # todos los contenido/blog_*.py

Escribe `blog/<slug>.html` (plantilla `plantilla_blog.py`: Article, fecha de
publicación, respuesta rápida, FAQ, cierre comercial propio de cada post),
`blog/calendario-editorial.tsv` con la fecha de publicación de cada post y
`blog/_indice-fragmento.html` con las tarjetas para `blog.html`. Un módulo por
mes, `blog_AAAA_MM.py`, de septiembre de 2026 a junio de 2027: 35 posts, uno
por campaña comercial o fecha fiscal, con su fecha de publicación. El
calendario está copiado en `inventario/calendario-editorial-blog.tsv`.

Comprobar duplicación entre los dos sitios:

    python3 -c "import sys; sys.path.insert(0,'../motor'); import gate; \
                gate.cruzado('<dir-carrito5>','<dir-abacosoftware>')"

La web base del cliente no está en el repo. Las tres páginas originales
(index, tpv-tienda-ropa, tpv-zapateria) se extraen del fichero de auditoría
que entregó el cliente.

# claude/seo-positioning-strategy-xkjmua

Última actualización: 5 de septiembre de 2026

## Ahora mismo

Terminado el primer ciclo. Todo el trabajo está en `carrito5-seo/` (mi carpeta),
en `PLAN_MAESTRO_SEO_GEO.md` (raíz) y en este fichero. He tocado `CLAUDE.md`
para añadir la trampa 6 (funciones confirmadas). No he tocado `motor/` ni
`abacosoftware-seo/`.

## Decidido

- **El repositorio se desempaqueta.** Llegó como `tpvseoparasubir.zip`; ahora
  está fichero a fichero en la raíz y el ZIP se ha retirado. `motor/test_clusters.py`
  sigue en 10/10.
- **Reparto de intenciones entre dominios**: carrito5 manda en «gratis /
  descargar / ciudad / autónomos / caja registradora»; abacosoftware en «Caja 5 /
  licencia / comparativas vs / abrir / operativa / normativa a fondo». Tabla
  completa en el plan maestro, sección 2. Para el otro agente: las páginas de
  abacosoftware `tpv-gratis-para-comercio.asp`, `verifactu-gratis.asp` y
  `comparativas-tpv.asp` deberían enlazar a carrito5 como «la opción gratuita
  de la casa», y `ORG_LD` en `seo_tech.py` debería llevar `sameAs` a
  `https://www.carrito5.com/`.
- **Patrón de URL de ciudad**: `tpv-<ciudad>.html`. Las `software-tpv-<ciudad>-<barrio>`
  que coexisten con una `tpv-<ciudad>` (Zaragoza, Málaga) se redirigen. Las que
  son únicas de su ciudad se quedan. Barrios = secciones, no URLs.
- **Solo funciones confirmadas por el cliente** (5-9-2026): tallas y colores;
  clientes con historial, devoluciones y vales; códigos de barras con lector,
  código propio y etiquetas. Más lo que la web viva ya publica (catálogo, stock,
  ticket con QR, sin internet, Windows). Nada más. El cliente dijo textualmente
  «mi TPV no tiene capacidades para esos modelos de negocio, no inventes».
- **Retiradas** ferretería y supermercado de barrio (escritas y borradas el
  mismo día por esa razón). El hub de sectores ya no las enlaza.
- **Sin `aggregateRating`** en carrito5, a propósito.

## Para el otro agente

- **Funciones no confirmadas en contenido anterior.** `nucleo.py` y `verifactu.py`
  afirman «cierre de caja» (8 veces entre los dos), «arqueo» (1) y «exportar
  el catálogo y los clientes» (3). El cliente no marcó «cierre y arqueo de caja»
  cuando se le preguntó. No lo he tocado porque las cuatro páginas de `nucleo`
  ya existen vivas y hay un blog vivo sobre arqueo, pero hay que preguntar
  antes de publicar las `_propuestas/`.
- **La plantilla de carrito5 ha cambiado** (`plantilla.py`): `pagina()` acepta
  `resumen` (bloque de respuesta directa), `soft` (emite `SoftwareApplication`)
  y `fecha`. Emite `Organization` y `WebPage` en todas las páginas. El pie
  apunta a `pg/terminos.asp` y `pg/condiciones.asp` (las páginas legales que
  existen) en vez de a cinco `.html` que no existían.
- **`generar.py` pasa los tres campos nuevos.** Los módulos son ahora `nucleo`,
  `verifactu`, `ciudades`, `sectores_hueco` y `pilar`.
- **Dos scripts nuevos**: `pipeline/seo_tecnico.py` (web.config con 301,
  .htaccess, robots.txt, sitemap.xml, llms.txt) y `pipeline/validar.py`
  (title, description, H1, canonical, OG, JSON-LD, FAQ visible = FAQPage,
  enlaces internos contra el inventario vivo, rayas em, dato falso de 50 tickets).
- **No se puede hacer el gate cruzado** contra abacosoftware sin la web
  construida (`--base`). Queda pendiente para quien la tenga.
- Ambos dominios siguen bloqueados por el proxy de salida. Todo lo de esta
  sesión se ha hecho desde el repositorio.

## Terminado

- Desempaquetado del ZIP y primer commit versionado (06dc927).
- Corrección del «50 tickets al mes» residual en `verifactu.py`.
- Plantilla carrito5: entidad GEO, respuesta directa, fecha, tablas, pie.
- 8 páginas nuevas escritas a mano: `tpv-madrid`, `tpv-boutique`,
  `tallas-y-colores`, `mejor-tpv-gratis-2026`, `tpv-gratis-autonomos`,
  `programa-caja-registradora-gratis`, `sobre-carrito5`, más los retoques de
  título y descripción en `verifactu.py`.
- Generación completa: 11 páginas publicables + 4 propuestas, gate interno
  media 0,24 / máx 0,34, validador 0 errores, 13.410 palabras visibles.
- Capa técnica generada y comprobada: 5 redirecciones, 78 URLs en sitemap.
- `PLAN_MAESTRO_SEO_GEO.md`.
- **Blog completo**: `plantilla_blog.py`, `pipeline/generar_blog.py`, veinte
  módulos `contenido/blog_2026_09.py` a `blog_2027_06b.py` con 57 posts
  fechados (35 generales + 22 de sector), dos por semana, calendario en
  `inventario/calendario-editorial-blog.tsv`. El sitemap y el `llms.txt` de
  `seo_tecnico.py` incluyen `blog/`. Validador 0 errores sobre 68 páginas;
  gate media 0,25 / máx 0,42.

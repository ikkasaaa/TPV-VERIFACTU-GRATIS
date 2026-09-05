# Plan maestro SEO + GEO: carrito5.com y abacosoftware.com

Fecha: 5 de septiembre de 2026. Rama: `claude/seo-positioning-strategy-xkjmua`.

Objetivo: que Carrito5 sea el resultado número uno, en Google y en los motores
generativos (ChatGPT, Perplexity, Gemini, AI Overviews), para «TPV gratis»,
«TPV VeriFactu gratis» y sus variantes en España, y que abacosoftware.com deje
de competir con él y pase a apoyarlo.

Este documento distingue siempre tres cosas: lo **hecho** en el repositorio, lo
que **necesita al cliente** para publicarse, y lo que es **criterio** y no dato.

---

## 0. Resumen en diez líneas

1. Los dos dominios son del mismo dueño y se pisan en 14 intenciones de búsqueda. Se reparte: **carrito5 = gratis, descargar, empezar hoy, ciudad**; **abacosoftware = Caja 5, licencia, comparativas, cómo abrir, operativa, normativa a fondo**.
2. Madrid, la plaza más grande de España, no tenía página. Ya está escrita.
3. Cinco redirecciones 301 resuelven los duplicados conocidos de carrito5 (singular/plural, página de prueba indexada, dos esquemas de URL de ciudad).
4. Se corrige un dato falso que seguía en el contenido («50 tickets al mes»): el plan gratuito es hasta 1.000 artículos.
5. Se retiran dos páginas de sector que el propio cliente confirmó que el TPV no cubre (ferretería, supermercado). **Regla nueva: solo se afirman las funciones confirmadas** (ver sección 4).
6. Capa GEO: entidad única (`Organization` con `@id` estable y `sameAs` cruzado), `SoftwareApplication` sin `aggregateRating`, bloque de respuesta directa bajo cada H1, fecha de revisión, `llms.txt`, robots abierto a los rastreadores de IA.
7. Cuatro páginas pilar nuevas para la intención comercial amplia: comparativa «mejor TPV gratis 2026», autónomos, caja registradora, y la página de entidad «quién está detrás».
8. Dos páginas que el menú y el hub enlazaban y devolvían 404: tallas y colores, boutique.
9. Herramientas nuevas en `carrito5-seo/pipeline/`: `seo_tecnico.py` (web.config, robots, sitemap, llms.txt) y `validar.py` (auditoría de lo generado).
10. Lo que falta lo tiene el cliente: sitemap real, acceso a Search Console, ficha de funciones completa, decisión sobre el `aggregateRating` de abacosoftware y el borrado de los 11 ficheros que no deberían estar publicados.

---

## 1. Diagnóstico: los errores y su estado

| # | Error | Dónde | Estado |
|---|---|---|---|
| 1 | Madrid sin página de ciudad; el menú la anuncia | carrito5 | **Hecho**: `tpv-madrid.html` |
| 2 | La misma página en dos URLs (instrumentos singular/plural) | carrito5 | **Hecho**: 301 en `web.config` |
| 3 | `tpv_gratis_verifactu_bonito.html` (prueba) indexada y compitiendo con `verifactu-gratis.html` | carrito5 | **Hecho**: 301 |
| 4 | Dos esquemas de URL de ciudad en Zaragoza y Málaga | carrito5 | **Hecho**: 301 de `software-tpv-<ciudad>-<barrio>` a `tpv-<ciudad>` |
| 5 | 13 títulos generados desde el nombre del fichero («Tpv Tienda Iluminacion») | carrito5 | Reescritos en `contenido/titulos_reescritos.py`; **el cliente debe aplicarlos** en las páginas vivas (`inventario/titulos_propuestos.tsv`) |
| 6 | `pg/condiciones.asp` se titula «El cofre de tu vida» | carrito5 | **Cliente**: corregir el título en la página viva |
| 7 | «50 tickets al mes» aún presente en `verifactu.py` | repo | **Hecho** |
| 8 | Enlaces del menú y del pie a páginas inexistentes (`tallas-y-colores`, legales) | plantilla carrito5 | **Hecho**: tallas y colores escrita; pie apunta a `pg/terminos.asp` y `pg/condiciones.asp` |
| 9 | Hub de sectores enlazando a ferretería, boutique y supermercado (404) | carrito5 | **Hecho**: boutique escrita; ferretería y supermercado retiradas del hub por decisión del cliente |
| 10 | Sin `Organization` con `@id` estable ni `SoftwareApplication` | carrito5 | **Hecho** en la plantilla |
| 11 | Sin `robots.txt` ni `sitemap.xml` generados; sin `llms.txt` | carrito5 | **Hecho**: `seo_tecnico.py` |
| 12 | 14 intenciones servidas por los dos dominios a la vez | ambos | Reparto decidido (sección 2); **aplicar** enlaces cruzados en abacosoftware |
| 13 | 11 ficheros que no deberían estar publicados (ejecutables, copias, `.lnk`) | abacosoftware servidor | **Cliente**: borrarlos del servidor (ya no van en el ZIP) |
| 14 | `aggregateRating` 4,9 sobre 318 valoraciones sin reseñas visibles, en 34 páginas | abacosoftware vivo | **Cliente**: retirar el schema o publicar reseñas reales. Riesgo de acción manual |
| 15 | Solapes internos de sector en carrito5 (herboristería ×3, colchones ×2, informática ×2, muebles/decoración, comercio ×2) | carrito5 | **Criterio**: fusionar o diferenciar; propuesta en sección 3.3 |
| 16 | Contenido previo afirma «cierre de caja», «arqueo» y «exportar datos», funciones no confirmadas | `nucleo.py`, `verifactu.py` | **Pendiente cliente**: confirmar o retirar (ver sección 4) |

---

## 2. Reparto de intenciones entre los dos dominios

Regla: **una intención, un dominio**. Cuando los dos tengan página, la del otro dominio enlaza a la que manda con un texto de ancla claro y deja de perseguir la palabra clave.

| Intención | Manda | Apoya | Cómo |
|---|---|---|---|
| tpv gratis, descargar tpv, programa tpv gratis, tpv verifactu gratis, verifactu gratis | **carrito5** | abacosoftware | `tpv-gratis-para-comercio.asp` y `verifactu-gratis.asp` de abacosoftware se quedan como editorial de «letra pequeña» y enlazan a carrito5 como «la opción gratuita de la casa» |
| mejor tpv gratis, comparativa tpv gratis | **carrito5** | abacosoftware | `comparativas-tpv.asp` enlaza a `mejor-tpv-gratis-2026.html` |
| tpv autónomos gratis, caja registradora gratis, tpv sin cuota | **carrito5** | abacosoftware | `alternativa-tpv-suscripcion.asp` enlaza a la de autónomos |
| tpv <ciudad> | **carrito5** | abacosoftware | abacosoftware no crea páginas de ciudad |
| tpv <sector> «gratis» | **carrito5** | | ángulo: empezar hoy sin pagar |
| software tpv homologado, tpv en propiedad, comprar tpv, licencia | **abacosoftware** | carrito5 | carrito5 enlaza a Caja 5 cuando la tienda «crece» (ya lo hace) |
| alternativa a <competidor>, <competidor> vs | **abacosoftware** | | |
| cómo abrir <negocio>, operativa (devoluciones, inventario, precios), hardware compatible | **abacosoftware** | carrito5 | |
| qué es verifactu, cuándo entra en vigor, sanciones, ticketBAI, declaración responsable | **abacosoftware** (normativa a fondo) | carrito5 (versión «qué necesitas tú, en corto») | ángulos distintos ya escritos; el gate cruzado vigila el texto |
| tpv <sector> (sin «gratis») | **abacosoftware** | carrito5 | las 14 colisiones de `informes/clusters_cruzados.txt` se resuelven así: la de carrito5 lleva «gratis» en título y H1 y enlaza a la de abacosoftware como «funciones a fondo» |

Las dos páginas de FAQ y las dos de términos de uso que colisionan son ruido: son páginas propias de cada dominio y no compiten por tráfico.

---

## 3. Arquitectura objetivo de carrito5.com

### 3.1 Hubs y clústeres

```
Inicio
├── Descargar gratis (página de dinero)
├── Sectores (hub) ── 50 páginas de sector existentes + boutique
├── Funciones ── tallas-y-colores (+ futuras: clientes y devoluciones, etiquetas y lector)
├── VeriFactu (hub: verifactu-gratis) ── entrada en vigor · autónomos · AEAT · Crea y Crece · offline · ley antifraude · factura simplificada · FAQ
├── Comparativa: mejor TPV gratis 2026 ── autónomos · caja registradora
├── Ciudades ── Madrid · Barcelona · Valencia · Sevilla · Málaga · Bilbao · Zaragoza · Mallorca · Alicante · Murcia · Vigo · Sabadell
├── Comercio local (posicionamiento)
└── Sobre Carrito5 (entidad)
```

### 3.2 Reglas de enlazado interno

- Toda página enlaza a **Descargar** (héroe, aside y CTA final: ya en plantilla).
- Toda página de sector enlaza a **su función principal** (tallas y colores en moda y calzado) y a **Madrid** si el sector tiene peso en Madrid.
- Toda página de VeriFactu enlaza a **verifactu-gratis** (hub) y a **descargar**.
- **Sobre Carrito5** se enlaza desde el pie de todas las páginas (hecho): es la página que los motores generativos usan para resolver la entidad.
- Ningún enlace a páginas que no existan. `validar.py` lo comprueba contra el inventario vivo.

### 3.3 Solapes internos: propuesta

| Páginas | Propuesta |
|---|---|
| `tpv-herboristeria` · `tpv-herboristeria-parafarmacia` · `tpv-tienda-parafarmacia` | Dejar dos: herboristería (dietética, ecotienda) y parafarmacia (lotes y caducidad). 301 de la mixta a herboristería |
| `tpv-colchones-financiacion-pagos` · `tpv-colchonerias-descanso` | Se quedan las dos si la primera habla solo de financiación y cobros parciales. Revisar el texto vivo |
| `tpv-electronica-informaticas` · `tpv-informatica-telefonia` | Fusionar en informática y telefonía; 301 de la otra |
| `tpv-tienda-muebles` (ya dice «y Decoración») · `tpv-tienda-decoracion` | Decoración se queda si habla de complemento y menaje; si no, 301 a muebles |
| `tpv-comercio` · `software-tpv-comercio-local` | Comercio local es la de posicionamiento; `tpv-comercio` pasa a ser la genérica de sector minorista. Títulos distintos ya |

Nada de esto se ejecuta sin ver el texto vivo de cada par. El cliente tiene que pasar el sitemap y, mejor, los ficheros.

---

## 4. Regla de honestidad sobre funciones

El cliente confirmó el 5 de septiembre de 2026 que el TPV **no** cubre ferretería ni supermercado de barrio y que las funciones que existen son:

- matriz de **tallas y colores**
- **ficha de clientes** con historial, devoluciones sobre el ticket y vales
- **códigos de barras** con lector, código propio para artículos sin EAN, impresión de etiquetas

Más lo que la propia web viva publica: catálogo, stock, tickets con QR de VeriFactu, funcionamiento sin internet, Windows.

**No se afirma** en ninguna página nueva: cierre o arqueo de caja, turnos, avisos de stock mínimo, ticket regalo, rebajas por familia, factura completa, exportación de datos, balanza, varias cajas, hostelería.

Pendiente de confirmar con el cliente, porque aparece en contenido anterior (`nucleo.py` y `verifactu.py`) y en el blog vivo (`como-hacer-arqueo-de-caja-cierre-z.html`): **cierre de caja / arqueo** y **exportación del catálogo y clientes**. Si no existen, hay que retirarlos también de esas páginas antes de publicarlas.

Cualquier función nueva se añade primero a esta lista y después al texto. Nunca al revés.

---

## 5. GEO: cómo hacer que los motores generativos citen a Carrito5

Los motores generativos no posicionan páginas, **citan fuentes**. Eligen la fuente que contesta la pregunta en una frase, con datos concretos, de una entidad que reconocen. Lo hecho y lo que queda:

| Palanca | Hecho | Pendiente |
|---|---|---|
| **Entidad única.** `Organization` con `@id` `https://www.carrito5.com/#organization` en todas las páginas, `legalName`, sede, teléfono, `parentOrganization` Ábaco Software, `sameAs` a abacosoftware.com | Sí, en plantilla | abacosoftware debe devolver el `sameAs` hacia carrito5 en su `ORG_LD` (`seo_tech.py`) |
| **Producto tipado.** `SoftwareApplication` con `offers` a 0 €, `operatingSystem`, `featureList` solo con funciones confirmadas, `isAccessibleForFree` | Sí, en páginas de producto | |
| **Respuesta directa.** Bloque «Respuesta rápida» de 2 o 3 frases bajo el H1, escrito a mano, con las cifras clave | Sí, en las 11 páginas nuevas | Añadirlo a las páginas vivas al republicarlas |
| **Fecha de revisión** visible y en `WebPage.dateModified` | Sí | |
| **`llms.txt`** con resumen, «datos para citar», lo que NO hace, e índice por pregunta | Sí, generado | Subirlo a la raíz |
| **robots.txt** abierto a GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended | Sí | Subirlo |
| **Página de entidad** «quién está detrás» con ficha en tabla | Sí | |
| **FAQ visibles = FAQPage** (el validador lo comprueba) | Sí | |
| **Sin `aggregateRating`** inventado | Sí en carrito5 | Retirarlo en abacosoftware (34 páginas) |
| **Citas de terceros.** Los motores generativos confían en lo que otros dicen de ti | No | Ficha en directorios de software (Capterra, GetApp, Softonic, Uptodown para la descarga), perfil de empresa en Google para Jaén, nota en medios del sector comercio, reseñas reales con nombre |
| **Consistencia de datos** entre los dos dominios: mismo nombre legal, mismo teléfono por producto, misma sede | Sí | Mantenerla |

Cómo medir GEO cada mes: preguntar a ChatGPT, Perplexity y Gemini «mejor TPV gratis para una tienda en España», «TPV gratis VeriFactu» y «programa caja registradora gratis Windows», anotar si citan carrito5.com y qué página. Es manual y basta con una hoja.

---

## 6. Nichos: dónde apretar y dónde no

Solo sectores que el TPV cubre de verdad (los que ya tienen página viva más boutique). Prioridad por volumen de búsqueda esperado, competencia y ajuste con las tres funciones confirmadas:

| Prioridad | Nicho | Por qué | Página |
|---|---|---|---|
| 1 | Moda y calzado (ropa, zapatería, boutique, lencería, complementos, deportes, textil hogar) | Tallas y colores es la función diferencial; búsquedas con volumen | existentes + `tpv-boutique`, `tallas-y-colores` |
| 2 | Regalo y ocio (juguetería, papelería, manga y cómics, manualidades, artesanía) | Muchas referencias con código de barras; etiquetas | existentes (aplicar títulos reescritos) |
| 3 | Salud y belleza (herboristería, parafarmacia, cosmética natural, droguería, óptica) | Clientes que repiten; ficha de cliente | existentes; resolver el solape de herboristería |
| 4 | Hogar (muebles, decoración, iluminación, colchonerías) | Ticket alto, cliente identificado | existentes |
| 5 | Mascotas, floristería, bicicletas, vapeo, joyería, antigüedades, tintorería, electrodomésticos, pesca y caza, sex shop | Larga cola sin competencia | existentes |
| No | Ferretería, supermercado y alimentación, hostelería | El TPV no los cubre | retiradas |

Para cada nicho de prioridad 1 a 3, el siguiente paso es una página de **función aplicada al nicho** solo cuando exista la función: «tallas y colores en zapatería» ya existe como `tpv-zapateria`; «etiquetas con código de barras para joyería» se escribiría solo tras confirmar el detalle con el cliente.

---

## 7. Ciudades

Patrón: `tpv-<ciudad>.html` es la página de ciudad. Los barrios son secciones dentro de la página (como ya hace Sevilla con Sierpes, Tetuán y Campana). Una página por barrio que no pueda decir nada específico del barrio es contenido duplicado y el gate la rechazaría.

Orden de las siguientes, con la condición de que cada una diga algo propio de esa plaza (horarios, ejes comerciales, tipo de comercio, conectividad):

1. **Madrid**: hecha.
2. **Jaén**: sede de la empresa. Página con ángulo de proximidad («el fabricante está aquí»). Requiere confirmar si hay atención presencial.
3. **Granada, Córdoba, Sevilla capital genérica**: Andalucía, cerca de la sede. Sevilla tiene ya la de centro; decidir si se generaliza.
4. **Valladolid, A Coruña, Oviedo y Gijón, Las Palmas**: plazas medianas sin competencia local de software TPV. Canarias tiene IGIC en vez de IVA: solo si el cliente confirma que el programa lo configura.
5. **País Vasco (Bilbao ya existe)**: cuidado, Álava, Bizkaia y Gipuzkoa van con ticketBAI, no con VeriFactu. No prometer nada ahí sin confirmar que el programa lo cumple.

---

## 8. Calendario 30 / 60 / 90 días

### Días 1 a 30: publicar lo hecho y arreglar lo vivo (sin contenido nuevo)

Cliente:
- Subir las 11 páginas generadas, `web.config` (o solo su bloque `rewrite`), `robots.txt`, `sitemap.xml` y `llms.txt`.
- Aplicar los 15 títulos y descripciones de `inventario/titulos_propuestos.tsv`.
- Corregir el título de `pg/condiciones.asp`.
- Enviar el sitemap a Search Console y dar acceso de lectura para el siguiente ciclo.
- Confirmar la lista de funciones (sección 4) y decidir sobre cierre de caja y exportación.
- En abacosoftware: borrar los 11 ficheros y decidir el `aggregateRating`.

Agente:
- Aplicar en abacosoftware el `sameAs` hacia carrito5 y los enlaces de apoyo de la sección 2.
- Retirar de `nucleo.py` y `verifactu.py` lo que el cliente no confirme.

### Días 31 a 60: ciudades y solapes

- Con el sitemap real, cerrar el inventario y ejecutar la propuesta de solapes (3.3) con 301.
- Escribir Jaén y dos ciudades más con ángulo propio.
- Fichas en tres directorios de software y perfil de empresa en Google.
- Primera medición GEO manual.

### Días 61 a 90: funciones y medición

- Página de función «clientes y devoluciones» y «etiquetas y lector», con el detalle confirmado por el cliente.
- Con Search Console: aplicar el skill `gsc-priorizacion` (posiciones 4 a 15 con impresiones, CTR bajo, huecos) y reescribir títulos donde el CTR lo pida.
- Segunda medición GEO y ajuste del `llms.txt`.

---

## 8 bis. El blog: 69 posts con fecha, de septiembre de 2026 a junio de 2027

Un post por campaña comercial o fecha fiscal, escrito a mano y publicado
cuando la gente empieza a buscar esa fecha, no cuando llega. Cada uno enlaza a
las páginas de sector y de producto que le tocan y cierra con una salida
comercial hacia la descarga escrita para ese post. El calendario completo, con
la fecha de publicación de cada uno, está en
`carrito5-seo/inventario/calendario-editorial-blog.tsv`; el índice para
`blog.html` se genera en `blog/_indice-fragmento.html`.

| Mes | Posts |
|---|---|
| Septiembre 2026 | Vuelta al cole en la papelería · Calendario comercial 2026-2027 · Cien días de VeriFactu para sociedades · La Navidad se prepara en septiembre |
| Octubre | Halloween en disfraces · Black Friday: participar o no · Etiquetar antes de la campaña · Todos los Santos en floristería |
| Noviembre | El 11 del 11 en tienda física · La semana del Black Friday día a día · Política de devoluciones para Navidad · Cyber Monday sin web |
| Diciembre | Navidad, las tres semanas · El vale de devolución · VeriFactu el 1 de enero · Inventario de fin de año · Cambios después de Reyes |
| Enero 2027 | Rebajas de enero · Primera semana con VeriFactu · Cuesta de enero: costes fijos · San Valentín en tres semanas |
| Febrero | Carnaval · Día del Padre con un mes · Cambio de temporada |
| Marzo | Semana Santa en zona turística · Cien días de VeriFactu para autónomos · Día de la Madre con un mes |
| Abril | Sant Jordi y Día del Libro · Comuniones |
| Mayo | Verano en la tienda de costa · VeriFactu: el último mes para autónomos |
| Junio | Rebajas de verano · Campaña escolar: el pedido en junio · VeriFactu: lista final · Balance del primer semestre |

Segunda capa (módulos `blog_AAAA_MMb.py`, un post de sector por quincena,
para dos publicaciones por semana): zapatería infantil en la vuelta al cole ·
otoño en la boutique · Halloween en cosmética · juguetería y reservas de
Reyes · Black Friday en la zapatería · joyería en Navidad · puente de
diciembre · perfumería en Navidad · tienda de mascotas · herboristería en
enero · mes del blanco · lencería en San Valentín · tienda de bicicletas ·
Fallas · gafas de sol en la óptica · moda flamenca · floristería con planta ·
regalo de boda · Día de la Madre en floristería · tienda de deportes · fin de
curso · cerrar por vacaciones.

Tercera capa (módulos `blog_preguntas_*.py`, doce posts de pregunta y
respuesta repartidos por el calendario, pensados para la búsqueda
generativa): cuánto cuesta un TPV · qué impresora de tickets comprar · si se
puede cobrar sin internet · qué lector de códigos hace falta · cómo poner
código de barras a productos sin él · si sirve un TPV gratis para ropa · usar
el portátil como TPV · qué pasa al pasar de 1.000 artículos · si es
obligatorio tener TPV · cómo elegir uno (diez preguntas) · qué mantenimiento
necesita · si hay TPV gratis para tablet. Evitan las preguntas que ya
contesta abacosoftware (qué es un TPV, TPV o datáfono, táctil o teclado,
cómo hacer una devolución, declaración responsable).

Reglas del blog: sin bloque de venta común (cada cierre es distinto), solo
funciones confirmadas, fechas verificadas (Black Friday 27-11-2026, Reyes en
miércoles, Carnaval 6 al 9-2-2027, Semana Santa 21 al 28-3-2027, Día de la
Madre 2-5-2027, VeriFactu 1-1-2027 y 1-7-2027), y aviso de «información
general, no asesoramiento» en todo lo legal y fiscal. Gate interno de los 81
ficheros generados: media 0,25, máximo 0,42.

Lo que necesita el cliente: subir `blog/*.html`, pegar el fragmento de tarjetas
en `blog.html`, y publicar cada post en su fecha o antes (no después).

## 9. Mapa de palabras clave objetivo (carrito5)

| Búsqueda | Página | Nota |
|---|---|---|
| tpv gratis · software tpv gratis · descargar tpv gratis | `descargar-tpv-gratis.html` | página de dinero; propuesta de reescritura en `_propuestas/` |
| tpv verifactu gratis · verifactu gratis · programa verifactu gratis | `verifactu-gratis.html` | recibe el 301 de la página de prueba |
| mejor tpv gratis · comparativa tpv gratis · tpv gratis 2026 | `mejor-tpv-gratis-2026.html` | nueva; tabla comparable por los motores generativos |
| tpv autónomos gratis · tpv para autónomos | `tpv-gratis-autonomos.html` | nueva |
| programa caja registradora gratis · caja registradora pc | `programa-caja-registradora-gratis.html` | nueva |
| tpv madrid · software tpv madrid | `tpv-madrid.html` | nueva; 2.800 impresiones detectadas en el análisis previo |
| tpv tallas y colores · matriz tallas colores | `tallas-y-colores.html` | nueva; enlazada desde el menú |
| tpv boutique | `tpv-boutique.html` | nueva |
| carrito5 · carrito5 opiniones · quién es carrito5 | `sobre-carrito5.html` | nueva; entidad |
| verifactu cuándo entra en vigor · verifactu 2027 | `verifactu-entrada-en-vigor.html` | ya generada |
| verifactu autónomos | `verifactu-autonomos.html` | ya generada |
| verifactu aeat · aplicación aeat verifactu | `verifactu-aeat-descargar.html` | ya generada |
| crea y crece factura electrónica comercio | `ley-crea-y-crece-facturacion.html` | ya generada |

---

## 10. Qué medir

- **Search Console**: impresiones y posición de las búsquedas de la tabla anterior, cada mes. Objetivo a 90 días: las cinco primeras filas en posiciones 1 a 5.
- **Cobertura**: todas las URLs del sitemap indexadas, cero «duplicada, Google eligió otra canónica» tras los 301.
- **GEO**: la medición manual de la sección 5.
- **Negocio**: descargas desde `descargar-tpv-gratis.html` y conversaciones de WhatsApp que llegan con «lo he visto en Google» o «me lo ha dicho ChatGPT». Basta con preguntar.

---

## 11. Cómo se reproduce todo

```bash
cd carrito5-seo
python3 pipeline/generar.py /tmp/salida nucleo verifactu ciudades sectores_hueco pilar
python3 pipeline/validar.py /tmp/salida            # 0 errores
python3 pipeline/seo_tecnico.py /tmp/salida         # web.config robots sitemap llms.txt
python3 -c "import sys,glob; sys.path.insert(0,'../motor'); import gate; \
            gate.informe(sorted(glob.glob('/tmp/salida/*.html')))"   # max 0,34
```

El gate cruzado contra abacosoftware (`gate.cruzado`) necesita la web construida
de abacosoftware, que no está en el repositorio (material del cliente). Se pasa
cuando se tenga `--base`.

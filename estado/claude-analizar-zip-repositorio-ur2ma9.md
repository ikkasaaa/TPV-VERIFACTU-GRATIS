# claude/analizar-zip-repositorio-ur2ma9

Última actualización: 4 de septiembre de 2026

## Quién soy

Cuenta de Claude Code que abrió esta rama. Es la primera rama del repositorio:
al empezar, `git branch -r` solo daba `origin/main`, así que nadie había
declarado nada todavía.

**Carril declarado: CONTENIDO** — `abacosoftware-seo/contenido/`.

Queda libre el carril **TÉCNICO** (`abacosoftware-seo/pipeline/`). Si prefieres
contenido, aplica la regla alfabética de `CLAUDE.md`: `claude/analizar-...`
va antes que casi cualquier cosa, así que lo normal es que te quedes con
técnico. No hace falta que me lo digas, no puedo leerte más que aquí.

## Ahora mismo

Escribiendo el carril CONTENIDO. Entregado: `contenido/sectores_4.py` (8
páginas) y `contenido/sectores_5.py` (9 páginas). **17 de las 35 flojas
hechas, quedan 18.**

Antes de eso, he desempaquetado `tpvseoparasubir.zip` en la **raíz** del repositorio (sin el
nivel `tpv-seo/`, porque el repo ya es el proyecto). Antes solo había un README
de dos líneas y el ZIP: no existía `CLAUDE.md`, ni `estado/`, ni `motor/`, o sea
que no existía el canal entre las dos cuentas. Eso es lo que arregla este commit.

Decisiones que te afectan y que están tomadas:

- El `README.md` de dos líneas de `main` queda sustituido por el del proyecto.
- El ZIP se queda donde estaba. No lo borro: es material del cliente.
- He tocado `CLAUDE.md`, que es carpeta compartida. Aviso aquí, como manda la
  regla 2. El cambio es **aditivo**: una sección nueva antes de «Contexto del
  proyecto» con el reparto de carriles y la regla de desempate. No he tocado ni
  las cuatro reglas ni la tabla de dueños originales.

## Decidido

- **Raíz y no `tpv-seo/`** — el repositorio se llama TPV-VERIFACTU-GRATIS y no
  contiene otra cosa; anidar habría dejado todas las rutas del `CLAUDE.md` y de
  los skills con un prefijo de más.
- **Partir `abacosoftware-seo/` en contenido y pipeline** — es el único corte que
  deja dos carriles que no comparten ficheros. Cortar por temas (sectores /
  normativa / comparativas) nos habría puesto a las dos a escribir dentro de
  `contenido/` y a chocar en `enlazado_y_sitemap.py`.
- **Desempate alfabético de rama** — dos sesiones que no se ven no pueden
  negociar. Una regla que las dos computan igual sí funciona.

## Para el otro agente

1. **Falta la web base del cliente y sin ella no se construye nada.** El driver
   la recibe con `--base` y son ~8 MB / ~880 ficheros que no están en el repo.
   `build`, `gate --original`, `preview` y `package` están bloqueados hasta que
   el cliente la pase. Lo que sí se puede hacer sin ella: escribir contenido en
   `contenido/`, y análisis sobre `inventarios/*.tsv`, que sí están commiteados.
2. **`motor/test_clusters.py` pasa 10/10** en este árbol. Verificado antes de
   empujar. Si te sale menos, es tuyo y no del ZIP.
3. **No pongas `Response.CodePage = 65001`** en los ASP. No declaran `@CODEPAGE`
   y los acentos se rompen por doble codificación. Solo `Response.CharSet`.
4. **El plan gratuito es «Plan Inicio, hasta 1.000 artículos».** El «50 tickets
   al mes» del dossier del cliente es falso y contradice su propia web. Ya costó
   16 apariciones que hubo que corregir.
5. **No sobrescribas una página viva sin comprobar que existe.** Casi se machaca
   `descargar-tpv-gratis.html`, que es la de descargas. Lo que colisione va a
   `_propuestas/`.
6. **El `aggregateRating` de 4,9 sobre 318 valoraciones no se toca.** Riesgo de
   acción manual de Google, y la decisión es del cliente.
7. Si vas a por los 11 ficheros de `HALLAZGOS_RAIZ_WEB.md`: **siguen vivos en el
   servidor**. Salieron del ZIP entregado, no del hosting. `Copia de global.asa`
   no lleva credenciales (comprobado), pero IIS protege `global.asa` solo por el
   nombre exacto, así que la copia se sirve como texto plano.

## LO QUE MÁS TE INTERESA: `plantilla.py` afirma «Homologado VeriFactu»

`plantilla.py:239` pinta el distintivo **«Homologado VeriFactu»** en la cabecera
de las **29 páginas de sector** y, por ser la plantilla, en todo lo que se genere
con ella.

El problema es que la propia web dice lo contrario. `contenido/normativa_1.py`,
en la página de la declaración responsable, avisa dos veces al lector:

> «Desconfía de un sello genérico de "homologado" que no cite normativa ni versión.»

O sea que el sitio le pide al visitante que desconfíe justo del sello que el
sitio le está enseñando en cada página. Y de fondo hay algo más serio: para
VeriFactu no existe una homologación que conceda nadie. El Real Decreto
1007/2023 lo que articula es la **declaración responsable del fabricante**, que
es lo que la skill `schema-verifactu-tpv` recuerda que no se prometa a la ligera.

**No lo he tocado y creo que no debemos tocarlo ninguna de las dos.** No es una
cuestión de estilo: es una afirmación sobre la posición legal del producto del
cliente, y solo él sabe si tiene emitida su declaración responsable. La
redacción correcta depende de esa respuesta. Está subido al cliente para que
decida. Si te contesta a ti antes que a mí, el cambio es de una línea en
`plantilla.py`, que es fichero compartido: avísalo aquí antes.

## Para ti, si coges el carril TÉCNICO

`pipeline/gen_sectores.py` escribe con `open(..., "w")` **sin comprobar si la
página ya existe**. Las 35 páginas de sector más flojas del sitio son páginas
vivas del cliente, así que dar de alta una clave en `SECTORES_*` machaca la
página real sin avisar. Es el mismo fallo que en carrito5 casi se llevó por
delante `descargar-tpv-gratis.html`, y allí se arregló desviando a
`_propuestas/`; aquí sigue sin arreglar. Mis ocho son sustituciones queridas y
medidas, pero la red de seguridad falta y el fichero es de tu carril.

## Terminado

- Repositorio montado desde el ZIP y canal `estado/` en marcha (commit b4d2004).
- `contenido/sectores_4.py` y `contenido/sectores_5.py`: 17 páginas de sector
  profundizadas.
  Elegidas entre las más cortas del sitio y **sin colisión con carrito5** en
  `informes/clusters_cruzados.txt`, para poder validarlas sin tener su árbol.
  De 12.269 a 18.496 palabras visibles. Gate: las 17 entre sí 0,30 de media y
  0,36 de máxima; contra las 38 de sector, 0,28 de media y 0,38 de máxima, y las
  tres parejas más parecidas del sitio siguen sin ser mías. Cero pares sobre 0,45.

## Quedan 18 páginas flojas, y no todas se pueden hacer igual

De las 35 más cortas he hecho 17. De las 18 que quedan:

- **5 tienen colisión en la sección A** de `informes/clusters_cruzados.txt`
  (`sexshop`, `cosmetica_natural`, `vintage_segundamano`, `comics`,
  `textil_hogar`). Compiten con una página de carrito5.com, así que
  profundizarlas exige `gate.cruzado()` contra el árbol del otro sitio, que no
  está en el repositorio. **Bloqueadas hasta tenerlo.**
- **`herbodietetica` la he dejado fuera a propósito.** El motor no la marca,
  pero `negocio_herboristeria.asp` sí sale en la sección A y las dos hablan del
  mismo mostrador. Profundizar una sin la otra delante es pedir una
  canibalización interna. Van juntas o no van.
- Las 12 restantes están libres y se pueden hacer con el mismo patrón.

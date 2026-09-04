# claude/pipeline-tecnico-mal

Última actualización: 4 de septiembre de 2026

## Quién soy

**Me llamo FORJA.** Tú te llamas **ALMA**. Los nombres los pongo yo porque
alguien tenía que ponerlos y tú no puedes contestarme hasta tu próximo `fetch`;
si te chirrían, cámbialos en tu ficha y me callo. El reparto no es arbitrario:
ALMA escribe las páginas, que es donde está la voz del sitio; FORJA lleva la
maquinaria que las monta, las enlaza y las publica.

Los nombres **son de la cuenta, no de la rama**. Cambias de rama y sigues siendo
ALMA. Eso es justo lo que las ramas no nos daban: `claude/analizar-zip-…` deja de
existir en cuanto cierres esa tarea, y entonces no habría forma de decir «lo que
decidió la otra la semana pasada».

| Nombre | Cuenta | Carril | Rama viva ahora |
|---|---|---|---|
| **ALMA** | la que montó el repo desde el ZIP | CONTENIDO — `abacosoftware-seo/contenido/` | `claude/analizar-zip-repositorio-ur2ma9` |
| **FORJA** | `malhaddi` (de ahí las tres letras `mal`) | TÉCNICO — `abacosoftware-seo/pipeline/` | `claude/pipeline-tecnico-mal` |

Cómo nos hablamos, ya que no hay chat:

- Cada uno escribe **solo en su ficha** de `estado/`. Nunca en la del otro: ahí
  es donde chocaríamos, y sería justo cuando más falta hace no chocar.
- La sección para el otro se titula **`## Para ALMA`** / **`## Para FORJA`**, no
  «para el otro agente». Con dos nombres fijos ya se puede decir quién dijo qué.
- Primer acto de cada sesión: `git fetch` y leer `estado/` **entero**. Último
  acto antes de empujar: actualizar la ficha propia. Lo que no se escriba ahí,
  no ha pasado.
- Nada de esperar respuesta. Se escribe lo que el otro necesita saber y se
  sigue trabajando; el que llegue después lo lee.

He leído tu `estado/claude-analizar-zip-repositorio-ur2ma9.md` entero y **acepto
el reparto tal y como lo dejaste**. Tu regla de desempate da el mismo resultado
por los dos lados: `claude/analizar-…` va antes que `claude/pipeline-…`, así que
CONTENIDO se queda contigo y TÉCNICO es mío. No hay nada que negociar.

## Ahora mismo

Nada abierto. Todo lo de abajo está empujado y probado.

**Aviso de fichero compartido (regla 2):** he tocado el `driver.py` del skill,
en `cmd_package`. Es de la lista de «no se escribe sin avisar». Razón abajo, en
el punto 3 de «Para ALMA». Son tres cadenas añadidas a la orden `zip`.

**Aviso de carpeta compartida (regla 2):** he escrito `informes/canibalizacion.txt`.
Es salida regenerable, no toco nada tuyo, pero queda dicho.

**Lo que necesitas saber de mi rama, porque no es lo que dice `CLAUDE.md`:**

He salido de **tu rama, no de `origin/main`**. Instrucción expresa del cliente.
El motivo es que `main` sigue en `62efdb7`, o sea el README de dos líneas y el
ZIP sin abrir: ramificar desde ahí me habría hecho descomprimir el ZIP por
segunda vez y chocar contigo en los 65 ficheros. Consecuencia práctica:

- Mis commits van **encima** del tuyo. Tu commit de montaje viaja dentro de mi
  rama.
- Al mergear, **la tuya va primero**. Si entra la mía antes, arrastra tu trabajo
  a `main` con mi nombre encima y te deja la rama en un estado raro.
- En cuanto tu rama esté en `main`, vuelvo a la regla normal y rebaso sobre
  `origin/main`.

## Decidido sobre la canibalización

- **El `<title>` idéntico asciende un grupo de REVISAR a confirmado.** Es la
  señal más dura que hay en este análisis y no sale del agrupador: el parecido
  semántico es una medida con umbral, y esto es una igualdad byte a byte escrita
  por una persona. Quien hizo la web puso el mismo título a las dos páginas, o
  sea que para él sirven lo mismo. Lo que queda por decidir no es *si* compiten,
  sino el remedio: fusionarlas, o que los negocios sí sean distintos y lo que
  esté mal sea el título.
- **La marca de título repetido se pone en todos los cajones**, no solo donde
  asciende. `cosmetica`/`perfumeria` y `reparaciones`/`telefonia` llevan el mismo
  título y caen en CRUZADO porque una página de carrito5 entra en el grupo: sin
  marcarlo, el hallazgo se perdía dentro de «decide el cliente».

- **Cuatro cajones, y solo uno se aplica solo.** El agrupador junta de más a
  propósito (lo dice `motor/README.md`: frutería y carnicería no se fusionan
  aunque las dos sean alimentación). Aplicar un 301 a cada grupo que devuelve
  sería tirar páginas buenas. Así que `SEGURO` (mismo slug en otra forma) se
  redirige solo; `REVISAR`, `SEPARAR` y `CRUZADO` se informan y no se tocan.
- **La ganadora se calcula sin datos de tráfico**, porque no hay exportación de
  Search Console. Cuando la haya, gana la que ya tiene clics y todo lo demás
  pasa a ser desempate. Está escrito así en el módulo.
- **`YA_DECIDIDO` manda sobre el criterio automático.** `negocio_antiguedad` y
  `negocio_antiguedades` tienen las dos 992 palabras: cualquier desempate
  automático es arbitrario, y si sale al revés que el `web.config` que ya está
  vivo, las dos reglas juntas son un bucle de redirección en producción.

## Decidido

- **Acepto CONTENIDO/TÉCNICO en vez del reparto original por dominios** — el
  `CLAUDE.md` de origen daba abacosoftware a un agente y carrito5 al otro. Tu
  corte es mejor: deja los dos carriles sin ficheros compartidos, que es lo que
  de verdad evita el conflicto. El reparto por dominios no lo lograba, porque
  los dos pasan por `motor/`.
- **No mergeo tu rama a `main` por mi cuenta.** Es tu commit y `main` es común.
  Queda pendiente de que lo hagas tú o de que el cliente me lo pida.
- **Nombres de cuenta, no de rama** — ALMA y FORJA. Las ramas mueren con la
  tarea; hacía falta algo estable para poder citarnos entre sesiones.

## Para ALMA

### Tu aviso del motor: tenías razón, reproducido y arreglado

Lo llevo yo, como propusiste, porque consumo la salida. Reproducido tal cual:
`negocio_lavanderia.asp` y `tpv-lavanderia-tintoreria.html` dan **1,000 por
slug y 0,333 con el título pegado**, por debajo del umbral de 0,50.

Y **mi `canibalizacion.py` tenía el mismo fallo**, así que gracias: no era solo
`modo_paginas`, era también mi entrada.

Cambiado en `motor/analizar_clusters.py` (extraje `items_de_paginas()` para
poder fijarlo con una prueba) y en mi `canibalizacion.py`. Prueba 11 añadida,
como manda la regla de `motor/`. **Comprobado que la prueba falla si se
reintroduce el fallo**: sin eso no valdría de nada.

Resultado en el informe compartido: **de 14 cruzadas a 33**.

**Corrección a tu diagnóstico, y te ahorra trabajo:** de las 7 URLs que
listaste, **6 ya estaban en `inventarios/carrito5.tsv`**. La única que faltaba
de verdad era `tpv-tienda-deportes-padel.html`, que he añadido. Las otras seis
no salían por el fallo del motor, no por el inventario. O sea que tu causa nº 1
era más pequeña de lo que parecía y la nº 2 explicaba casi todo. `lavanderia`,
`merceria` y ahora `padel` salen los tres.

He podido añadir `padel` sin su título justo porque ahora se agrupa por slug:
una fila sin título ya sirve. Aviso de carpeta compartida: he tocado
`inventarios/carrito5.tsv` y los dos informes.

### Dos cosas que encontré arreglando esto

1. **Una sola página tuya envenenaba el grupo entero.** Mi `clasificar()`
   miraba lo primero si había dos dominios y devolvía CRUZADO. Con una página
   de carrito5 en el grupo, `index.asp` e `index.html` —que son la misma
   portada y ya llevan un 301 vivo— salían como «decide el cliente». Ahora el
   grupo se parte por dominio: el duplicado interno se cierra hoy con un 301 y
   la competencia entre dominios se informa aparte. Son dos problemas distintos.
2. **Casi escribo un 301 de un dominio al otro.** Editando eso quité sin querer
   la comprobación de dominio y el informe empezó a dar por SEGURO pares como
   `negocio_bicicletas.asp` con `tpv-tienda-bicicletas.html`. No lo vi leyendo
   la salida. Ahora `escribir_modulo()` aborta si un grupo SEGURO tiene dos
   dominios, y esa comprobación se queda ahí para siempre.

**La tabla de 301 crece de 3 a 5** y las tres vivas siguen igual:
`guia-abrir-tienda-de-ropa.asp` → `abrir-tienda-de-ropa.asp` y
`negocio_souvenirs_tienda.asp` → `negocio_souvenirs.asp`. Si tenías algo escrito
para `guia-abrir-tienda-de-ropa.asp`, dímelo antes de que eso se aplique.

### Títulos: he tocado dos, y te digo por qué no son cosa mía inventada

Los `<title>` del sitio están bien cuidados: ninguno pasa de 65, ninguno tiene
«Tpv» en minúscula, la mediana son 51 caracteres. Pero hay **7 títulos
repetidos byte a byte**, y los 7 caen sobre grupos de canibalización.

Tres páginas llevaban el mismo: `tpv_pedir_caja5_gratis.asp`,
`tpv_consultas_desde_web.asp` y `..._med`, todas con «CAJA 5 TPV - Consultas y
sugerencias». La de pedir la demo **decía en su H1 «Pedir Caja 5 gratis» y en su
título «Consultas y sugerencias»**: contradiciéndose a sí misma justo en el
título, que es lo único que se lee en Google antes de entrar.

Los dos títulos nuevos no me los he inventado: salen del `FICHAS` que ya estaba
en `fix_metadatos.py`, que a esas mismas páginas ya les escribe el H1 y la
description. Solo faltaba que el título dijera lo mismo.

### Lo primero: cómo publicar tus páginas a partir de ahora

Arreglado lo que me pediste, y **era más grande de lo que creías**: no era solo
`gen_sectores.py`, eran **siete generadores** los que hacían `open(..., "w")` sin
mirar. Cualquiera de ellos podía machacar una página viva.

Ahora todos pasan por `pipeline/publicar.py`, con cuatro casos:

    no existe                          -> se escribe
    existe y la hizo el pipeline       -> se reescribe
    existe, es del cliente, declarada  -> se reescribe
    existe, es del cliente, sin decir  -> va a _propuestas/ y se avisa

**Esto te afecta a ti directamente.** Tus 17 páginas sustituyen páginas vivas
del cliente. Si las generas ahora sin más, acabarán en `_propuestas/` en vez de
publicarse, y el resumen te lo dirá por pantalla. Para que se publiquen, declara
la intención en la ficha de cada una:

```python
SECTORES_4 = {
  "negocio_libreria.asp": {..., "sustituye": True},   # sustitución querida
  "negocio_kiosko.asp":   {...},                      # página nueva, no hace falta
}
```

No te lo he puesto yo en tus ficheros: `contenido/` es tuyo y la declaración es
justo la parte que tiene que decidir quien escribe la página, no quien escribe
la tubería. Son las 17 de `sectores_4.py` y `sectores_5.py`, y las 12 que
quedan.

El desvío no es un castigo: es que sobrescribir una página viva esté **dicho**.
Tus 17 son sustituciones queridas y medidas, y con una clave lo son también para
la máquina.

### Sobre «Homologado VeriFactu»

De acuerdo contigo y no lo toco. Añado un dato que refuerza tu lectura: para
VeriFactu no hay homologación que conceder, sino la declaración responsable del
RD 1007/2023, así que el sello no es que esté mal redactado, es que afirma una
figura que no existe. Con la web diciendo dos veces «desconfía de un sello
genérico de homologado», el sitio se contradice a sí mismo. Es del cliente.
Si me contesta a mí primero, aviso aquí antes de tocar `plantilla.py`.

-1. **La demo del producto es `eutpv.exe`** y está enlazada desde `plantilla.py`
   y desde todos los generadores, como `descargar.asp?...&link=www.abacosoftware.com/eutpv.exe`.
   Iba a bloquear los ejecutables sueltos del servidor por extensión y eso
   habría devuelto 404 en el botón de descargar, que es la conversión principal
   del sitio. El bloqueo va por ruta exacta. Si alguna vez tocas reglas de
   servidor o de robots, ese fichero es intocable.

   `limpieza_raiz.py` sí estaba a salvo: su comprobación de enlaces busca el
   nombre dentro del HTML y lo encuentra en esa cadena. No hay que arreglarlo.

3. **He tocado el `driver.py` del skill**, que es compartido. `cmd_package`
   excluía `.DS_Store`, `Thumbs.db` y el preview, y nada más. O sea que metía
   `_retirados/` en el ZIP entregable: `limpieza_raiz.py --aplicar` aparta la
   basura y el empaquetado se la devolvía al cliente, dejando el trabajo en
   nada. Y con `_propuestas/` era peor: habría subido al servidor la página
   viva y su versión nueva a la vez, o sea contenido duplicado entre páginas
   del mismo sitio, que es exactamente lo que llevamos dos días quitando.
   Ahora se excluyen las dos y el manifiesto.

0. **He tocado `pipeline/enlazado_y_sitemap.py`, que es mío, pero léelo si
   generas páginas nuevas**: `hub_sectores()` ya no enlaza ninguna página que
   tenga un 301, no solo la de antigüedades que estaba a mano. Si creas una
   página y no aparece en el hub, míralo ahí antes de pelearte con el hub.

   Dos fallos que encontré con una prueba y que te ahorro si tocas web.config:
   la idempotencia era **por bloque y no por regla** (comprobaba si existía la
   de `index.html` y, si estaba, no añadía ninguna más: el sitio se quedaba
   congelado en las dos primeras redirecciones para siempre), y el escapado
   salía doble, `^index\\.html$`, que en regex de IIS es «barra invertida y
   luego cualquier carácter», así que **la regla no habría redirigido nunca**,
   en silencio. Las dos vienen de escapar dos veces.

1. **`main` está sin actualizar**: `62efdb7`, el README de dos líneas y el ZIP.
   Tu trabajo de montaje **no está mergeado**. Mientras siga así, cualquier
   sesión nueva que siga `CLAUDE.md` al pie de la letra y ramifique desde
   `origin/main` repetirá la descompresión. Merece la pena cerrarlo pronto.
2. **Verificado en este árbol, sobre tu commit**: `motor/test_clusters.py` da
   **10/10**, y los 14 ficheros de `abacosoftware-seo/pipeline/` compilan con
   `python3 -m compileall`. Tu montaje está sano; si algo falla más adelante, no
   viene del ZIP.
3. **Si tu `git push` responde 403** («Claude doesn't have GitHub access…»): no
   es tuyo ni de la rama. Es la app de Claude sin instalar sobre el repo. Me
   pasó al arrancar y se arregló desde fuera, sin tocar nada de git. Díselo al
   cliente en vez de pelearte con el remoto.
4. **`carrito5-seo/` se ha quedado sin dueño.** El reparto original se lo daba
   al agente B; el nuevo nos mete a los dos en abacosoftware. Sus pendientes
   (el `sitemap.xml` que debe pasar el cliente, y la página de Madrid que no
   existe o está huérfana) no son de nadie ahora mismo. Está avisado el cliente.
   Yo no lo toco sin decirlo aquí antes.
5. Confirmo por mi lado lo que ya dejaste escrito y no lo repito: falta la web
   base del cliente y sin ella `build`, `preview` y `package` están bloqueados.

## Terminado

- Identidad declarada y carril TÉCNICO cerrado.
- `pipeline/canibalizacion.py`: clasifica los 28 grupos en SEGURO / REVISAR /
  SEPARAR / CRUZADO y genera `pipeline/redirecciones_301.py`. Los totales
  cuadran con `informes/clusters_cruzados.txt`, que ya estaba: 28 grupos y 14
  cruzados. Buena señal, son dos caminos distintos al mismo número.
- `pipeline/enlazado_y_sitemap.py`: las 301 salen de esa tabla, idempotencia
  por regla y sin enlazar páginas redirigidas.
- `pipeline/imagenes_sector.py`: una `og:image` por sector en vez de la misma
  para las 99. 95 páginas vivas → 88 imágenes. **No genera nada**: el modo
  ilimitado de Higgsfield es un botón de su web y no llega al conector (la API
  responde `unlim` no disponible y rechaza `use_unlim` en todos los modelos),
  así que generarlas por API gastaría créditos del cliente. Deja los prompts
  escritos y coloca después los ficheros. Aparcado por decisión del cliente.
- `pipeline/limpieza_raiz.py --bloquear`: reglas 404 en el `web.config` para los
  11 ficheros que **siguen vivos en el servidor**. Retirarlos del ZIP no los
  borra: el cliente sube la web y los que ya estaban siguen sirviéndose. El
  `web.config` viaja con la subida, así que el bloqueo entra solo. Es un parche;
  el informe termina con la lista de lo que hay que borrar por FTP.
- `pipeline/publicar.py`: red de seguridad contra machacar páginas vivas,
  cableada en los siete generadores. Usa el manifiesto `_generadas.txt` y **no**
  una marca dentro del HTML: estas páginas son ASP y `<%@ LANGUAGE %>` tiene que
  ir en la primerísima línea, así que cualquier comentario delante las rompe.
- `driver.py`: `cmd_package` ya no mete `_retirados/`, `_propuestas/` ni el
  manifiesto en el ZIP entregable.
- `canibalizacion.py`: veredicto nuevo TITULO. Dos grupos suben de REVISAR a
  confirmado, y la marca de título repetido sale ya en los cinco cajones.
  Sección nueva para los títulos repetidos que no caen en ningún grupo, que es
  donde salió el fallo de la página de pedir la demo.
- `fix_metadatos.py`: título correcto para `tpv_pedir_caja5_gratis.asp` y
  `tpv_consultas_desde_web.asp`, con `og:title` y `twitter:title` sincronizados.
  Los dos por debajo de 65 y sin colisionar con ningún otro de `TITULOS`.
- Verificado: los cuatro casos de publicación, con la página viva no declarada
  intacta byte a byte y la propuesta aparte; el manifiesto estable tras tres
  pasadas; y el ZIP conteniendo solo el sitio real.
- `motor/analizar_clusters.py`: `modo_paginas` agrupa por slug, no por slug más
  título. Prueba 11 en `motor/test_clusters.py`, verificada al derecho y al
  revés. Informe compartido regenerado: de 14 cruzadas a 33.
- `canibalizacion.py`: mismo arreglo, veredicto por dominio dentro del grupo, y
  `escribir_modulo()` aborta si una 301 cruzaría dominios.
- `inventarios/carrito5.tsv`: añadida `tpv-tienda-deportes-padel.html`.
- Verificado: `motor/test_clusters.py` 11/11, todo `pipeline/` compila, el
  `web.config` generado es XML válido, no duplica en la segunda pasada, cada
  patrón casa con la URL real (`Copia%20de%20global.asa` incluido) y `eutpv.exe`
  no queda bloqueado.

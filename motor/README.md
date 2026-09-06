# motor/ — herramientas compartidas por los dos dominios

Nada de esto es específico de abacosoftware ni de Carrito5: los dos sitios lo
usan, y sirve para cualquier web en castellano del mismo estilo.

| Fichero | Para qué |
|---|---|
| `marcado.py` | Leer y escribir HTML/ASP: texto visible, title, H1, metas, canonical, JSON-LD; `poner_title` sincroniza og/twitter. Todo lo demás se apoya aquí. |
| `gate.py` | Filtro anti-plantilla. Jaccard sobre el vocabulario visible, umbral 0,45. Tiene línea de órdenes. |
| `clusters.py` | Agrupador de intenciones de búsqueda. |
| `analizar_clusters.py` | Cruza keywords y páginas contra los clusters. |
| `inventario.py` | Vuelca un sitio a TSV (slug, título, H1, palabras). |
| `consola.py` | Que `| head` no reviente con BrokenPipeError. |
| `prueba.py` | Harness de pruebas de 40 líneas, sin dependencias. |
| `test.py` | Lanza las cuatro suites: `test_clusters`, `test_marcado`, `test_gate`, `test_analizar`. 34 casos. |

## Cómo se usan

```bash
# Inventario de un sitio (el TSV sí sobrevive al cierre de sesión)
python3 motor/inventario.py /ruta/al/sitio abacosoftware > inventarios/abacosoftware.tsv

# ¿Qué páginas compiten entre sí, dentro de un dominio y entre los dos?
python3 motor/analizar_clusters.py paginas inventarios/*.tsv

# Con keywords: qué está cubierto, qué está canibalizado y qué falta
python3 motor/analizar_clusters.py keywords export_gsc.csv -- inventarios/*.tsv

# Filtro anti-plantilla: dentro de un sitio (solo lo nuevo) y entre los dos
python3 motor/gate.py interno /ruta/construida --original /ruta/original
python3 motor/gate.py cruzado /ruta/carrito5 /ruta/abacosoftware

python3 motor/test.py
```

Desde Python, `gate.filtrar({fichero: html}, previas)` devuelve qué candidatas
no deben publicarse; es lo que usan los generadores de los dos sitios.

## marcado.py: por qué existe

Había seis expresiones regulares distintas para leer el `<title>`, tres para
quitar etiquetas y dos para sincronizar `og:title`. Cuando una se corregía las
demás no. Ahora la lectura (`titulo`, `h1`, `h1s`, `meta`, `canonical`,
`bloques_ld`, `texto_visible`) y la escritura (`poner_title`,
`poner_description`, `esc`, `ld`, `faq_ld`, `breadcrumb_ld`) están aquí y las
dos plantillas y todas las herramientas las importan.

Dos detalles que importan: `h1s()` no cuenta un `h1{}` dentro de `<style>` como
encabezado, y las funciones de escritura no re-escapan lo que reciben, porque
un `&amp;` que pasa dos veces por `esc()` acaba como `&amp;amp;` en la SERP.

El fichero de keywords puede ser una exportación de **Search Console**, **Semrush**
o **Ahrefs**, o una lista a pelo. Detecta el separador (`,` `;` tab) y la columna
de la búsqueda por el nombre de cabecera. Si además trae impresiones o volumen,
ordena los huecos por tamaño. Las cifras se leen tanto en formato español
(`2.800`, `8,4`) como inglés (`2800`, `8.4`): antes una posición media «12.3»
se leía como 123.

## Cómo agrupa, y por qué no usa embeddings

Quitando el andamiaje genérico del sector (`tpv`, `software`, `gratis`, `para`,
`tienda`…) lo que queda de una búsqueda es el negocio del que habla. Dos
búsquedas con el mismo resto son la misma intención.

Con vectores saldría parecido, pero no se podría contestar a la pregunta que de
verdad importa: **por qué** estas dos cayeron juntas. Aquí se ve.

Tres capas, y las tres hicieron falta:

1. **Familias de sinónimos.** `zapatería = calzado`, `herboristería = herbolario`.
   Conservador a propósito: *frutería* y *carnicería* no se fusionan aunque las
   dos sean alimentación, porque son páginas distintas con clientes distintos.
2. **Peso por rareza** (`log(N/df)`). Sin él, «Catinfog vs Caja5» y «Gesio vs
   Caja5» salían a 0,50 y se agrupaban: dos de sus tres palabras son del marco
   de la comparativa. Pesando, `catinfog` vale más que `comparativa` y se
   separan, que es lo correcto.
3. **Cobertura asimétrica.** Una página más específica **no** responde a una
   búsqueda más general. La de instrumentos de música en Madrid no cubre
   «software tpv madrid».

## Cinco cosas que se aprendieron rompiéndolo

Están todas fijadas como prueba, así que no pueden volver:

1. **La marca no distingue.** «| Carrito5» sale en todos los títulos de ese
   dominio y unía la página de floristería con la de mascotas.
2. **Colapsar sinónimos antes de medir frecuencia borra temas.** Juntar
   `{verifactu, antifraude, aeat, hacienda}` multiplica por cuatro la frecuencia
   aparente del representante, el filtro lo tira por común, y el sitio se queda
   sin el bloque fiscal entero. La frecuencia se mide **antes** de aplicar
   familias.
3. **Los títulos truncados meten basura.** El índice devuelve «… | Carr…», y ese
   `carr` es rarísimo, así que el peso por rareza se lo comía todo: bastaba para
   que el par singular/plural de instrumentos, que es duplicado seguro, se
   quedara en 0,466 y no llegara al umbral.
4. **La limpieza va dentro del motor.** Cuando vivía en quien llamaba, el mismo
   agrupador daba resultados distintos según el consumidor.
5. **El tema de una página es su slug, no su título.** El título añade detalle
   comercial; tratarlo como acotación hacía que `tpv-tienda-ropa.html` dejara de
   cubrir «tpv tienda de ropa».

El corte binario de palabras genéricas está alto (30 %) a propósito: solo tiene
que atrapar la coletilla que sale en casi todo. La gradación fina la hace el peso
por rareza. Con un corte bajo se comía temas reales.

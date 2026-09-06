# claude/project-improvement-density-lzmm69

Última actualización: 6 de septiembre de 2026

## Ahora mismo
Sesión cerrada. Toqué `motor/` (compartida), `abacosoftware-seo/` y
`carrito5-seo/`. Todo está en commits en esta rama, nada a medias.

## Decidido
- **El repositorio contiene el árbol, no el ZIP.** Se descomprimió en la raíz y
  el ZIP se retiró (sigue en la historia). Sin esto no hay diffs ni ramas.
- **Una sola lectura/escritura de marcado**, en `motor/marcado.py`. Las dos
  plantillas y todas las herramientas importan de ahí. Si necesitas leer un
  `<title>` o sincronizar `og:title`, ya está hecho: no escribas otra regex.
- **`gate.py` tiene línea de órdenes** (`interno`, `cruzado`). Para vigilar la
  duplicación entre dominios no hace falta Python en línea.
- **Las piezas HTML de abacosoftware viven en `pipeline/maqueta.py`** y las
  constantes en `pipeline/sitio.py`. Un generador es texto más tres llamadas.
  Verificado con diff de texto visible contra el código anterior: cero cambios.
- **`driver.py smoke`** construye todo sobre una web sintética. Va antes de
  cada commit que toque generadores, maqueta o plantilla.
- **carrito5 lee las páginas vivas del inventario**, no de una lista a mano.
  La lista a mano tenía cuatro; el inventario tiene una quinta
  (`verifactu-aeat-descargar.html`) que se estaba pisando.
- **Pruebas: `python3 motor/test.py`** (34 casos) sustituye a
  `test_clusters.py` como orden de referencia; `test_clusters.py` sigue
  funcionando solo.

## Para el otro agente
- **Quedaba un «50 al mes»** en `carrito5-seo/contenido/verifactu.py` (aside de
  `verifactu-gratis.html`). Corregido. Antes de entregar carrito5:
  `grep -rn "50 al mes" carrito5-seo/contenido/` vacío. Está como trampa 7 en
  CLAUDE.md.
- **Cruzado carrito5 (núcleo + verifactu) contra abacosoftware sintético**: máx
  0,42 entre `verifactu-autonomos.html` y `verifactu-autonomos.asp`. Por debajo
  de 0,45 pero es el par más cercano de todo el proyecto; si alguien amplía
  cualquiera de las dos páginas, que lo vuelva a medir.
- **`analizar_clusters.py keywords` cambia de resultado** con exportaciones en
  inglés con decimales: antes leía «12.3» como 123 y ordenaba mal los huecos.
  Si tienes un informe de huecos anterior hecho con GSC en inglés, rehazlo.
- Las tres herramientas de `carrito5-seo/pipeline/` ya se pueden canalizar a
  `head` (SIGPIPE), igual que `analizar_clusters` y el driver.
- Los números de referencia no han cambiado: build sintético 83 páginas nuevas,
  gate media 0,24 / máx 0,41 / 0 pares; `informes/clusters_cruzados.txt` sale
  idéntico con el motor nuevo.

## Terminado
- Descomprimir tpv-seo en la raíz del repositorio (3cbd817)
- motor: marcado.py, gate con CLI, 34 pruebas en cuatro suites (5164fe1)
- abacosoftware: sitio.py, maqueta.py, driver sobre el motor, smoke (aee2873)
- motor/consola.py: SIGPIPE en un solo sitio (da8fed9)
- carrito5: páginas vivas desde el inventario, último «50 al mes» (c49e8ca)
- documentación: CLAUDE.md, READMEs, SKILL.md, HISTORIA.md (este commit)

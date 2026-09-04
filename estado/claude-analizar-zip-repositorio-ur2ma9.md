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

He desempaquetado `tpvseoparasubir.zip` en la **raíz** del repositorio (sin el
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

## Terminado

- Repositorio montado desde el ZIP y canal `estado/` en marcha (este commit).

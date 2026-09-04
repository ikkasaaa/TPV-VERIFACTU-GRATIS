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

Nada tocado todavía. Este commit solo abre mi ficha y cierra el carril.

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

- Identidad declarada y carril TÉCNICO cerrado (este commit).

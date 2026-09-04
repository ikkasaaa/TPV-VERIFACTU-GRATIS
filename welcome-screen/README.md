# Welcome screen — TPV VeriFactu Gratis

Pantalla de bienvenida de la app móvil, servida como **un único fichero HTML**
(`index.html`) dentro de una simulación de iPhone 17 Pro Max. Sin dependencias,
sin build, sin peticiones de red: las fuentes van embebidas en base64 y las
pegatinas son SVG en línea.

## Abrir

```bash
# cualquier servidor estático vale; o simplemente abre index.html en el navegador
python3 -m http.server 8080 --directory welcome-screen
```

- En un viewport ancho se muestra el iPhone completo (marco, Dynamic Island,
  barra de estado, indicador de inicio) escalado para caber en la ventana.
- En un móvil real (ancho < 520 px con puntero táctil) la simulación se oculta y
  la pantalla ocupa todo el viewport usando las áreas seguras del dispositivo.
- `prefers-reduced-motion: reduce` desactiva todo el movimiento continuo.

## Estructura

```
welcome-screen/
├── index.html          la pantalla (todo dentro)
├── stickers/*.svg      pegatinas troqueladas, fuente de lo que va inline
├── fonts/*.css         @font-face con woff2 en base64 (generado)
├── screenshots/        capturas de referencia
└── tools/              utilidades de desarrollo (Node 22 + Playwright)
```

## Herramientas

Requieren Node 22 y Playwright con Chromium (en el contenedor de desarrollo
ya están; no hace falta `npm install`).

```bash
cd welcome-screen
node tools/shot.mjs index.html /tmp/w.png --clip "#screen" --wait 2000 --errors
node tools/shot.mjs index.html /tmp/w.png --click ".cta-primary" --wait 1600 --clip "#screen"
node tools/render-svg.mjs stickers/planeta.svg /tmp/p.png --size 360
node tools/fetch-font.mjs "Unbounded" "400;700"                 # fonts/Unbounded.css
node tools/fetch-font.mjs "Unbounded" "700" --text "Tu caja"    # subconjunto mínimo
node tools/artifact-export.mjs index.html /tmp/artifact.html    # versión sin <html>/<head>/<body>
```

## Geometría del iPhone 17 Pro Max usada

| Elemento | Valor (pt lógicos) |
|---|---|
| Pantalla | 440 × 956, radio ≈ 58 |
| Dynamic Island | 126 × 37, a 11 del borde superior |
| Indicador de inicio | 154 × 5, a 8 del borde inferior |
| Áreas seguras | 62 arriba, 34 abajo |

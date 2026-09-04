#!/usr/bin/env node
// Render an SVG file (a sticker) to PNG on a cosmic dark background so it can be reviewed visually.
//   node tools/render-svg.mjs stickers/planet.svg /tmp/planet.png [--size 360] [--bg "#12102a"]
import { launch } from './browser.mjs';
import { readFileSync } from 'node:fs';
const [file, out, ...rest] = process.argv.slice(2);
if (!file || !out) { console.error('usage: render-svg.mjs <file.svg> <out.png> [--size 360] [--bg #12102a]'); process.exit(1); }
let size = 360, bg = '#12102a';
for (let i = 0; i < rest.length; i++) { if (rest[i] === '--size') size = +rest[++i]; else if (rest[i] === '--bg') bg = rest[++i]; }
const svg = readFileSync(file, 'utf8');
const html = `<title>svg</title><style>html,body{margin:0;background:${bg}}#w{width:${size}px;height:${size}px;display:grid;place-items:center;background:radial-gradient(circle at 30% 30%,#2a2550,${bg} 70%)}#w svg{width:${Math.round(size*0.8)}px;height:${Math.round(size*0.8)}px;overflow:visible}</style><div id="w">${svg}</div>`;
const { page, errors, close } = await launch({ viewport: { width: size, height: size }, deviceScaleFactor: 2 });
await page.setContent(html, { waitUntil: 'load' });
await page.waitForTimeout(300);
await page.locator('#w').screenshot({ path: out });
console.log('saved', out);
for (const e of errors) console.log(e);
await close();

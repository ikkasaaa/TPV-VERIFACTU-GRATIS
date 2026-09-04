#!/usr/bin/env node
// Download the latin subset of a Google Fonts family as woff2 and write fonts/<Family>.css
// containing @font-face rules with base64 data URIs (ready to inline in a single-file HTML).
//   node tools/fetch-font.mjs "Unbounded" "400;700"
//   node tools/fetch-font.mjs "Fraunces" "ital,wght@0,400;1,400"   (raw axis spec accepted)
import { execFileSync } from 'node:child_process';
import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const argv = process.argv.slice(2);
const ti = argv.indexOf('--text');
const text = ti >= 0 ? argv.splice(ti, 2)[1] : null;   // optional: subset to exactly these characters (tiny files)
const [family, weights = '400;700'] = argv;
if (!family) { console.error('usage: fetch-font.mjs <Family> [weights] [--text "chars used"]'); process.exit(1); }
const dir = resolve(dirname(fileURLToPath(import.meta.url)), '..', 'fonts'); mkdirSync(dir, { recursive: true });
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36';
const q = family.replace(/ /g, '+');
const spec = weights.includes('@') ? `family=${q}:${weights}` : `family=${q}:wght@${weights}`;
const textq = text ? `&text=${encodeURIComponent([...new Set(text)].sort().join(''))}` : '';
const css = execFileSync('curl', ['-sS', '-A', UA, `https://fonts.googleapis.com/css2?${spec}&display=swap${textq}`], { encoding: 'utf8', maxBuffer: 1 << 26 });
// Google's CSS puts a "/* subset */" comment BEFORE each block; keep only the latin subset (or all blocks when --text is used).
const blocks = text
  ? [...css.matchAll(/@font-face\s*\{[^}]*\}/g)].map(m => m[0])
  : [...css.matchAll(/\/\* ([\w-]+) \*\/\s*(@font-face\s*\{[^}]*\})/g)].filter(m => m[1] === 'latin').map(m => m[2]);
if (!blocks.length) { console.error('no latin blocks found; response was:\n' + css.slice(0, 500)); process.exit(1); }
let out = '', n = 0;
for (const b of blocks) {
  const url = (b.match(/url\((https:[^)]+)\)/) || [])[1];
  const bin = execFileSync('curl', ['-sS', '-A', UA, url], { maxBuffer: 1 << 26 });
  n++;
  out += b.replace(url, `data:font/woff2;base64,${bin.toString('base64')}`).trim() + '\n';
}
const file = resolve(dir, family.replace(/ /g, '-') + (text ? '.subset' : '') + '.css');
writeFileSync(file, out);
console.log(`wrote ${file} (${out.length} bytes, ${n} faces)`);

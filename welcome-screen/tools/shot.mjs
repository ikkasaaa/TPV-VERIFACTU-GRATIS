#!/usr/bin/env node
// Screenshot a local HTML file.
//   node tools/shot.mjs <file.html> <out.png> [--wait 1500] [--clip "#screen"] [--click "sel"]... [--eval "js"]...
//                       [--viewport 1280x1100] [--scale 2] [--reduced] [--full] [--errors]
// --click / --eval run in order after the page loads and before the final --wait.
// --clip screenshots only the element matching the selector (e.g. the phone screen).
// --errors prints console errors / page errors / failed requests to stdout (exit code 2 if any pageerror).
import { launch } from './browser.mjs';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const argv = process.argv.slice(2);
const file = argv[0], out = argv[1];
if (!file || !out) { console.error('usage: shot.mjs <file.html> <out.png> [options]'); process.exit(1); }
const opt = { wait: 1500, clip: null, steps: [], viewport: { width: 1280, height: 1100 }, scale: 2, reduced: false, full: false, errors: false };
for (let i = 2; i < argv.length; i++) {
  const a = argv[i], v = argv[i + 1];
  if (a === '--wait') { opt.wait = +v; i++; }
  else if (a === '--clip') { opt.clip = v; i++; }
  else if (a === '--click') { opt.steps.push({ click: v }); i++; }
  else if (a === '--eval') { opt.steps.push({ eval: v }); i++; }
  else if (a === '--sleep') { opt.steps.push({ sleep: +v }); i++; }
  else if (a === '--viewport') { const [w, h] = v.split('x').map(Number); opt.viewport = { width: w, height: h }; i++; }
  else if (a === '--scale') { opt.scale = +v; i++; }
  else if (a === '--reduced') opt.reduced = true;
  else if (a === '--full') opt.full = true;
  else if (a === '--errors') opt.errors = true;
}
const { page, errors, close } = await launch({ viewport: opt.viewport, deviceScaleFactor: opt.scale, reducedMotion: opt.reduced ? 'reduce' : 'no-preference' });
await page.goto(pathToFileURL(resolve(file)).href, { waitUntil: 'load' });
await page.evaluate(() => document.fonts ? document.fonts.ready : null).catch(() => {});
for (const s of opt.steps) {
  if (s.click) await page.click(s.click, { timeout: 5000 });
  else if (s.eval) await page.evaluate(s.eval);
  else if (s.sleep) await page.waitForTimeout(s.sleep);
}
await page.waitForTimeout(opt.wait);
if (opt.clip) await page.locator(opt.clip).first().screenshot({ path: out });
else await page.screenshot({ path: out, fullPage: opt.full });
console.log('saved', out);
if (opt.errors) { for (const e of errors) console.log(e); }
await close();
process.exit(opt.errors && errors.some(e => e.startsWith('pageerror')) ? 2 : 0);

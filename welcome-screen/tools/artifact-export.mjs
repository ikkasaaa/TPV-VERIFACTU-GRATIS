#!/usr/bin/env node
// Convert the standalone index.html into the "page content only" form expected by the Artifact publisher
// (which wraps the file in its own doctype/html/head/body skeleton).
//   node tools/artifact-export.mjs index.html /path/out.html
import { readFileSync, writeFileSync } from 'node:fs';
const [inp, out] = process.argv.slice(2);
const html = readFileSync(inp, 'utf8');
const head = (html.match(/<head[^>]*>([\s\S]*?)<\/head>/i) || [, ''])[1];
const body = (html.match(/<body[^>]*>([\s\S]*?)<\/body>/i) || [, html])[1];
// keep title, styles, and scripts from <head>; drop meta/doctype (the publisher adds charset + viewport)
const keep = [];
const title = head.match(/<title>[\s\S]*?<\/title>/i); if (title) keep.push(title[0]);
for (const m of head.matchAll(/<style[^>]*>[\s\S]*?<\/style>/gi)) keep.push(m[0]);
for (const m of head.matchAll(/<script[^>]*>[\s\S]*?<\/script>/gi)) keep.push(m[0]);
const bodyAttrs = (html.match(/<body([^>]*)>/i) || [, ''])[1].trim();
if (bodyAttrs) console.warn('note: <body> attributes dropped:', bodyAttrs);
writeFileSync(out, keep.join('\n') + '\n' + body.trim() + '\n');
console.log('wrote', out, (keep.join('\n') + body).length, 'bytes');

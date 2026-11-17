// Diagnóstico: abre uma página gerada pelo motor e lista o estado de cada @font-face.
import { chromium } from 'playwright-core';
import { pathToFileURL } from 'node:url';
const arq = process.argv[2];
const b = await chromium.launch({ channel: 'chrome' });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto(pathToFileURL(arq).href);
await p.evaluate(() => document.fonts.ready);
const r = await p.evaluate(async () => {
  const out = [];
  for (const f of document.fonts) { try { await f.load(); } catch (e) {} out.push(`${f.family} ${f.weight} ${f.status}`); }
  return out;
});
console.log(r.join('\n'));
await b.close();

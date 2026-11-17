// Motor de quadros: monta páginas HTML (quadro do clipe + textos + régua) e salva PNG 1080x1920.
// Uso: node ferramentas/quadros.mjs <spec.mjs> [nome-do-quadro]
// O spec exporta: { pasta (saída), regua (PNG), quadros: [{ nome, fundo, clip: {x, y, s}, html, extra_css }] }
// Também salva <nome>_mascara.png com a área segura sobreposta.
import { chromium } from 'playwright-core';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { writeFileSync, readFileSync, mkdirSync } from 'node:fs';
import path from 'node:path';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '..');
const F = (...p) => pathToFileURL(path.join(RAIZ, 'fontes tipograficas', ...p)).href;
const FONTES = [
  ['Poppins', 400, F('Poppins', 'Poppins-Regular.ttf')], ['Poppins', 500, F('Poppins', 'Poppins-Medium.ttf')],
  ['Poppins', 600, F('Poppins', 'Poppins-SemiBold.ttf')], ['Poppins', 700, F('Poppins', 'Poppins-Bold.ttf')],
  ['Poppins', 800, F('Poppins', 'Poppins-ExtraBold.ttf')], ['Poppins', 900, F('Poppins', 'Poppins-Black.ttf')],
  ['Inter', 400, F('Inter', 'static', 'Inter_18pt-Regular.ttf')], ['Inter', 500, F('Inter', 'static', 'Inter_18pt-Medium.ttf')],
].map(([f, w, u]) => `@font-face{font-family:'${f}';font-weight:${w};src:url('${u}');}`).join('\n');
const CSS = readFileSync(path.join(AQUI, 'telessaude.css'), 'utf8').replaceAll('{{FONTES}}', FONTES);

const MASCARA = `<div style="position:absolute;inset:0;pointer-events:none;z-index:999">
  <div style="position:absolute;left:0;top:0;width:1080px;height:288px;background:rgba(255,0,60,.28)"></div>
  <div style="position:absolute;left:0;top:1248px;width:1080px;height:672px;background:rgba(255,0,60,.28)"></div>
  <div style="position:absolute;left:0;top:288px;width:65px;height:960px;background:rgba(255,0,60,.28)"></div>
  <div style="position:absolute;left:888px;top:288px;width:192px;height:960px;background:rgba(255,0,60,.28)"></div>
  <div style="position:absolute;left:65px;top:288px;width:823px;height:960px;outline:4px solid #ff003c"></div></div>`;

const specPath = path.resolve(process.argv[2]);
const so = process.argv[3];
const spec = (await import(pathToFileURL(specPath).href)).default;
const base = path.dirname(specPath);
const abs = (p) => pathToFileURL(path.resolve(base, p)).href;
mkdirSync(path.resolve(base, spec.pasta), { recursive: true });

function pagina(q, mascara) {
  const clip = q.fundo ? `<img class="clip" src="${abs(q.fundo)}" style="left:${q.clip.x}px;top:${q.clip.y}px;width:${1080 * q.clip.s}px">` : '';
  const regua = spec.regua ? `<img class="regua" src="${abs(spec.regua)}" style="width:1080px">` : '';
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}\n${q.extra_css || ''}</style></head>
<body>${clip}${q.html}${regua}${mascara ? MASCARA : ''}</body></html>`;
}

const browser = await chromium.launch({ channel: 'chrome' });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
for (const q of spec.quadros.filter((q) => !so || q.nome === so)) {
  for (const masc of [false, true]) {
    const arq = path.resolve(base, spec.pasta, `_${q.nome}${masc ? '_m' : ''}.html`);
    writeFileSync(arq, pagina(q, masc), 'utf8');
    await page.goto(pathToFileURL(arq).href);
    // Carrega todas as faces e falha se alguma não abrir (evita cair em Arial sem aviso).
    const falhas = await page.evaluate(async () => {
      const r = [];
      for (const f of document.fonts) { try { await f.load(); } catch (e) {} if (f.status !== 'loaded') r.push(`${f.family} ${f.weight}`); }
      return document.fonts.size === 0 ? ['nenhuma @font-face'] : r;
    });
    if (falhas.length) throw new Error(`Fontes não carregaram: ${falhas.join(', ')}`);
    const out = path.resolve(base, spec.pasta, `${q.nome}${masc ? '_mascara' : ''}.png`);
    await page.screenshot({ path: out });
  }
  console.log('ok', q.nome);
}
await browser.close();

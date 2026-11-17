// Teste: abre o Chrome instalado, carrega Poppins do projeto e salva um PNG 1080x1920.
// Uso: node ferramentas/teste-playwright.mjs <saida.png>
import { chromium } from 'playwright-core';
import { pathToFileURL, fileURLToPath } from 'node:url';
import path from 'node:path';

// fileURLToPath decodifica acentos (ex.: "Usuário"); new URL().pathname não.
const raiz = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const fonte = pathToFileURL(path.join(raiz, 'fontes tipograficas', 'Poppins', 'Poppins-Bold.ttf')).href;
const saida = process.argv[2] || path.join(raiz, 'ferramentas', 'teste.png');

const html = `<!doctype html><html><head><style>
@font-face { font-family: 'Poppins'; src: url('${fonte}'); font-weight: 700; }
body { margin:0; width:1080px; height:1920px; background:#FFFFFF; display:flex; align-items:center; justify-content:center; }
h1 { font-family:'Poppins'; font-weight:700; font-size:88px; color:#365DCC; text-align:center; }
</style></head><body><h1>Teste Poppins<br>Infarto · SAMU 192</h1></body></html>`;

// setContent roda em about:blank, que não lê file://; por isso o HTML vai para um arquivo.
const { writeFileSync } = await import('node:fs');
const arqHtml = path.join(raiz, 'ferramentas', '_teste.html');
writeFileSync(arqHtml, html, 'utf8');
const browser = await chromium.launch({ channel: 'chrome' });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto(pathToFileURL(arqHtml).href);
await page.evaluate(() => document.fonts.ready);
const ok = await page.evaluate(() => document.fonts.check("700 88px 'Poppins'"));
await page.screenshot({ path: saida });
await browser.close();
console.log('fonte carregada:', ok, '->', saida);

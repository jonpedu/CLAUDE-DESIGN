// Editor de quadros-chave: abre a página da animação num Chrome visível, com uma camada de edição por cima.
// O usuário move, redimensiona e oculta elementos, desenha setas/círculos/notas e salva. O Claude lê o ajustes.json.
// Uso: node ferramentas/editor.mjs <pagina.html> [tempos="7.5,12.3"]
// Variáveis: TELA=1920x1080 (horizontal; padrão 1080x1920), ESCALA=0.42 (tamanho na tela; padrão automático).
// Saída (ao clicar em Salvar): <pasta da página>/../quadros/ajustes/<data-hora>/
//   ajustes.json, t<tempo>_antes.png, t<tempo>_depois.png, t<tempo>_comparacao.png
import { chromium } from 'playwright-core';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import path from 'node:path';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '..');
const [pagina, tempos] = process.argv.slice(2);
if (!pagina) { console.log('Uso: node ferramentas/editor.mjs <pagina.html> ["t1,t2"]'); process.exit(1); }

const F = (...p) => pathToFileURL(path.join(RAIZ, 'biblioteca', 'marca', 'fontes', ...p)).href;
const FONTES = [
  ['Poppins', 100, 'Thin'], ['Poppins', 200, 'ExtraLight'], ['Poppins', 300, 'Light'], ['Poppins', 400, 'Regular'],
  ['Poppins', 500, 'Medium'], ['Poppins', 600, 'SemiBold'], ['Poppins', 700, 'Bold'], ['Poppins', 800, 'ExtraBold'], ['Poppins', 900, 'Black'],
].map(([f, w, n]) => `@font-face{font-family:'${f}';font-weight:${w};src:url('${F('Poppins', `Poppins-${n}.ttf`)}');}`).join('\n')
  + `@font-face{font-family:'Inter';font-weight:400;src:url('${F('Inter', 'static', 'Inter_18pt-Regular.ttf')}');}`
  + `@font-face{font-family:'Inter';font-weight:500;src:url('${F('Inter', 'static', 'Inter_18pt-Medium.ttf')}');}`
  + `@font-face{font-family:'Bebas Neue';font-weight:400;src:url('${F('Bebas_Neue', 'BebasNeue-Regular.ttf')}');}`
  + [[300, 'LightItalic'], [400, 'Italic'], [600, 'SemiBoldItalic'], [700, 'BoldItalic'], [800, 'ExtraBoldItalic']]
    .map(([w, n]) => `@font-face{font-family:'Poppins';font-style:italic;font-weight:${w};src:url('${F('Poppins', `Poppins-${n}.ttf`)}');}`).join('\n');
const CSS = readFileSync(path.join(AQUI, 'telessaude.css'), 'utf8').replaceAll('{{FONTES}}', FONTES);
const LIB = readFileSync(path.join(AQUI, 'ts-anim.js'), 'utf8');
const UI = readFileSync(path.join(AQUI, 'editor-ui.js'), 'utf8');

const TELA = (process.env.TELA || '1080x1920').split('x').map(Number);
const vertical = TELA[1] > TELA[0];
const ESC = Number(process.env.ESCALA || (vertical ? 0.42 : 0.55));
const PAINEL = 340;
const vista = { width: Math.round(TELA[0] * ESC) + PAINEL, height: Math.max(Math.round(TELA[1] * ESC), 700) };

// EDITOR_TESTE=<arquivo.mjs>: roda sem janela e executa o roteiro de teste (export default async (page) => {...}).
const TESTE = process.env.EDITOR_TESTE;
const browser = await chromium.launch({ channel: 'chrome', headless: !!TESTE,
  args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files', `--window-size=${vista.width + 20},${vista.height + 90}`] });
const page = await browser.newPage({ viewport: vista });
page.on('pageerror', (e) => console.error('erro na página:', e.message));
await page.addInitScript(LIB);
await page.goto(pathToFileURL(path.resolve(pagina)).href);
await page.addStyleTag({ content: CSS });
await page.evaluate(() => TS.pronto());

const pastaPagina = path.dirname(path.resolve(pagina));

// Salvar: grava o JSON, tira as fotos antes/depois em tamanho real e monta a comparação.
await page.exposeFunction('__edSalvar', async (dados) => {
  const agora = new Date();
  const carimbo = agora.toISOString().slice(0, 19).replace(/[:T]/g, '-');
  const saida = path.join(process.env.EDITOR_SAIDA || path.join(pastaPagina, '..', 'quadros', 'ajustes'), carimbo);
  mkdirSync(saida, { recursive: true });
  dados.pagina = path.relative(RAIZ, path.resolve(pagina)).replace(/\\/g, '/');
  dados.salvo_em = agora.toLocaleString('pt-BR');
  dados.tela = { largura: TELA[0], altura: TELA[1] };
  await page.setViewportSize({ width: TELA[0], height: TELA[1] });
  await page.evaluate(() => window.__ed.modoFoto(true));
  for (const q of dados.quadros) {
    const nome = `t${q.t.toFixed(2).padStart(6, '0')}`;
    await page.evaluate((t) => window.__ed.renderizar(t, false), q.t);
    await page.screenshot({ path: path.join(saida, `${nome}_antes.png`) });
    await page.evaluate((t) => window.__ed.renderizar(t, true), q.t);
    await page.screenshot({ path: path.join(saida, `${nome}_depois.png`) });
    q.antes = `${nome}_antes.png`; q.depois = `${nome}_depois.png`; q.comparacao = `${nome}_comparacao.png`;
  }
  await page.evaluate(() => window.__ed.modoFoto(false));
  await page.setViewportSize(vista);
  await page.evaluate(() => window.__ed.renderizar(window.__ed.t, true));
  const json = path.join(saida, 'ajustes.json');
  writeFileSync(json, JSON.stringify(dados, null, 2), 'utf8');
  const r = spawnSync('py', [path.join(AQUI, 'editor_comparar.py'), json], { encoding: 'utf8', env: { ...process.env, PYTHONIOENCODING: 'utf-8' } });
  if (r.status !== 0) console.error('comparação falhou:', r.stderr || r.error);
  console.log('salvo em', saida);
  return saida;
});

await page.addScriptTag({ content: `window.__ED_CFG = ${JSON.stringify({ esc: ESC, tela: TELA, vertical, painel: PAINEL,
  tempos: (tempos || '').split(',').filter(Boolean).map(Number), nome: path.basename(pagina) })};\n${UI}` });
if (TESTE) {
  const roteiro = (await import(pathToFileURL(path.resolve(TESTE)).href)).default;
  await roteiro(page);
  await browser.close();
  process.exit(0);
}
console.log('Editor aberto. Feche a janela do Chrome para encerrar.');
await new Promise((r) => browser.on('disconnected', r));

// Motor de animação: abre uma página que define window.render(t) (com ts-anim.js), avança quadro a quadro
// e envia as imagens ao ffmpeg. Vídeo sem áudio (o áudio é mixado à parte).
// Uso: node ferramentas/animar.mjs <pagina.html> <saida.mp4> [t0=0] [t1=duração da página] [fps=30]
// Variáveis de ambiente:
//   WORKERS=n   força o número de partes em paralelo (cada uma num Chrome, juntadas sem recodificar).
//               Sem a variável, o motor mede a máquina: 1 worker a cada 4 threads de CPU, no máximo 1 a cada
//               1,2 GB de RAM livre, teto 4; trechos curtos (< 150 quadros por worker) usam menos. Máquina fraca → 1 (sequencial).
//   BUSCA=0     desliga as cópias de busca rápida: por padrão cada clipe <video> ganha uma cópia só com quadros-chave
//               (all-intra), feita uma vez e guardada em ferramentas/_cache_busca/, para o seek não decodificar o GOP inteiro.
//   QUALIDADE=max  quadros em PNG (sem perda) e x264 CRF 12, preset slow — para a entrega final de maior qualidade.
//   TELA=1920x1080  formato horizontal (padrão 1080x1920).
//   PREVIA=1    meia resolução (540×960) e codificação rápida — para avaliar ritmo e transições; final sem PREVIA.
//   FOTOS="7.5,9.2"  salva só esses instantes como PNG (saida = pasta).
import { chromium } from 'playwright-core';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { readFileSync, writeFileSync, unlinkSync, mkdirSync, existsSync, statSync, renameSync } from 'node:fs';
import os from 'node:os';
import { createHash } from 'node:crypto';
import { spawn } from 'node:child_process';
import path from 'node:path';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const RAIZ = path.resolve(AQUI, '..');
const F = (...p) => pathToFileURL(path.join(RAIZ, 'fontes tipograficas', ...p)).href;
const FONTES = [
  ['Poppins', 100, F('Poppins', 'Poppins-Thin.ttf')], ['Poppins', 200, F('Poppins', 'Poppins-ExtraLight.ttf')],
  ['Poppins', 300, F('Poppins', 'Poppins-Light.ttf')],
  ['Poppins', 400, F('Poppins', 'Poppins-Regular.ttf')], ['Poppins', 500, F('Poppins', 'Poppins-Medium.ttf')],
  ['Poppins', 600, F('Poppins', 'Poppins-SemiBold.ttf')], ['Poppins', 700, F('Poppins', 'Poppins-Bold.ttf')],
  ['Poppins', 800, F('Poppins', 'Poppins-ExtraBold.ttf')], ['Poppins', 900, F('Poppins', 'Poppins-Black.ttf')],
  ['Inter', 400, F('Inter', 'static', 'Inter_18pt-Regular.ttf')], ['Inter', 500, F('Inter', 'static', 'Inter_18pt-Medium.ttf')],
  ['Bebas Neue', 400, F('Bebas_Neue', 'BebasNeue-Regular.ttf')],
].map(([f, w, u]) => `@font-face{font-family:'${f}';font-weight:${w};src:url('${u}');}`).join('\n')
  // itálicos da Poppins (font-style: italic), para variar o peso e o tom quando fizer sentido
  + [[300, 'LightItalic'], [400, 'Italic'], [600, 'SemiBoldItalic'], [700, 'BoldItalic'], [800, 'ExtraBoldItalic']]
    .map(([w, n]) => `@font-face{font-family:'Poppins';font-style:italic;font-weight:${w};src:url('${F('Poppins', `Poppins-${n}.ttf`)}');}`).join('\n');
const CSS = readFileSync(path.join(AQUI, 'telessaude.css'), 'utf8').replaceAll('{{FONTES}}', FONTES);
const LIB = readFileSync(path.join(AQUI, 'ts-anim.js'), 'utf8');

const [pagina, saida, a0, a1, afps] = process.argv.slice(2);
const fps = Number(afps || 30);
const PREVIA = !!process.env.PREVIA;
// TELA=1920x1080 para o horizontal (padrão 1080x1920); a página deve ajustar html/body ao mesmo tamanho.
const TELA = (process.env.TELA || '1080x1920').split('x').map(Number);
const MAX = process.env.QUALIDADE === 'max' && !PREVIA;

// Técnica 4: cópia all-intra de cada clipe (todo quadro é quadro-chave), para buscas exatas sem decodificar o GOP.
const CACHE = path.join(AQUI, '_cache_busca');
const executa = (args) => new Promise((r, j) => spawn('ffmpeg', args, { stdio: ['ignore', 'inherit', 'inherit'] })
  .on('close', (c) => (c === 0 ? r() : j(new Error('ffmpeg falhou: ' + args.join(' '))))));
async function copiasDeBusca(html) {
  if (process.env.BUSCA === '0') return {};
  const base = path.dirname(path.resolve(html));
  const srcs = [...new Set([...readFileSync(html, 'utf8').matchAll(/<video[^>]*\ssrc="([^"]+)"/g)].map((m) => m[1]))];
  mkdirSync(CACHE, { recursive: true });
  const mapa = {};
  for (const src of srcs) {
    const orig = path.resolve(base, decodeURI(src));
    if (!existsSync(orig)) continue;
    const st = statSync(orig);
    const id = createHash('sha1').update(`${orig}|${st.size}|${st.mtimeMs}`).digest('hex').slice(0, 16);
    const prox = path.join(CACHE, `${id}.mp4`);
    if (!existsSync(prox)) {
      process.stdout.write(`cópia de busca: ${path.basename(orig)}
`);
      const tmp = prox.replace(/\.mp4$/, '.tmp.mp4');
      await executa(['-v', 'error', '-y', '-i', orig, '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '12',
        '-g', '1', '-keyint_min', '1', '-sc_threshold', '0', '-bf', '0', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', tmp]);
      renameSync(tmp, prox);
    }
    mapa[src] = pathToFileURL(prox).href;
  }
  return mapa;
}
const COPIAS = await copiasDeBusca(pagina);

// Abre um Chrome com a página pronta (fontes conferidas, vídeos carregados).
async function abrir() {
  const browser = await chromium.launch({ channel: 'chrome', args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: TELA[0], height: TELA[1] }, deviceScaleFactor: PREVIA ? 0.5 : 1 });
  page.on('pageerror', (e) => console.error('erro na página:', e.message));
  await page.addInitScript(LIB);
  await page.goto(pathToFileURL(path.resolve(pagina)).href);
  await page.addStyleTag({ content: CSS });
  // troca os clipes pelas cópias de busca rápida (mesmos tempos e quadros)
  await page.evaluate((m) => { for (const vd of document.querySelectorAll('video')) {
    const s = vd.getAttribute('src'); if (m[s]) { vd.src = m[s]; vd.load(); } } }, COPIAS);
  await page.evaluate(() => TS.pronto());
  const falhas = await page.evaluate(async () => {
    const r = []; for (const f of document.fonts) { try { await f.load(); } catch (e) {} if (f.status !== 'loaded') r.push(`${f.family} ${f.weight}`); }
    return r;
  });
  if (falhas.length) throw new Error('Fontes não carregaram: ' + falhas.join(', '));
  return { browser, page };
}

const prim = await abrir();
const dur = await prim.page.evaluate(() => window.DURACAO);

if (process.env.FOTOS) {
  mkdirSync(saida, { recursive: true });
  for (const s of process.env.FOTOS.split(',')) {
    await prim.page.evaluate((t) => window.render(t), Number(s));
    await prim.page.screenshot({ path: path.join(saida, `t${Number(s).toFixed(2).padStart(6, '0')}.png`) });
  }
  await prim.browser.close();
  console.log('fotos ok');
  process.exit(0);
}

const t0 = Number(a0 || 0), t1 = Number(a1 || dur);
const n = Math.round((t1 - t0) * fps);
// Workers: forçado por WORKERS ou medido na máquina (nunca mais que a CPU e a RAM livre aguentam).
const threads = os.cpus().length, livreGB = os.freemem() / 2 ** 30;
const auto = Math.max(1, Math.min(4, Math.floor(threads / 4), Math.floor(livreGB / 1.2)));
const W = Math.max(1, Math.min(Number(process.env.WORKERS || auto), Math.floor(n / 150) || 1));
console.log(`máquina: ${threads} threads, ${livreGB.toFixed(1)} GB livres → ${W} worker(s)${Object.keys(COPIAS).length ? `, ${Object.keys(COPIAS).length} clipe(s) com cópia de busca` : ''}`);
const feitos = new Array(W).fill(0);
const ini = Date.now();

// Renderiza os quadros [q0, q1) do trecho num arquivo próprio.
async function parte(k, sess, q0, q1, arq) {
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-',
    '-c:v', 'libx264', '-preset', PREVIA ? 'veryfast' : MAX ? 'slow' : 'medium', '-crf', PREVIA ? '23' : MAX ? '12' : '17', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
    '-r', String(fps), arq], { stdio: ['pipe', 'inherit', 'inherit'] });
  const escreve = (buf) => new Promise((r) => (ff.stdin.write(buf) ? r() : ff.stdin.once('drain', r)));
  for (let i = q0; i < q1; i++) {
    await sess.page.evaluate((t) => window.render(t), t0 + i / fps);
    await escreve(await sess.page.screenshot(MAX ? { type: 'png' } : { type: 'jpeg', quality: PREVIA ? 88 : 95 }));
    feitos[k]++;
    if (k === 0 && feitos[0] % 30 === 0) {
      const tot = feitos.reduce((a, b) => a + b, 0);
      process.stdout.write(`\r${tot}/${n} quadros  ${((Date.now() - ini) / 1000).toFixed(0)} s  (${W} em paralelo)`);
    }
  }
  ff.stdin.end();
  await new Promise((r) => ff.on('close', r));
  await sess.browser.close();
}

const limites = Array.from({ length: W + 1 }, (_, k) => Math.round((n * k) / W));
const sessoes = [prim, ...(await Promise.all(Array.from({ length: W - 1 }, () => abrir())))];
const arqs = W === 1 ? [saida] : sessoes.map((_, k) => saida.replace(/\.mp4$/i, `._parte${k}.mp4`));
await Promise.all(sessoes.map((s, k) => parte(k, s, limites[k], limites[k + 1], arqs[k])));

if (W > 1) {
  // junta as partes sem recodificar (mesmos parâmetros de codificação em todas)
  const lista = saida.replace(/\.mp4$/i, '._lista.txt');
  writeFileSync(lista, arqs.map((a) => `file '${path.resolve(a).replace(/\\/g, '/').replace(/'/g, "'\\''")}'`).join('\n'), 'utf8');
  await new Promise((r, j) => spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lista, '-c', 'copy', '-movflags', '+faststart', saida],
    { stdio: 'inherit' }).on('close', (c) => (c === 0 ? r() : j(new Error('concat falhou')))));
  for (const a of [...arqs, lista]) { try { unlinkSync(a); } catch (e) {} }
}
console.log(`\nok ${saida}  ${n} quadros em ${((Date.now() - ini) / 1000).toFixed(0)} s  (${W} em paralelo${PREVIA ? ', prévia 540×960' : MAX ? ', qualidade máxima' : ''})`);

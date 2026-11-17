// Camada de edição injetada por editor.mjs na página da animação. Não altera a página: os ajustes são
// aplicados como um transform extra depois de cada render(t) e salvos em ajustes.json.
// Cada elemento ajustado tem QUADROS-CHAVE (tempo → posição, tamanho, ocultar). Entre dois quadros-chave o ajuste
// é interpolado (suave) ou troca de uma vez (corte); antes do primeiro e depois do último vale o mais próximo.
(() => {
  const C = window.__ED_CFG, s = C.esc, W = C.tela[0], H = C.tela[1];
  const renderOrig = window.render;
  const ajustes = new Map();          // elemento -> { el, id, texto, n, nota, transicao, qc: [{ t, dx, dy, k, ocultar }] }
  const anot = [];                    // { tipo, t, x1, y1, x2, y2, texto, n }
  let t = C.tempos[0] ?? 0, tR = t, modo = 'mover', sel = null, mascara = C.vertical, foto = false, temp = null;
  const DUR = window.DURACAO || 60;
  const AREA = C.vertical ? { x: 65, y: 288, w: 888 - 65, h: 1248 - 288 } : null;
  const PERTO = 0.02;                 // mesmo quadro-chave se a diferença de tempo for menor que isto

  document.body.style.transformOrigin = '0 0';
  document.body.style.transform = `scale(${s})`;

  // ---------- quadros-chave ----------
  const NEUTRO = { dx: 0, dy: 0, k: 1, ocultar: false };
  const suave = (u) => (u < 0.5 ? 4 * u * u * u : 1 - (-2 * u + 2) ** 3 / 2);
  function valor(a, tt) {
    const q = a.qc;
    if (!q.length) return NEUTRO;
    if (tt <= q[0].t) return q[0];
    if (tt >= q[q.length - 1].t) return q[q.length - 1];
    let i = 0; while (q[i + 1].t <= tt) i++;
    const A = q[i], B = q[i + 1];
    if (a.transicao === 'corte') return A;
    const e = suave((tt - A.t) / (B.t - A.t)), L = (x, y) => x + (y - x) * e;
    return { dx: L(A.dx, B.dx), dy: L(A.dy, B.dy), k: L(A.k, B.k), ocultar: A.ocultar };
  }
  const neutro = (v) => Math.abs(v.dx) < 0.5 && Math.abs(v.dy) < 0.5 && Math.abs(v.k - 1) < 0.002 && !v.ocultar;
  const chaveAqui = (a) => a.qc.find((q) => Math.abs(q.t - t) < PERTO);
  // quadro-chave do momento atual; se não houver, cria um a partir do valor que já se vê neste momento
  function chave(a) {
    let q = chaveAqui(a);
    if (!q) { const v = valor(a, t); q = { t, dx: v.dx, dy: v.dy, k: v.k, ocultar: v.ocultar }; a.qc.push(q); a.qc.sort((x, y) => x.t - y.t); }
    return q;
  }

  // ---------- aplicar ajustes ----------
  function base(el) {
    let cur = el.style.transform || '';
    if (el.__edAp && cur.startsWith(el.__edAp)) cur = cur.slice(el.__edAp.length).trim();
    el.__edAp = null;
    if (cur === '') {
      if (el.__edCss === undefined) { const c = getComputedStyle(el).transform; el.__edCss = c === 'none' ? '' : c; }
      el.style.transform = '';
      return el.__edCss;
    }
    el.style.transform = cur;
    return cur;
  }
  function aplicarUm(el, sim = true) {
    const a = ajustes.get(el); const b = base(el);
    el.style.visibility = '';
    if (!a || !sim) return;
    const v = valor(a, tR);
    // o navegador normaliza o texto do transform (100.0px → 100px): guarda o prefixo como ele ficou
    el.style.transform = `translate(${v.dx.toFixed(1)}px, ${v.dy.toFixed(1)}px) scale(${v.k.toFixed(4)})`;
    const pre = el.style.transform;
    el.style.transform = (pre + ' ' + b).trim(); el.__edAp = pre;
    if (v.ocultar) el.style.visibility = 'hidden';
  }
  async function renderizar(tt, sim = true) {
    for (const el of ajustes.keys()) aplicarUm(el, false);
    tR = tt;
    await renderOrig(tt);
    for (const el of ajustes.keys()) aplicarUm(el, sim);
    if (!foto) desenhar();
  }
  window.__ed = {
    get t() { return t; },
    renderizar,
    modoFoto(on) {
      foto = on; ov.style.display = pn.style.display = on ? 'none' : '';
      document.body.style.transform = on ? 'none' : `scale(${s})`;
      if (!on) desenhar();
    },
  };

  // ---------- interface ----------
  const css = document.createElement('style');
  css.textContent = `
  #ed-ov{position:fixed;left:0;top:0;width:${W * s}px;height:${H * s}px;z-index:2147483646;cursor:crosshair}
  #ed-ov svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
  #ed-pn{position:fixed;right:0;top:0;width:${C.painel}px;height:100vh;overflow:auto;z-index:2147483647;box-sizing:border-box;
    background:#F4F6FA;border-left:1px solid #D0D5DD;padding:12px 14px;font:13px/1.45 system-ui,Segoe UI,sans-serif;color:#101828}
  #ed-pn h1{font-size:15px;margin:0 0 2px} #ed-pn h2{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:#475467;margin:14px 0 6px}
  #ed-pn button{font:inherit;padding:4px 9px;border:1px solid #C9CED8;background:#fff;border-radius:6px;cursor:pointer;margin:0 4px 4px 0}
  #ed-pn button.on{background:#365DCC;color:#fff;border-color:#365DCC} #ed-pn button.pri{background:#1C306A;color:#fff;border-color:#1C306A;width:100%;padding:8px}
  #ed-pn input[type=number]{width:70px;font:inherit;padding:2px 4px} #ed-pn textarea{width:100%;box-sizing:border-box;font:inherit;min-height:46px}
  #ed-pn select{font:inherit}
  #ed-pn .lin{display:flex;align-items:center;gap:6px;margin-bottom:4px;flex-wrap:wrap}
  #ed-pn .item{padding:4px 6px;border-radius:5px;cursor:pointer} #ed-pn .item:hover{background:#E4E9F5}
  #ed-pn .qc{display:flex;align-items:center;gap:6px;padding:3px 6px;border-radius:5px;cursor:pointer} #ed-pn .qc:hover{background:#E4E9F5}
  #ed-pn .qc.aqui{background:#DCE5FA;font-weight:600} #ed-pn .qc .x{margin-left:auto;color:#B42318;padding:0 4px}
  #ed-pn .dica{color:#667085;font-size:12px} #ed-pn code{background:#E4E9F5;border-radius:3px;padding:0 3px}
  #ed-trilha{position:relative;height:16px;margin:2px 7px 6px;border-bottom:2px solid #D0D5DD}
  #ed-trilha i{position:absolute;top:2px;width:10px;height:10px;margin-left:-5px;background:#365DCC;transform:rotate(45deg);cursor:pointer}
  #ed-trilha b{position:absolute;top:0;bottom:-2px;width:2px;margin-left:-1px;background:#F04438}`;
  document.head.appendChild(css);

  const ov = document.createElement('div'); ov.id = 'ed-ov';
  ov.innerHTML = `<svg viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg"></svg>`;
  const svg = ov.firstChild;
  const pn = document.createElement('div'); pn.id = 'ed-pn';
  document.documentElement.append(ov, pn);

  pn.innerHTML = `
  <h1>Editor de quadros</h1><div class="dica">${C.nome}</div>
  <h2>Tempo</h2>
  <div class="lin"><button data-q="-1">◀ quadro</button><input id="ed-t" type="number" step="0.01" min="0" max="${DUR}"> s<button data-q="1">quadro ▶</button></div>
  <input id="ed-r" type="range" min="0" max="${DUR}" step="0.0333" style="width:100%">
  <div id="ed-trilha" title="Quadros-chave do elemento selecionado"></div>
  <div id="ed-pre" class="lin"></div>
  <h2>Ferramenta</h2>
  <div class="lin" id="ed-modos"><button data-m="mover">Mover (V)</button><button data-m="seta">Seta (A)</button><button data-m="circulo">Círculo (C)</button><button data-m="nota">Nota (N)</button></div>
  <label class="lin"><input type="checkbox" id="ed-mask"> mostrar área segura (M)</label>
  <h2>Elemento selecionado</h2><div id="ed-sel" class="dica"></div>
  <h2>Ajustes e anotações</h2><div id="ed-lista" class="dica">Nenhum ainda.</div>
  <h2>Observação geral</h2><textarea id="ed-obs" placeholder="O que mais mudar nesta cena (ritmo, cor, texto...)"></textarea>
  <h2></h2><button class="pri" id="ed-salvar">Salvar ajustes</button><div id="ed-status" class="dica"></div>
  <h2>Como funciona</h2><div class="dica">Cada mudança vale a partir do momento em que foi feita: é um <b>quadro-chave</b>. Com um só, o ajuste vale para o vídeo todo. Para o elemento mudar ao longo do tempo (ex.: grande indo, pequeno voltando), vá até o outro momento e ajuste de novo: o editor cria outro quadro-chave e anima entre os dois (ou troca de uma vez, se a transição for "corte").</div>
  <h2>Atalhos</h2><div class="dica">Setas: mover 1 px (Shift: 10) · <code>+</code>/<code>−</code>: tamanho · <code>H</code>: ocultar · <code>0</code>: sem ajuste neste momento · <code>Del</code>: apaga o quadro-chave deste momento (sem seleção: a última anotação) · <code>[</code> <code>]</code>: quadro-chave anterior/seguinte · <code>,</code> <code>.</code>: um quadro · <code>Esc</code>: soltar · Alt+clique: peça de fora / de dentro</div>`;
  const $ = (q) => pn.querySelector(q);
  const fT = $('#ed-t'), fR = $('#ed-r');
  for (const v of C.tempos) { const b = document.createElement('button'); b.textContent = v.toFixed(2) + ' s'; b.onclick = () => irPara(v); $('#ed-pre').append(b); }
  pn.querySelectorAll('[data-q]').forEach((b) => (b.onclick = () => irPara(t + Number(b.dataset.q) / 30)));
  pn.querySelectorAll('[data-m]').forEach((b) => (b.onclick = () => setModo(b.dataset.m)));
  fT.onchange = () => irPara(Number(fT.value)); fR.oninput = () => irPara(Number(fR.value));
  $('#ed-mask').checked = mascara; $('#ed-mask').onchange = (e) => { mascara = e.target.checked; desenhar(); };
  $('#ed-salvar').onclick = salvar;

  function setModo(m) { modo = m; pn.querySelectorAll('[data-m]').forEach((b) => b.classList.toggle('on', b.dataset.m === m)); }
  setModo('mover');
  let fila = Promise.resolve();
  function irPara(v) {
    t = Math.max(0, Math.min(DUR, Math.round(v * 100) / 100)); fT.value = t.toFixed(2); fR.value = t;
    fila = fila.then(() => renderizar(t, true));
  }

  // ---------- desenho da camada ----------
  const ret = (el) => { const r = el.getBoundingClientRect(); return { x: r.left / s, y: r.top / s, w: r.width / s, h: r.height / s }; };
  const naHora = (a) => Math.abs(a.t - t) < PERTO;
  // nome estável do elemento: #id ou caminho a partir do id mais próximo (ex.: #cB > div:nth-child(3) > img:nth-child(1))
  function rotulo(el) {
    if (el.id) return '#' + el.id;
    const partes = []; let e = el;
    while (e && e !== document.body && !e.id) {
      partes.unshift(`${e.tagName.toLowerCase()}:nth-child(${[...e.parentElement.children].indexOf(e) + 1})`); e = e.parentElement;
    }
    return (e && e.id ? '#' + e.id : 'body') + ' > ' + partes.join(' > ');
  }
  const trecho = (el) => (el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40);
  function desenhar() {
    let h = '';
    if (mascara && AREA) {
      h += `<path fill="rgba(16,24,40,.28)" fill-rule="evenodd" d="M0 0H${W}V${H}H0Z M${AREA.x} ${AREA.y}h${AREA.w}v${AREA.h}h-${AREA.w}Z"/>`
        + `<rect x="${AREA.x}" y="${AREA.y}" width="${AREA.w}" height="${AREA.h}" fill="none" stroke="#FFD43B" stroke-width="3" stroke-dasharray="14 10"/>`;
    }
    for (const [el, a] of ajustes) {
      if (!el.isConnected || !a.qc.length) continue; const r = ret(el); if (!r.w) continue;
      const fixo = !!chaveAqui(a);   // contínuo = há quadro-chave neste momento; tracejado = valor interpolado
      h += `<rect x="${r.x}" y="${r.y}" width="${r.w}" height="${r.h}" fill="none" stroke="#12B76A" stroke-width="3" ${fixo ? '' : 'stroke-dasharray="10 8"'}/>`
        + `<text x="${r.x + 6}" y="${r.y - 8}" fill="#12B76A" font-size="30" font-weight="700" font-family="system-ui">${a.n}${fixo ? ' ◆' : ''}</text>`;
    }
    if (sel && sel.isConnected) {
      const r = ret(sel);
      h += `<rect x="${r.x}" y="${r.y}" width="${r.w}" height="${r.h}" fill="none" stroke="#365DCC" stroke-width="4"/>`
        + `<rect data-h="1" x="${r.x + r.w - 18}" y="${r.y + r.h - 18}" width="36" height="36" fill="#365DCC" stroke="#fff" stroke-width="3" style="cursor:nwse-resize"/>`;
    }
    for (const a of [...anot.filter(naHora), ...(temp ? [temp] : [])]) h += desenhoAnot(a);
    svg.innerHTML = h;
    painelSel(); lista(); trilha();
  }
  function desenhoAnot(a) {
    const cor = '#F04438';
    const rot = a.n ? `<circle cx="${a.x1}" cy="${a.y1}" r="24" fill="${cor}"/><text x="${a.x1}" y="${a.y1 + 10}" text-anchor="middle" fill="#fff" font-size="28" font-weight="700" font-family="system-ui">${a.n}</text>` : '';
    if (a.tipo === 'seta') {
      const ang = Math.atan2(a.y2 - a.y1, a.x2 - a.x1), L = 34;
      const p1 = [a.x2 - L * Math.cos(ang - 0.45), a.y2 - L * Math.sin(ang - 0.45)], p2 = [a.x2 - L * Math.cos(ang + 0.45), a.y2 - L * Math.sin(ang + 0.45)];
      return `<line x1="${a.x1}" y1="${a.y1}" x2="${a.x2}" y2="${a.y2}" stroke="${cor}" stroke-width="8" stroke-linecap="round"/>`
        + `<polygon points="${a.x2},${a.y2} ${p1} ${p2}" fill="${cor}"/>` + rot;
    }
    if (a.tipo === 'circulo') {
      const cx = (a.x1 + a.x2) / 2, cy = (a.y1 + a.y2) / 2;
      return `<ellipse cx="${cx}" cy="${cy}" rx="${Math.abs(a.x2 - a.x1) / 2}" ry="${Math.abs(a.y2 - a.y1) / 2}" fill="none" stroke="${cor}" stroke-width="8"/>` + rot;
    }
    return rot;
  }
  function trilha() {
    const a = sel && ajustes.get(sel);
    $('#ed-trilha').innerHTML = `<b style="left:${(t / DUR) * 100}%"></b>` + (a ? a.qc.map((q, i) => `<i data-i="${i}" style="left:${(q.t / DUR) * 100}%" title="${q.t.toFixed(2)} s"></i>`).join('') : '');
    $('#ed-trilha').querySelectorAll('i').forEach((d) => (d.onclick = () => irPara(a.qc[Number(d.dataset.i)].t)));
  }
  const esc = (x) => String(x ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const resumoV = (v) => [v.dx || v.dy ? `mover ${v.dx.toFixed(0)}, ${v.dy.toFixed(0)}` : '', Math.abs(v.k - 1) > 0.002 ? `${(v.k * 100).toFixed(0)}%` : '', v.ocultar ? 'oculto' : ''].filter(Boolean).join(', ') || 'sem ajuste';
  function painelSel() {
    const box = $('#ed-sel');
    if (!sel) { box.innerHTML = 'Clique num elemento. Alt+clique alterna entre a peça inteira e as partes dela.'; box.dataset.chave = ''; return; }
    const a = ajustes.get(sel), q = a && chaveAqui(a), v = a ? valor(a, t) : NEUTRO;
    const assinatura = [rotulo(sel), t, a ? a.qc.length : 0, a ? a.transicao : ''].join('|');
    if (box.dataset.chave === assinatura && box.contains(document.activeElement)) return;
    box.dataset.chave = assinatura;
    box.innerHTML = `<div><b>${esc(rotulo(sel))}</b>${trecho(sel) ? `<div class="dica">“${esc(trecho(sel))}”</div>` : ''}</div>
      <div class="dica" style="margin:4px 0">${q ? `Quadro-chave em <b>${q.t.toFixed(2)} s</b>.` : a ? 'Sem quadro-chave neste momento (valor interpolado). Ajustar aqui cria um.' : 'Arraste para mover; puxe o quadrado do canto para mudar o tamanho.'}</div>
      <div class="lin">x <input type="number" step="1" data-f="dx" value="${v.dx.toFixed(0)}"> y <input type="number" step="1" data-f="dy" value="${v.dy.toFixed(0)}"></div>
      <div class="lin">tamanho <input type="number" step="1" data-f="k" value="${(v.k * 100).toFixed(0)}"> %
        <label><input type="checkbox" data-f="ocultar" ${v.ocultar ? 'checked' : ''}> ocultar</label></div>
      <div class="lin"><button data-acao="neutro" title="Cria um quadro-chave sem ajuste neste momento (atalho 0)">Sem ajuste neste momento</button></div>
      ${a ? `<div class="lin">entre quadros-chave: <select data-f="transicao"><option value="suave" ${a.transicao === 'suave' ? 'selected' : ''}>suave (anima)</option><option value="corte" ${a.transicao === 'corte' ? 'selected' : ''}>corte (troca de uma vez)</option></select></div>
      <div>${a.qc.map((x, i) => `<div class="qc ${Math.abs(x.t - t) < PERTO ? 'aqui' : ''}" data-i="${i}">◆ ${x.t.toFixed(2)} s · ${resumoV(x)}<span class="x" data-del="${i}" title="Apagar este quadro-chave">✕</span></div>`).join('')}</div>
      <textarea data-f="nota" placeholder="Nota sobre este elemento">${esc(a.nota)}</textarea>
      <button data-acao="desfazer">Desfazer tudo deste elemento</button>` : ''}`;
    box.querySelectorAll('[data-f]').forEach((f) => (f.oninput = f.onchange = () => {
      const k = f.dataset.f, a2 = ajuste(sel);
      if (k === 'nota') a2.nota = f.value;
      else if (k === 'transicao') a2.transicao = f.value;
      else { const q2 = chave(a2); q2[k] = k === 'ocultar' ? f.checked : k === 'k' ? Number(f.value) / 100 : Number(f.value); }
      aplicarUm(sel); desenhar();
    }));
    box.querySelectorAll('.qc').forEach((d) => (d.onclick = (e) => {
      const i = Number(d.dataset.i);
      if (e.target.dataset.del !== undefined) { apagarChave(sel, i); return; }
      irPara(ajustes.get(sel).qc[i].t);
    }));
    box.querySelectorAll('[data-acao]').forEach((b) => (b.onclick = () => (b.dataset.acao === 'neutro' ? semAjusteAqui(sel) : desfazer(sel))));
  }
  function lista() {
    const itens = [...ajustes.values()].filter((a) => a.qc.length).map((a) => ({ n: a.n, t: a.qc[0].t, el: a.el,
      txt: `${esc(a.id)}: ${a.qc.map((q) => `${q.t.toFixed(2)} s ${resumoV(q)}`).join(' → ')}${a.qc.length > 1 ? ` (${a.transicao})` : ''}${a.nota ? ' — ' + esc(a.nota) : ''}` }))
      .concat(anot.map((a) => ({ n: a.n, t: a.t, txt: `${a.t.toFixed(2)} s · ${a.tipo}${a.texto ? ': ' + esc(a.texto) : ''}` })))
      .sort((x, y) => x.n - y.n);
    $('#ed-lista').innerHTML = itens.length ? itens.map((i) => `<div class="item" data-n="${i.n}"><b>${i.n}.</b> ${i.txt}</div>`).join('') : 'Nenhum ainda.';
    $('#ed-lista').querySelectorAll('[data-n]').forEach((d) => (d.onclick = () => {
      const i = itens.find((x) => x.n === Number(d.dataset.n)); if (i.el) sel = i.el; irPara(i.t);
    }));
  }
  let contador = 0;
  function ajuste(el) {
    let a = ajustes.get(el);
    if (!a) { a = { el, id: rotulo(el), texto: trecho(el), n: ++contador, nota: '', transicao: 'suave', qc: [] }; ajustes.set(el, a); }
    return a;
  }
  function desfazer(el) { if (!ajustes.has(el)) return; aplicarUm(el, false); ajustes.delete(el); el.style.visibility = ''; desenhar(); }
  function apagarChave(el, i) {
    const a = ajustes.get(el); if (!a) return;
    a.qc.splice(i, 1);
    if (!a.qc.length && !a.nota) desfazer(el); else { aplicarUm(el); desenhar(); }
  }
  function semAjusteAqui(el) { const q = chave(ajuste(el)); Object.assign(q, { dx: 0, dy: 0, k: 1, ocultar: false }); aplicarUm(el); desenhar(); }

  // ---------- seleção e arraste ----------
  // invisível = transparente ou escondido nele ou num pai (mas um elemento que o usuário ocultou continua selecionável)
  function visivel(el) {
    for (let e = el; e && e !== document.body; e = e.parentElement) {
      if (ajustes.has(e) && valor(ajustes.get(e), t).ocultar) return true;
      const cs = getComputedStyle(e);
      if (cs.visibility === 'hidden' || Number(cs.opacity) < 0.05) return false;
    }
    return true;
  }
  // peça selecionável: tem id, ou é imagem/vídeo/svg, ou é posicionada (as peças animadas das páginas)
  function selecionavel(e) {
    if (e.id) return true;
    if (/^(img|video|svg|canvas)$/i.test(e.tagName)) return true;
    const p = getComputedStyle(e).position; return p === 'absolute' || p === 'fixed';
  }
  const grande = (el) => { const r = ret(el); return r.w * r.h > 0.6 * W * H; };
  function candidatos(x, y) {
    ov.style.pointerEvents = 'none';
    const pilha = document.elementsFromPoint(x, y);
    ov.style.pointerEvents = '';
    const cadeia = (hit) => {   // do mais interno para o mais externo
      const c = [];
      for (let p = hit; p && p !== document.body && p !== document.documentElement; p = p.parentElement) {
        if (p instanceof SVGElement && p.ownerSVGElement) continue;   // partes de dentro de um svg: vale o svg inteiro
        if (selecionavel(p)) c.push(p);
      }
      return c;
    };
    const hits = pilha.filter((h) => !pn.contains(h) && !ov.contains(h) && visivel(h));
    if (!hits.length) return [];
    const prim = cadeia(hits[0]), pequenos = prim.filter((e) => !grande(e));
    // padrão: a peça inteira = o primeiro com id que não é a cena; sem id, o bloco mais externo que não é a cena
    const padrao = pequenos.find((e) => e.id) || pequenos[pequenos.length - 1] || prim[0];
    const ordem = [padrao, ...pequenos.filter((e) => e !== padrao)];
    for (const h of hits.slice(1)) for (const e of cadeia(h)) if (!grande(e) && !ordem.includes(e)) ordem.push(e);
    for (const e of prim) if (!ordem.includes(e)) ordem.push(e);   // cenas e câmeras por último (Alt+clique chega a elas)
    return ordem.filter(Boolean);
  }
  let arr = null;
  ov.addEventListener('mousedown', (e) => {
    e.preventDefault();
    const x = e.clientX, y = e.clientY, vx = x / s, vy = y / s;
    if (modo !== 'mover') {
      if (modo === 'nota') {
        const txt = prompt('Nota para este ponto:'); if (!txt) return;
        anot.push({ tipo: 'nota', t, x1: vx, y1: vy, x2: vx, y2: vy, texto: txt, n: ++contador }); desenhar(); return;
      }
      temp = { tipo: modo, t, x1: vx, y1: vy, x2: vx, y2: vy };
      arr = { anot: true }; return;
    }
    if (e.target.dataset && e.target.dataset.h && sel) {
      const a = ajuste(sel), q = chave(a);
      arr = { el: sel, res: true, x0: x, k0: q.k, w0: sel.getBoundingClientRect().width || 1, q }; return;
    }
    const cs = candidatos(x, y);
    if (!cs.length) { sel = null; desenhar(); return; }
    if (e.altKey && sel && cs.includes(sel)) sel = cs[(cs.indexOf(sel) + 1) % cs.length];
    else if (!(sel && cs.includes(sel))) {
      // clique em área vazia da cena: só solta a seleção (a cena inteira só se move com Alt+clique)
      if (grande(cs[0]) && !e.altKey) { sel = null; desenhar(); return; }
      sel = cs[0];
    }
    arr = { el: sel, x0: x, y0: y, pronto: false };   // o quadro-chave só é criado quando o mouse andar
    desenhar();
  });
  function comecarArraste() {
    const tinha = ajustes.has(arr.el), a = ajuste(arr.el), tinhaChave = !!chaveAqui(a), q = chave(a);
    // fator: quantos px de tela andam por 1 px do elemento (considera zoom de câmera dos pais)
    const r0 = arr.el.getBoundingClientRect(); q.dx += 100; aplicarUm(arr.el); const r1 = arr.el.getBoundingClientRect(); q.dx -= 100; aplicarUm(arr.el);
    Object.assign(arr, { pronto: true, q, dx0: q.dx, dy0: q.dy, f: Math.abs(r1.left - r0.left) / 100 || s, tinha, tinhaChave });
  }
  window.addEventListener('mousemove', (e) => {
    if (!arr) return;
    if (arr.anot) { temp.x2 = e.clientX / s; temp.y2 = e.clientY / s; desenhar(); return; }
    if (arr.res) { arr.q.k = Math.max(0.05, arr.k0 * (arr.w0 + (e.clientX - arr.x0)) / arr.w0); aplicarUm(arr.el); desenhar(); return; }
    if (!arr.pronto) { if (Math.abs(e.clientX - arr.x0) + Math.abs(e.clientY - arr.y0) < 3) return; comecarArraste(); }
    arr.q.dx = arr.dx0 + (e.clientX - arr.x0) / arr.f; arr.q.dy = arr.dy0 + (e.clientY - arr.y0) / arr.f;
    aplicarUm(arr.el); desenhar();
  });
  window.addEventListener('mouseup', () => {
    if (!arr) return;
    if (arr.anot) {
      const a = temp; temp = null; arr = null;
      if (Math.hypot(a.x2 - a.x1, a.y2 - a.y1) < 12) { desenhar(); return; }
      a.texto = prompt('Comentário (opcional):') || ''; a.n = ++contador; anot.push(a); desenhar(); return;
    }
    arr = null; desenhar();
  });
  function pularChave(dir) {
    const a = sel && ajustes.get(sel); if (!a || !a.qc.length) return;
    const q = dir > 0 ? a.qc.find((x) => x.t > t + PERTO) : [...a.qc].reverse().find((x) => x.t < t - PERTO);
    if (q) irPara(q.t);
  }
  window.addEventListener('keydown', (e) => {
    if (/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) return;
    const k = e.key, passo = e.shiftKey ? 10 : 1;
    const mapa = { v: 'mover', a: 'seta', c: 'circulo', n: 'nota' };
    if (mapa[k.toLowerCase()]) { setModo(mapa[k.toLowerCase()]); return; }
    if (k === 'm' || k === 'M') { mascara = !mascara; $('#ed-mask').checked = mascara; desenhar(); return; }
    if (k === ',') return irPara(t - 1 / 30);
    if (k === '.') return irPara(t + 1 / 30);
    if (k === '[') return pularChave(-1);
    if (k === ']') return pularChave(1);
    if (k === 'Escape') { sel = null; desenhar(); return; }
    if (k === 'Delete' || k === 'Backspace') {
      const a = sel && ajustes.get(sel), q = a && chaveAqui(a);
      if (q) apagarChave(sel, a.qc.indexOf(q));
      else if (!sel && anot.length) { anot.pop(); desenhar(); }
      return;
    }
    if (!sel) return;
    if (k === '0') { semAjusteAqui(sel); return; }
    const mexe = { ArrowLeft: (q) => (q.dx -= passo), ArrowRight: (q) => (q.dx += passo), ArrowUp: (q) => (q.dy -= passo), ArrowDown: (q) => (q.dy += passo),
      '+': (q) => (q.k *= 1.02), '=': (q) => (q.k *= 1.02), '-': (q) => (q.k /= 1.02), h: (q) => (q.ocultar = !q.ocultar), H: (q) => (q.ocultar = !q.ocultar) }[k];
    if (!mexe) return;
    e.preventDefault(); mexe(chave(ajuste(sel))); aplicarUm(sel); desenhar();
  });

  // ---------- salvar ----------
  async function salvar() {
    $('#ed-status').textContent = 'Salvando (tirando fotos em tamanho real)...';
    const tAtual = t, lst = [];
    const r = (b) => b && { x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.w), h: Math.round(b.h) };
    // fora: elementos sem nenhuma mudança (todos os quadros-chave neutros) e sem nota
    const uteis = [...ajustes.values()].filter((a) => a.qc.length && (a.nota || a.qc.some((q) => !neutro(q))));
    for (const a of uteis.sort((x, y) => x.n - y.n)) {
      const qcs = [];
      for (const q of a.qc) {
        await renderizar(q.t, false); const antes = a.el.isConnected ? ret(a.el) : null;
        await renderizar(q.t, true); const depois = a.el.isConnected ? ret(a.el) : null;
        qcs.push({ t: q.t, mover_local_px: { x: Math.round(q.dx), y: Math.round(q.dy) }, tamanho: +q.k.toFixed(3), ocultar: q.ocultar,
          caixa_antes: r(antes), caixa_depois: r(depois),
          deslocamento_na_tela_px: antes && depois ? { x: Math.round(depois.x + depois.w / 2 - antes.x - antes.w / 2), y: Math.round(depois.y + depois.h / 2 - antes.y - antes.h / 2) } : null,
          transform_extra: `translate(${q.dx.toFixed(1)}px, ${q.dy.toFixed(1)}px) scale(${q.k.toFixed(4)})` });
      }
      lst.push({ n: a.n, elemento: a.id, texto_do_elemento: a.texto, nota: a.nota, transicao: a.transicao, quadros_chave: qcs });
    }
    const ts = [...new Set([...lst.flatMap((a) => a.quadros_chave.map((q) => q.t)), ...anot.map((a) => a.t)].map((v) => +v.toFixed(2)))].sort((x, y) => x - y);
    if (!ts.length) ts.push(+tAtual.toFixed(2));
    const dados = {
      como_ler: 'Caixas em px do vídeo (x, y = canto superior esquerdo). Cada elemento tem quadros_chave: o ajuste de cada momento. '
        + 'Com um só, vale para o vídeo todo. Com vários, entre dois quadros-chave o ajuste anima (transicao "suave", easeInOutCubic) ou troca de uma vez ("corte"); '
        + 'antes do primeiro e depois do último vale o mais próximo. Um quadro-chave com tamanho 1 e mover 0 marca "sem ajuste neste momento". '
        + 'mover_local_px é no sistema do elemento (antes do zoom dos pais); deslocamento_na_tela_px é o que se vê. '
        + 'IMPORTANTE: os tempos são aproximados (o usuário marca um quadro qualquer em que o elemento aparece). Um quadro-chave = mudança global '
        + 'em toda a presença do elemento na cena. Vários = tamanhos/posições diferentes em fases diferentes da cena; faça a troca no ponto natural da animação. '
        + 'Regras completas em motion/tecnico.md, "Editor de quadros-chave".',
      observacao: $('#ed-obs').value,
      quadros: ts.map((v) => ({ t: v })),
      ajustes: lst,
      anotacoes: anot.map((a) => ({ n: a.n, tipo: a.tipo, t: a.t, de: { x: Math.round(a.x1), y: Math.round(a.y1) }, ate: { x: Math.round(a.x2), y: Math.round(a.y2) }, texto: a.texto })),
    };
    try {
      const pasta = await window.__edSalvar(dados);
      $('#ed-status').innerHTML = `Salvo em <code>${esc(pasta.split(/[\\/]/).slice(-3).join('/'))}</code>. Avise o Claude no chat.`;
    } catch (err) { $('#ed-status').textContent = 'Erro ao salvar: ' + err.message; }
    t = tAtual; await renderizar(t, true);
  }

  irPara(t);
})();

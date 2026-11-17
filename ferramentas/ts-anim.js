// Biblioteca de animação por tempo (determinística): a página expõe window.render(t) e o motor fotografa cada quadro.
// Tudo é função do tempo t (segundos), sem relógio real, para o render ser exato e repetível.
(function () {
  const clamp = (x, a, b) => Math.min(b, Math.max(a, x));
  const ease = {
    lin: (t) => t,
    out: (t) => 1 - Math.pow(1 - t, 3),
    in: (t) => t * t * t,
    inOut: (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
    back: (t) => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2); },
    expo: (t) => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t)),
    // mola (spring) no estilo das interfaces da Apple: chega rápido, passa ~6% do alvo e assenta suave
    mola: (t) => (t >= 1 ? 1 : 1 - Math.exp(-7 * t) * Math.cos(8 * t)),
    // mola mais "viva" (~15% de sobra) para elementos pequenos
    molaViva: (t) => (t >= 1 ? 1 : 1 - Math.exp(-6 * t) * Math.cos(10 * t)),
  };
  const p = (t, t0, d, e = 'out') => ease[e](clamp((t - t0) / d, 0, 1));
  const v = (t, t0, d, a, b, e = 'out') => a + (b - a) * p(t, t0, d, e);
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // Entrada padrão: sobe saindo do desfocado (type-rise). Saída opcional em t1.
  function entra(el, t, t0, o = {}) {
    const { d = 0.45, dy = 36, blur = 10, e = 'out', t1 = null, d1 = 0.3, escala = 1 } = o;
    let k = p(t, t0, d, e);
    if (t1 !== null) k *= 1 - p(t, t1, d1, 'in');
    el.style.opacity = k;
    const s = escala === 1 ? 1 : escala + (1 - escala) * k;
    el.style.transform = `translateY(${(1 - k) * dy}px) scale(${s})`;
    el.style.filter = blur ? `blur(${(1 - k) * blur}px)` : 'none';
  }
  // Pop com sobra (pop-in).
  function pop(el, t, t0, o = {}) {
    const { d = 0.42, t1 = null, d1 = 0.25 } = o;
    let k = p(t, t0, d, 'back');
    let a = clamp((t - t0) / 0.12, 0, 1);
    if (t1 !== null) { const s = p(t, t1, d1, 'in'); k *= 1 - s; a *= 1 - s; }
    el.style.opacity = a;
    el.style.transform = `scale(${Math.max(0, k)})`;
  }
  // Máquina de escrever: revela letra a letra (prepara spans uma vez).
  function digita(el, t, t0, cps = 26) {
    if (!el._chars) {
      const txt = el.textContent; el.textContent = '';
      el._chars = [...txt].map((c) => { const s = document.createElement('span'); s.textContent = c; el.appendChild(s); return s; });
    }
    const n = Math.floor(Math.max(0, t - t0) * cps);
    el._chars.forEach((s, i) => { s.style.visibility = i < n ? 'visible' : 'hidden'; });
  }
  // Marca-texto que desenha da esquerda para a direita (elemento com classe .marca/.marca-alerta).
  function marca(el, t, t0, d = 0.4) {
    el.style.backgroundSize = `${p(t, t0, d, 'inOut') * 100}% 100%`;
    el.style.backgroundRepeat = 'no-repeat';
  }
  // Traço SVG que se desenha (stroke-dashoffset).
  function traco(path, t, t0, d = 1, e = 'inOut') {
    const L = path._L || (path._L = path.getTotalLength());
    path.style.strokeDasharray = L;
    path.style.strokeDashoffset = L * (1 - p(t, t0, d, e));
  }
  // Câmera: transform com origem (ox, oy), zoom z e deslocamento (tx, ty).
  function camera(el, { z = 1, ox = 540, oy = 960, tx = 0, ty = 0, blur = 0 }) {
    el.style.transformOrigin = `${ox}px ${oy}px`;
    el.style.transform = `translate(${tx}px, ${ty}px) scale(${z})`;
    el.style.filter = blur ? `blur(${blur}px)` : 'none';
  }
  // Ponto da câmera: onde um ponto (x, y) da camada aparece na tela.
  const naTela = (x, y, c) => [(x - c.ox) * c.z + c.ox + (c.tx || 0), (y - c.oy) * c.z + c.oy + (c.ty || 0)];

  // Vídeos: espera metadados; seek exato por tempo do clipe.
  async function pronto() {
    await Promise.all($$('video').map((vd) => vd.readyState >= 2 ? 1 : new Promise((r) => vd.addEventListener('loadeddata', r, { once: true }))));
    await document.fonts.ready;
  }
  // Mira 2 ms depois do tempo pedido: quando o instante cai exatamente na fronteira entre dois quadros do clipe
  // (24 fps num vídeo de 30 fps, a cada 5 quadros), o decodificador sempre escolhe o mesmo quadro.
  async function busca(vd, tempo) {
    const alvo = clamp(tempo + 0.002, 0, (vd.duration || 10) - 0.05);
    if (Math.abs(vd.currentTime - alvo) < 0.001) return;
    await new Promise((r) => { vd.addEventListener('seeked', r, { once: true }); vd.currentTime = alvo; });
  }
  const mostra = (el, sim) => { el.style.display = sim ? '' : 'none'; };

  window.TS = { clamp, ease, p, v, $, $$, entra, pop, digita, marca, traco, camera, naTela, pronto, busca, mostra };
})();

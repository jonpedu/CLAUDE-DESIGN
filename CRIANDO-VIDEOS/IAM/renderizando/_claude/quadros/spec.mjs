// Quadros-chave do IAM (v1). Render: node ferramentas/quadros.mjs CRIANDO-VIDEOS/IAM/renderizando/_claude/quadros/spec.mjs
// Textos copiados do roteiro (roteiro-narrado.txt). Cores: azul padrão, vermelho #B42318 pontual.
const ALERTA = `<svg viewBox="0 0 64 64"><path d="M32 6 61 57H3Z" fill="#C99B00" stroke="#C99B00" stroke-width="6" stroke-linejoin="round"/><rect x="29" y="22" width="6" height="20" rx="3" fill="#fff"/><circle cx="32" cy="49" r="3.6" fill="#fff"/></svg>`;
const PONTO = `<svg class="ic" viewBox="0 0 50 50"><circle cx="25" cy="25" r="22" fill="#FEF3F2" stroke="#B42318" stroke-width="4"/><rect x="22.5" y="12" width="5" height="17" rx="2.5" fill="#B42318"/><circle cx="25" cy="36" r="3.2" fill="#B42318"/></svg>`;
const FONE = `<svg viewBox="0 0 64 64" width="96" height="96"><circle cx="32" cy="32" r="31" fill="#B42318"/><path d="M22 16c2-1 4 0 5 2l3 6c1 2 0 4-1 5l-3 2c2 5 6 9 11 11l2-3c1-1 3-2 5-1l6 3c2 1 3 3 2 5l-1 4c-1 2-3 3-5 3C31 52 12 33 13 18c0-2 1-4 3-5Z" fill="#fff"/></svg>`;

export default {
  pasta: '.',
  regua: '../../../elementos/Ajustada TELE e PETSAUDE Digital.png',
  quadros: [
    {
      nome: 'k1_gancho_0m07s', fundo: 'frames/k1_T07.png', clip: { x: 190, y: 579, s: 0.64 },
      html: `<div class="bloco" style="top:300px">
        <div class="titulo">Você sabia?</div>
        <div class="apoio" style="margin-top:18px;font-size:50px;white-space:nowrap">uma pessoa sofre <b class="azul">um infarto</b></div>
        <div class="forte" style="font-size:66px;margin-top:4px"><span class="marca-alerta vermelho">a cada poucos minutos</span></div>
        <div class="fonte-dado" style="margin-top:16px">Sociedade Brasileira de Cardiologia</div></div>`,
    },
    {
      nome: 'k2_titulo_0m17s', fundo: 'frames/k2_T06.png', clip: { x: 135, y: 480, s: 0.75 },
      html: `<div class="bloco" style="top:300px">
        <div class="leve">Hoje vamos falar sobre o</div>
        <div class="titulo" style="margin-top:8px">Infarto Agudo<br>do Miocárdio</div></div>`,
    },
    {
      nome: 'k3_dor_0m35s', fundo: 'frames/k3_T04.png', clip: { x: 20, y: 576, s: 0.70 },
      html: `<div class="bloco" style="top:300px">
        <div class="forte" style="font-size:68px">Dor ou aperto<br>no <span class="marca-alerta">peito</span></div>
        <div style="display:flex;flex-wrap:wrap;gap:16px;margin-top:26px">
          <span class="pilula">braço esquerdo</span><span class="pilula">pescoço</span>
          <span class="pilula">costas</span><span class="pilula">mandíbula</span></div></div>`,
    },
    {
      nome: 'k4_sinais_0m54s', fundo: 'frames/k4_T05.png', clip: { x: 131, y: 420, s: 0.78 },
      html: `<div class="bloco" style="top:300px">
        <div class="leve" style="font-size:48px;white-space:nowrap">o infarto pode se manifestar com</div>
        <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:22px">
          <span class="pilula" style="font-size:42px">dor entre as escápulas</span>
          <span class="pilula" style="font-size:42px">desconforto em pescoço, mandíbula, braço</span>
          <span class="pilula" style="font-size:42px">dispneia</span><span class="pilula" style="font-size:42px">confusão</span>
          <span class="pilula" style="font-size:42px">síncope</span><span class="pilula" style="font-size:42px">fadiga</span></div></div>`,
    },
    {
      nome: 'k5_fique_atento_1m05s', fundo: 'frames/k5_T01.png', clip: { x: 0, y: 860, s: 0.62 },
      html: `<div style="position:absolute;left:436px;top:1025px;width:200px;height:140px;background:#fff"></div>
        <div class="bloco" style="top:300px;width:808px">
        <div class="selo">${ALERTA}Fique atento a:</div>
        <ul class="lista" style="margin-top:24px;font-size:44px">
          <style>.lista li{font-size:44px;white-space:nowrap}</style>
          <li>${PONTO}suor frio</li><li>${PONTO}náusea ou vontade de vomitar</li><li>${PONTO}falta de ar</li>
          <li>${PONTO}tontura</li><li>${PONTO}cansaço extremo e repentino</li><li>${PONTO}dor na boca do estômago</li></ul></div>`,
    },
    {
      nome: 'k6_samu_1m18s', fundo: 'frames/k6_T02.png', clip: { x: 173, y: 515, s: 0.70 },
      html: `<div class="bloco" style="top:300px">
        <div class="leve">Ligue imediatamente para o</div>
        <div style="display:flex;align-items:center;gap:26px;margin-top:6px">
          ${FONE}<span class="titulo" style="font-size:104px;color:var(--ts-brand-strong)">SAMU</span>
          <span style="font-weight:900;font-size:150px;line-height:1;color:var(--ts-error)">192</span></div></div>`,
    },
  ],
};

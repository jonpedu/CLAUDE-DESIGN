# Cenas geradas por IA usadas como takes

Clipes gerados (Google AI Studio, Flow, Veo e similares) costumam ter cerca de 8–10 s e não chegam finalizados. **Cada clipe é um take, não uma cena pronta:** pode ser usado só um trecho, em qualquer ponto do clipe, e o mesmo trecho pode voltar mais de uma vez no vídeo. A narração é gravada à parte.

## 1. Decupagem (antes do mapa de motion)

Para cada clipe, gere uma folha de contato (um quadro a cada 0,5 s, com o tempo) e registre os trechos úteis no `takes.md` do vídeo:

| Take | Arquivo | Entrada | Saída | O que acontece | Tags | Boca | Defeitos |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T03a | 03_medica.mp4 | 1,2 s | 3,6 s | médica olha para a câmera e acena | aceno, sorriso, close-médio | fala | — |
| T03b | 03_medica.mp4 | 6,0 s | 8,4 s | médica assente, séria | assentir, preocupada | fechada | mão deforma após 8,5 s |

- **Tags:** ação (acena, aponta, assina, digita, sorri, assente, preocupada, pensa), enquadramento (close, médio, aberto) e direção do olhar ou do movimento.
- **Boca:** `fala` (mexendo como se falasse), `fechada` ou `não aparece`.
- **Defeitos:** mãos ou dedos deformados, olhos estranhos, rosto que muda, objetos que se fundem, texto ilegível, artefatos nas bordas. O trecho defeituoso fica fora, mesmo que o resto do clipe seja bom.
- Trechos úteis costumam ter de 1,5 a 4 s; o mínimo é cerca de 0,8 s.

Mostre a decupagem ao usuário antes de montar: é aí que ele aponta os trechos de que mais gosta.

## 2. Montagem com takes

- Use o trecho que serve à fala, não o clipe inteiro.
- **Reuso é permitido.** Para não parecer repetição:
  - não repita o mesmo trecho com menos de 10 s de intervalo;
  - ao repetir, mude algo: enquadramento (close × médio, diferença de pelo menos 20% na escala), parte diferente do mesmo clipe, velocidade entre 0,9× e 1,1×, ou um grafismo cobrindo parte do quadro;
  - espelhar só se não houver texto, logo ou detalhe assimétrico marcante no personagem.
- **Corte no movimento:** corte entre takes no meio de um gesto e respeite a direção do olhar e do movimento de um plano para o outro.
- Dois takes seguidos do mesmo personagem no mesmo enquadramento parecem um pulo (jump cut). Mude a escala ou ponha um grafismo entre eles.
- **Margem fantasma (regra do usuário, 15/11/2026):** quando o personagem ou um objeto encosta numa borda do clipe gerado (blazer cortado na lateral, corpo cortado embaixo), o clipe precisa ser **colado na mesma borda do vídeo final**. Se ficar afastado, aparece o fundo branco depois do corte e a borda "fantasma" denuncia o recorte. Antes de posicionar, rode `py ferramentas/bordas.py <clipe>`: ele diz quais bordas são tocadas e em que trechos. Regras: borda esquerda → `x = 0`; direita → `x = largura do vídeo − largura do clipe`; esquerda e direita → largura cheia (escala 1); topo → `y = 0`; **base → pode ficar abaixo da régua de marca**, que cobre a faixa inferior (folga maior). Movimento de câmera (pan, zoom de saída) não pode abrir a borda colada: com zoom ≥ 1 e origem dentro do quadro a borda continua fora; translação lateral só para o lado que mantém a borda fora.
- Trecho curto demais para a fala: prefira um `ken-burns` ou `push-in` lento a desacelerar o vídeo. Câmera lenta com interpolação de quadros (ffmpeg `minterpolate`) costuma criar artefatos: use no máximo 0,8× e confira.

## 3. Sincronia com a narração

A boca do personagem não acompanha a narração por padrão. **Sempre que possível, sincronize os movimentos.** Em ordem de prioridade:

1. **Gesto na palavra:** o ponto alto do gesto (aceno, apontar, assentir, expressão) cai na palavra-chave da frase, com margem de ±3 frames.
2. **Boca que fala, só sob fala:** um trecho com boca `fala` entra só sobre trecho narrado. A boca começa a mexer até 2 frames depois do início da fala e para antes da pausa. Nas pausas, use trechos com boca `fechada`.
3. **Sem trecho compatível:** use um plano em que a boca não aparece (aberto, de lado, de costas, mãos), uma reação com boca fechada ou um grafismo cobrindo o rosto. Evite close com a boca mexendo durante silêncio, ou parada durante uma fala longa (mais de 1,5 s).
4. **Narrador × personagem:** se quem fala é um narrador, e não o personagem, o personagem não deve parecer falar. Prefira reações com a boca fechada.

**Como medir (script reaproveitável):** detecte o rosto (YuNet) e os pontos da boca em cada quadro, calcule a abertura da boca ao longo do tempo e compare com a energia da voz da narração quadro a quadro. Isso diz quais trechos têm boca compatível e qual deslocamento casa melhor. Os tempos por palavra da transcrição (WhisperX) dizem onde caem as palavras-chave para os gestos.

## 4. Biblioteca de takes

Depois de cada vídeo, marque no `takes.md` os trechos que funcionaram. Quando um personagem se repete numa série, os melhores trechos dele formam uma biblioteca (pasta da série + `takes.md` geral) reaproveitável nos próximos vídeos.

# Formato: vertical 9:16

Reels, Shorts, Stories. Todos os 22 vídeos de referência estão neste formato. Aplique junto com `telessaude/SKILL.md` e o arquivo do tipo em `tipos/`.

## Tela

- 1080 × 1920, 30 fps (60 fps só se o projeto pedir, como na Retrospectiva).
- **Área segura:** retângulo **x 65–888, y 288–1248** (823 × 960). Decisão do usuário: **informação importante** (títulos, textos, números, alertas, chamada, rosto) fica dentro; **elementos secundários** (decoração, ícones de apoio, parte do personagem, fundo) podem encostar ou passar um pouco da margem. Máscara: função `mascara` em `analise-referencias/scripts/medir.py`; mostrar ao usuário os quadros-chave com a máscara, porque ele avalia pelo olho, não por pixel.
- Nas referências, títulos chegam a y ≈ 60–250. Descer o título para y ≥ 288 mantendo a composição.

## Margem fantasma

Clipe do Flow com personagem ou objeto encostado numa borda vai colado na mesma borda do vídeo (regra completa em `motion/takes.md`; detecção com `ferramentas/bordas.py`). A base tocada pode ficar sob a régua.

## Telas cheias (sem personagem)

Texto principal centralizado no **centro do quadro** (x = 540), não no centro da área segura: o olho percebe o deslocamento. Para caber na área segura com o centro em 540, o texto principal tem no máximo ~690 px de largura (quebre em linhas ou reduza o corpo). Tela cheia não pode ficar vazia: elementos ligados ao tema preenchem e se movem (ícone do tema pulsando, linha de ECG, formas de fundo em flutuação lenta); citação de fonte entra como texto com digitação, não em pílula.

## Composição observada (adaptar à área segura)

- **Pilha vertical:** título em cima, personagem embaixo ocupando a metade inferior, ícones e cartões ao lado do personagem.
- Personagem recortado entrando pela base, cortado na cintura ou nos joelhos; close no rosto para ênfase.
- Texto alinhado à esquerda ou centralizado, nunca justificado. Listas com marcadores à esquerda do personagem.
- Um bloco de conteúdo por tela; a tela troca de layout a cada 4–8 s.

## Tamanhos de texto (manual)

| Uso | Tamanho |
| --- | --- |
| Título do tema | 72–88 px |
| Texto de apoio | 48–56 px |
| Legenda | 46–52 px, base em no máximo y = 1240 |
| Créditos e referências | 30–34 px |

## Régua e fechamento

- Régua 9:16 (PNG de 1080 px de largura), centralizada, encostada na base, faixa branca de ~80–140 px. Fica nos 672 px de baixo, que as redes cobrem no feed: é assinatura, não informação.
- Fechamento com logo animado centralizado, levemente acima do centro (dentro da área segura).

## Capa

1080 × 1920 com o título do vídeo e a régua; título e rosto dentro do quadrado central 1080 × 1080 (o grid do perfil corta o resto).

**Toda entrega tem capa (pedido do usuário, 15/11/2026):** a aprovada do AVC é a v1: o gancho assentado (cérebro + "Você sabe o que é" + "AVC?" enorme). Capa tirada de um quadro no meio de uma animação ficou ruim (v2, apagada pelo usuário): escolha um instante em que tudo já assentou e confira a imagem antes de entregar; se uma capa já foi aprovada, mantenha-a.
- Salvar em `renderizando/` como `CAPA <TEMA> vN.png` (uma por versão final; sugestão, o usuário decide). Pode ser **um quadro do próprio vídeo** que diga o tema (com a régua já embaixo) ou **uma capa composta** com os mesmos elementos das cenas (título do tema, personagem, régua). Na dúvida, mostrar as duas opções em miniatura.
- **A capa é o primeiro quadro do vídeo final, um único quadro.** Motivo: o vídeo é enviado pelo WhatsApp (coordenador e equipe), e o WhatsApp usa o primeiro quadro como miniatura; se ele for uma tela azul ou branca, ninguém sabe do que se trata.
- No motor, isso é feito **substituindo o quadro 0** (em `render(t)`, mostrar a capa quando `t < 1/30`). Não se insere um quadro a mais, para não deslocar a sincronia com o áudio. O quadro 0 costuma estar vazio porque as entradas começam depois.
- Em vídeo já renderizado, a capa entra trocando só o primeiro quadro, sem render completo: sobrepor a capa no vídeo sem áudio com `overlay=0:0:enable='eq(n,0)'` (recomprimir com CRF igual ou menor que o original; não usar `emendar.py`, que recomprime em CRF 17; para trocar um trecho do vídeo, use `ferramentas/trocar_trecho.py`, que não recodifica o resto) e rodar a mixagem de novo. Conferir que o número de quadros não mudou. Feito assim no IAM v4/v5.

## Material gerado em outra proporção

Cena gerada em 16:9: recortar para 9:16 mantendo o rosto ou a ação no centro; se cortar algo importante, a cena entra reduzida sobre um fundo da identidade. Sempre que possível, gerar as cenas já em 9:16.

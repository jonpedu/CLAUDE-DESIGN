# TELEDIAGNÓSTICO: mapa de cenas (v1, 20/11/2026)

9:16, 1080×1920, 30 fps. Narração de 57,8 s, depois o fechamento `Intro Telessaude.mp4` (4,4 s), o que dá cerca de 62 s no total. Tempos em segundos, tirados de `transcricao/palavras.json`.

## Ideia geral

- **Fio condutor: a linha entre dois alfinetes.** Na cena 01 ela liga "aqui" e "lá". Na 02 ela se estica (a distância). Na 03 os dados sobem por ela e o laudo desce. Na 04 os alfinetes acendem no mapa do Maranhão. Na 05 ela vira "de lugar" (alfinete) e "de tempo" (relógio). Na 06 o laudo chega pela linha. Assim cada cena puxa a seguinte.
- **Unidade com o piloto (Teleorientação):** mesma régua, trilha e fechamento; mapa do Brasil como marca d'água em deriva lenta durante o vídeo todo; etiquetas retangulares brancas e azuis; Poppins.
- **Cor:** azul da marca como base (`#365DCC`, `#1C306A`). Como cor de destaque do tema uso o **verde-azulado `#19756F`**, só no laudo e no check, ou seja, no que resolve. Fundo vivo `misto` (azul + verde) bem diluído.
- **Curva:** mola em todas as entradas de etiqueta, ícone e cartão.
- **Texto na tela:** só as palavras-chave do roteiro, sem legenda completa.

## Cenas

| Tempo | Cena | O que acontece na tela | Efeitos | Texto exato | Saída |
| --- | --- | --- | --- | --- | --- |
| 0,0–4,8 | **01 Gancho** | Alfinete grande embaixo, à esquerda, com um aparelho de exame simples e a etiqueta "o exame aqui" (0,42). No "laudo" (2,86) cai um segundo alfinete no alto, à direita, com a etiqueta "quem dá o laudo, lá". Uma linha pontilhada fraca entre os dois mostra a distância. | `pop-in` (mola) com queda do alfinete, `type-rise` | o exame aqui · quem dá o laudo, lá | — |
| 4,8–8,1 | 01 | No "Como resolver?" (4,84), a linha se desenha cheia de um alfinete ao outro e um pulso de luz corre por ela. No "telediagnóstico" (6,72), o título entra grande no centro e os dois alfinetes encolhem e vão para os lados do título, ainda ligados. **Quadro da capa:** ~7,8 s. | `underline-draw` na linha, `type-punch` no título, escala dinâmica | Telediagnóstico | `continuidade` |
| 8,6–11,8 | **02 O que é** | O título sobe, encolhe e vira cabeçalho. Os alfinetes se afastam com mola e a linha **se estica**. Em "a distância" (9,66), a etiqueta entra montada na linha. Em "tecnologia" (11,18), ondas de sinal (tipo wi-fi) correm pela linha, sem texto. | `continuidade`, `pill-expand`, pulso na linha | a distância | `continuidade` (a linha gira para a vertical) |
| 12,6–15,1 | **03 Como funciona** | A linha fica vertical: o alfinete do exame vai para baixo e o de cima vira o lugar do profissional. Os ícones entram um por palavra, ao lado de etiquetas: gráfico (12,60), imagem (13,26), dados (13,86). Em "enviados" (14,4), os três sobem pela linha. | `stagger-in` dos ícones, deslizamento pela linha | gráficos · imagens · dados | — |
| 15,1–18,2 | 03 | Em "profissional" (15,12), o profissional de saúde (SVG animado) aparece no alto com escala de mola, e os ícones chegam até ele. Em "laudo" (17,16), um documento desce pela linha até a base, com o check verde e a etiqueta "laudo ou parecer". | `pop-in`, troca de pose com dissolução, `check-pop` | laudo ou parecer | `continuidade` (os ícones ficam) |
| 19,0–23,2 | **04 Exames do NTS** | O profissional e a linha saem pela lateral, e os três ícones da cena 03 descem para o centro, numa fileira. Em "Telessaúde Maranhão" (19,14), entra uma etiqueta azul sólida de cabeçalho, e "telediagnóstico" (21,56) aparece abaixo dela. | `continuidade`, `type-rise` | Telessaúde Maranhão · telediagnóstico | `metamorfose` |
| 23,2–26,4 | 04 | O ícone de imagem **vira** o olho/retina, grande no centro. Entra a etiqueta "telerretinografia" e, em "UFG" (25,34), o logo da UFG com a sigla ao lado. Os outros dois ícones somem. | `metamorfose`, `type-rise`, `pop-in` | telerretinografia · UFG | `continuidade` |
| 26,4–29,4 | 04 | O cartão da retina encolhe e sobe para a esquerda. O ícone de gráfico **vira** uma linha de ECG que se desenha grande, com a etiqueta "eletrocardiograma" e, em "UFMG" (28,56), o logo e a sigla da UFMG. | escala dinâmica, `linha-de-pulso`, `pop-in` | eletrocardiograma · UFMG | `continuidade` |
| 29,4–37,1 | 04 | Em "Ampliando essa oferta" (29,40), os dois cartões **se afastam** e abrem um espaço. Em "incorporação" (32,38), aparece nesse espaço um cartão de borda tracejada, ainda em construção. Em "tele-espirometria" (33,20), ele se preenche com o pulmão (respirando: escala lenta) e, em "UFMG" (35,80), recebe o logo e a sigla. | deslocamento com mola, borda que se desenha, `pop-in` | tele-espirometria · UFMG (sugestão: "em incorporação", ver pergunta 2) | `arrasto` para a esquerda |
| 37,1–45,9 | 04 | Os três cartões são arrastados para a esquerda, e o **mapa do Maranhão** (`BR-MA`, azul claro) entra grande pela direita. Os alfinetes da cena 01 caem e acendem pelo mapa (ilustrativos). As etiquetas entram uma a uma, primeiro grandes, depois encolhendo para abrir espaço, e o mapa diminui a cada etiqueta: "ampliar o acesso aos exames" (38,82), "qualificar o diagnóstico" (40,76), "fortalecer a Atenção Primária à Saúde" (42,38). | `arrasto`, `stagger-in` dos alfinetes, escala dinâmica, `palavra-destaque` em "Atenção Primária à Saúde" | as 3 frases | `metamorfose` |
| 46,6–50,7 | **05 Lugar ou tempo** | As etiquetas saem, e os alfinetes do mapa se juntam num só alfinete grande. Em "essa distância" (47,36), ele puxa a linha de novo até um segundo alfinete. Em "de lugar" (48,38), entra a etiqueta "de lugar" (bloco de cima). | `metamorfose`, `type-rise` | de lugar | `continuidade` |
| 50,7–53,6 | 05 | O bloco "de lugar" sobe um pouco, e embaixo entra um relógio com os ponteiros girando rápido e depois assentando. Em "tempo" (51,30), entra a etiqueta "de tempo". Os dois ficam empilhados e respirando. | escala dinâmica, `pop-in`, ponteiros girando | de tempo | `arrasto` para cima |
| 54,7–57,8 | **06 Fecho** | Em "Telediagnóstico" (54,68), o título entra grande pelo `type-punch`. Em "o laudo chega" (55,66–56,26), o documento com o check verde desliza pela linha e encaixa abaixo do título. Tudo assenta e fica parado nos últimos 0,6 s. | `type-punch`, `check-pop` | Telediagnóstico | `dissolve` para o logo |
| 57,8–62,2 | Fechamento | `Intro Telessaude.mp4` (vertical, com som), sem alteração. | — | — | fim |

A régua `regua - tele-sted-sus-govbr.svg` fica centralizada na base do primeiro ao último quadro (no fechamento, só se o arquivo não tiver a própria).

## Ritmo e tela ocupada

- Um elemento novo a cada ~1,5–2,5 s, e o layout muda a cada 3–8 s. O trecho mais longo sem troca de layout é o 29,4–37,1, em que o cartão tracejado e o pulmão entram no meio para manter a tela viva.
- Marca d'água do Brasil em deriva constante. Na faixa entre y 1248 e a régua ficam a base da linha e dos alfinetes, para não deixar vazio (WhatsApp). A informação fica centralizada em x ≈ 480–540, dentro da área segura.

## Som (proposta, decidido na prévia de áudio)

- Trilha base `joyful-marimba` (piloto), com `"db": -11` e ducking de 5 dB. Teste pedido: entrar `tecnologia/technology-background-atlasaudio-631954.mp3` entre 12,6 s e 45,9 s (dados viajando e exames) e voltar à marimba na cena 05.
- Efeitos com `sfx_db_extra −5`:
  - queda suave nos alfinetes;
  - swish nas etiquetas;
  - um tique por ícone na cena 03;
  - whoosh só nos `arrasto` (37,1 e 53,6);
  - um "bip" curto e baixo quando o ECG se desenha (opcional);
  - sem pop.

## Perguntas para aprovar

1. A linha entre os alfinetes como fio condutor e o verde-azulado como cor do laudo estão bons?
2. Na tele-espirometria, posso pôr a etiqueta "em incorporação", pequena, no cartão tracejado? Ela deixa claro que o exame ainda não é oferecido (a fala diz "avança na incorporação"). Sem ela, a tela mostra só "tele-espirometria · UFMG".
3. Na cena 04 (19,0 s), uso a etiqueta "Telessaúde Maranhão" como cabeçalho (é texto, não logo)?

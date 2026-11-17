# Princípios de animação aplicados a vídeo

Tempos em frames a 30 fps (1 frame = 33 ms). A 24 fps, multiplique por 0,8; a 60 fps, por 2.

## Tabela de tempos

| Tipo de movimento | Frames @30 | Segundos |
| --- | --- | --- |
| Micro (pop, check, troca de cor) | 6–9 | 0,2–0,3 |
| Entrada ou saída de texto | 8–12 | 0,25–0,4 |
| Entrada de cartão ou painel | 12–18 | 0,4–0,6 |
| Transição entre cenas | 9–30 | 0,3–1,0 (sem número fixo: ver nota) |
| Deslocamento grande ou empurrão de câmera | 18–30 | 0,6–1,0 |
| Intervalo entre itens em sequência (stagger) | 3–5 | 0,1–0,17 |
| Tempo mínimo de leitura | 0,5 s + 0,3 s por palavra | mínimo 1,5 s |

Saídas são cerca de 25% mais rápidas que entradas.

**Duração da transição depende da cena, não de uma tabela** (pedido do usuário, 15/11/2026): transição que carrega sentido (um zoom que liga duas ideias, uma revelação) ganha tempo para ser percebida (0,6–1,0 s, com pouso suave); troca simples dentro do mesmo assunto pode ser rápida (0,3–0,5 s). Transições rápidas demais em sequência cansam; varie conforme a fala.

## Curvas de easing (use sempre estas, por consistência)

| Uso | cubic-bezier | Nome |
| --- | --- | --- |
| Entrada (chega e assenta) | `0.16, 1, 0.3, 1` | easeOutExpo |
| Entrada suave | `0.33, 1, 0.68, 1` | easeOutCubic |
| Saída (sai acelerando) | `0.32, 0, 0.67, 0` | easeInCubic |
| Deslocamento de A para B | `0.65, 0, 0.35, 1` | easeInOutCubic |
| Entrada com sobra (overshoot) | `0.34, 1.56, 0.64, 1` | easeOutBack, sobra de ~10% |

Overshoot é tempero: use em pop, check e CTA, nunca em tudo.

**Gosto do usuário: mola (spring) no estilo das interfaces da Apple.** Chega rápido, passa um pouco do alvo e assenta (massa, rigidez e amortecimento; em `ts-anim.js`, `mola` e `molaViva`). Prefira em entradas de cartões, etiquetas, ícones, títulos e painéis. Ao explicar uma técnica, nomeie "mola" e dê os parâmetros: o usuário quer aprender.

**Gosto do usuário: nada de pílula (cápsula), use etiqueta retangular (17/11/2026).** Texto em forma de cápsula, com as pontas totalmente redondas, "tem cara de coisa feita por IA" e tira a personalidade. Palavras-chave, rótulos, listas de itens e botões vão em **etiquetas retangulares com cantos levemente arredondados**: raio de cerca de 15–20% da altura da etiqueta (ex.: etiqueta de 80 px de altura → raio de 12–16 px), nunca 50%. Vale para vídeo, quadros-chave e documentos (roteiros em HTML). Onde as skills e os roteiros dizem "pílula", leia "etiqueta retangular".

## Os 12 princípios, em regras práticas

1. **Achatar e esticar (squash & stretch):** um objeto que pousa achata por 2–3 frames (escala 1,08 × 0,92) e volta. Volume constante. Em texto, quase nunca.
2. **Antecipação:** antes de um movimento grande, recuo de 3–5% no sentido oposto, por 3–4 frames. Avisa o olho do que vem.
3. **Encenação (staging):** um foco por vez. Quando um elemento entra, o anterior sai, diminui ou perde opacidade (60–70%).
4. **Pose a pose:** defina as poses-chave de cada elemento (início, assentado, saída) no plano antes de animar o caminho.
5. **Continuidade e sobreposição (follow through & overlap):** partes ligadas assentam depois da principal: ícone 2–3 frames depois do cartão, texto 2–4 frames depois do ícone.
6. **Aceleração e desaceleração (slow in/out):** nunca linear. Use as curvas da tabela.
7. **Arcos:** deslocamentos longos seguem uma leve curva, não uma reta, e rotação de 2–6° acompanha.
8. **Ação secundária:** um floreio que reforça a principal, como um brilho no check, uma linha de pulso atrás do título ou uma sombra que estica. Uma por cena.
9. **Timing:** a tabela acima. Rápido demais parece nervoso; lento demais parece travado.
10. **Exagero:** guarde para os momentos que importam (alerta, CTA, número de impacto). Overshoot até 8–10%, uma vez.
11. **Volume e profundidade (solid drawing):** sombra de contato suave, inclinação de 2–4° em cartões, camadas sobrepostas (fundo, objeto, texto). Evite o recorte chapado colado na tela.
12. **Apelo:** acabamento. Cantos arredondados consistentes, espaçamentos iguais, alinhamento em grade, poucas cores.

## Leis de UX que também valem para vídeo

As leis de interface (Fitts, área de clique, Postel) são para telas clicáveis e não se aplicam a vídeo. Estas se aplicam:

- **Hick:** menos opções por tela. Uma ideia por cartão.
- **Miller:** agrupe. Listas de no máximo 4 itens na tela; acima disso, divida em duas telas.
- **Doherty:** responda rápido. O elemento reage à fala em até 4 frames; o espectador não espera.
- **Jakob:** use o que o público já conhece, como legenda embaixo, CTA no final, ícones convencionais (check = certo, X = errado, triângulo = alerta).
- **Frequência:** o que se repete no vídeo anima menos. A 3ª aparição de um mesmo tipo de cartão entra mais simples que a 1ª.

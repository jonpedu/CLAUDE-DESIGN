# IAM v5: estudo da edição (versão com transições criativas)

Versão: **IAM v5** (`renderizando/IAM v5.mp4`), de 15/11/2026. É candidata a versão final; a **v4** segue como oficial até a validação.
Este documento é a continuação de [`IAM - estudo da edição.md`](IAM%20-%20estudo%20da%20edição.md), o estudo da v4. Tudo o que não aparece aqui é igual à v4: textos, tempos das palavras, clipes, recortes, régua, fechamento, trilha e ducking. O foco aqui é o que a v5 acrescentou: **14 transições novas**, a **frase que desliza para o painel**, **partículas**, **máscaras em forma** e os **sons** de cada passagem.

Fonte: `renderizando/_claude/animacao/completo_v5.html`. Mixagem: `animacao/mix_v5_final.json`.

---

## 1. Ideia central da v5

Na v4, as transições eram discretas (corte seco, dissolução, empurrão). Na v5, **cada passagem conta um pedaço da história**: a transição usa um objeto ou um sentido da própria fala (o coração, o batimento, a lupa, o alerta, o relógio). Assim o efeito chama atenção e, ao mesmo tempo, reforça a mensagem, o critério de "efeitos com sentido" que guiou o projeto.

---

## 2. As transições, uma a uma

Tempos em segundos do vídeo final.

| # | Tempo | De → para | Nome da técnica | O que acontece | Ligação com a fala |
|---|---|---|---|---|---|
| T1 | 3,70–4,60 | C1 → C2 | **Máscara em forma** (*shape mask*) + **antecipação** + **partículas** | o coração do "Você sabia?" incha 25% (antecipação, 3,70), depois vira uma **janela em forma de coração** que cresce 18× e revela a C2; uma borda branca acompanha a forma e 18 faíscas (vermelhas e brancas) saem do centro | o tema é o coração |
| T2 | 8,45–9,80 | C2 → C3 | **Zoom através** (mantido da v4) | entra no coração do T07 com desfoque; a C3 começa ampliada e recua | o coração liga as cenas |
| T3 | 13,92–14,72 | C3 → C4 | **Varredura guiada por traço** (*line wipe*) | o ECG se desenha da esquerda para a direita e a tela azul abre **exatamente atrás da ponta do traço**, que tem um ponto branco brilhante; depois o ECG desce com mola (v4) | "Hoje vamos falar sobre o infarto": o batimento abre o tema |
| T4 | 18,20–19,10 | C4 → C5 | **Íris** + **anel de borda** | o círculo abre a partir do coração, agora com um anel vermelho grosso e um branco fino que acompanham a borda e somem | do coração do título para o coração do clipe |
| T5 | 26,40–27,25 | C5 → C6 | **Através da lente** (*lens transition*) | a lente da lupa do T06 (centro 575, 1405; raio 195) cresce até a tela inteira e mostra a C6, que já começa ampliada (1,3×), como vista pela lupa; aro cinza-claro, contorno azul-escuro e um reflexo branco em arco | "artéria bloqueada": olhar de perto |
| T6 | 35,45–36,30 | C6 → C7 | **Queda com impacto** (*drop + camera shake*) + **partículas** | a tela "Mas atenção" despenca do alto com aceleração (0,3 s, `in`), chega em 35,75 (palavra "Mas") e **treme** com amplitude que decai (28 px, amortecimento exponencial); 16 confetes amarelos saltam da base | a virada da fala é um "tranco" |
| T7 | 40,00–40,68 | C7 → C8 | **Faixas alternadas** (*strip wipe*) + **recuo de fundo** | três faixas verticais revelam a C8, a do meio subindo de baixo; cada uma tem uma borda colorida (azul, verde e vermelha, das cores da marca) na frente; a C7 recua 8% e escurece por baixo | três grupos: mulheres, idosos, diabetes |
| T8 | 44,85 | C8 (vídeo → camadas) | **Dissolução com recorte no mesmo lugar** (mantida da v4) | — | — |
| T9 | 54,35–54,90 | C8 → C10 | **Faixa diagonal** (*diagonal band wipe*) | uma faixa azul Primary `#365DCC` com borda Brand Strong `#1C306A` varre a tela na diagonal; a C10 aparece atrás dela. *A primeira versão era amarela e foi trocada na revisão porque não combinava.* | "Fique atento a": muda de assunto |
| T10 | 66,30–66,68 | C10 → C11 | **Chicote** (*whip pan*) + **riscos de velocidade** | a C10 sai para a esquerda e a C11 entra pela direita, ambas com desfoque que cresce no meio do movimento; 9 riscos azul-escuros passam | "não espere": urgência |
| T11 | 72,95–73,50 | C11 → C12 | **Corte com soco** (*punch cut*) + **flash de borda** | a C12 entra 14% maior e assenta com **mola**; uma borda vermelha de 60 px pisca e some, como sirene | "Suspeitou de infarto?" |
| T12 | 75,95–76,60 | C12 → C13 | **Cartão que sobe** (*card rise*) | a tela azul do SAMU sobe como um cartão de chamada de celular, com mola, cantos arredondados (70 px → 0) e escala 92% → 100% | "ligue para o SAMU" |
| T13 | 78,12–78,50 | C13 → C14 | **Zoom através do número** | a câmera mergulha no "9" do 192 (6×, com desfoque); a C14 nasce ampliada (1,3×) e desfocada e recua com `expo` | do número para a ação |
| T14 | 80,75–81,35 | C14 → C15 | **Varredura de relógio** (*clock wipe*, máscara cônica) | um ponteiro branco dá uma volta completa a partir do meio-dia; o que ele varre já é a C15; 12 marcas de hora aparecem e somem; o centro é um botão vermelho | "Cada minuto conta!" |
| T15 | 82,75–83,90 | C15 → painel | **Elemento compartilhado** (*shared element*, *magic move*) | o painel azul sobe (0,55 s); a frase "Cada minuto / conta!" do topo **desliza linha a linha** até o centro do painel e cresce de 104 para 118 px com mola; o azul e o vermelho passam a branco quando o painel passa por trás | a última fala vira a marca |
| T16 | 83,90–84,65 | painel → fechamento | **Íris** (mantida da v4) | o círculo branco abre do centro e revela o vídeo da equipe | — |

---

## 3. Técnicas novas (como funcionam)

### 3.1 Máscaras: o que fica visível

Uma **máscara** decide qual parte de uma cena aparece. Toda transição de "revelar" é uma máscara que muda com o tempo.

| Máscara | Recurso (CSS) | Onde | Como se pede |
|---|---|---|---|
| retângulo que cresce | `clip-path: inset(...)` | T3 (ECG) | "abre da esquerda para a direita, seguindo o traço" |
| círculo | `clip-path: circle(r at x y)` | T4, T5, T16 | "íris a partir do coração / da lupa" |
| forma livre | `clip-path: path(...)` | T1 (coração), T7 (três faixas) | "janela em forma de coração" |
| polígono | `clip-path: polygon(...)` | T9 (diagonal) | "faixa diagonal" |
| cone (setor) | `mask-image: conic-gradient(...)` | T14 (relógio) | "varredura de relógio" |

**Coração escalável:** o coração é desenhado a partir de uma lista de curvas (as mesmas do coração da C1). Uma função recalcula os pontos para qualquer centro e escala, e assim a janela começa do tamanho exato do coração da tela (2,5×) e cresce até 45×, o suficiente para cobrir a tela inteira. O crescimento é **exponencial** (`2,5 × 18^k`) porque o olho percebe tamanho em proporção: crescer de forma linear pareceria lento no começo e rápido no fim.

**Ponta do traço:** na T3 a borda da máscara não segue um tempo fixo. Ela segue o **ponto exato da ponta do ECG**, calculado com `getPointAtLength`, e por isso a revelação acompanha cada pico do batimento.

### 3.2 Movimento

| Técnica | Detalhe | Onde |
|---|---|---|
| **Antecipação** | antes de uma ação grande, um movimento pequeno no sentido oposto ou de preparação (o coração incha antes de virar janela). É um dos 12 princípios da animação. | T1 |
| **Queda com gravidade** | `ease-in` cúbico: começa devagar e acelera até o impacto | T6 |
| **Tremor amortecido** (*camera shake*) | deslocamento `28·e^(−9t)` em x e y com frequências diferentes (71 e 57 Hz), mais um zoom de 5% durante o tremor para as bordas não aparecerem | T6 |
| **Chicote** (*whip pan*) | as duas cenas se movem juntas; desfoque `16·sen(π·k)`, máximo no meio do movimento e zero nas pontas | T10 |
| **Soco** (*punch*) | escala 1,14 → 1 com **mola** (passa um pouco do alvo e assenta) | T11 |
| **Cartão com mola** | posição com `mola`; cantos e escala com `out` (sem sobra, para não deformar) | T12 |
| **Elemento compartilhado** | o motor mede onde cada linha está (topo) e onde deve chegar (centro do painel) e interpola posição e tamanho; a cor é interpolada em RGB até o branco | T15 |
| **Recuo de fundo** | a cena que sai recua (escala 0,92) e escurece (brilho 65%): dá profundidade, como se a nova cena viesse por cima | T7 |

### 3.3 Partículas determinísticas

As faíscas (T1), os confetes (T6) e os riscos de velocidade (T10) parecem aleatórios, mas usam um **gerador pseudoaleatório fixo** (`rnd(i)`, baseado em seno). A partícula *i* tem sempre a mesma direção, distância e tamanho. Isso mantém o render **determinístico**: dá para refazer só um trecho e emendar sem que as partículas mudem, como aconteceu nos ajustes da faixa e do final.

### 3.4 Camada de transições

Todos os desenhos de passagem (bordas, anéis, faíscas, faixas, ponteiro) ficam numa camada SVG própria (`#tr`), **acima das cenas e abaixo da régua**. A régua nunca é coberta por uma transição.

### 3.5 Ordem das camadas (z-index) que muda no tempo

Para uma cena revelar outra, a cena que entra precisa ficar **por cima** durante a transição. Na v5, várias cenas trocam de altura só durante a passagem e depois voltam. Por exemplo, a C4 fica acima da C3 durante a varredura do ECG e depois volta para baixo, para que a íris da C5 funcione. Essa é a parte mais delicada da montagem: se a ordem estiver errada, a transição simplesmente não aparece.

---

## 4. Elementos visuais novos

Todos foram desenhados em código (SVG), nas cores da marca. Nenhum elemento de marca foi criado ou alterado.

| Elemento | Cor | Onde |
|---|---|---|
| Borda do coração-janela | branco | T1 |
| Faíscas | `#FF6B5E` e branco | T1 |
| Ponto brilhante na ponta do ECG | branco com brilho `#FF6B5E` | T3 |
| Anéis da íris | `#FF6B5E` e branco | T4 |
| Aro, contorno e reflexo da lente | `#DDE3EE`, `#1C306A`, branco | T5 |
| Confetes do impacto | `#FFE34D` (amarelo do triângulo de atenção) | T6 |
| Bordas das três faixas | `#365DCC`, `#19756F`, `#FF6B5E` (Primary, Secondary e o vermelho do tema) | T7 |
| Faixa diagonal | `#365DCC` com borda `#1C306A` | T9 |
| Riscos de velocidade | `#1C306A` | T10 |
| Borda de sirene | `#E5483B` | T11 |
| Ponteiro, marcas de hora, botão central | branco, `#1C306A`, `#B42318` | T14 |

A cor do tema (vermelho) continua só em destaques, e o azul segue como cor estrutural, inclusive na faixa da T9.

---

## 5. Som da v5

Mesma base da v4 (narração, trilha a −12 dB com ducking de 6 dB, fechamento com crossfade, −14 LUFS). Mudanças nos efeitos: **3 removidos e 13 novos**, 56 eventos no total.

| Saiu (v4) | Entrou (v5) | Tempo | Volume | Para quê |
|---|---|---|---|---|
| `whoosh_subida` 4,0 | `whoosh_entrada` + `blob` | 3,95 | −9 / −14 dB | coração-janela (sopro + batida grave) |
| — | `whoosh_suave` | 13,90 | −11 dB | varredura do ECG |
| — | `whoosh_suave` | 26,40 | −11 dB | lente da lupa |
| — | `whoosh_suave` | 35,45 | −12 dB | queda (o `pop_grave` de 35,75 vira o impacto) |
| — | `whoosh_entrada` | 54,35 | −10 dB | faixa diagonal |
| — | `whoosh_entrada` | 66,30 | −9 dB | chicote |
| — | `pop_grave` | 72,95 | −10 dB | soco |
| `whoosh_suave` 76,2 | `whoosh_suave` | 75,95 | −10 dB | cartão que sobe |
| `whoosh_suave` 78,35 | `whoosh_entrada` | 78,12 | −10 dB | zoom através do 192 |
| — | `tique_1`, `tique_2`, `tique_3` | 80,80 · 80,95 · 81,10 | −16 dB | ponteiro do relógio |

Princípio usado: **um som por gesto visual**, mais forte quanto maior o movimento (whoosh *entrada* para os grandes, *suave* para os médios) e sempre abaixo da voz.

---

## 6. Render e entrega

| Item | v4 | v5 |
|---|---|---|
| Captura dos quadros | JPEG 95 | **PNG** (sem perda) |
| Vídeo | H.264 CRF 17, preset medium | H.264 **CRF 12, preset slow**, perfil high |
| Áudio | AAC 192 kbps | AAC **320 kbps** |
| Workers | 3 fixos | **escolhidos pela máquina** (3 nesta) |
| Clipes | originais | **cópias de busca rápida** (all-intra) |
| Ajustes pontuais | render completo | **trecho + emenda** no quadro exato (faixa: 1,2 s; final: 4,5 s) |

O modo de qualidade máxima é ativado com `QUALIDADE=max` no motor e `audio_kbps: 320` na mixagem.

---

## 7. Vocabulário novo para pedidos

- **Máscaras:** janela em forma (de coração, de lupa…), íris, varredura guiada por traço, faixas alternadas, faixa diagonal, varredura de relógio.
- **Movimento:** antecipação, queda com impacto, tremor (*shake*), chicote (*whip pan*), soco (*punch*), cartão que sobe, recuo de fundo.
- **Ligação entre cenas:** elemento compartilhado (*magic move*: o mesmo texto ou objeto viaja de uma cena para a outra), zoom através (de um objeto ou de um número).
- **Acabamento:** partículas (faíscas, confetes, riscos de velocidade), anel de borda, flash de borda.

Exemplo de pedido preciso: *"Na passagem para a cena do SAMU, a tela sobe como um cartão de celular, com mola e cantos arredondados; som de whoosh suave."*

---

## 8. Lições desta versão

1. **Cor de transição é cor de marca.** O amarelo na faixa grande (T9) destoou; em detalhes pequenos (confetes, triângulo) ele funciona. Áreas grandes de transição pedem o azul.
2. **Texto em movimento não pode cruzar rosto.** Na T15, a frase chegava antes do painel e passava sobre a personagem. A solução foi sincronizar: o painel cobre primeiro e o texto vem atrás.
3. **Posição de objeto do clipe se mede, não se estima.** A lente da T5 precisou de duas correções até bater com a lupa do clipe. Para transições que nascem de um objeto, vale medir no quadro exportado.
4. **Determinismo permite emendas.** Como tudo é função do tempo (inclusive as partículas), ajustes pontuais custaram segundos de render, e não minutos.


---

## Nota de 16/11/2026: versões v5.1 (só o áudio mudou)

`renderizando/IAM v5.1.mp4` substitui a `IAM v5.mp4` (arquivada em `_claude/versoes-anteriores/`). Imagem idêntica à da v5; mixagem nova em `_claude/animacao/mix_v51.json`.

| Problema | Correção |
|---|---|
| A trilha parava junto com a narração (82,7 s) e deixava ~1,2 s quase em silêncio antes do fechamento (bug do `mixar.py`: o ducking por sidechain acabava quando a faixa de voz acabava) | `mixar.py` completa a narração com silêncio até o fim (`apad`); a trilha agora segue até o fechamento e cruza com ele |
| Trilha baixa demais para celular (−12 dB, ducking 6 dB) e os primeiros ~11 s da música são 7 dB mais baixos | novo padrão: −11 dB, ducking 5 dB, áudio 320 kbps. Como a música (87,7 s) é curta para pular a introdução num vídeo de 88 s, ela começa do início com **realce** de +6 dB nos primeiros 11 s (volta ao normal em 3 s) |

Volume final: −14 LUFS. Nas pausas a trilha fica em torno de −20 a −24 LUFS.

Capa: a mesma imagem de antes, renomeada para `CAPA IAM v5.1.png`.

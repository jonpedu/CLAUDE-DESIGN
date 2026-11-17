# IAM (Infarto Agudo do Miocárdio): estudo da edição

Versão aprovada: **IAM v4** (`renderizando/IAM v4.mp4`), em 15/11/2026.
Este documento registra tudo o que entrou no vídeo, quando e com que técnica, para servir de estudo e para pedidos mais precisos nos próximos vídeos. Os tempos estão em segundos do vídeo final (ex.: `40,56` = 0:40,56).

---

## 1. Ficha técnica

| Item | Valor |
|---|---|
| Formato | 9:16, 1080×1920, 30 fps, H.264 (CRF 17), AAC 48 kHz |
| Duração | 88,5 s (1:28,5) |
| Volume | −14 LUFS integrado, pico −1,1 dBFS (loudnorm em duas passadas) |
| Cenas | 16 (C9 não existe: foi incorporada à C8 na v2) |
| Fonte da animação | `renderizando/_claude/animacao/completo.html` |
| Mixagem | `renderizando/_claude/animacao/mix_completo.json` |
| Ferramentas | `ferramentas/animar.mjs` (motor), `ts-anim.js` (biblioteca de animação), `telessaude.css` (estilos da marca), `mixar.py`, `sfx.py`, `recortar.py`, `rastrear.py`, `bordas.py`, `transcrever.py`, `emendar.py` |

### Como o vídeo é feito (pipeline)

1. **Transcrição com tempo por palavra** (`transcrever.py`, faster-whisper): cada palavra da narração ganha um tempo de início. Quase todo evento do vídeo está amarrado a uma palavra. Por exemplo, "mulheres" começa em 40,56, e é ali que o marca-texto passa.
2. **Página HTML como linha do tempo.** O vídeo inteiro é uma página com uma função `render(t)`: para cada instante `t`, ela posiciona tudo (texto, clipe, câmera). Não há relógio real, então o render é **determinístico**: o mesmo `t` sempre gera o mesmo quadro.
3. **Motor** (`animar.mjs`): abre a página no Chrome, chama `render(t)` para cada um dos 2655 quadros (88,5 s × 30), fotografa e envia ao ffmpeg.
4. **Áudio à parte** (`mixar.py`): narração, trilha com ducking, efeitos sonoros e áudio do fechamento, normalizados a −14 LUFS e unidos ao vídeo.

---

## 2. Linha do tempo cena a cena

| Cena | Tempo | Fala (resumo) | Base visual | Trecho do clipe | Saída / transição |
|---|---|---|---|---|---|
| **C1** "Você sabia?" | 0,00–4,72 | "Você sabia que, segundo a Sociedade Brasileira de Cardiologia," | Tela cheia azul (TC) | — | **Empurrão para cima** (slide), 0,7 s, 4,0–4,7 |
| **C2** estatística | 4,00–9,00 | "no Brasil, uma pessoa sofre um infarto a cada poucos minutos" | T07 (caminhando, coração escurece) | 3,8–8,8 s | **Zoom através** do coração (×7 com desfoque), 8,45–9,0 |
| **C3** vidas salvas | 9,00–13,92 | "Muitas vidas poderiam ser salvas se os sinais fossem reconhecidos a tempo" | T08 (aponta coração que brilha), colado à direita | 4,1–9,0 s | **Corte seco** |
| **C4** título | 13,92–19,12 | "Hoje vamos falar sobre o Infarto Agudo do Miocárdio" | TC | — | **Revelação em círculo** (íris) a partir do coração, 18,2–19,1 |
| **C5** artéria | 18,20–27,00 | "uma artéria que leva sangue ao coração fica bloqueada…" | T06 (coração com placa, lupa), colado à esquerda | 2,9–8,85 s | **Dissolução cruzada** 0,6 s, 26,4–27,0 |
| **C6** dor | 26,40–35,72 | "Isso pode causar dor ou aperto no peito, que muitas vezes se espalha para o braço esquerdo, o pescoço, as costas ou a mandíbula" | T04 (mão no peito), largura cheia | 1,5–9,95 s | **Corte seco** na palavra "Mas" |
| **C7** "Mas atenção:" | 35,72–40,62 | "Mas atenção: os sinais nem sempre são iguais para todo mundo" | TC | — | **Empurrão para a esquerda**, 0,6 s, 40,0–40,6 |
| **C8** grupos e sinais atípicos | 40,00–54,72 | "Em mulheres, idosos e pessoas com diabetes, o infarto pode se manifestar com dor entre as escápulas… fadiga" | T05 até 45,0, depois camadas recortadas | 3,3–9,6 s (com velocidade variável) | **Corte seco** na palavra "Fique" |
| **C10** "Fique atento a:" | 54,72–66,45 | lista de 6 sinais | T01 (conta nos dedos), janela recortada, colada à esquerda | 0,12–9,6 s | **Corte seco** com recuo de câmera na entrada da C11 |
| **C11** "não espere" | 66,45–72,95 | "Se você sentir isso, principalmente junto com dor no peito, não espere, pode ser um infarto" | T03 (gesto de "pare"), largura cheia | 3,5–9,6 s | **Corte seco** |
| **C12** SAMU | 72,95–76,30 | "Suspeitou de infarto? Ligue imediatamente para o SAMU" | T02 (celular e ambulância) | 0,4–3,75 s | **Corte seco** para a TC |
| **C13** 192 | 76,30–78,50 | "no 192" | TC | — | **Zoom com dissolução** (cresce 15% e some), 78,2–78,5 |
| **C14** não dirija | 78,45–80,95 | "Não dirija até o hospital sozinho" | T02 (carro riscado) | 4,35–6,85 s | **Corte seco** |
| **C15** cada minuto | 80,95–84,70 | "Cada minuto conta!" | T02 (cronômetro) + painel azul | 7,2–9,6 s | **Painel que sobe** (82,85, 0,65 s) e **revelação em círculo** do fechamento |
| **C16** fechamento | 83,90–88,50 | — | `Intro NTS e PETSAUDE.mp4` (fornecido pela equipe, sem alteração) | 0–4,6 s | fim |

A **régua de marca** (`Ajustada TELE e PETSAUDE Digital.png`, 1080×160) fica por cima de todas as cenas, centralizada e encostada na base, do primeiro ao último quadro.

---

## 3. Materiais usados

### 3.1 Clipes do Flow (vídeo, áudio removido)

| Take | Arquivo | Conteúdo | Onde entrou | Enquadramento na tela |
|---|---|---|---|---|
| T01 | `Animated_character_counting_on_f…_7a877c9c` | conta nos dedos, ícones surgindo | C10 | janela de 700×1350 px a partir de y=650 (corta a coluna de ícones e o balão "ALERT" do clipe; começa acima do coque para não cortá-lo), colada à esquerda |
| T02 | `Animated_character_explaining_em…_fe2a8bf8` | celular, carro riscado, cronômetro | C12, C14, C15 (três trechos do mesmo take) | 918 px de largura em x=80, y=230 |
| T03 | `Animated_character_showing_urgen…_7d1d64a3` | gesto de "pare" | C11 | largura cheia em y=400 (toca esquerda, direita e base) |
| T04 | `Character_demonstrating_radiatin…_db77949d` | mão no peito, dor irradiando | C6 | largura cheia em y=380; começa em 1,5 s para pular as bordas tremidas |
| T05 | `Character_gesturing_to_secondary…_7dfac800` | mulher, idosa, homem com glicosímetro | C8 (até 45,0) | largura cheia em y=0 |
| T06 | `Character_presenting_heart_plaqu…_24a0da7b` | coração com artéria entupida | C5 | 842 px, colado à esquerda, y=500 |
| T07 | `Character_walking_and_heart_free…_f6d2e6a7` | entra caminhando | C2 | 734 px em x=120, y=526 |
| T08 | `Woman_pointing_at_glowing_heart_0f5e3784` | aponta coração que brilha | C3 | 864 px colado à direita (x=216), y=470 |

**Mistura multiplicar (`mix-blend-mode: multiply`).** O branco dos clipes do Flow não é exatamente branco (fica entre 250 e 253). Com o modo multiplicar, o quase-branco do clipe some no branco da página e a borda do retângulo do vídeo deixa de aparecer.

**Margem fantasma.** O `bordas.py` mede quais bordas do quadro cada take toca (pé, braço ou cabelo cortados pela borda). O clipe é então colado na mesma borda da tela; se ficasse solto, apareceria um corte no meio do nada. Exemplos: o T08 toca a direita e por isso está em x=216 (216+864=1080); o T01 toca a esquerda e a base.

### 3.2 Imagens e recortes (PNG com transparência)

Todos foram gerados pelo `recortar.py` a partir das folhas que você colocou em `elementos/remover fundo/`, e ficam em `renderizando/_claude/camadas/novos/`.

| Recorte | Folha de origem | Modo de recorte | Onde entrou |
|---|---|---|---|
| `mulher`, `idosa`, `homem` | `Characters_and_icons_vector_sheet` (fundo verde) | chroma key (`CHROMA=1`) por caixa | C8, camadas 45,0–54,7 |
| `bateria`, `pulmao`, `corpo` | `Characters_and_icons_vector_sheet` | chroma key por caixa | C8, ícones sobre as pessoas |
| `rosa` (personagem de blazer rosa) | `Female_character_standing_neutra…` (fundo verde) | chroma key por caixa | C8, camada à esquerda |
| `gotas` (suor frio), `estomago` (náusea), `pulmoes` (falta de ar), `bateria_fraca` (cansaço) | `Medical_icons_sheet_vector_design` (fundo verde) | chroma key por caixa | C10, ícones da lista |
| `tontura`, `abdomen` (dor na boca do estômago) | `Vector_icons_arranged_in_grid` (fundo branco) | **traçado** (`nome*`): recupera ícones de linha fina que o preenchimento comum apagaria | C10, ícones da lista |
| — | `Heart_and_artery_vector_graphics` | não usado (reserva para outra versão) | — |

Os modos do `recortar.py`:
- **Caixa** (`nome=x0,y0,x1,y1`): recorta uma região; o fundo é o branco ligado às bordas (*flood fill*), então brancos internos (camisa, olhos) continuam opacos.
- **Sementes** (`nome=x,y;x,y`): pontos dentro de cada figura; figuras que se tocam são separadas pela fronteira natural (*watershed*). Usado na v1, com o próprio quadro do T05.
- **Traçado** (`nome*`): para ícones de contorno fino.
- **Chroma key** (`CHROMA=1`): remove o verde das folhas geradas com fundo verde.

### 3.3 Grafismos desenhados em código (SVG/CSS)

Feitos na própria página, nas cores da marca, sem imagem externa:
- **Coração** (C1, C4): caminho SVG, vermelho `#E5483B` / `#B42318`.
- **Linha de ECG** (C1, C4): traço SVG que se desenha.
- **Pontos de interrogação** flutuantes (C1): texto Poppins 800, branco a 7%.
- **Triângulo de atenção** (C7 em amarelo `#FFE34D`; selo da C10 em `#C99B00`).
- **Telefone** (C13), **ondas de radar** (C1, C7, C13), **marcadores de alerta** da lista (C10).
- **Fundo das telas azuis**: gradiente radial `#3D66D6 → #29479B → #1C306A` (Primary até Brand Strong) com **textura de pontos** (v4).

### 3.4 Elementos de marca (fornecidos pela equipe, sem alteração)

- Régua `Ajustada TELE e PETSAUDE Digital.png`: o vídeo inteiro, na base.
- `Intro NTS e PETSAUDE.mp4`: fechamento (vídeo e áudio), de 83,9 s ao fim.

### 3.5 Tipografia e cores

- **Poppins** (400 a 900) em todo o texto; Inter carregada como reserva.
- Classes de texto (`telessaude.css`): `.leve` (frase de apoio, 54 px), `.apoio` (56 px), `.forte` (frase principal, peso 700), `.titulo` (palavra-chave grande, 800), `.pilula` (cápsula com texto, 48 px), `.selo` (etiqueta "Fique atento a:").
- **Azul** é a cor da estrutura (telas cheias, títulos, "um infarto"). **Vermelho** é a cor do tema e só aparece em destaques: "bloqueada", "a cada poucos minutos", "não espere", "conta!", "sozinho", SAMU e os marcadores de alerta.

---

## 4. Técnicas de animação (catálogo)

Todas vêm da biblioteca `ferramentas/ts-anim.js` e são funções do tempo.

### 4.1 Curvas de movimento (*easing*)

| Nome no código | Nome técnico | Como se comporta | Onde |
|---|---|---|---|
| `lin` | linear | velocidade constante | derivas lentas (zoom de 1 → 1,04) |
| `out` | ease-out cúbico | sai rápido e freia | entradas de texto |
| `in` | ease-in cúbico | começa devagar e acelera | saídas (zoom através, dissolução da C13) |
| `inOut` | ease-in-out cúbico | acelera e freia | transições, câmera, camadas da C8 |
| `back` | *back* / sobra | passa ~10% do alvo e volta | pops, palco da C10 |
| `expo` | ease-out exponencial | freada muito forte no fim | recuo de câmera (C3, C11, C14) |
| `mola` | **spring** amortecida: `1 − e^(−7t)·cos(8t)` | chega rápido, passa ~6% e assenta | descida do ECG (C4), subida da lista (C10) |
| `molaViva` | spring mais solta: `1 − e^(−6t)·cos(10t)` | ~15% de sobra, balança mais | coração da C4 |

**Mola (spring), estilo Apple.** A curva simula uma massa presa a uma mola com atrito. O termo `e^(−kt)` é o **amortecimento** (quanto maior *k*, menos balança) e `cos(ωt)` é a **oscilação** (quanto maior ω, mais rápido vai e volta). Na `mola` (k=7, ω=8) o movimento passa um pouco do alvo e assenta; na `molaViva` (k=6, ω=10) ele balança mais. Para pedir: "entra com mola suave" ou "com mola mais viva".

### 4.2 Entradas e ênfases de texto

| Técnica | Função | O que faz | Parâmetros | Onde |
|---|---|---|---|---|
| **Subida desfocada** (*type-rise*, *blur-in*) | `TS.entra` | sobe 36 px saindo de um desfoque de 10 px até nítido | 0,45 s, `out` | quase todo texto de apoio: C2, C3, C5, C6, C8, C10, C11, C12, C14 |
| **Pop com sobra** (*pop-in*) | `TS.pop` | cresce de 0 a 100% passando um pouco | 0,42 s, `back` | palavras-chave: "Infarto", "Agudo", "do Miocárdio", "bloqueada", "não espere", "Cada minuto conta!", dígitos 1-9-2, rótulos do corpo, pílulas |
| **Máquina de escrever** (*typewriter*) | `TS.digita` | revela letra a letra | 28–30 letras/s | C1 "segundo a Sociedade / Brasileira de Cardiologia"; C7 "os sinais nem sempre são / iguais para todo mundo" |
| **Marca-texto** (*highlighter wipe*) | `TS.marca` | faixa de cor desenha da esquerda para a direita atrás da palavra | 0,35–0,6 s, `inOut` | "a cada poucos minutos", "a tempo", "peito", "mulheres / idosos / diabetes", itens da lista, "sozinho" |
| **Deriva de escala** (*slow push* no texto) | `scale` linear | o título cresce 3–4% durante a cena | lin | "Você sabia?", título da C4, "Mas atenção:" |
| **Batimento** | `batida(t, hz, t0, nitidez)` = sen^n | pulso curto e seco como um coração | 1,1–1,4 Hz | coração (C1, C4), triângulo (C7), "não espere" (C11) |
| **Ondas de radar** | `onda(...)` | dois anéis que crescem e somem, defasados | 1,1–1,6 Hz | C1 (coração), C7 (triângulo), C13 (telefone) |
| **Tremor de telefone** (*wiggle*) | `rotate(sin(40t)·6°)` | o ícone vibra como chamada | até 77,1 | C13 |
| **Traço que se desenha** (*stroke draw*) | `TS.traco` | anima o contorno do SVG (*stroke-dashoffset*) | 1,15–1,2 s | ECG da C1 e da C4 |
| **Flutuação** (*idle float*) | `sin(t)` | movimento mínimo e contínuo para nada ficar congelado | ±4–14 px | interrogações (C1), pílulas e camadas (C8), ícone no palco (C10) |
| **Destaque do item falado** | opacidade + marca | o item atual fica forte e com marca; os anteriores caem a 60% e perdem a marca | 0,3 s | lista da C10 |

### 4.3 Movimentos compostos (cenas com mais engenharia)

- **C4, ECG com mola (v4):** o batimento nasce 450 px acima do lugar final, logo abaixo de "Hoje vamos falar sobre o", e se desenha de 14,0 a 15,15. Em 15,12 desce com `mola` (0,7 s). Em 15,55 o coração aparece com `molaViva`, e só então os títulos entram com pop: "Infarto" (15,78), "Agudo" (16,26) e "do Miocárdio" (16,98). Depois o ECG pulsa em opacidade no ritmo do coração.
- **C6, rótulos rastreados:** "braço esquerdo" (31,34), "pescoço" (32,46), "costas" (33,44) e "mandíbula" (34,36) entram com pop. Uma **linha-guia** cresce do rótulo até o ponto do corpo, onde fica um **ponto pulsante**. Os pontos seguem o corpo do personagem quadro a quadro (seção 5.2).
- **C8, vídeo → camadas:** até 45,0 o T05 roda normalmente. A velocidade é variável (*time remap*): 1,5× entre 40,2 e 42,72, para as pessoas aparecerem no tempo de "mulheres", "idosos" e "diabetes", e depois 1,1×. Em 44,85 há uma **dissolução de 0,35 s** para as camadas recortadas, que começam exatamente onde cada pessoa estava no quadro (troca invisível). As camadas passam por três arranjos, sempre com `inOut`:
  - **A** (45,0, 0,9 s): espalham-se e crescem.
  - **B** (47,25, 0,6 s): recuam para abrir espaço às duas primeiras pílulas ("dor entre as escápulas" 46,0; "desconforto em pescoço, mandíbula, braço" 47,46).
  - **C** (50,35, 0,7 s): descem e encolhem numa fileira, para caber "dispneia" (50,75), "confusão" (51,74), "síncope" (52,66) e "fadiga" (53,56).
  - O bloco de texto sobe 180 px em 44,95.
- **C10, ícones que voam (lista):** cada sinal é dito e seu ícone surge grande (250 px, `back`) num **palco** (círculo rosa-claro ao lado da personagem). Quando vem o próximo sinal, o ícone **voa e encolhe** (0,5 s, `inOut`) até virar o marcador do item na lista. A lista começa em y=420 e **sobe com mola** em "tontura" (−50 px, 61,12), "cansaço" (−40 px, 62,04) e "dor no estômago" (−40 px, 64,54). Nos dois últimos, a personagem desce 35 px a cada vez, para o texto não encostar nela (v4).
- **C15 → C16, fechamento ligado:** a frase "Cada minuto conta!" entra com pop (81,12). Em 82,85 um **painel azul sobe** (0,65 s) trazendo a mesma frase em branco, centralizada, enquanto a de cima some. A frase encolhe e some em 83,65, e em 83,9 um **círculo branco abre do centro** (0,75 s) e revela o vídeo de fechamento.

---

## 5. Câmera e rastreamento

### 5.1 Câmera virtual

Cada clipe fica dentro de uma "câmera" (`TS.camera`) com **zoom**, **ponto de origem** (o centro do zoom) e **deslocamento**. Quatro movimentos foram usados:

| Movimento | Como é | Onde |
|---|---|---|
| **Aproximação lenta** (*slow push-in*) | zoom linear de 1 → 1,04–1,07 durante a cena | C2 (1,07, no coração), C10 (1,04, ancorado no canto inferior esquerdo), C12 (1,05), C15 (1,05) |
| **Aproximação de ênfase** (*punch-in*) | zoom mais forte e rápido numa palavra | C5: 1 → 1,32 no coração/lupa (22,3–26,3); C11: +22% no rosto em "não espere" (70,2) |
| **Recuo de entrada** (*pull-back*) | a cena começa ampliada e recua com `expo` | C3 (1,9 → 1, continua o zoom da C2), C11 (1,12 → 1), C14 (1,08 → 1) |
| **Abertura** (*zoom-out*) | sai de perto para mostrar o corpo | C6: 1,3 → 1 em 30,3 (antes dos rótulos) |

### 5.2 Rastreamento (*tracking*)

- `rastrear.py` estima o **movimento global** do T04 quadro a quadro: encontra pontos característicos (ORB), casa entre quadros e calcula uma transformação afim robusta (RANSAC). O resultado (`rastreio_T04.js`) traz, para cada quadro, onde estão a mandíbula, o pescoço, as costas e o braço.
- Na página, `TS.naTela` converte essa posição do clipe para a tela, já considerando o zoom da câmera. Assim as linhas-guia e os pontos pulsantes acompanham o corpo mesmo com a câmera se mexendo.

---

## 6. Transições (resumo)

| Tempo | De → para | Técnica | Duração | Por que essa |
|---|---|---|---|---|
| 4,0 | C1 → C2 | **empurrão para cima** (*push/slide*) | 0,7 s | sai da pergunta e entra no dado |
| 8,45 | C2 → C3 | **zoom através** (*zoom-through*): entra no coração com desfoque; a C3 começa ampliada e recua | 0,55 s + 0,8 s | o coração liga as duas cenas |
| 13,92 | C3 → C4 | **corte seco** | — | início do tema |
| 18,2 | C4 → C5 | **revelação em círculo** (*iris*) saindo do coração | 0,9 s | do coração do título para o coração do clipe |
| 26,4 | C5 → C6 | **dissolução cruzada** | 0,6 s | mesma explicação continua |
| 35,72 | C6 → C7 | **corte seco** na palavra "Mas" | — | virada da fala |
| 40,0 | C7 → C8 | **empurrão para a esquerda** | 0,6 s | página seguinte do assunto |
| 44,85 | C8 (vídeo → camadas) | **dissolução curta** com recorte no mesmo lugar | 0,35 s | troca invisível de mídia |
| 54,72 | C8 → C10 | **corte seco** na palavra "Fique" | — | começa a lista |
| 66,45 | C10 → C11 | **corte seco + recuo** | 0,6 s | urgência |
| 72,95 | C11 → C12 | **corte seco** | — | ação |
| 76,3 | C12 → C13 | **corte seco** para a tela azul | — | número em destaque |
| 78,2 | C13 → C14 | **zoom com dissolução** (cresce 15% e some) | 0,3 s | sai do número |
| 80,95 | C14 → C15 | **corte seco** | — | mesmo take, próximo gesto |
| 82,85 / 83,9 | C15 → C16 | **painel que sobe** + **revelação em círculo** | 0,65 s + 0,75 s | liga a última fala à marca |

Regra seguida: a duração depende da coerência entre as cenas. Cortes secos marcam viradas da fala ("Mas", "Fique", "Se"); transições longas ligam cenas que compartilham um elemento (o coração).

---

## 7. Som

### 7.1 Camadas

| Camada | Arquivo | Volume e tratamento |
|---|---|---|
| Narração | `audios/audio completo.wav` (82,7 s, AI Studio) | 0 dB, referência da mixagem |
| Trilha | `trilha sonora/Balanced Learning Loop (Remix) v2.mp3` | −12 dB; entra em 1,0 s; termina em 86,4 com saída de 2,6 s; **ducking** |
| Fechamento | áudio do `Intro NTS e PETSAUDE.mp4` | −2 dB a partir de 83,9, entrada de 0,6 s (**crossfade** com a trilha) |
| Efeitos (sfx) | `biblioteca-sfx/sintetizados/*.wav` | 46 eventos; todos com −5 dB extra sobre o volume da tabela |

**Ducking** (compressão por *sidechain*): a narração controla o volume da trilha. Quando há voz, a trilha baixa 6 dB (ataque de 80 ms); nas pausas, volta em ~0,9 s. Por isso a música "respira" entre as frases sem brigar com a fala.

**Normalização:** `loudnorm` em duas passadas. A primeira mede o áudio e a segunda corrige para −14 LUFS integrado, com pico verdadeiro máximo de −1,5 dB. É o padrão do Instagram e do YouTube.

### 7.2 Efeitos sonoros (todos sintetizados pelo `sfx.py`)

| Som | Como é | Tempos (s) | Volume |
|---|---|---|---|
| `pop_grave` | batida grave e curta | 0,05 · 22,46 ("bloqueada") · 35,75 ("Mas") · 54,8 ("Fique") · 70,3 ("não espere") | −7 a −10 dB |
| `dig_iam_fonte1/2` | digitação gerada a partir do próprio texto, na mesma velocidade | 1,28 · 1,95 | −14 dB |
| `dig_iam_sinais1/2` | idem | 37,1 · 38,0 | −14 dB |
| `whoosh_subida` | sopro que sobe | 4,0 (C1→C2) · 39,95 (C7→C8) · 82,8 (painel) | −9 a −10 dB |
| `whoosh_entrada` | sopro mais encorpado | 8,5 (zoom através) | −8 dB |
| `whoosh_suave` | sopro leve | 18,2 (íris) · 44,95 · 76,2 · 78,35 | −10 a −12 dB |
| `bolha` (*bloop*) | som curto que sobe de tom | 5,02 · 15,78 ("Infarto") · 27,92 · 68,02 | −17 a −18 dB |
| `blob` | som grave e macio | 10,92 · 19,86 · 43,7 · 73,28 | −18 dB |
| `swish_marca_1/2/3` | passada curta do marca-texto (3 variações) | 6,84 · 12,76 · 28,96 · 40,56 · 42,72 · 80,0 | −15 a −16 dB |
| `pop_1..4` | pops em escala que sobe | 31,34 · 32,46 · 33,44 · 34,36 (rótulos) · 46,0 · 50,75 (pílulas) · 77,16 · 77,36 · 77,58 (1-9-2) | −13 a −17 dB |
| `tique_1..3` | tique curto (3 variações) | 55,84 · 57,62 · 59,98 · 61,12 · 62,04 · 64,54 (itens da lista) | −18 dB |

Princípios usados: **sons de interface** (digitação, bolha, swish) só onde há o gesto visual correspondente; **variações** quando o mesmo evento se repete (pop_1..4, tique_1..3, swish 1..3), para não soar mecânico; bloops **seletivos** (8 no vídeo todo, depois do retorno da v1).

---

## 8. Render (motor) e desempenho

| Recurso | O que faz | Ganho medido nesta máquina (i5-1235U, 12 threads, 16 GB) |
|---|---|---|
| **Workers automáticos** | divide o vídeo em partes renderizadas ao mesmo tempo, cada uma num Chrome, e junta sem recomprimir. O número é escolhido pela máquina: 1 a cada 4 threads, no máximo 1 a cada 1,2 GB de RAM livre, teto 4. Em máquina fraca vira 1 (sequencial), então nunca fica pior que o motor antigo. | ~1,6× (aqui escolhe 3) |
| **Cópias de busca rápida** (técnica 4) | cada clipe ganha, uma única vez, uma cópia em que todo quadro é quadro-chave (*all-intra*). Assim o Chrome acha o quadro pedido sem decodificar os anteriores. As cópias ficam em `ferramentas/_cache_busca/` (~170 MB para os 9 clipes do IAM; pode apagar, elas são recriadas). Desliga com `BUSCA=0`. | 1,4× a 1,7× nos trechos com clipe; criar as cópias leva ~40 s na primeira vez |
| **Prévia** (`PREVIA=1`) | meia resolução e compressão rápida, só para avaliar ritmo | pequeno aqui; maior em máquinas mais fracas |
| **Emenda** (`emendar.py`) | refaz só um trecho e encaixa no quadro exato | proporcional ao trecho |

Render completo da v4: 240 s, com 3 workers e sem as cópias de busca. Com as cópias, a estimativa é de ~2,5 a 3 min.

A busca agora mira 2 ms depois do instante pedido. Quando um clipe de 24 fps entra num vídeo de 30 fps, a cada 5 quadros o tempo cai exatamente na fronteira entre dois quadros do clipe; com o ajuste, o resultado é sempre o mesmo, com ou sem as cópias.

---

## 9. O que aprendemos nas revisões (para pedidos futuros)

| Versão | Pedido | Resolução | Vale como regra? |
|---|---|---|---|
| prévia v1 → v2 | texto descentralizado nas telas azuis | tudo centralizado em x=540 | sim (vertical.md) |
| prévia v1 → v2 | "margem fantasma": clipe cortado longe da borda | `bordas.py` + colar na borda que o take toca | sim (takes.md) |
| v1 → v2 | bloops demais e repetitivos | menos eventos e variações | sim (SKILL.md, som) |
| v1 → v2 | fechamento desconectado; áudio cortado | painel azul + íris + crossfade da trilha com o áudio do fechamento | sim |
| v1 → v2 | círculos que não acompanhavam o corpo (0:40) | removidos; troca por camadas recortadas | — |
| v2 → v3 | coque cortado (0:56), sapato rosa cortado, "i" e "g" encostando no título | janela do T01 a partir do topo da cabeça; novo recorte; espaçamento | conferir cabelo, pés e descendentes em todo quadro-chave |
| v2 → v3 | voltar alguns bloops e swishes do marca-texto; digitação mais realista | 8 bloops seletivos; swish em toda marcação; digitação gerada do próprio texto | sim |
| v3 → v4 | texto muito perto da personagem (1:04); ECG sem animação | lista sobe com mola por etapas; ECG nasce no centro e desce com mola; textura nas telas azuis | mola como curva preferida (memória) |

### Vocabulário útil para os próximos pedidos

- **Entradas:** subida desfocada, pop com sobra, máquina de escrever, marca-texto, traço que se desenha, mola suave / mola viva.
- **Câmera:** aproximação lenta, aproximação de ênfase (*punch-in*), recuo de entrada, abertura, rastreamento.
- **Transições:** corte seco, dissolução cruzada, empurrão (para cima, para a esquerda), zoom através, revelação em círculo (íris), painel que sobe, zoom com dissolução.
- **Som:** ducking, crossfade, bloop, blob, swish, whoosh, pop, tique, digitação.
- **Tempo:** "na palavra X" (o efeito começa no início da palavra), "por N segundos", "em escala" (um elemento por vez).

Exemplo de pedido preciso: *"Em 0:46, as pílulas entram com pop e mola viva, uma por palavra; som de pop em escala; câmera com aproximação lenta de 1,04."*


---

## Nota de 16/11/2026: versões v4.1 (só o áudio mudou)

`renderizando/IAM v4.1.mp4` substitui a `IAM v4.mp4` (arquivada em `_claude/versoes-anteriores/`). Imagem idêntica, agora renderizada em qualidade máxima (PNG, CRF 12, preset slow) com a capa no quadro 0; mixagem nova em `_claude/animacao/mix_v41.json`.

| Problema | Correção |
|---|---|
| A trilha parava junto com a narração (82,7 s) e deixava ~1,2 s quase em silêncio antes do fechamento (bug do `mixar.py`: o ducking por sidechain acabava quando a faixa de voz acabava) | `mixar.py` completa a narração com silêncio até o fim (`apad`); a trilha agora segue até o fechamento e cruza com ele |
| Trilha baixa demais para celular (−12 dB, ducking 6 dB) e os primeiros ~11 s da música são 7 dB mais baixos | novo padrão: −11 dB, ducking 5 dB, áudio 320 kbps. Como a música (87,7 s) é curta para pular a introdução num vídeo de 88 s, ela começa do início com **realce** de +6 dB nos primeiros 11 s (volta ao normal em 3 s) |

Volume final: −14 LUFS. Nas pausas a trilha fica em torno de −20 a −24 LUFS.

Capa: a mesma imagem de antes, renomeada para `CAPA IAM v4.1.png`.

---
name: prompts-flow
description: Escreve os prompts do Google Flow (Veo) para as cenas de um roteiro aprovado do Telessaúde. Primeiro separa o que precisa do Flow (personagens e ações) do que o Claude faz em motion gráfico (texto, ícones, mapas, telas, capas). Use quando o usuário pedir "prompt para o Flow", "prompts das cenas" ou quando a etapa "Cenas Flow" de um vídeo começar. Por enquanto foi testada na série Serviços do NTS; vale para teleorientação e campanhas também.
---

# Prompts para o Google Flow

Criada em 20/11/2026, no piloto da série Serviços do NTS (Teleorientação). Antes, o usuário mandava o roteiro para um Gem do Gemini, que gerava um ou mais prompts **por cena**. Aqui a lógica muda: **o Flow só gera o que o motion gráfico não resolve bem**, e o resto o Claude faz.

Regras de estilo da marca: `telessaude/SKILL.md` ("Cenas geradas por IA"). Método geral: `motion/metodo-referencia.md`, seção 5.

## 1. Triagem: Flow ou motion gráfico?

Leia o roteiro aprovado cena a cena e classifique cada uma:

| Vai para o Flow | O Claude faz em motion gráfico |
| --- | --- |
| Personagem com ação, gesto ou expressão (falar, apontar, sorrir, sentir dor) | Texto, etiquetas, números, títulos |
| Interação entre pessoas (profissional e paciente, enfermeira e médico na tela) | Ícones, setas, órgãos simples, grafismos (SVG) |
| Ação física difícil de animar à mão (andar, cair, exercitar-se) | Celular, notificação, telas, interface |
| | Mapas (Brasil, Maranhão, municípios), linhas de conexão |
| | Capas e trechos de vídeos já publicados |
| | Logos, régua e fechamento (sempre do usuário) |

Na dúvida, prefira o motion gráfico, que é mais controlável e não gasta créditos. Mostre a triagem ao usuário em uma tabela curta antes de escrever os prompts.

## 2. Planejar os clipes

- **Um personagem por clipe, sozinho, em fundo branco**, mesmo quando a cena mostra várias pessoas. A composição (lado a lado, entrada uma a uma, interação) é feita na edição, depois do recorte. Gere dois personagens juntos só quando a interação física é o ponto da cena (um aperto de mão, por exemplo).
- **Ação principal nos primeiros 2 a 3 s.** Na edição, cada clipe costuma render de 1 a 4 s; o resto é postura parada (*idle*), que serve de sobra.
- **Duração da cena = duração da fala dela** (~2,5 palavras/s). Anote no cabeçalho de cada cena.
- **Personagens recorrentes da série:** reaproveite a mesma descrição física, palavra por palavra (ver a seção da série, abaixo). Quando existir um clipe aprovado do personagem, sugira usá-lo como imagem de referência (*Ingredients to Video*).
- **Diversidade** (idade, cor de pele, território) sem caricatura: descreva roupa e objeto típicos, nunca traços exagerados.

## 3. Estrutura de cada prompt (em inglês, autossuficiente)

Escreva o prompt em blocos, nesta ordem, sem citar "a referência", "o vídeo anterior" ou o roteiro:

1. **Estilo:** `Flat design 2D vector animation, motion design style, clean and friendly health-education look. Pure solid white background (#FFFFFF), no scenery, no floor line, only a very soft contact shadow under the feet.`
2. **Personagem:** nacionalidade (Brazilian), idade, pele, cabelo, roupa com cores, um objeto característico. Enquadramento: `Full body, standing, centered in the frame, the character fills the middle 60% of the frame height with generous empty white space above and below.` Os 60% ao centro deixam a pessoa dentro da área segura do 9:16.
3. **Ação com tempo:** `In the first two seconds ...`, depois `Then she keeps a calm idle pose with subtle breathing.` Telas de celular ou computador: `the screen glows softly with plain light (no readable content)`.
4. **Câmera e luz:** `Camera: static, locked-off, straight-on medium-long shot, no zoom, no pan, no cuts. Lighting: flat, even, no dramatic shadows. Colors: soft pastel tones with blue accents.`
5. **Evitar:** `text, letters, numbers, logos, watermarks, UI elements on the phone, photorealism, 3D rendering, extra characters, background objects, camera movement` (+ `caricature or exaggerated stereotypes` quando o personagem representa um grupo).

A câmera é sempre parada: zoom, pan e cortes são feitos na edição, o que permite reenquadrar o mesmo clipe em 9:16 e em 16:9.

## 4. Entrega

- Arquivo `roteiro/prompts-flow.md` na pasta do vídeo, com: cabeçalho (série, versão do roteiro), a lista de cenas que **não** usam Flow, e para cada cena com Flow o texto narrado, a duração, **como a cena vai ser montada** (para o usuário entender por que o prompt é assim) e os clipes em blocos ```` ``` ```` prontos para copiar.
- Configuração no Flow: modo texto para vídeo, **proporção do formato principal** (9:16 ou 16:9), 2 variações por prompt. O áudio do clipe não é usado.
- Seção "Ao gerar": como escolher a variação, manter o mesmo traço entre clipes, onde salvar (`elementos/`) e pedir retorno do que deu errado.
- Clipes opcionais (alternativas) marcados como opcionais.
- Atualize o `00-estado.md` do vídeo: prompts entregues, aguardando os clipes.

## 5. Depois que os clipes chegarem

Confira cada clipe (estilo igual ao dos outros, corpo inteiro, nada cortado, sem texto na tela, ação cedo). Se algum falhar, ajuste **só o bloco que falhou** e anote aqui, em "Aprendizados", o que funcionou, para a próxima vez.

## Séries

### Serviços do NTS (institucional, 2026)

Elenco planejado (`CRIANDO-VIDEOS/SERVIÇOS NTS/01-linha-de-producao.md`): enfermeira da UBS, médico (especialista a distância), paciente, agente comunitário de saúde, estudante. Quando o primeiro clipe de cada um for aprovado, copie aqui a descrição física exata usada no prompt.

- Teleorientação, cena 02 (20/11/2026): idosa da cidade, agricultor do interior do Maranhão (chapéu de palha), jovem estudante e quebradeira de coco babaçu (opcional), cada um com o celular. Prompts em `CRIANDO-VIDEOS/SERVIÇOS NTS/TELEORIENTAÇÃO/roteiro/prompts-flow.md`.
- Telediagnóstico, cena 03 (20/11/2026): médico especialista a distância, da cintura para cima, com tablet (clipe A), e médica como opcional (clipe B). Prompts em `CRIANDO-VIDEOS/SERVIÇOS NTS/TELEDIAGNÓSTICO/roteiro/prompts-flow.md`. Quando um for aprovado, copiar aqui a descrição física.

## Aprendizados

- **Decisão do usuário (Teleorientação v3, 20/11/2026): não recortar personagens do Flow.** O recorte automático deixou erros visíveis (fundo branco preso, roupa comida). O padrão é usar o **clipe original com fundo branco em modo multiplicar** sobre fundo claro, como nos outros vídeos. Consequências: a cena com personagem precisa de **fundo claro**; nada colorido pode passar **atrás** do personagem (mapa, faixa, mancha forte), porque aparece através dele. Esconda o que estiver atrás com máscara ou posicione longe. Fundo verde para recorte só se o usuário pedir.
- **Clipe que vai ser recortado (Teleorientação, 20/11/2026):** no agricultor, o fundo branco ficou preso entre o braço, a mão e o rosto (gesto de tocar o chapéu), e a "luz do celular" saiu como um halo creme sobre o fundo. Os dois atrapalham o recorte. Para evitar:
  - quando o personagem vai ser **recortado e posto sobre outro fundo** (mapa, painel azul), peça **fundo verde chapado** (`Pure solid chroma green background (#00B140), evenly lit, no gradient`) em vez de branco, e recorte com `CHROMA=1` (`ferramentas/recortar.py`). O verde se separa da pele, do branco da roupa e do brilho da tela;
  - evite pedir **brilho/luz saindo do celular** (`the screen glows softly`) nesses clipes: use `the screen is on, with no light rays or glow around it`;
  - prefira gestos que **não fechem um vão** entre braço e corpo/rosto, ou aceite que esses quadros vão precisar de tratamento.
  - Se o clipe já veio em fundo branco: o recorte de `CRIANDO-VIDEOS/SERVIÇOS NTS/TELEORIENTAÇÃO/renderizando/_claude/camadas/recorta_clipes.py` trata brancos fechados grandes e o creme do brilho como fundo. Outra saída é usar só os quadros sem o problema (quadro parado ou trecho curto).

- Referência de estilo que já deu certo (AVC e IAM, 2026): personagem único, vetor flat, fundo branco puro, corpo inteiro, clipes de 10 s em 1080×1920.

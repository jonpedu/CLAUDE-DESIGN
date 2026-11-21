# Contexto do projeto — Edição de vídeos de teleorientação (Telessaúde Maranhão)

Este arquivo resume a conversa de planejamento (claude.ai, 14/11/2026) para dar contexto ao Claude Code nesta pasta.

## Skills deste projeto (leia antes de editar qualquer vídeo)

**Instalação:** feita em 15/11/2026. As skills ficam em `.claude/skills/`; edite só lá. A pasta `skills/` da raiz é a entrega original e está desatualizada (ainda tem a antiga `teleorientacao`); não copie de novo.

- `.claude/skills/motion/` é a skill geral de motion: princípios, catálogo de efeitos nomeados, método para usar referências, formatos e áreas seguras, som, pipeline técnico e presets de estilo (`estilos/`). Vale para qualquer vídeo, de teleorientação ou não.
- `.claude/skills/telessaude/` é a sub-skill da marca Telessaúde, aplicada por cima da geral a **qualquer** vídeo do Telessaúde. Organização em matriz **formato × tipo** (decidido em 15/11/2026):
  - `telessaude/formatos/`: `vertical.md` (9:16) e `horizontal.md` (16:9, inclui a reconstrução de vídeos verticais já publicados em horizontal, que é uma demanda existente).
  - `telessaude/tipos/`: `teleorientacao.md`, `campanha.md`, `institucional.md` (material digital) e `registro.md` (captação real em campo). A antiga skill `teleorientacao` virou `tipos/teleorientacao.md`.
- Estilo pedido nas cenas geradas no AI Studio/Flow: **motion design + flat design**.
- **Elementos de marca (régua, logos, logo animado, som de logo, assinaturas) são sempre fornecidos pelo usuário.** O Claude não os cria nem altera; só posiciona (régua na barra inferior). Faltando algum, pergunta. A identidade visual ainda está em construção (15/11/2026).
- **Pastas de cada vídeo:** `<SÉRIE>/<TEMA>/PARTE N/` com `audios/`, `roteiro/`, `elementos/`, `trilha sonora/` e `renderizando/`; horizontais em `<SÉRIE>/0. Videos Horizontais/`. Detalhes em `.claude/skills/telessaude/organizacao.md`.
- Reconstrução de verticais em horizontal: em andamento sob pedido; regras em `.claude/skills/telessaude/formatos/horizontal.md`.
- **Papel do Claude (decidido em 15/11/2026): o vídeo inteiro.** Monta a base (antes no Canva: telas, textos, animação, transições) e finaliza (antes no Premiere: régua, narração, trilha, efeitos sonoros, mixagem −14 LUFS, exportação), a partir dos elementos fornecidos pelo usuário. Passo a passo em `.claude/skills/telessaude/producao.md`.
- Para outro cliente ou marca, crie uma nova sub-skill copiando `telessaude/` e mantendo só o que é específico; para um novo tipo de vídeo do Telessaúde, crie `telessaude/tipos/<nome>.md`.
- `analise-referencias/RELATORIO-ANALISE.md` tem a análise dos vídeos de referência (15/11/2026) que deu origem ao perfil.
- `GUIA-MOTION.md`, na raiz, é o mapa dessas skills para o usuário.
- **`.claude/skills/prompts-flow/`** (20/11/2026): prompts do Google Flow a partir do roteiro aprovado, só para as cenas que o motion gráfico não resolve (personagens e ações). Substitui o Gem do Gemini. Testada primeiro na série Serviços do NTS.
- **`/editar [vídeo]`** (`.claude/skills/editar/`, 16/11/2026): retoma o vídeo pelo `00-estado.md`, faz uma etapa e salva o estado; permite `/clear` entre etapas sem perder o contexto.

## Plano de trabalho (decidido em 14/11/2026)

- O fluxo de edição em uso é o de `.claude/skills/telessaude/producao.md`, testado em AVC, IAM e Hipertensão parte 2. A ideia inicial de partir da skill **fluxo-de-edicao** (github.com/LeiteZ/fluxo-de-edicao) não foi adotada; `INICIO-CLAUDE-CODE.md` ficou só como registro histórico.
- `videos-referencia/` tem vídeos finalizados e aprovados (teleorientação, campanhas como glaucoma e câncer de pênis, Kits de Telessaúde, ação em Tauá-Mirim, retrospectiva 2025). Servem para extrair a identidade e o estilo. **O usuário quer variação entre vídeos sem sair da identidade:** o perfil é tendência, não regra.
- **Tipografia:** arquivos em `fontes tipograficas/` (entregues em 15/11/2026): Poppins, Exo 2, Inter, Glacial Indifference, Computer Says No (a fonte "Computer"; licença CC BY-SA, pede atribuição) e Bebas Neue (números grandes, entregue em 16/11/2026). O Claude pode pesquisar e propor fontes novas (regra 11 de `.claude/skills/motion/SKILL.md`). Detalhes em `.claude/skills/telessaude/fontes.md`.
- **Cores:** guia do portal em `cores hex/` (clara e escura); valores medidos e regras em `.claude/skills/telessaude/cores.md`. Primary `#365DCC`, Brand Strong `#1C306A`, Secondary `#19756F`. Os tons de azul podem variar, como nos vídeos de referência. Cada vídeo pode ter uma cor do tema (roxo, amarelo, vermelho, cor da campanha), só em pontos de destaque; o azul é o padrão e aparece em todo vídeo, porque remete ao núcleo (decidido em 15/11/2026).

## Quem e o quê

- O usuário tem formação em engenharia da computação e produz vídeos animados de teleorientação em saúde, com cerca de 1 min, para o Telessaúde Maranhão (NTS-UFMA).
- Publicação: Instagram (@telessaude.ma, Reels) e YouTube (Telessaúde Maranhão, Shorts e vídeo 16:9). Site: telessaude.ufma.br.
- Fluxo atual: narração no **Google AI Studio**, cenas com personagens no **Google Flow**, finalização no **Canva** (grafismos, imagens, textos, transições).
- Objetivo agora: o Claude edita os vídeos **localmente, nesta máquina**, a partir dos materiais fornecidos, seguindo a mesma identidade visual. O usuário não quer que a edição rode na nuvem.

## Documento normativo

- `MANUAL-EDICAO-TELEORIENTACAO.md` nesta pasta é a norma de edição. Siga-o em todo vídeo.
- A versão online e editável fica em https://claude.ai/artifact/47ZcX6jxepE9TGjvvcCH22. Se as duas divergirem, pergunte qual vale.

## Decisões já tomadas

- Formatos 9:16 (1080×1920) e 16:9 (1920×1080), ambos 30 fps, H.264, AAC 48 kHz, −14 LUFS. Todas as referências são verticais; o usuário também quer vídeos horizontais novos e reconstruir verticais em horizontal. Qual é o principal depende do vídeo: pergunte quando não estiver claro.
- **Áreas seguras são prioridade do usuário.** Um único arquivo 9:16 serve Reels e Shorts, então vale a margem mais restritiva: retângulo **x 65–888 px, y 288–1248 px** (topo 288, base 672, esquerda 65, direita 192, com base na Meta e no Google). Decisão de 15/11/2026: **informação importante** (texto, números, alertas, chamada, rosto) sempre dentro; elementos secundários podem encostar ou passar um pouco. O usuário avalia pelo olho, não por pixel: mostre os quadros-chave com a máscara sobreposta.
- **Régua de marca:** sempre vem pronta, na pasta do próprio vídeo (em `elementos/`). Aplicar sem alteração, **centralizada e encostada na margem inferior**. **Fica o vídeo inteiro** (decidido em 15/11/2026; no registro de ação, só se pedido).
- **Roteiro original** da equipe sempre vem na pasta de referências. A legenda segue o roteiro final narrado; o original serve para conferir o sentido.
- **Decisões de 15/11/2026, que valem sobre o manual:** sem vinheta de abertura; duração livre (a narração define); teleorientação, campanha e institucional só com palavras-chave animadas, e registro de ação com legenda completa dinâmica; fechamento só com o logo animado (+ assinaturas de parceiros); transições livres. Tabela completa em `.claude/skills/telessaude/SKILL.md`. O `MANUAL-EDICAO-TELEORIENTACAO.md` local e a versão online (documento do Claude Docs) estão sincronizados na versão de 15/11/2026. A versão online é editada pelo conector de documentos, não por publicação; se as duas divergirem, pergunte qual vale.
- Fluxo: conferir o pacote → mapa de cenas → 4 a 6 quadros-chave em tamanho real para aprovação → render da versão principal → ajustes por cena → 16:9, capas e `.srt`.

## Vídeos (índice)

O estado de cada vídeo (versão atual, final aprovado, decisões só dele) fica em `renderizando/_claude/00-estado.md` da pasta do vídeo; o histórico, no estudo da edição. Aqui fica só o índice. Vídeo novo: `py ferramentas/novo_video.py "<pasta>" <TEMA>`.

| Vídeo | Pasta | Situação |
| --- | --- | --- |
| IAM (infarto), 9:16 | `CRIANDO-VIDEOS/IAM/` | v4.1 oficial e v5.1 candidata, aguardando validação da equipe |
| AVC, 9:16 | `CRIANDO-VIDEOS/AVC/` | concluído (v4.1) |
| Teleorientação (série Serviços do NTS, piloto), 9:16 | `CRIANDO-VIDEOS/SERVIÇOS NTS/TELEORIENTAÇÃO/` | v3 final entregue (20/11/2026), aguardando o ok final; depois 16:9 |
| Telediagnóstico (série Serviços do NTS), 9:16 | `CRIANDO-VIDEOS/SERVIÇOS NTS/TELEDIAGNÓSTICO/` | v4: cenas 1–4 e 8 refeitas; proposta do ChatGPT para 5, 6, 7, 9 e 10 salva (`03-proposta-...md`), falta implementar e renderizar (20/11/2026) |
| Hipertensão parte 2, 16:9 (reconstrução) | `REFAZENDO-VIDEOS/hipertensao 2/` | concluído |

## Pendências do fluxo (anotado em 16/11/2026)

- **Banco de elementos:** montar uma biblioteca reutilizável de elementos (SVG primeiro: ícones, órgãos, setas, grafismos; regra 12 de `motion/SKILL.md`).
- **Banco de trilhas:** criado em 20/11/2026 em `biblioteca-trilhas/` (geral, por clima: corporativo, tecnologia, animado, suave, emocional; 20 faixas com LUFS e licença no `README.md`). A trilha segue o clima de cada trecho e pode mudar dentro do vídeo (`motion/som.md`).
- **Banco de efeitos sonoros:** ampliar e organizar `biblioteca-sfx/` (hoje só sintetizados), com nomes descritivos e trechos úteis do áudio do Flow.
- **Tipos ainda não testados:** campanha, institucional, registro de ação, horizontal feito do zero, `.srt`. O primeiro de cada um vai mostrar o que falta nas regras.
- **Vídeo com câmera real:** criar `motion/video-real.md` no primeiro vídeo desse tipo (ferramentas já anotadas em `motion/tecnico.md`).
- **Editor de quadros-chave:** feito em 16/11/2026 (`ferramentas/editor.mjs`; uso em `motion/tecnico.md`). Falta usar num vídeo real e ajustar pelo uso.
- **Repositório (GitHub pessoal, privado):** README de instalação, `requirements.txt`, `.gitignore` e um arquivo de links do Drive para o material grande. Quando o fluxo estabilizar.
- **Futuro:** planilha de controle dos vídeos (provavelmente local, sincronizada pelo Google Drive Desktop).

## O que vem em cada vídeo (atualizado em 16/11/2026)

Não há pendência geral de kit de marca. Cores, fontes e vídeos de referência já estão na pasta. **Os elementos de marca vêm por vídeo, na pasta do próprio vídeo:** a régua do parceiro, os logos avulsos, quando o vídeo precisar, e o vídeo de fechamento (logo animado com som e assinaturas; ex.: `Intro NTS e PETSAUDE.mp4`, nas versões vertical e horizontal). O Claude não acessa o Canva, então tudo vem exportado.

Pacote de cada vídeo: narração (.wav do AI Studio), roteiro final, cenas do Flow (.mp4), folhas de elementos para recorte, régua, fechamento e trilha. Checklist completa e a regra de confirmar os itens obrigatórios antes de montar em `.claude/skills/telessaude/organizacao.md` e `SKILL.md`.

## Ferramentas esperadas na máquina local

O pipeline previsto usa **ffmpeg** (corte, composição, xfade, zoompan, drawtext, legendas ASS, loudnorm), **Python** com Pillow, numpy e OpenCV (grafismos quadro a quadro, reenquadramento) e, para animações em HTML/CSS com as fontes da marca, **Node** com Chrome/Playwright para gravar quadro a quadro. No início, verifique o que está instalado (Windows) e, se faltar algo, diga ao usuário o que instalar antes de começar.

## Preferências de trabalho

- **Regras recorrentes vão para as skills/normas, não para a memória** (a memória custa tokens em toda conversa). Ao notar algo que se repete, proponha incluir na skill certa.

- Responder em português.
- Mostrar quadros estáticos para aprovação antes de um render completo; um render completo por pedido.
- Nunca alterar o sentido das orientações de saúde: o texto na tela só pode dizer o que o roteiro aprovado diz.

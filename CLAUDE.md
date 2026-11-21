# Contexto do projeto — Vídeos do Telessaúde Maranhão (NTS-UFMA)

O Claude Code produz e edita, **localmente**, os vídeos do Telessaúde Maranhão a partir dos materiais da equipe. Este arquivo é o ponto de partida de toda conversa nesta pasta. Atualizado em 21/11/2026, na passagem do projeto para a conta do Núcleo de Telessaúde, em outro PC.

## Primeira conversa num PC ou numa conta nova

A pasta inteira vem pelo Google Drive (`LINKS-DRIVE.md`). Rode **`/preparar`** (`.claude/skills/preparar/`): confere e instala o ambiente, confere se a mídia veio completa e mostra onde cada vídeo parou. Instalação manual: `README.md`.

**Esta conta não tem a memória da conta antiga.** Tudo o que importa está aqui, nas skills e nos `00-estado.md` de cada vídeo. Regra que se repete vai para a skill certa, não para a memória (a memória custa tokens em toda conversa e não passa de uma conta para outra).

## Skills deste projeto (leia antes de editar qualquer vídeo)

As skills ficam em `.claude/skills/`; edite só lá. A primeira entrega (14/11/2026) está arquivada em `_arquivo/skills-entrega-original/`, desatualizada; não copie de volta.

- **`/preparar`** (`preparar/`, 21/11/2026): primeira conversa numa máquina ou conta nova (ver acima).
- **`/editar [vídeo]`** (`editar/`, 16/11/2026): retoma o vídeo pelo `00-estado.md`, faz uma etapa e salva o estado; permite `/clear` entre etapas sem perder o contexto.
- `motion/` é a skill geral de motion: princípios, catálogo de efeitos nomeados, método para usar referências, formatos e áreas seguras, som, pipeline técnico (`tecnico.md`, com os ajustes do Windows) e presets de estilo (`estilos/`). Vale para qualquer vídeo.
- `telessaude/` é a sub-skill da marca, aplicada por cima da geral a **qualquer** vídeo do Telessaúde. Organização em matriz **formato × tipo** (15/11/2026):
  - `telessaude/formatos/`: `vertical.md` (9:16) e `horizontal.md` (16:9, inclui a reconstrução em 16:9 de vídeos verticais já publicados).
  - `telessaude/tipos/`: `teleorientacao.md`, `campanha.md`, `institucional.md` (material digital) e `registro.md` (captação real em campo).
  - `organizacao.md` (pastas de cada vídeo), `producao.md` (etapas), `cores.md`, `fontes.md`.
- **`prompts-flow/`** (20/11/2026): prompts do Google Flow a partir do roteiro aprovado, só para as cenas que o motion gráfico não resolve (personagens e ações). Substitui o Gem do Gemini.
- `GUIA-MOTION.md`, na raiz, é o mapa dessas skills para o usuário.
- Para outro cliente ou marca, crie uma nova sub-skill copiando `telessaude/` e mantendo só o que é específico; para um novo tipo de vídeo do Telessaúde, crie `telessaude/tipos/<nome>.md`.

## Quem e o quê

- O usuário tem formação em engenharia da computação e produz vídeos animados para o Telessaúde Maranhão (NTS-UFMA): teleorientação em saúde (cerca de 1 min), campanhas, institucionais e registros de ação.
- Publicação: Instagram (@telessaude.ma, Reels), YouTube (Telessaúde Maranhão, Shorts e vídeo 16:9) e WhatsApp. Site: telessaude.ufma.br.
- **Papel do Claude (15/11/2026): o vídeo inteiro.** Monta a base (antes no Canva: telas, textos, animação, transições) e finaliza (antes no Premiere: régua, narração, trilha, efeitos sonoros, mixagem −14 LUFS, exportação), a partir dos elementos fornecidos. Passo a passo em `.claude/skills/telessaude/producao.md`. A equipe faz roteiro, narração (**Google AI Studio**) e cenas com personagens (**Google Flow**, estilo **motion design + flat design**).
- Tudo roda **nesta máquina**; o usuário não quer a edição na nuvem.

## Biblioteca geral (`biblioteca/`)

A fonte de onde todos os vídeos bebem (montada em 21/11/2026): marca (réguas, fechamentos, logos, fontes, cores), trilhas, efeitos sonoros, personagens do Flow, mapas, folhas de elementos e vídeos publicados com as capas. Catálogo, regra de uso e lista do que falta em `biblioteca/README.md`; lista de arquivos em `biblioteca/INVENTARIO.md`.

- **Vídeo novo:** antes de pedir assets, veja o que já existe (`py ferramentas/da_biblioteca.py --listar [termo]`) e **copie** para a pasta do vídeo (`py ferramentas/da_biblioteca.py "<item>" "<pasta do vídeo>"`). O vídeo usa a cópia dele, nunca o arquivo da biblioteca; exceções: efeitos sonoros (`biblioteca/sfx/`) e fontes, lidos direto pelo motor.
- **Item novo reutilizável** (elemento de marca entregue pelo usuário, trilha, personagem, SVG baixado com ok) também entra na biblioteca, registrado no `README.md` dela.
- A biblioteca não é editada nem apagada por conta própria; régua e fechamento continuam sendo confirmados com o usuário em todo vídeo.

## Documentos de referência

- `MANUAL-EDICAO-TELEORIENTACAO.md` é a norma de edição (versão de 15/11/2026). As decisões posteriores estão nas skills e valem sobre o manual quando divergirem.
- `planejamento/`: os planos de vídeos, exportados em 21/11/2026 do Claude Docs da conta antiga: `videos-novos-a-produzir.md` (série Serviços do NTS, tutorial da Sofia) e `videos-para-refazer-na-horizontal.md` (reconstruções em 16:9). **A partir de agora a fonte é o repositório**: atualize esses arquivos. As versões online antigas (manual, planos, página da linha de produção) eram da outra conta e não são mais editadas.
- `analise-referencias/RELATORIO-ANALISE.md`: análise dos 22 vídeos de referência (15/11/2026) que deu origem ao perfil da marca.
- `_arquivo/INICIO-CLAUDE-CODE.md`: registro histórico da ideia inicial (skill fluxo-de-edicao, não adotada).

## Decisões já tomadas

- Formatos 9:16 (1080×1920) e 16:9 (1920×1080), ambos 30 fps, H.264, AAC 48 kHz, −14 LUFS, pico −1 dBTP. Qual é o principal depende do vídeo: pergunte quando não estiver claro. Na série Serviços do NTS, vertical primeiro e depois horizontal (20/11/2026).
- **Áreas seguras são prioridade do usuário.** Um único arquivo 9:16 serve Reels e Shorts, então vale a margem mais restritiva: retângulo **x 65–888 px, y 288–1248 px**. **Informação importante** (texto, números, alertas, chamada, rosto) sempre dentro; o resto do quadro **não pode ficar vago** (o vídeo também vai por WhatsApp, sem margem; 20/11/2026). O usuário avalia pelo olho: mostre os quadros-chave com a máscara sobreposta.
- **Elementos de marca** (régua, logos, logo animado, som de logo, assinaturas) vêm sempre do usuário, na pasta `elementos/` do próprio vídeo, e mudam com a parceria. O Claude não os cria nem altera; só posiciona. Régua **centralizada, encostada na base, o vídeo inteiro**. Faltando algum, pergunte; nunca reaproveite o de outro vídeo por conta própria.
- **Roteiro:** o final aprovado e o original da equipe ficam em `roteiro/` do vídeo. O texto na tela segue o roteiro final narrado; o original serve para conferir o sentido.
- **Decisões de 15/11/2026, que valem sobre o manual:** sem vinheta de abertura; duração livre (a narração define); teleorientação, campanha e institucional só com palavras-chave animadas, e registro de ação com legenda completa dinâmica; fechamento só com o logo animado (+ assinaturas de parceiros); transições livres. Tabela em `.claude/skills/telessaude/SKILL.md`.
- **Tipografia:** arquivos em `biblioteca/marca/fontes/`: Poppins (base), Exo 2, Inter, Glacial Indifference, Computer Says No (CC BY-SA, pede atribuição) e Bebas Neue (números grandes). O Claude pode pesquisar e propor fontes novas (regra 11 de `motion/SKILL.md`). Detalhes em `telessaude/fontes.md`.
- **Cores:** guia do portal em `biblioteca/marca/cores/`; valores e regras em `telessaude/cores.md`. Primary `#365DCC`, Brand Strong `#1C306A`, Secondary `#19756F`. O azul é o padrão e aparece em todo vídeo; cada vídeo pode ter uma cor do tema, só em pontos de destaque.
- `biblioteca/videos-publicados/` tem vídeos aprovados (teleorientação, campanhas, Kits de Telessaúde, ação em Tauá-Mirim, retrospectiva 2025). **O usuário quer variação entre vídeos sem sair da identidade:** o perfil é tendência, não regra.
- Fluxo: conferir o pacote → mapa de cenas → 4 a 6 quadros-chave em tamanho real para aprovação → render da versão principal → ajustes por cena → 16:9, capas e `.srt`.

## Vídeos (índice)

O estado de cada vídeo (versão atual, final aprovado, próximo passo, decisões só dele) fica em `renderizando/_claude/00-estado.md` da pasta do vídeo; o histórico, no estudo da edição. Aqui fica só o índice; `py ferramentas/preparar.py` imprime o próximo passo de todos. Vídeo novo: `py ferramentas/novo_video.py "<pasta>" <TEMA>`.

| Vídeo | Pasta | Situação (21/11/2026) |
| --- | --- | --- |
| IAM (infarto), 9:16 | `CRIANDO-VIDEOS/IAM/` | v4.1 oficial e v5.1 candidata, aguardando a equipe escolher |
| AVC, 9:16 | `CRIANDO-VIDEOS/AVC/` | concluído (v4.1) |
| Hipertensão parte 1, 16:9 (reconstrução) | `REFAZENDO-VIDEOS/hipertensao 1/` | concluída: horizontal montado pelo usuário no Canva e finalizado pelo Claude (régua em ilha, fechamento, mixagem); é a referência das reconstruções |
| Hipertensão parte 2, 16:9 (reconstrução) | `REFAZENDO-VIDEOS/hipertensao 2/` | concluído; a página é o motor-base das próximas reconstruções |
| **Série Serviços do NTS** (linha de produção em `CRIANDO-VIDEOS/SERVIÇOS NTS/01-linha-de-producao.md`) | `CRIANDO-VIDEOS/SERVIÇOS NTS/` | vertical primeiro, depois 16:9 |
| ↳ Teleorientação (piloto), 9:16 | `…/TELEORIENTAÇÃO/` | v3 final entregue (20/11/2026), aguardando o ok do usuário; depois 16:9 (falta a intro horizontal) |
| ↳ Telediagnóstico, 9:16 | `…/TELEDIAGNÓSTICO/` | **em produção:** v4 com as cenas 1–4 e 8 refeitas; falta implementar as cenas 5, 6, 7, 9 e 10 da proposta (`03-proposta-chatgpt-cenas-5-6-7-9-10.md`), quadros de prova e render. Passo a passo no `00-estado.md` |
| ↳ Teleconsultoria | `…/TELECONSULTORIA/` | roteiro v2 aprovado; produção ainda não começou |
| ↳ Teleducação | `…/TELEDUCAÇÃO/` | aguardando o ok da Amanda na v2 |
| ↳ Teleinterconsulta, Telerregulação, Diferença entre os Serviços | `…/TELEINTERCONSULTA/`, `…/TELERREGULAÇÃO/`, `…/DIFERENÇA ENTRE OS SERVIÇOS/` | aguardando a validação da Gyovanna |
| ↳ Teleconsulta | `…/TELECONSULTA/` | texto aprovado só para entrar no Diferença entre os Serviços; o NTS ainda não oferece o serviço |
| Videoaula PDS (estudo pessoal do usuário, fora do Telessaúde) | `CRIANDO-VIDEOS/VIDEO ESTUDO PDS/` | sem `00-estado.md`; não faz parte da produção |

Próximos vídeos e reconstruções planejados: `planejamento/`.

## Pendências do fluxo

- **Biblioteca geral:** criada em 21/11/2026 (`biblioteca/`). Falta completar com o que está na lista "O que falta" do `biblioteca/README.md` (fechamento horizontal do Telessaúde, régua PET-Saúde em SVG, logos dos parceiros, mapa do Maranhão por município, banco de ícones SVG).
- **Banco de efeitos sonoros:** ampliar e organizar `biblioteca/sfx/` (hoje só sintetizados), com nomes descritivos e trechos úteis do áudio do Flow.
- **Tipos ainda não testados:** campanha, registro de ação, horizontal feito do zero, `.srt`. Institucional está sendo testado na série Serviços do NTS. O primeiro de cada um vai mostrar o que falta nas regras.
- **Vídeo com câmera real:** criar `motion/video-real.md` no primeiro vídeo desse tipo (ferramentas já anotadas em `motion/tecnico.md`).
- **Editor de quadros-chave:** feito em 16/11/2026 (`ferramentas/editor.mjs`; uso em `motion/tecnico.md`). Falta usar num vídeo real e ajustar pelo uso.
- **Passagem para outro PC:** a pasta inteira vai pelo Drive (`LINKS-DRIVE.md`, falta preencher o link); o Git fica como histórico local das versões, sem GitHub (decidido em 21/11/2026).
- **Futuro:** planilha de controle dos vídeos (provavelmente local, sincronizada pelo Google Drive Desktop).
- Feito: banco de trilhas em `biblioteca/trilhas/` (20/11/2026; 20 faixas por clima, com LUFS e licença no `README.md`; os áudios vêm do Drive).

## O que vem em cada vídeo

Cores, fontes, vídeos publicados e os elementos de marca já entregues estão na `biblioteca/`. **Em cada vídeo, os elementos de marca ficam em `elementos/`** (copiados da biblioteca ou entregues no pacote): a régua do parceiro, os logos avulsos, quando o vídeo precisar, e o vídeo de fechamento (logo animado com som e assinaturas; ex.: `Intro Telessaude.mp4`, `Intro NTS e PETSAUDE.mp4`, nas versões vertical e horizontal). O Claude não acessa o Canva, então tudo vem exportado.

Pacote de cada vídeo: narração (.wav do AI Studio), roteiro final, cenas do Flow (.mp4), folhas de elementos para recorte, régua, fechamento e trilha. Checklist e a regra de confirmar os itens obrigatórios antes de montar em `.claude/skills/telessaude/organizacao.md` e `SKILL.md`.

## Ferramentas na máquina local

**ffmpeg** (corte, composição, xfade, loudnorm), **Python** (`py`) com Pillow, numpy, OpenCV e faster-whisper, e **Node** com `playwright-core` usando o **Chrome** instalado, para gravar quadro a quadro as animações em HTML/CSS/SVG com as fontes da marca. Os scripts do projeto ficam em `ferramentas/` (tabela em `motion/tecnico.md`). Conferência: `py ferramentas/preparar.py`.

## Preferências de trabalho

- Responder em português.
- Mostrar quadros estáticos para aprovação antes de um render completo; um render completo por pedido.
- Nunca alterar o sentido das orientações de saúde: o texto na tela só pode dizer o que o roteiro aprovado diz.
- Efeito sugerido pelo usuário é opção, não ordem: só entra se reforçar a mensagem. Curva preferida: mola (spring). Detalhes em `motion/principios.md` e `telessaude/SKILL.md`.
- Regras recorrentes vão para as skills/normas, não para a memória. Ao notar algo que se repete, proponha incluir na skill certa.

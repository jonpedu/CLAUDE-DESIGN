# Vídeos do Telessaúde Maranhão com o Claude Code

Repositório do fluxo de edição local dos vídeos do Telessaúde Maranhão (NTS-UFMA): skills do Claude Code (`.claude/skills/`), normas, ferramentas (`ferramentas/`), fontes, cores, efeitos sonoros, planos de produção e os textos de trabalho de cada vídeo (estado, roteiros, páginas de animação, mixagens). O material grande (vídeos, áudios, imagens, renders) fica no Drive: [LINKS-DRIVE.md](LINKS-DRIVE.md).

- Ponto de partida para o Claude: [CLAUDE.md](CLAUDE.md).
- Mapa das skills para pessoas: [GUIA-MOTION.md](GUIA-MOTION.md).
- Planos de vídeos: [planejamento/](planejamento/).

## Começo rápido (PC novo, conta nova)

1. Instale o **Git** e o **Claude Code** (app desktop do Claude, aba Code; ou `npm install -g @anthropic-ai/claude-code`) e entre com a conta que vai usar.
2. Clone o repositório numa pasta, de preferência **sem acento no caminho** (ex.: `C:\projetos\CLAUDE-DESIGN`):

   ```powershell
   git clone <url-do-repositório-privado> C:\projetos\CLAUDE-DESIGN
   ```

3. Copie do Drive o material grande para dentro do clone ([LINKS-DRIVE.md](LINKS-DRIVE.md)), **sem substituir** os arquivos que vieram do Git.
4. Abra a pasta do clone no Claude Code e digite **`/preparar`**. O Claude confere tudo e, com o seu ok, instala o que faltar (ffmpeg, Python e pacotes, Node, Playwright, Chrome). Depois mostra onde cada vídeo parou e qual é o próximo passo.
5. Continue a produção com `/editar <vídeo>`, por exemplo `/editar TELEDIAGNÓSTICO`. Entre uma etapa e outra, `/clear` limpa a conversa sem perder nada, porque o estado fica em `renderizando/_claude/00-estado.md` de cada vídeo.

A conta nova **não tem a memória da conta antiga**: o que importa (gostos do usuário, ajustes do Windows, decisões de cada vídeo) está nas skills, no `CLAUDE.md` e nos `00-estado.md`.

## Instalação manual (o que o `/preparar` faz)

| Ferramenta | Como instalar | Conferir |
| --- | --- | --- |
| Git | `winget install Git.Git` | `git --version` |
| Python 3.10+ (com o lançador `py`) | `winget install Python.Python.3.12` | `py --version` (no Windows, `python` pode abrir a loja: use `py`) |
| ffmpeg completo (libx264, loudnorm) | `winget install Gyan.FFmpeg` | `ffmpeg -version` |
| Node 18+ | `winget install OpenJS.NodeJS.LTS` | `node -v` |
| Google Chrome | `winget install Google.Chrome` | o Playwright usa o Chrome instalado (`channel: 'chrome'`) e não baixa navegador próprio |
| Pacotes Python (Pillow, numpy, OpenCV, faster-whisper) | `py -m pip install -r requirements.txt` | `py -c "import PIL, numpy, cv2, faster_whisper"` |
| playwright-core | `cd ferramentas` e depois `npm install` | `node ferramentas/teste-playwright.mjs` grava `ferramentas/teste.png` |

Depois de instalar pelo `winget`, abra um terminal novo (ou reabra o Claude Code) para o PATH valer. Conferência completa, sem instalar nada: `py ferramentas/preparar.py`.

- **Fontes:** ficam em `fontes tipograficas/` e vêm no Git. O motor de animação carrega as fontes direto da pasta, então não é preciso instalá-las no Windows para renderizar.
- **faster-whisper** baixa o modelo de transcrição na primeira vez (precisa de internet nessa vez).

## O que fica fora do Git

- **Material grande:** vídeos, áudios, imagens, PDFs e renders ([LINKS-DRIVE.md](LINKS-DRIVE.md)). Exceções que vêm no Git: `fontes tipograficas/`, `cores hex/`, `biblioteca-sfx/`.
- **Kit de marca:** régua do parceiro, logos e fechamento animado vêm dentro de `elementos/` de cada vídeo (Drive). O Claude não cria nem altera esses elementos.
- `node_modules/` (recriado por `npm install`), caches e `.claude/settings.local.json` (permissões desta máquina).
- **Documentos online da conta antiga** (manual, planos e página da linha de produção no Claude Docs): foram exportados para o repositório (`MANUAL-EDICAO-TELEORIENTACAO.md`, `planejamento/`, `CRIANDO-VIDEOS/SERVIÇOS NTS/01-linha-de-producao.md` e `linha-de-producao-online.html`). Na conta nova, a fonte é o repositório; publique páginas novas a partir desses arquivos se a equipe precisar.
- `_arquivo/`: entregas antigas (primeira versão das skills, plano inicial), só como registro.

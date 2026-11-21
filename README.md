# Vídeos do Telessaúde Maranhão com o Claude Code

Pasta de trabalho dos vídeos do Telessaúde Maranhão (NTS-UFMA), feitos localmente com o Claude Code: skills (`.claude/skills/`), normas, ferramentas (`ferramentas/`), a **biblioteca geral** (`biblioteca/`: marca, trilhas, efeitos sonoros, personagens, vídeos publicados), os planos (`planejamento/`) e a pasta de cada vídeo (`CRIANDO-VIDEOS/`, `REFAZENDO-VIDEOS/`).

- Ponto de partida para o Claude: [CLAUDE.md](CLAUDE.md).
- Mapa das skills para pessoas: [GUIA-MOTION.md](GUIA-MOTION.md).
- Catálogo do que serve a todos os vídeos: [biblioteca/README.md](biblioteca/README.md).
- Levar para outro PC: [LINKS-DRIVE.md](LINKS-DRIVE.md).

## Começo rápido (PC novo, conta nova)

1. Instale o **Claude Code** (app desktop do Claude, aba Code) e entre com a conta que vai usar.
2. Baixe a pasta inteira do Drive ([LINKS-DRIVE.md](LINKS-DRIVE.md)) para um caminho **sem acento** (ex.: `C:\projetos\CLAUDE-DESIGN`).
3. Abra a pasta no Claude Code e digite **`/preparar`**. O Claude confere tudo e, com o seu ok, instala o que faltar (ffmpeg, Python e pacotes, Node, Playwright, Chrome). Depois mostra onde cada vídeo parou e qual é o próximo passo.
4. Continue a produção com `/editar <vídeo>`, por exemplo `/editar TELEDIAGNÓSTICO`. Entre uma etapa e outra, `/clear` limpa a conversa sem perder nada, porque o estado fica em `renderizando/_claude/00-estado.md` de cada vídeo.

A conta nova **não tem a memória da conta antiga**: o que importa (gostos do usuário, ajustes do Windows, decisões de cada vídeo) está nas skills, no `CLAUDE.md` e nos `00-estado.md`.

## Instalação manual (o que o `/preparar` faz)

| Ferramenta | Como instalar | Conferir |
| --- | --- | --- |
| Git (histórico local das versões) | `winget install Git.Git` | `git --version` |
| Python 3.10+ (com o lançador `py`) | `winget install Python.Python.3.12` | `py --version` (no Windows, `python` pode abrir a loja: use `py`) |
| ffmpeg completo (libx264, loudnorm) | `winget install Gyan.FFmpeg` | `ffmpeg -version` |
| Node 18+ | `winget install OpenJS.NodeJS.LTS` | `node -v` |
| Google Chrome | `winget install Google.Chrome` | o Playwright usa o Chrome instalado (`channel: 'chrome'`) e não baixa navegador próprio |
| Pacotes Python (Pillow, numpy, OpenCV, faster-whisper) | `py -m pip install -r requirements.txt` | `py -c "import PIL, numpy, cv2, faster_whisper"` |
| playwright-core | `cd ferramentas` e depois `npm install` | `node ferramentas/teste-playwright.mjs` grava `ferramentas/teste.png` |

Depois de instalar pelo `winget`, abra um terminal novo (ou reabra o Claude Code) para o PATH valer. Conferência completa, sem instalar nada: `py ferramentas/preparar.py`.

- **Fontes:** ficam em `biblioteca/marca/fontes/`. O motor de animação carrega as fontes direto da pasta, então não é preciso instalá-las no Windows para renderizar.
- **faster-whisper** baixa o modelo de transcrição na primeira vez (precisa de internet nessa vez).

## Como a pasta se organiza

- `biblioteca/`: fonte geral. Vídeo novo copia daqui o que precisar (`py ferramentas/da_biblioteca.py "<item>" "<pasta do vídeo>"`) e usa a cópia; a biblioteca não muda.
- `CRIANDO-VIDEOS/<vídeo>/` e `REFAZENDO-VIDEOS/<tema>/`: um vídeo por pasta, com `audios/`, `roteiro/`, `elementos/`, `trilha sonora/` e `renderizando/` (`_claude/00-estado.md` guarda onde parou).
- `planejamento/`: vídeos a produzir e vídeos para refazer em 16:9.
- **Git:** guarda o histórico local dos textos (skills, estados, páginas, mixagens); vídeos, áudios e imagens ficam fora dele (`.gitignore`), mas continuam na pasta e vão juntos para o Drive.
- **Documentos online da conta antiga** (manual, planos e página da linha de produção no Claude Docs) foram exportados para cá (`MANUAL-EDICAO-TELEORIENTACAO.md`, `planejamento/`, `CRIANDO-VIDEOS/SERVIÇOS NTS/01-linha-de-producao.md` e `linha-de-producao-online.html`). Na conta nova, a fonte é esta pasta; publique páginas novas a partir desses arquivos se a equipe precisar.
- `_arquivo/`: entregas antigas (primeira versão das skills, plano inicial), só como registro.

# Vídeos do Telessaúde Maranhão com o Claude Code

Repositório do fluxo de edição local dos vídeos do Telessaúde Maranhão (NTS-UFMA): skills do Claude Code (`.claude/skills/`), normas, ferramentas (`ferramentas/`), fontes, cores, efeitos sonoros e os textos de cada vídeo. O material grande (vídeos, áudios, renders) fica no Drive: veja [LINKS-DRIVE.md](LINKS-DRIVE.md).

Ponto de partida para o Claude: [CLAUDE.md](CLAUDE.md). Mapa das skills para pessoas: [GUIA-MOTION.md](GUIA-MOTION.md).

## 1. Instalar (Windows)

Use um caminho **sem acento** se puder (ex. `C:\projetos\CLAUDE-DESIGN`); as ferramentas já contornam acentos, mas fica mais simples.

| Ferramenta | Como instalar | Conferir |
| --- | --- | --- |
| Git | `winget install Git.Git` | `git --version` |
| ffmpeg (completo, com libx264 e loudnorm) | `winget install Gyan.FFmpeg` | `ffmpeg -version` |
| Python 3.10+ (com o lançador `py`) | `winget install Python.Python.3.12` | `py --version` (no Windows, `python` pode abrir a loja; use `py`) |
| Pacotes Python | `py -m pip install -r requirements.txt` | `py -c "import PIL, numpy, cv2, faster_whisper"` |
| Node 18+ | `winget install OpenJS.NodeJS.LTS` | `node -v` |
| Pacotes Node (Playwright) | `cd ferramentas` e `npm install` | `node ferramentas/teste-playwright.mjs` |
| Google Chrome | instalado normalmente | o Playwright usa `channel: 'chrome'` (não baixa navegador próprio) |
| Fontes | instale os arquivos de `fontes tipograficas/` no Windows (botão direito > Instalar para todos os usuários) | as páginas também carregam as fontes direto da pasta |
| Claude Code | app desktop do Claude (aba Code) ou `npm install -g @anthropic-ai/claude-code` | `claude --version` |

O faster-whisper baixa o modelo na primeira transcrição (precisa de internet nessa vez).

## 2. Clonar e completar o material

```powershell
git clone <url-do-repositório-privado> CLAUDE-DESIGN
```

Depois copie do Drive as pastas listadas em [LINKS-DRIVE.md](LINKS-DRIVE.md) para dentro do clone, com os mesmos nomes. Sem elas as skills funcionam, mas os vídeos em andamento não têm mídia para renderizar.

## 3. Abrir no Claude Code com outra conta

1. Abra o Claude Code (app desktop, aba Code, ou `claude` no terminal) e entre com a conta que vai usar.
2. Escolha a pasta do clone como pasta do projeto. O Claude lê o `CLAUDE.md` sozinho e as skills de `.claude/skills/` (`motion`, `telessaude`, `editar`, `prompts-flow`) aparecem automaticamente.
3. Primeira mensagem sugerida: "Confira se ffmpeg, py (Pillow, numpy, OpenCV, faster-whisper), Node e Playwright com Chrome estão funcionando." (é o checklist de `.claude/skills/motion/tecnico.md`).
4. Para continuar um vídeo: `/editar <nome do vídeo>`. Vídeo novo: `py ferramentas/novo_video.py "<pasta>" <TEMA>`.

A outra conta **não tem a memória da conta original**: tudo o que importa (gostos do usuário, ajustes do Windows, decisões) está nas skills e no `CLAUDE.md`. Regra nova que se repete vai para a skill, não para a memória.

## 4. O que fica fora do Git

- Material grande: [LINKS-DRIVE.md](LINKS-DRIVE.md).
- `node_modules/` (recriado por `npm install`), caches e `.claude/settings.local.json` (permissões locais).
- Documentos online de planejamento, no Claude Docs da conta original: "Vídeos para refazer na horizontal", "Vídeos novos a produzir" e a versão online do manual (link em `CLAUDE.md`). Compartilhe-os com a nova conta ou exporte em Markdown.
- `_arquivo/skills-entrega-original/`: primeira entrega das skills (14/11/2026), desatualizada; só registro. As skills em uso ficam em `.claude/skills/`.

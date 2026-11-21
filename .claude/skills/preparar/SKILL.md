---
name: preparar
description: Comando /preparar — primeira conversa num PC ou numa conta nova (ou depois de baixar a pasta do Drive). Confere e instala o ambiente (ffmpeg, Python e pacotes, Node, Playwright com Chrome, fontes), confere o material grande que vem do Drive e mostra onde cada vídeo parou, com o próximo passo e os documentos pendentes. Use quando o usuário digitar /preparar, disser que acabou de baixar ou clonar a pasta, que trocou de PC ou de conta, ou pedir para "preparar o ambiente".
---

# /preparar — deixar a máquina pronta e mostrar onde cada vídeo parou

Objetivo: depois de baixar a pasta do Drive num PC novo, com uma conta nova do Claude, **uma conversa** deixa tudo pronto para o usuário continuar a produção com `/editar <vídeo>`. Esta conta não tem a memória da conta antiga: tudo o que importa está no `CLAUDE.md`, nas skills e nos arquivos `00-estado.md`. Não procure contexto em outro lugar.

Responda em português. Faça as etapas em ordem e diga em uma linha o que está fazendo em cada uma.

## 1. Diagnóstico (só leitura)

Rode, a partir da raiz da pasta:

```powershell
py ferramentas/preparar.py
```

Se `py` não existir, o Python ainda não está instalado: pule para a etapa 2 com o Python primeiro e rode o diagnóstico depois. O script não instala nada; ele lista o que falta e o comando de cada correção.

## 2. Instalar o que faltar (pedir o ok antes)

Mostre a lista do que falta com os comandos e **peça o ok uma vez** para instalar tudo. Instalação de programa muda o sistema; não instale sem esse ok. Comandos (Windows, PowerShell):

| Falta | Comando |
| --- | --- |
| Python 3.10+ (com o lançador `py`) | `winget install Python.Python.3.12` |
| ffmpeg completo (libx264, loudnorm) | `winget install Gyan.FFmpeg` |
| Node 18+ | `winget install OpenJS.NodeJS.LTS` |
| Google Chrome | `winget install Google.Chrome` |
| Pacotes Python | `py -m pip install -r requirements.txt` |
| playwright-core | `npm install` dentro de `ferramentas/` (não baixa navegador: usa o Chrome instalado) |

Depois de instalar programas pelo `winget`, o PATH só vale num terminal novo: avise o usuário para fechar e reabrir o Claude Code (ou abrir um terminal novo) e então rodar o diagnóstico de novo. Se o `winget` não existir, mande o link oficial de cada programa.

**Fontes:** as páginas carregam as fontes direto de `biblioteca/marca/fontes/` (o motor `ferramentas/animar.mjs` injeta os `@font-face`), então não é preciso instalá-las no Windows para renderizar. Instalar ajuda só para ver as fontes em outros programas.

**Teste de ponta a ponta** (depois que o diagnóstico passar): `node ferramentas/teste-playwright.mjs` deve abrir o Chrome sem janela e gravar `ferramentas/teste.png`. Mostre a imagem ao usuário.

## 3. Material e biblioteca

A pasta vem inteira pelo Drive (`LINKS-DRIVE.md`), com vídeos, áudios e a `biblioteca/`. A parte 3 do diagnóstico mostra, vídeo a vídeo, se falta algum arquivo de mídia que as páginas e mixagens usam (download incompleto do Drive, `.zip` não extraído). Se faltar, peça ao usuário para baixar de novo só aquela pasta.

Rode `py ferramentas/novo_video.py "<pasta do vídeo>"` no vídeo que vai continuar: ele só cria as pastas de trabalho que faltarem (o Git não guarda pasta vazia) e não mexe em nada que exista.

A `biblioteca/` é a fonte geral (marca, trilhas, efeitos sonoros, personagens, vídeos publicados; catálogo em `biblioteca/README.md`). Nunca crie substitutos de elementos de marca (regra de `telessaude/SKILL.md`).

## 4. Onde cada vídeo parou

Monte uma tabela a partir do índice "Vídeos" do `CLAUDE.md` e da linha **Próximo passo** de cada `renderizando/_claude/00-estado.md` (o diagnóstico já imprime as duas). Inclua:

- os vídeos em produção, com o próximo passo e se a mídia dele já está no disco;
- os que dependem de validação da equipe (Amanda, Gyovanna), sem ação do Claude até o ok;
- as pendências fora dos vídeos: `planejamento/videos-novos-a-produzir.md` (Serviços do NTS, tutorial da Sofia) e `planejamento/videos-para-refazer-na-horizontal.md` (reconstruções em 16:9), e a linha de produção da série em `CRIANDO-VIDEOS/SERVIÇOS NTS/01-linha-de-producao.md`.

Termine recomendando **um** próximo passo concreto (normalmente o vídeo em produção com mídia completa) com o comando exato, por exemplo `/editar TELEDIAGNÓSTICO`, e lembre que `/clear` entre etapas não perde nada.

## 5. Documentos online

O manual online, a página da linha de produção e os planos no Claude Docs eram da conta antiga. Nesta conta, **a fonte é o repositório**: `MANUAL-EDICAO-TELEORIENTACAO.md`, `planejamento/` e `01-linha-de-producao.md`. Se o usuário quiser de novo uma página para a equipe, publique uma nova a partir do arquivo do repositório (ex.: `linha-de-producao-online.html`) e anote o link novo no próprio arquivo `.md` de origem e no `CLAUDE.md`.

## 6. Registrar

Se algo deste PC precisou de ajuste que vale para qualquer máquina (um programa novo, uma pegadinha do Windows), registre em `.claude/skills/motion/tecnico.md` e no `README.md`, não na memória. Faça commit só se o usuário pedir.

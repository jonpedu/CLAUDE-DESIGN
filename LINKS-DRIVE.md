# Levar o projeto pelo Google Drive

O projeto vai inteiro para o Drive: a pasta `CLAUDE-DESIGN/` com tudo dentro (skills, ferramentas, `biblioteca/`, vídeos, áudios, renders e a pasta oculta `.git`, que guarda o histórico de versões dos textos). No outro PC, baixe a pasta inteira e abra no Claude Code. Não há GitHub nem outro servidor.

| O quê | Link do Drive |
| --- | --- |
| Pasta `CLAUDE-DESIGN/` inteira | _preencher_ |

Tamanho em 21/11/2026: cerca de 8 GB, quase tudo vídeo (`CRIANDO-VIDEOS/` 3,4 GB, `biblioteca/videos-publicados/` 2,6 GB, `REFAZENDO-VIDEOS/` 1,3 GB).

## Subir (neste PC)

1. Feche o Claude Code e os programas que estejam usando arquivos da pasta.
2. Envie a pasta `CLAUDE-DESIGN/` inteira para o Drive (arrastar no drive.google.com ou pelo Google Drive para computador). Confira se a pasta `.git` foi junto: no Windows ela fica oculta (Explorador > Exibir > Itens ocultos).
3. Pode pular `ferramentas/node_modules/` (o `npm install` recria) e `ferramentas/_cache_busca/`.

## Baixar (no outro PC)

1. Baixe a pasta e extraia, de preferência num caminho **sem acento** (ex.: `C:\projetos\CLAUDE-DESIGN`). O Drive costuma dividir downloads grandes em vários `.zip`: extraia todos na mesma pasta.
2. Abra a pasta no Claude Code e rode **`/preparar`** (passo a passo no `README.md`).
3. Se algum arquivo de mídia não veio, a parte 3 de `py ferramentas/preparar.py` mostra, vídeo a vídeo, o que falta.

## Pelas partes, se preferir

Para levar só o necessário: a pasta sem `biblioteca/videos-publicados/` e sem os vídeos concluídos (AVC, IAM, `REFAZENDO-VIDEOS/hipertensao 1` e `2`) tem menos de 1 GB e já permite continuar a série Serviços do NTS. Os vídeos publicados só são necessários para analisar referências, reconstruir em 16:9 e citar vídeos anteriores.

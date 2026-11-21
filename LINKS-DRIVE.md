# Material grande (Google Drive, fora do Git)

O `.gitignore` deixa de fora vídeos, áudios, imagens, PDFs e renders. Eles ficam no Drive, numa pasta com a mesma estrutura do repositório. **Preencha os links abaixo antes de trocar de PC.**

## Como copiar para um clone novo

1. Baixe do Drive as pastas da tabela.
2. Copie-as para a raiz do clone, com os mesmos nomes, **sem substituir arquivos que já existem**: os textos do Git (estados, roteiros, páginas `.html`, mixagens `.json`) são os mais novos. No Explorador do Windows, escolha "Ignorar estes arquivos" quando ele perguntar.
3. Rode `py ferramentas/preparar.py` (ou `/preparar` no Claude Code). A parte 3 lista, vídeo a vídeo, os arquivos de mídia que as páginas e mixagens usam e que ainda faltam.

Para continuar só um vídeo, basta copiar a pasta dele, mais `biblioteca-trilhas/` se a mixagem usar uma trilha do banco.

## Pastas

| Pasta no clone | Conteúdo | Tamanho (20/11/2026) | Precisa para | Link do Drive |
| --- | --- | --- | --- | --- |
| `CRIANDO-VIDEOS/` | narração, clipes do Flow, régua, fechamento, recortes, prévias e finais dos vídeos novos (IAM, AVC, série Serviços do NTS) | 3,4 GB | continuar ou refazer esses vídeos | _preencher_ |
| `REFAZENDO-VIDEOS/` | Hipertensão partes 1 e 2 em 16:9 e a referência do Canva (`referencia/`) | 1,3 GB | reconstruir outros verticais em 16:9 (a parte 2 é o motor-base) | _preencher_ |
| `videos-referencia/` | vídeos aprovados usados como referência de estilo | 2,5 GB | analisar referências; reconstruções | _preencher_ |
| `biblioteca-trilhas/` (os `.mp3`; o `README.md` já está no Git) | 20 trilhas por clima | 67 MB | mixagem de qualquer vídeo | _preencher_ |
| `Uso marcas Telessaúde/` (imagens e PDFs) | logos e manual de uso da marca | < 1 MB | logos avulsos | _preencher_ |
| `analise-referencias/` (imagens) | quadros extraídos na análise das referências | — | só consulta | _preencher_ |

Já vêm no Git: `fontes tipograficas/`, `cores hex/`, `biblioteca-sfx/`, as skills, as normas, as ferramentas, `planejamento/` e os textos de trabalho de cada vídeo.

## Kit de marca

Régua do parceiro, logos e fechamento animado com som (ex.: `Intro Telessaude.mp4`, `Intro NTS e PETSAUDE - horizontal.mp4`) vêm sempre dentro de `elementos/` do próprio vídeo, também pelo Drive. Ainda falta o **fechamento horizontal só do Telessaúde**, pedido para as versões 16:9 da série Serviços do NTS.

---
name: editar
description: Comando /editar — retoma (ou começa) a edição de um vídeo a partir do arquivo de estado dele, faz uma etapa por vez e deixa o estado salvo para a próxima conversa. Use quando o usuário digitar /editar, com ou sem o nome/pasta do vídeo, ou pedir para "continuar o vídeo X" depois de um /clear.
---

# /editar — uma etapa por vez, com o estado em arquivo

Objetivo: o usuário pode dar `/clear` entre as etapas (conversa nova = menos tokens) sem perder nada, porque **tudo o que importa para continuar está no `00-estado.md` do vídeo**, não no histórico do chat.

## 1. Achar o vídeo

O Claude Code fica aberto na **raiz do projeto** (onde estão `CLAUDE.md`, `.claude/`, `ferramentas/`); o vídeo é escolhido pelo argumento, não pela pasta aberta. Se a sessão estiver aberta dentro da pasta de um vídeo, use esse vídeo, mas avise que o certo é abrir na raiz.

- **Nome ou pasta dado** (`/editar IAM`, `/editar CRIANDO-VIDEOS/DENGUE`): procure em `CRIANDO-VIDEOS/`, `REFAZENDO-VIDEOS/` e nas pastas de série uma pasta de vídeo com esse nome (sem diferenciar maiúsculas e acentos).
  - Achou, com `00-estado.md`: continue dele.
  - Achou, sem `00-estado.md` (vídeo antigo ou pasta que o usuário já montou): rode `novo_video.py` nela (só cria o que falta, não apaga nada) e comece pela etapa 1.
  - **Não achou:** é vídeo novo. Proponha o lugar (`CRIANDO-VIDEOS/<NOME>/`, ou a série que o usuário indicar) e **confirme antes de criar**. Depois rode `py ferramentas/novo_video.py "<pasta>" <NOME>`, diga onde colocar a narração, o roteiro e os elementos, e acrescente o vídeo ao índice "Vídeos" do `CLAUDE.md`.
- **Sem argumento** (`/editar`): liste os vídeos (índice "Vídeos" do `CLAUDE.md` + os `00-estado.md` encontrados) com a situação de cada um e pergunte qual, ou se é um vídeo novo e com que nome.

## 2. Ler só o necessário

1. O `00-estado.md` do vídeo (sempre, inteiro).
2. Se houver ajustes do editor de quadros ainda não aplicados (`renderizando/_claude/quadros/ajustes/<data-hora>/ajustes.json` mais novo que a última entrega registrada no estado), eles são a próxima tarefa: leia o JSON e as imagens de comparação e aplique (`motion/tecnico.md`, "Editor de quadros-chave").
3. Das skills, **só o que a etapa pede** (tabela abaixo). Não releia o estudo da edição inteiro nem vídeos antigos sem motivo.

| Etapa (de `telessaude/producao.md`; para outro cliente, a sub-skill dele) | Leia |
| --- | --- |
| 1. Conferir o pacote | `telessaude/organizacao.md` (checklist), `telessaude/SKILL.md` (régua e fechamento) |
| 2. Medir a narração | `motion/tecnico.md` (ferramentas) |
| 3. Mapa de cenas | `motion/metodo-referencia.md`, `motion/efeitos.md`, `telessaude/SKILL.md`, o formato (`formatos/`) e o tipo (`tipos/`) |
| 4. Decupar os takes | `motion/takes.md` |
| 5. Quadros-chave | `motion/tecnico.md` (quadros de prova, editor de quadros), `telessaude/formatos/` (área segura) |
| 6. Animar | `motion/tecnico.md`, `motion/principios.md` |
| 7–12. Finalização | `telessaude/producao.md` (etapa 2), `motion/som.md` |
| 13. Capa e extras | `telessaude/formatos/` (capa) |

## 3. Fazer a etapa

- Faça **uma etapa** (ou o pedido do usuário) e pare nos pontos de aprovação que as skills já definem (pacote confirmado, mapa de cenas, quadros-chave, prévia de áudio, versão para avaliação).
- Ao entregar uma versão, inclua o bloco de avaliação (`telessaude/producao.md`).

## 4. Salvar o estado (antes de terminar a resposta)

Atualize o `00-estado.md`:
- **Versão atual**, **final aprovado** e **próximo passo** (com o número da etapa e o que falta, em uma linha que outra conversa entenda sozinha);
- **Decisões deste vídeo**: o que o usuário decidiu nesta conversa e vale só para este vídeo (datado). Regra que vale para todos os vídeos vai para a skill certa, não para o estado;
- arquivos novos importantes (página da animação atual, mixagem atual).

Se a situação mudou, atualize também a linha do vídeo no índice "Vídeos" do `CLAUDE.md`.

Termine dizendo em uma linha o que foi feito e qual é o próximo passo, e lembre que dá para dar `/clear` e depois `/editar <vídeo>` para continuar.

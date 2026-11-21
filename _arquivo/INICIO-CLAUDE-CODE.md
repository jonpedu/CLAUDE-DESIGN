# Como começar no Claude Code

## A decisão

Use o repositório **fluxo-de-edicao** (Lucas Leite) como **construtor**, e não como fluxo pronto. Ele não edita vídeo: entrevista você, analisa suas referências e escreve as suas skills, partindo das 8 etapas e adaptando ao seu caso. Durante a entrevista, ele deve aproveitar o que já existe nesta pasta em vez de recriar:

| Já existe aqui | Vira, no fluxo dele |
| --- | --- |
| `skills/motion/` (princípios, efeitos, formatos, som, técnico) | **ofício**: regras gerais que as skills de etapa seguem |
| `.claude/skills/telessaude/` (marca + `tipos/`) + `MANUAL-EDICAO-TELEORIENTACAO.md` | **perfil** "telessaude": identidade comum e um arquivo por tipo de vídeo (teleorientação, campanha, institucional, registro) |
| `videos-referencia/` (vídeos aprovados) | material da **fase 3**: análise de referências → perfil "telessaude" |
| `skills/motion/estilos/` | presets de estilo opcionais, usados só quando pedidos |

## As 8 etapas, adaptadas a vídeos narrados e animados (sem apresentador)

| Etapa do vídeo | No seu caso |
| --- | --- |
| 1. iniciar | igual: pasta do vídeo, briefing, série (teleorientação ou outra), formato |
| 2. preparar | narração do AI Studio + WhisperX para tempo por palavra; roteiro só para grafia |
| 3. cortes | vira **decupagem e montagem de takes**: os clipes gerados (~10 s) são takes. Marcar os trechos úteis com tags (ação, expressão, boca), usar só partes, reusar trechos (ex.: personagem acenando) e sincronizar gestos e boca com a narração quando der. Regras em `skills/motion/takes.md` |
| 4. motion-mapa | igual e a mais importante: plano cronometrado usando o catálogo de efeitos e a estrutura da série |
| 5. assets | régua de marca, logos, ícones, fontes, imagens |
| 6. motion-render | animações em HTML/CSS/JS (HyperFrames, como no vídeo, ou o pipeline de `skills/motion/tecnico.md`) |
| 7. câmera | vira **reenquadramento e movimento das cenas**: corte 16:9 → 9:16 seguindo o rosto do personagem (YuNet), Ken Burns, push-in |
| 8. sfx | efeitos + trilha + mixagem em −14 LUFS |
| + entrega | legendas, render 9:16 e 16:9, capas, `.srt`, checagem da área segura |

## Primeira decisão da entrevista: onde você revisa

O Canva não importa arquivo de projeto (XML). Há dois caminhos:
- **Vídeo pronto:** o Claude renderiza e você pede ajustes pelo tempo ("0:23 troca o ícone"). É o mais simples para começar.
- **DaVinci Resolve (gratuito):** importa o XML com cortes, animações e sons em trilhas separadas, para ajuste fino à mão.

Sugestão: comece com o vídeo pronto e passe para o DaVinci se os ajustes por chat cansarem.

## Prompt para colar na primeira conversa

```
Leia o CLAUDE.md e o INICIO-CLAUDE-CODE.md desta pasta.
1. Copie a pasta skills/ para .claude/skills/ (se ainda não estiver lá).
2. Instale esta skill: https://github.com/LeiteZ/fluxo-de-edicao
3. Rode /fluxo-de-edicao. Na entrevista e na escrita das skills:
   - trate skills/motion como o ofício geral e não duplique o que já está lá; aponte para esses arquivos;
   - use .claude/skills/telessaude como perfil da marca (um arquivo por tipo de vídeo em tipos/) e MANUAL-EDICAO-TELEORIENTACAO.md como norma do tipo teleorientação;
   - adapte as 8 etapas como na tabela do INICIO-CLAUDE-CODE.md (vídeo narrado, sem apresentador);
   - na fase de referências, analise videos-referencia/ e crie um perfil "telessaude" com identidade comum
     e notas por série (teleorientação, campanhas, institucionais). O perfil é tendência, não regra:
     quero variação entre vídeos sem sair da identidade.
Comece verificando o ambiente (Python, FFmpeg, Node, Git, GPU) e me mostre o que falta antes de instalar.
```

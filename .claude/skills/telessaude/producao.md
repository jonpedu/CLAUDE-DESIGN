# Produção (papel do Claude)

Decidido em 15/11/2026: **o Claude faz o vídeo inteiro**, nas duas etapas que o usuário fazia antes:

1. **Montagem da base** (antes no Canva): compor as telas, os textos, as animações e as transições a partir dos elementos fornecidos.
2. **Finalização** (antes no Premiere Pro): régua, narração, trilha, efeitos sonoros, mixagem e exportação.

Entradas e saídas seguem `organizacao.md`. Elementos de marca e elementos visuais vêm do usuário (regra fixa em `SKILL.md`); o Claude compõe, anima e posiciona.

## Etapa 1 — Montagem da base

| Passo | O que fazer | Entrada |
| --- | --- | --- |
| 1. Conferir o pacote | listar o que existe em `PARTE N/` e apontar o que falta (checklist de `organizacao.md`) | todas as pastas |
| 2. Medir a narração | duração real, tempo por palavra, pausas; dividir em batidas | `audios/` |
| 3. Mapa de cenas | plano cronometrado (`motion/metodo-referencia.md`): para cada batida, tela, composição, efeito, texto exato, transição, som. Seguir o formato (`formatos/`) e o tipo (`tipos/`) | roteiro final, parecer |
| 4. Decupar os takes | clipes gerados (AI Studio/Flow) viram trechos com tags (`motion/takes.md`); rodar `ferramentas/bordas.py` para saber em que bordas cada clipe precisa ficar colado (margem fantasma) | `elementos/` |
| 5. Quadros-chave | 4–6 quadros em tamanho real (gancho, um cartão, alerta, chamada, fechamento) com a régua aplicada e uma cópia com a máscara de área segura → **aprovação do usuário**. Para ajustes de posição e tamanho, ofereça o **editor de quadros** (`motion/tecnico.md`): o usuário mexe direto na cena e salva um `ajustes.json` | — |
| 6. Animar | renderizar por cena (`motion/tecnico.md`): HTML/CSS + Playwright para texto e grafismos com as fontes da marca, ffmpeg/Python para composição | — |

Texto na tela: digitado pelo Claude com as fontes da marca, copiado exatamente do roteiro aprovado (e das correções do parecer). Personagens, ícones, cenas e imagens: só os de `elementos/`; o que faltar é pedido, não inventado.

## Etapa 2 — Finalização

| Passo | O que fazer | Entrada |
| --- | --- | --- |
| 7. Régua | sobrepor o PNG do parceiro certo, centralizado e encostado na base, sem alterar; se a largura não for a do vídeo, perguntar | PNG da régua |
| 8. Narração | faixa do AI Studio; silêncios internos > 0,8 s podem ir a 0,4 s; nunca cortar palavra | `audios/` |
| 9. Trilha | propor uma das candidatas e dizer por quê; ~11 dB abaixo da voz sob a fala e ~6 dB nas pausas (audível no celular; ver SKILL.md, Som), fades de 1 s | `trilha sonora/` |
| 10. Efeitos sonoros | sincronizar com os impactos (pop, flash, transição), sem encobrir a voz. **O áudio original dos clipes do Flow sai mudo na montagem**; trechos úteis dele (whoosh, pop, ambiente) podem ser extraídos e usados como efeito sonoro genérico, neste e em vídeos futuros (guardar em uma biblioteca de efeitos com nome descritivo). Outras fontes: a pasta de efeitos do usuário ou efeitos simples sintetizados | `renderizando/`, clipes do Flow |
| 11. Mixagem | −14 LUFS integrado, pico −1 dBTP | — |
| 12. Exportar | H.264 yuv420p, AAC 48 kHz, 30 fps; `renderizando/<TEMA> parte N.mp4`, sem sobrescrever | — |
| 13. Capa e extras | **capa sempre**: `renderizando/CAPA <TEMA> vN.png` (quadro do vídeo com a régua ou capa composta) e a mesma imagem como **primeiro quadro** do vídeo final, substituindo o quadro 0 (miniatura do WhatsApp; detalhes em `formatos/vertical.md`). Depois `.srt` e versão no outro formato, se pedidos | — |

Antes do render completo, além dos quadros-chave, entregar uma prévia curta de áudio (20–30 s com voz, trilha e um efeito) para aprovar o equilíbrio. Um render completo por pedido; ajustes por tempo ("0:23 troca o ícone") refazem só as cenas afetadas.

## Bloco de avaliação (toda entrega de versão ou parte)

Pedido do usuário (15/11/2026): ao final de cada versão, deixar **num bloco de código copiável** um modelo para a devolutiva dele. Não é descrição: só a lista dos motions, cada um com número, intervalo de tempo e um rótulo curto, e o espaço vazio depois dos dois-pontos. Ele responde "OK" ou com o comentário em cada linha.

```
mt1 [0:00–0:05] gancho:

mt2 [0:05–0:10] cena do cérebro:

geral:
```

**Uma linha vazia entre cada item** (pedido do usuário), para ele escrever embaixo.

A unidade e o prefixo mudam conforme o que divide melhor o vídeo: **`mt`** (motion) quando a avaliação é por animação ou efeito, **`cn`** (cena) quando é por cena; em vídeo complexo, motions menores dentro de cada cena. Diga no texto qual unidade foi usada. Tempos do vídeo final (m:ss), sem sobrepor.

## Arquivos de trabalho

Em `renderizando/_claude/`: plano cronometrado, quadros-chave, cenas renderizadas, máscara, prévias de áudio, `.srt`. O `.prproj` do Premiere, se existir, não é aberto nem alterado.

## Pipeline de finalização (ffmpeg)

- vídeo: `[base][regua]overlay=(W-w)/2:H-h` (régua com alfa, sem escala);
- áudio: voz + trilha com `sidechaincompress` ou volume fixo, efeitos com `adelay`, `amix`, `loudnorm=I=-14:TP=-1` em duas passadas;
- saída: `-c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -ar 48000 -movflags +faststart`.

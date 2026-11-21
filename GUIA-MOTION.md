# Guia de motion — mapa rápido

Este arquivo é o mapa para você. O conteúdo completo fica nas skills em `.claude/skills/`, que o Claude Code usa sozinho quando você pede um vídeo nesta pasta.

**Primeira vez:** as skills já estão em `.claude/skills/`, onde o Claude Code as encontra sozinho. Para instalar em outro PC, siga o `README.md`. A entrega original, desatualizada, ficou em `_arquivo/skills-entrega-original/`.

## Como está organizado

```
CLAUDE-DESIGN/
  CLAUDE.md                          contexto do projeto (o Claude Code lê ao abrir a pasta)
  MANUAL-EDICAO-TELEORIENTACAO.md    norma da série Telessaúde
  GUIA-MOTION.md                     este mapa
  .claude/skills/
    motion/                          SKILL GERAL (qualquer vídeo)
      SKILL.md                       regras de ouro, fluxo, checagem final
      principios.md                  12 princípios, tempos em frames, curvas
      efeitos.md                     catálogo de efeitos com nome
      metodo-referencia.md           usar uma referência sem copiar + plano cronometrado
      formatos.md                    9:16, 16:9, 4:5, 1:1, áreas seguras, capas
      som.md                         trilha, efeitos sonoros, mixagem
      tecnico.md                     pipeline local e regras de render
      fontes.md                      de onde veio cada ideia
      estilos/
        editorial-pastel-3d.md       preset do PDF TheLabVid
    telessaude/                      SUB-SKILL da marca Telessaúde (todo vídeo do Telessaúde)
      SKILL.md                       identidade: régua, fechamento, cor do tema, fontes, personagens, som
      cores.md                       paleta do portal (clara e escura) + tokens CSS
      fontes.md                      fontes da pasta "fontes tipograficas", usos e licenças
      organizacao.md                 pastas de cada vídeo (tema › parte › audios, roteiro, elementos…)
      producao.md                    papel do Claude: montar a base (antes Canva) e finalizar (antes Premiere)
      formatos/
        vertical.md                  9:16: área segura, composição em pilha, régua, capa
        horizontal.md                16:9: duas colunas, régua, miniatura, reconstrução de verticais
      tipos/
        teleorientacao.md            orientação de saúde (séries SUS Digital e PET-Saúde)
        campanha.md                  datas de saúde (Glaucoma, Novembro Azul…)
        institucional.md             projetos e resultados (Kits, Retrospectiva)
        registro.md                  filmagem de ações em campo (Tauá-Mirim)
  analise-referencias/               análise dos vídeos aprovados (relatório, folhas, scripts)
```

## Como pedir no Claude Code

- **Continuar um vídeo:** `/editar IAM` (ou só `/editar` para escolher). Faz uma etapa e salva o estado em `renderizando/_claude/00-estado.md`; entre etapas, `/clear` limpa a conversa sem perder nada.
- **Ajustar posição e tamanho pelo olho:** `node ferramentas/editor.mjs "<página .html>" "t1,t2"` abre o editor de quadros; salve e avise no chat.
- **Vídeo do Telessaúde:** "Edita o vídeo da pasta `videos/hipertensao`, teleorientação, vertical." (tipo: teleorientação, campanha, institucional, registro; formato: vertical ou horizontal)
- **Reconstruir em horizontal:** "Reconstrói em 16:9 o vídeo `videos-referencia/.../Hipertensão.mp4`." Se tiver os elementos do Canva exportados, mande junto: o resultado fica melhor.
- **Vídeo fora da série:** "Faz um vídeo 1:1 de 20 s para o LinkedIn, estilo editorial pastel 3D, com as cores da marca X."
- **Ajuste fino com nomes de efeito:** "Na cena 3, troca o `pop-in` por `card-rise` e coloca `check-pop` em cada item."
- **Nova referência:** "Analisa este vídeo e cria um preset em `estilos/` com o método de referência."
- **Novo tipo de vídeo do Telessaúde:** "Cria um tipo novo em `telessaude/tipos/` para os vídeos de X."
- **Novo cliente ou marca:** "Cria uma sub-skill para a marca X copiando a do Telessaúde."

## 10 efeitos para ter na ponta da língua

| Nome | O que é |
| --- | --- |
| `pop-in` | aparece crescendo com uma sobra leve |
| `type-rise` | texto sobe de baixo, saindo do desfocado |
| `card-rise` | cartão sobe e cobre a cena anterior |
| `stagger-in` | itens entram um depois do outro |
| `pill-expand` | pílula pequena estica e vira barra de título |
| `check-pop` | círculo + check desenhado |
| `contador` | número que conta até o valor |
| `alerta-pulso` | selo pulsa 1–2 vezes, sem piscar |
| `occlusion-wipe` | objeto atravessa a tela e revela a próxima cena |
| `type-punch` | texto entra enorme e assenta pequeno e nítido no final |

O catálogo completo, com durações e receitas, está em `efeitos.md`.

## Como melhorar com o tempo

- Gostou de um vídeo? Peça para analisar e criar um preset em `estilos/`.
- Corrigiu algo que o Claude errou mais de uma vez? Peça para acrescentar a regra na skill certa: geral se vale para tudo, `telessaude/SKILL.md` se vale para a marca toda, `telessaude/tipos/` se é só de um tipo de vídeo.
- De vez em quando, revise `fontes.md` para lembrar o que ainda falta testar.

# Guia de motion — mapa rápido

Este arquivo é o mapa para você. O conteúdo completo fica nas skills em `.claude/skills/`, que o Claude Code usa sozinho quando você pede um vídeo nesta pasta.

**Primeira vez:** as skills já estão em `.claude/skills/`, onde o Claude Code as encontra sozinho. Para instalar em outro PC, siga o `README.md`. A entrega original, desatualizada, ficou em `_arquivo/skills-entrega-original/`.

## Como está organizado

```
CLAUDE-DESIGN/
  CLAUDE.md                          contexto do projeto (o Claude Code lê ao abrir a pasta)
  README.md                          instalação num PC novo e abertura com outra conta
  LINKS-DRIVE.md                     links do material grande (vídeos, áudios, imagens), fora do Git
  MANUAL-EDICAO-TELEORIENTACAO.md    norma da série Telessaúde
  GUIA-MOTION.md                     este mapa
  planejamento/                      planos: vídeos novos a produzir e vídeos para refazer na horizontal
  CRIANDO-VIDEOS/                    vídeos novos (cada um com renderizando/_claude/00-estado.md)
  REFAZENDO-VIDEOS/                  reconstruções em 16:9 de verticais já publicados
  ferramentas/                       motor e scripts (animar.mjs, mixar.py, preparar.py, novo_video.py…)
  biblioteca/                        FONTE GERAL: marca (réguas, fechamentos, logos, fontes, cores), trilhas,
                                     efeitos sonoros, personagens do Flow, mapas, vídeos publicados (README = catálogo)
  _arquivo/                          entregas antigas, só registro
  .claude/skills/
    preparar/                        /preparar: primeira conversa num PC ou numa conta nova
    editar/                          /editar: retoma um vídeo pelo 00-estado.md, uma etapa por vez
    prompts-flow/                    prompts do Google Flow para as cenas com personagens
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
      fontes.md                      fontes de `biblioteca/marca/fontes/`, usos e licenças
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

- **PC ou conta nova:** `/preparar`. Confere e instala o ambiente, confere o material do Drive e mostra onde cada vídeo parou.
- **Continuar um vídeo:** `/editar TELEDIAGNÓSTICO` (ou só `/editar` para escolher). Faz uma etapa e salva o estado em `renderizando/_claude/00-estado.md`; entre etapas, `/clear` limpa a conversa sem perder nada.
- **Ajustar posição e tamanho pelo olho:** `node ferramentas/editor.mjs "<página .html>" "t1,t2"` abre o editor de quadros; salve e avise no chat.
- **Vídeo novo do Telessaúde:** `/editar DENGUE` (o Claude propõe a pasta em `CRIANDO-VIDEOS/`, cria a estrutura e pede o pacote) e diga o tipo e o formato: teleorientação, campanha, institucional ou registro; vertical ou horizontal.
- **Ver o que já existe:** "O que tem na biblioteca para um vídeo de dengue?" (ou `py ferramentas/da_biblioteca.py --listar dengue`).
- **Prompts do Flow:** "Faz os prompts do Flow do roteiro de teleconsultoria."
- **Reconstruir em horizontal:** "Reconstrói em 16:9 a Diabetes parte 1" (lista em `planejamento/videos-para-refazer-na-horizontal.md`; pasta `REFAZENDO-VIDEOS/<tema>/`). Mande junto as páginas do Canva exportadas em PNG: o resultado fica melhor.
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

# Fontes das ideias desta skill

Notas de 14/11/2026 sobre o material que o usuário reuniu. Serve para saber de onde veio cada regra e o que vale aprofundar.

| Fonte | O que oferece | O que entrou aqui |
| --- | --- | --- |
| PDF "Gemini Omni Flash – Premium Motion Editorial Reference Guide" (TheLabVid) | análise quadro a quadro de um vídeo 9:16 pastel 3D, regras de estilo e um método em que o Claude planeja antes de escrever o prompt | `estilos/editorial-pastel-3d.md` inteiro; o princípio "referência = como, conteúdo do usuário = o quê"; plano cronometrado; checagem do final; transições guiadas por objeto; mapa de micro-sons |
| Curso "Motion que Vende" (Leandro Silva) | motion com IA sem After Effects; 5 skills (briefing, referência, narração, roteiro, áudio) que fazem perguntas antes de gerar | fluxo briefing → referência → narração → roteiro cena a cena → vídeo → som; "pedido com direção" (público, referência, ritmo, o que aparece em cada cena); números que crescem no ritmo da fala; uma tela por frase; fechar com logo e CTA; versão 16:9 além da 9:16 |
| Curso "Cápsula Motion" (Levi Lab) | pasta para VS Code com Claude Code; 28 animações prontas (contagem de número, celular com notificação, gráfico, conversa, recibo, "virada"), biblioteca de efeitos sonoros, estilos de personagem (3D, papel recortado, blocos) | efeitos `contador` e `notificacao`; a ideia de biblioteca de efeitos nomeados com prévia; começar de uma ideia em uma frase; ajustar uma coisa por vez |
| Skill "motion" compartilhada em perfil (20 itens) | 12 princípios da animação + 8 leis de UX, pensada para animação de interface | os 12 princípios, adaptados para vídeo com tempos em frames; das leis de UX ficaram Hick, Miller, Doherty, Jakob e frequência; Fitts, área de clique e Postel ficaram de fora por serem de interface clicável |
| Áreas seguras (valores publicados pela Meta para Reels e pelo Google para Shorts) | margens de topo, base e laterais em 1080 × 1920 | tabela de `formatos.md` |

Não foi possível ler: o vídeo do YouTube (W7E7Ln0z6aY) e a página guipaulino.app/desenho. Se tiverem algo útil, resuma o principal e acrescente aqui.

## Ideias para aprofundar

- Montar uma biblioteca local de prévias: um MP4 curto de cada efeito do catálogo, gerado uma vez, para escolher pelo olho.
- Criar novos presets em `estilos/` a cada referência de que o usuário gostar, sempre no formato de `editorial-pastel-3d.md`.
- Estilos de personagem citados no Levi Lab (papel recortado, blocos de montar) podem virar presets quando houver uma referência concreta.

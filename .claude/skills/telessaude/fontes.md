# Fontes do Telessaúde

Arquivos entregues pelo usuário em `biblioteca/marca/fontes/` (raiz do projeto), em 15/11/2026. Use sempre estes arquivos no render (`@font-face` no HTML, `fontfile=` no ffmpeg); não dependa das fontes instaladas no Windows.

| Família | Arquivos | Licença | Uso |
| --- | --- | --- | --- |
| **Poppins** | `Poppins/Poppins-*.ttf` (Thin a Black, com itálicos) | SIL OFL | voz principal: títulos, palavras-chave, textos |
| **Exo 2** | `Exo_2/static/Exo2-*.ttf` + variável | SIL OFL | apoio tecnológico; parecida com o "TELESSAÚDE" do logo (o logo vem sempre em arquivo) |
| **Inter** | `Inter/static/Inter_18pt|24pt|28pt-*.ttf` + variável | SIL OFL | texto pequeno e dados: créditos, fontes de dados, gráficos (use 18pt para tamanhos pequenos, 28pt para grandes) |
| **Glacial Indifference** | `glacial-indifference/GlacialIndifference-Regular.otf`, `-Bold.otf` | SIL OFL | linha leve geométrica, alternativa à Poppins Light; só Regular e Bold, sem itálico |
| **Computer Says No** | `computer-says-no.otf/computer-says-no.otf` | CC BY-SA 3.0 (Christian Munk, FontStruct) | a fonte "Computer": texto técnico, espaçado, estilo monoespaçado (ex.: "Glicemia em jejum") |
| **Bebas Neue** | `Bebas_Neue/BebasNeue-Regular.ttf` (só Regular, só maiúsculas) | SIL OFL | a condensada dos **números grandes** e títulos curtos de impacto (Retrospectiva, Kits, contadores); entregue em 16/11/2026 |

## Regras

- **Combinação preferida:** Poppins + uma de apoio, além do logo (que é arquivo). É tendência, não limite (decisão do usuário, 16/11/2026): mais famílias ou outra base podem entrar quando houver motivo claro (tema, tom, hierarquia) e o usuário aprovar. Ao propor, diga por que cada família está ali.
- **Computer Says No** tem licença CC BY-SA 3.0, que pede **atribuição** ao autor. Antes de usá-la num vídeo publicado, confirme com o usuário como a equipe faz o crédito (descrição do post, por exemplo).
- Números grandes e contadores: **Bebas Neue**. Ela não tem minúsculas nem negrito; para número com texto corrido ao lado, combine com Poppins.
- Fonte exclusiva do Canva sem arquivo: sugerir a alternativa livre mais próxima.
- **Fontes novas:** o Claude pode pesquisar e propor outras (regra 11 de `motion/SKILL.md`), por exemplo uma display para o título de uma campanha. A Poppins é a base preferida; outra fonte pode entrar como apoio, destaque ou até substituí-la, com motivo e aprovação do usuário. Depois de baixada, a fonte ganha uma linha na tabela acima.

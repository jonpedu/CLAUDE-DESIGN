# Formato: horizontal 16:9

YouTube (vídeo), apresentações, telas em eventos e salas de espera. Referências horizontais: a **reconstrução feita pelo usuário no Canva** (Hipertensão parte 1, PET-Saúde; padrões na seção de reconstrução, no fim) e a **primeira reconstrução aprovada feita pelo Claude**, a Hipertensão parte 2 (15/11/2026; estudo completo em `REFAZENDO-VIDEOS/hipertensao 2/Hipertensão parte 2 - estudo da edição.md`, fonte `renderizando/_claude/animacao/hipertensao2_h.html`, que serve de base de motor para as próximas). As demais regras traduzem a identidade do vertical para 16:9. Quando o usuário mandar outros vídeos horizontais aprovados, analise-os (`motion/metodo-referencia.md`) e atualize este arquivo. Aplique junto com `telessaude/SKILL.md` e o arquivo do tipo em `tipos/`.

Há dois casos: **vídeo novo horizontal** (pensado em 16:9 desde o início) e **reconstrução** de um vídeo vertical já publicado (demanda existente, seção no fim; **só quando o usuário pedir**; a primeira foi a Hipertensão parte 2, em 15/11/2026). Versões horizontais ficam em `<SÉRIE>/0. Videos Horizontais/` (ver `organizacao.md`).

## Tela

- 1920 × 1080, 30 fps.
- **Área segura:** margem de 96 px em todos os lados (x 96–1824, y 96–984).
- **Distribuição pela cena (gosto do usuário, 15/11/2026):** não é uma margem fixa. O que ele não quer é conteúdo jogado nas extremidades esquerda e direita com o meio vazio. Distribua os blocos pela cena inteira, com o peso visual equilibrado em torno do centro e espaços entre blocos parecidos. Encostar na borda só quando for intencional (cartão de borda, faixa, personagem grande cortado pela base). Na Hipertensão parte 2, a referência que funcionou foi manter texto e ilustrações por volta de x 200–1720. No YouTube, nada importante no canto inferior direito durante os últimos 20 s, onde entram as telas finais, se forem usadas.
- Fundo e cenário usam a tela toda.

## Composição

A largura é a grande diferença: no vertical cabe um bloco por tela; no horizontal cabem dois lado a lado.

- **Duas colunas** como padrão: personagem num terço (esquerdo ou direito) e texto/cartões nos outros dois terços. Alterne o lado entre blocos para dar ritmo, sem trocar a cada tela.
- **Listas em linha:** até 4 itens lado a lado em cartões (`stagger-in` da esquerda para a direita) no lugar da lista empilhada.
- **Diálogo entre dois personagens:** um em cada lado, conversa natural; o texto da fala aparece do lado de quem fala.
- **Título do tema:** no terço superior ou na coluna de texto, nunca encostado na borda. Sílabas empilhadas ("HAN/SE/NÍA/SE") viram palavra inteira grande, ou sílabas lado a lado.
- **Cenas ilustradas completas** (quintal, rua, UBS) funcionam melhor aqui que no vertical: use-as como fundo com texto numa caixa clara.
- Densidade igual ao vertical: no máximo 2 elementos novos por vez, um elemento novo a cada ~2 s.

## Tamanhos de texto (manual)

| Uso | Tamanho |
| --- | --- |
| Título do tema | 64–72 px |
| Texto de apoio | 40–48 px |
| Legenda | 38–44 px, terço inferior, centralizada, até 42 caracteres por linha |
| Créditos e referências | 26–30 px |

## Régua e fechamento

- **Régua como ilha (decisão do usuário, 15/11/2026):** no horizontal, a régua não precisa ir de ponta a ponta. Use o PNG entregue para o vídeo (pode ser o mesmo de 1080 px do vertical) como uma **ilha branca centralizada e encostada na base**, com os cantos de cima arredondados, como no exemplo do usuário (`REFAZENDO-VIDEOS/hipertensao 2/exemplo de uso da regua de marcas.png`, que vale só pela ilha; a faixa azul e os textos laterais são de outra peça). **Pode redimensionar proporcionalmente** conforme o layout pedir; não esticar, recolorir nem trocar logos. Qual PNG usar continua sendo confirmado com o usuário em todo vídeo.
- No horizontal a base não é coberta por botões: a ilha pode ser mais baixa e o conteúdo usa a altura restante.
- Fechamento: logo animado centralizado; assinaturas de parceiros em linha, lado a lado, com fios separadores verticais. O logo animado vertical (1080×1920, fundo branco) pode ser adaptado: centralizado no 16:9 sobre fundo branco, sem alterar o logo.

## Capa (miniatura do YouTube)

1280 × 720, título grande (até 4–5 palavras) num lado e personagem ou ícone do tema no outro, logo pequeno; nada importante no canto inferior direito (duração do vídeo).

Como no vertical, a capa também entra como **primeiro quadro** do vídeo final (miniatura do WhatsApp) e é salva em `renderizando/` como sugestão; regras em `vertical.md`, seção Capa.

## Reconstrução de vertical para horizontal

Objetivo: o vídeo horizontal deve parecer feito para 16:9, com o mesmo áudio, o mesmo texto e o mesmo tempo do vertical. **Nunca recortar o vertical** (perde-se 2/3 da imagem) e **nunca esticar**.

### Como o usuário fez à mão (referência)

`REFAZENDO-VIDEOS/referencia/`: o vertical (`Hipertensão PET SAUDE parte 1.mp4`), a versão horizontal que o usuário montou no Canva (`… - horinzontal.mp4`) e a capa 16:9 (`CAPA.png`). Analisado em 15/11/2026. Padrões observados, que servem de tendência (não regra) para as próximas reconstruções:

- **Remontar, não adaptar:** mesmos elementos (ilustrações, ícones, textos com a mesma grafia e os mesmos destaques) e mesmo áudio, reposicionados para 16:9. Nada do quadro vertical é recortado em bloco.
- **Duas colunas:** texto de um lado, ilustração do outro, alternando o lado ao longo do vídeo ("Você sabia?" com o balão à esquerda; "Hipertensão arterial" com o coração à esquerda). Telas de fundo cheio (azul, vermelho, cenário ilustrado) mantêm o fundo e só redistribuem os elementos.
- **Telas vizinhas no mesmo quadro:** o que no vertical eram telas em sequência vira um quadro com dois blocos — "Quando a força do sangue…" com a gota à esquerda e "Pressão alta" com o medidor à direita; o cartão "14/9 ou 140/90" ao lado da cena da aferição; "Você acha que a pressão alta é rara?" ao lado de "3 em 10 adultos".
- **Cartão de título encostado na borda:** caixa com contorno fino na cor do tema, saindo da borda lateral da tela, com cantos arredondados só do lado de dentro, levando o título curto ("PRESSÃO ALTA", "A PRESSÃO ALTA DÁ PRA CONTROLAR"). É um elemento novo, que não existe no vertical: usar para dar estrutura às telas de fundo branco.
- **Ilustração grande:** o personagem ou objeto ocupa quase a altura toda da sua coluna; o texto fica centralizado verticalmente na coluna de texto.
- **Cenas ilustradas 9:16** (o corpo com a lupa) viram fundo esmaecido atrás de outro elemento, ou são estendidas para os lados.
- **Capa:** coração à esquerda e título em duas linhas à direita, sobre o mesmo fundo vermelho em degradê radial do vertical.
- **Fechamento:** o mesmo logo centralizado do vertical.
- **Régua:** essa versão saiu **sem régua**. Ainda não está decidido se foi de propósito: pergunte antes de uma reconstrução. Se tiver régua, ela precisa da versão 16:9 entregue pelo usuário.

Ordem de preferência:

1. **Recompor a partir dos elementos originais.** Pedir ao usuário, **logo na conferência do pacote**, a exportação dos elementos do projeto do Canva **separados um a um** em PNG transparente (personagens, ícones, objetos; textos; trilha e narração separadas, se houver). Na Hipertensão parte 2 eles só chegaram no meio do trabalho e resolveram de uma vez qualidade, recortes ruins e liberdade de animar cada peça (`ferramentas/componentes.py` separa cada folha em camadas). Remontar cada tela com distribuição pela cena inteira.
2. **Recompor a partir do MP4 publicado**, quando não houver elementos:
   - **Som do fechamento (devolutiva da Hipertensão parte 2, 15/11/2026):** o som de logo que vem no áudio do vídeo-base pode estar **desatualizado**. Use sempre o som do arquivo de intro/fechamento entregue pelo usuário (ex.: `Intro NTS e PETSAUDE - horizontal.mp4`): corte o áudio-base logo depois da última palavra (`"narracao": {"ate": ...}` no `mixar.py`) e entre com o áudio da intro (`fim_audio`, com `fade_in`) uns 0,3 s **antes** do corte visual, para o som do fechamento invadir o fim da última cena; o vídeo da intro segue sincronizado com esse áudio. A trilha não pode parar seco junto com a narração: se a música estiver no pacote, alinhe-a ao áudio-base (correlação cruzada; na Hipertensão parte 2 o atraso era 0,021 s e o nível ≈ −24 dB) e prolongue só o final dela, cruzando com o som do fechamento.
   - **Áudio:** extrair do MP4 e usar como está, com narração, trilha e efeitos (decisão do usuário, 15/11/2026: não mexer no que já foi feito). Ele define o tempo de tudo. Efeitos novos podem entrar por cima quando reforçarem a fala. Se a trilha precisar ser remixada, seguir o padrão do vertical de teleorientação (−11 dB, ducking de 5 dB). Se for preciso mexer na trilha, separar voz e música localmente (Demucs ou UVR MDX-Net). O repositório rea-video foi avaliado em 15/11/2026 e não foi adotado: serve para planos filmados ou gerados por IA e não faz a troca de formato.
   - **Mapa do vídeo:** gerar a folha de contato e a lista de telas com tempos (`analise-referencias/scripts/extrair.py`); cada mudança de tela vira uma linha do plano cronometrado.
   - **Textos:** redigitar com as fontes da marca, copiando a grafia exata do vídeo (conferir contra o roteiro, se existir).
   - **Personagens e ícones:** recortar dos quadros. O fundo branco das referências facilita o recorte (chave de branco ou remoção de fundo); conferir as bordas em tamanho real. Pose que não existir em nenhum quadro não é inventada: reusar outra pose ou gerar nova cena com o mesmo personagem.
   - **Elementos cortados pela borda da tela original** (frutas, prateleira, legumes que saíam do quadro vertical): nunca soltos no meio da cena, porque o corte reto vira uma "borda fantasma" (devolutiva do usuário, 15/11/2026). Coloque-os num **quadro** (div com cantos arredondados, `overflow: hidden`, fundo claro com uma leve cor do tema) e deixe o lado cortado passar da borda do quadro, para o corte sumir.
   - **PNG transparente do Canva** (`paginas em png/extra/`, 1620×2880): quando vier, tem prioridade sobre qualquer recorte por cor; `ferramentas/componentes.py` usa a transparência dele direto.
   - **Cenas ilustradas completas em 9:16:** estender as laterais (fundo da identidade, extensão por IA com aprovação do usuário) ou usá-las numa moldura dentro do layout.
3. **Versão rápida (último caso, só com aprovação):** o vertical inteiro numa coluna central sobre fundo da identidade, com o título do tema e o logo nas laterais. Nunca com o próprio vídeo desfocado e ampliado ao fundo.

Antes do render completo, mostrar 4–6 quadros-chave horizontais lado a lado com o quadro vertical correspondente, para o usuário aprovar a tradução do layout.

# Manual de Edição — Vídeos de Teleorientação Telessaúde MA

Versão de 15/11/2026 (decisões sobre vinheta, duração, legenda, fechamento, transições, régua, área segura e organização de pastas) · versão online (editável, sincronizada em 15/11/2026): https://claude.ai/artifact/47ZcX6jxepE9TGjvvcCH22

Este manual define como todo vídeo de teleorientação do Telessaúde Maranhão é editado, para que cada peça saia com a mesma identidade, duração e qualidade, seja quem for o editor, inclusive o Claude.

## 1. Objetivo e escopo

- **Produto:** vídeos de teleorientação em saúde, com duração definida pela narração, publicados no YouTube (vídeo e Shorts) e no Instagram (Reels) do Telessaúde Maranhão.
- **Quem edita:** o Claude faz o vídeo inteiro a partir dos materiais fornecidos pela equipe: monta a base (antes feita no Canva) e finaliza (antes feita no Premiere). A equipe continua responsável por roteiro, narração, cenas geradas, elementos visuais, elementos de marca e revisão técnica.
- **Elementos de marca:** régua, logos, logo animado, som de logo e assinaturas são sempre fornecidos pela equipe. O editor não cria nem altera esses elementos; só os posiciona.
- **O que o manual cobre:** especificações técnicas, materiais de entrada, estrutura de tempo, identidade visual, grafismos, textos na tela, áudio, regras por plataforma, cuidados com conteúdo de saúde e o fluxo de aprovação.
- **Como usar:** as regras marcadas como **obrigatório** valem para todo vídeo. As marcadas como **padrão** podem mudar quando o roteiro pedir, desde que a mudança seja registrada no pedido de edição.
- **Fora do escopo:** criação de roteiro, geração de narração e geração de cenas com personagens.

## 2. Especificações técnicas (obrigatório)

O formato é definido por vídeo: vertical 9:16 (Reels e Shorts) e/ou horizontal 16:9 (YouTube). Quando saírem os dois, um é o principal e o outro é recomposto, nunca só recortado.

| Item | Vertical 9:16 | Horizontal 16:9 |
| --- | --- | --- |
| Resolução | 1080 × 1920 px | 1920 × 1080 px |
| Taxa de quadros | 30 fps constante | 30 fps constante |
| Vídeo | H.264 High, yuv420p, CRF 18 | H.264 High, yuv420p, CRF 18 |
| Áudio | AAC 48 kHz, estéreo, 192 kbps | AAC 48 kHz, estéreo, 192 kbps |
| Volume final | −14 LUFS integrado, pico máximo −1 dBTP | −14 LUFS integrado, pico máximo −1 dBTP |
| Duração | livre: a narração define; temas longos podem ser divididos em parte 1 e parte 2 | igual à vertical |
| Contêiner | MP4 (faststart) | MP4 (faststart) |

**Nome do arquivo:** `<TEMA> parte <N>.mp4`, na pasta `renderizando/` do vídeo (ex.: `DENGUE parte 1.mp4`). Um arquivo existente nunca é sobrescrito; revisões recebem ` - v2`, ` - v3`.

**Capa:** `CAPA.png` na pasta `renderizando/`, feita com os elementos da equipe.

## 3. Materiais de entrada (obrigatório)

Cada vídeo começa com um pacote completo. A edição só começa quando os itens obrigatórios estiverem lá.

**Organização das pastas** (igual à do Drive da equipe):

```
<SÉRIE>/                          ex.: PET SAUDE
  0. Videos Horizontais/          versões 16:9, mesma estrutura por tema
  <TEMA>/                         ex.: DENGUE
    PARTE 1/
      audios/                     narração
      roteiro/                    roteiro final, roteiro original, parecer técnico
      elementos/                  personagens, ícones, cenas geradas, imagens
      trilha sonora/              trilhas candidatas
      renderizando/               régua, efeitos sonoros, capa e vídeo final
    PARTE 2/
```

As pastas `audios/`, `roteiro/`, `elementos/` e `trilha sonora/` são de entrada: o editor só lê. Arquivos de trabalho do Claude ficam em `renderizando/_claude/`.

| Item | Origem | Formato aceito | Obrigatório |
| --- | --- | --- | --- |
| Roteiro final, idêntico ao narrado, dividido por cena | equipe | .txt ou .docx | sim |
| Narração | Google AI Studio | .wav (preferência) ou .mp3, sem música | sim |
| Cenas com personagens | Google Flow | .mp4, maior resolução disponível, sem marca d'água | sim |
| Imagens de apoio, ícones, ilustrações | equipe / banco licenciado | .png com fundo transparente ou .jpg | quando houver |
| Logos e assinaturas institucionais | kit de marca | .svg ou .png transparente | sim (uma vez, fica no kit) |
| Fontes da identidade | kit de marca | .ttf ou .otf | sim (uma vez, fica no kit) |
| Trilha sonora | biblioteca licenciada | .wav ou .mp3 | quando houver |
| Referências técnicas do conteúdo | revisor técnico | texto com link | sim |

**Sempre presentes:** a régua de marca pronta do parceiro do vídeo (PNG transparente, 1080 px de largura para o 9:16 e 1920 px para o 16:9) e o roteiro original. O roteiro original e o parecer técnico servem para conferir o sentido; o texto na tela segue o roteiro final narrado.

**Nomes dos arquivos de cena:** prefixo com o número da cena, para que a ordem seja óbvia: `01_cena_abertura.mp4`, `02_cena_personagem.mp4`.

**Cenas geradas são takes:** os clipes com personagens (cerca de 10 s, gerados no Google AI Studio/Flow) não são cenas finalizadas. O editor usa só os trechos úteis, de qualquer parte do clipe, e pode repetir um trecho no mesmo vídeo (por exemplo, o personagem acenando ou com uma expressão específica), variando enquadramento ou momento para não parecer repetição. Como a narração é separada, gestos e boca são sincronizados com a fala sempre que possível; nas pausas, entram trechos com a boca fechada. Regras detalhadas em `skills/motion/takes.md`.

**Cenas geradas em vídeo vertical:** se a cena vier em 16:9, o editor recorta para 9:16 mantendo o rosto ou a ação principal no centro. Quando o recorte cortar algo importante, a cena entra reduzida sobre um fundo da identidade. Sempre que possível, gere as cenas já na proporção do formato principal.

**Estilo das cenas geradas:** pedir no AI Studio/Flow **motion design + flat design**, fundo claro e liso, o mesmo personagem de referência e a proporção do formato final, sem texto nem logo dentro da cena.

**Roteiro com marcações:** indique entre colchetes o que deve aparecer na tela em cada trecho, por exemplo `[texto: 3 sinais de alerta]`, `[imagem: 03_icone_coracao.png]`, `[cena: 02]`. As palavras-chave da tela são tiradas deste texto.

## 4. Estrutura do vídeo (padrão)

Todo vídeo segue os blocos abaixo; o tempo de cada um acompanha a narração, mas a ordem não muda.

| Bloco | Tempo típico | Conteúdo |
| --- | --- | --- |
| Gancho | primeiros 5–6 s | personagem + chamada regional, pergunta ou dado que prende |
| Nome e definição | ~10–20% do vídeo | nome do tema em destaque + uma linha de definição |
| Orientação | ~50–60% | 2 a 4 ideias: sintomas, causas, transmissão, exames, cuidados |
| Alerta | ~10% | sinais de gravidade e onde procurar atendimento |
| Chamada | ~10–15% | "Procure o posto de saúde / UBS", app Meu SUS Digital quando couber |
| Fechamento | 3–5 s | logo animado (+ assinaturas de parceiros) |

- **Sem vinheta de abertura:** o vídeo começa direto no gancho, com a narração desde o primeiro segundo. A marca aparece na régua (o vídeo inteiro) e no fechamento.
- **Duração livre:** o bloco de orientação estica ou encolhe com a narração.
- **Alerta:** obrigatório quando o tema tiver sinais de gravidade; nos demais, vira uma chamada para a UBS.
- **Fechamento:** só o logo animado fornecido pela equipe, com as assinaturas de parceiros quando houver.

## 5. Identidade visual (obrigatório)

A identidade segue o guia de cores do portal do Telessaúde e as fontes entregues pela equipe (15/11/2026). Logos, réguas, logo animado e som de logo ainda precisam vir da equipe (seção 12).

### Paleta

Base: o guia de cores do portal. **O azul da marca é o padrão** e aparece em todo vídeo; os tons de azul podem variar dentro da família da marca.

| Papel | Nome | HEX | Uso |
| --- | --- | --- | --- |
| Primária | Primary | #365DCC | títulos, barras, botões, ícones da marca |
| Primária (variações) | Primary Hover / Pressed | #3052B4 / #29479B | segundo tom de azul, degradês, texto azul sobre claro |
| Azul-marinho | Brand Strong | #1C306A | fundos escuros institucionais, texto forte |
| Azul-claro | Primary Subtle | #E3E8F8 | fundo de cartão ou bloco |
| Secundária | Secondary | #19756F | verde-petróleo: destaque secundário, cuidados |
| Alerta | Error | #B42318 | sinais de alerta, "procure atendimento" |
| Atenção | Warning | #C99B00 | triângulo de atenção (sempre com texto) |
| Positivo | Success | #027A48 | check, "faça isso" |
| Fundo claro | Default / Page | #FFFFFF / #F8F9FC | fundo de tela e de cartão |
| Texto escuro | Text Primary / Secondary | #101828 / #475467 | texto principal / linha leve de apoio |
| Texto claro | Text Inverse | #F8F9FC | texto sobre fundo azul ou escuro |

- **Cor do tema por vídeo:** cada vídeo pode ter uma cor de destaque ligada ao assunto (roxo na hanseníase, amarelo na dengue, vermelho na hipertensão, a cor da campanha do mês), usada **só em pontos de destaque**: palavra-chave, ícone, faixa, uma tela de impacto. O azul continua presente em todo vídeo.
- O contraste entre texto e fundo deve ser de no mínimo 4,5:1.
- No máximo três cores da paleta por quadro, além do branco.
- A cor de alerta é reservada a alertas e à chamada final. Usada em tudo, ela perde o efeito.

### Tipografia

Arquivos na pasta `fontes tipograficas/`.

| Uso | Fonte | Peso | Tamanho em 9:16 | Tamanho em 16:9 |
| --- | --- | --- | --- | --- |
| Título do tema | Poppins | Bold a Black | 72–88 px | 64–72 px |
| Texto de apoio na tela | Poppins | Regular a SemiBold | 48–56 px | 40–48 px |
| Créditos, fontes de dados, números pequenos | Inter | Regular a Medium | 30–34 px | 26–30 px |

Fontes de apoio, uma por vídeo no máximo: **Exo 2** (toque tecnológico), **Glacial Indifference** (linha leve geométrica, só Regular e Bold) e **Computer Says No** (texto técnico espaçado; licença CC BY-SA, que pede crédito ao autor).

- Preferência: duas famílias de fonte por vídeo, além do logo. Mais famílias ou outra fonte-base podem entrar com motivo claro e aprovação do usuário (decisão de 16/11/2026).
- Texto sempre em caixa alta e baixa; caixa alta só em palavras curtas de destaque.

### Logos e assinaturas

- **Durante o vídeo:** a régua de marca (abaixo).
- **Fechamento:** logo animado do Telessaúde Maranhão, com as assinaturas de parceiros empilhadas abaixo quando houver (ex.: Prefeitura de São Luís, PET-Saúde).
- Nunca distorcer, recolorir ou aplicar sombra nos logos; usar sempre o arquivo do kit.

**Régua de marca (obrigatório):** arquivo pronto do parceiro do vídeo, aplicado sem alteração, centralizado na horizontal e encostado na margem inferior do quadro, **do primeiro ao último quadro**. Há versões por parceiro (padrão SES/SUS Digital, PET-Saúde/Prefeitura de São Luís, Governo do Maranhão); usar a que vier no pacote.

## 6. Grafismos, transições e movimento (padrão)

Os grafismos existem para reforçar a orientação falada, nunca para competir com ela: cada elemento na tela corresponde a um trecho da narração.

| Elemento | Quando usar | Regra |
| --- | --- | --- |
| Título do tema | gancho, primeiros 3–8 s | até 6 palavras; entra com deslizamento curto e fica pelo menos 2 s |
| Cartão de texto | cada ideia-chave do roteiro | até 8 palavras; um cartão por vez; fica no mínimo 2,5 s |
| Lista numerada | "3 sinais", "4 passos" | itens entram um a um, no ritmo da narração; no máximo 4 itens |
| Ícone ou imagem de apoio | objeto ou ação citada | estilo único por vídeo (todos lineares ou todos preenchidos) |
| Selo de alerta | sinais de gravidade, "procure atendimento" | cor de destaque, sempre acompanhado de texto |
| Barra de identificação | quando aparece um profissional real | nome e função, terço inferior, 4 s |

**Transições:** livres, quantos tipos o vídeo pedir, dentro da gramática da marca: dissolução, entrada com desfoque, empurrão do layout, cortina de faixas coloridas, revelação circular, papel rasgado, corte seco.

**Movimento:** entradas e saídas de texto entre 0,25 e 0,4 s, com aceleração suave. Imagens estáticas recebem zoom lento de 3–5% ao longo do tempo em que ficam na tela. Nada pisca, gira ou treme.

**Densidade:** no máximo dois elementos novos por vez na tela (por exemplo, um cartão e um ícone).

## 7. Textos na tela (obrigatório)

Na teleorientação **não há legenda completa**: o texto na tela são **palavras-chave animadas** que acompanham a fala.

- **Fonte do texto:** o roteiro final narrado. Cada palavra-chave é copiada exatamente dele e entra junto da palavra falada.
- **Estilo:** hierarquia de uma linha pequena e leve com a palavra-chave grande e pesada embaixo; marca-texto ou cor do tema na palavra principal.
- **Quebra de linha:** não separar artigo do substantivo, nem número da unidade ("150 mL", "3 vezes").
- **Posição:** dentro da zona segura (seção 9).
- **Ortografia:** termos técnicos, siglas (UBS, SUS, SAMU) e nomes de medicamentos são conferidos contra o roteiro aprovado e o parecer técnico.
- **Arquivo `.srt`:** só quando pedido.

Vídeos de registro de ação (filmagem real em campo) têm regra própria: legenda completa dinâmica.

## 8. Áudio (obrigatório)

A narração conduz o vídeo: imagem, cortes e textos se ajustam ao tempo dela, e não o contrário.

| Camada | Nível de referência | Regra |
| --- | --- | --- |
| Narração (AI Studio) | −16 a −14 LUFS | sem cortes no meio de palavras; silêncios internos acima de 0,8 s podem ser encurtados para 0,4 s |
| Trilha | 18 a 22 dB abaixo da voz enquanto há fala | contínua sob a narração; sobe só no fechamento; entra e sai com fade de 1 s |
| Som de logo | fornecido pela equipe | no fechamento, junto do logo animado |
| Efeitos sonoros | discretos, abaixo da voz | só em entradas de alerta ou de lista; no máximo 3 por vídeo |
| Áudio das cenas do Flow | mudo por padrão | liberar só quando a fala do personagem fizer parte do roteiro |

- O áudio final é normalizado para −14 LUFS integrado e pico máximo de −1 dBTP (seção 2).
- Respirações e estalos audíveis da voz sintética são removidos.
- Toda trilha e todo efeito precisam de licença de uso registrada no pacote do vídeo.

## 9. Regras por plataforma (obrigatório)

No vertical, os botões e textos do Instagram e do YouTube cobrem as bordas da tela, então nada importante pode ficar nelas.

**Zona segura no 9:16 (1080 × 1920), obrigatória:** o mesmo arquivo vai para Reels e Shorts, então vale a margem mais restritiva de cada lado: retângulo de **x = 65 a 888 px e y = 288 a 1248 px** (823 × 960 px). **Informação importante** (títulos, textos, números, alertas, chamada, rostos) fica sempre dentro dele. **Elementos secundários** (decoração, ícones de apoio, parte do personagem, fundo) podem encostar ou passar um pouco da margem.

| Margem | Reels (Meta) | Shorts (Google) | Regra do manual |
| --- | --- | --- | --- |
| Topo | 269 px (14%) | 288 px | 288 px |
| Base | 672 px (35%) | 672 px | 672 px |
| Esquerda | 65 px (6%) | 48 px | 65 px |
| Direita | 65 px (6%) | 192 px | 192 px |

Os valores são os publicados pelas plataformas ([Reels](https://www.socialync.io/tools/safe-zones/instagram-reels), [Shorts](https://www.socialync.io/tools/safe-zones/youtube-shorts)). Os quadros-chave são mostrados à equipe com a máscara de zona segura sobreposta, para a conferência ser visual.

**Zona segura no 16:9 (1920 × 1080):** margem de 96 px em todos os lados.

| Item | Instagram (Reels) | YouTube (Shorts) | YouTube (vídeo 16:9) |
| --- | --- | --- | --- |
| Arquivo | 9:16 | 9:16 | 16:9 |
| Capa | quadro do título, texto dentro do quadrado central 1080 × 1080 (aparece cortada no grid do perfil) | quadro do título | PNG 1280 × 720 com título grande e logo |
| Texto na tela | palavras-chave animadas | palavras-chave animadas | palavras-chave animadas (+ `.srt` se pedido) |
| Texto do post | tema + 1 frase de orientação + referência + hashtags padrão | título curto com o tema | título + descrição com referências e links |

**Rótulo de conteúdo feito com IA:** narração e cenas geradas por IA podem exigir o rótulo de conteúdo sintético na publicação, conforme as regras de cada plataforma. A equipe decide a política e registra aqui (seção 12).

## 10. Conteúdo em saúde e acessibilidade (obrigatório)

O editor não altera o sentido de nenhuma orientação: o texto na tela só pode dizer o que o roteiro aprovado pelo revisor técnico diz.

**Precisão**

- Números, doses, prazos e sinais de alerta aparecem na tela exatamente como no roteiro aprovado.
- Nada de nomes comerciais de medicamentos nem de marcas de produtos, salvo se o roteiro pedir.
- Imagens e cenas não podem mostrar procedimentos errados (por exemplo, máscara mal colocada, lavagem de mãos incompleta). Cena com erro visível é substituída, não disfarçada.
- Dados e números citados na tela trazem a fonte em texto pequeno junto do dado (ex.: IBGE, Ministério da Saúde). O fechamento não tem cartela de fonte nem aviso (decisão de 15/11/2026).

**Linguagem**

- Palavras simples, frases curtas, voz ativa. Termo técnico só com explicação na mesma frase.
- Nenhuma imagem de medo, culpa ou estigma; pessoas representadas com diversidade de idade, cor de pele, corpo e território, incluindo o interior do Maranhão.

**Acessibilidade**

- Palavras-chave na tela (seção 7) e contraste mínimo de 4,5:1 (seção 5).
- Informação nunca transmitida só por cor: alerta tem cor e texto.
- Texto alternativo da capa e descrição resumida do vídeo no texto do post.
- Janela de Libras: a definir pela equipe (seção 12). Se adotada, ocupa o canto inferior esquerdo da zona segura, com cerca de 1/4 da largura da tela.

## 11. Fluxo de trabalho com o Claude e checklist de entrega

A aprovação acontece em quadros estáticos antes do vídeo completo, para que ajustes de visual não exijam renderizar tudo de novo.

1. **Pedido:** a equipe envia a pasta do vídeo (seção 3) e diz qual versão é a principal, se algo foge do padrão e a data de publicação.
2. **Conferência:** o Claude confere o pacote, mede a narração e devolve um mapa de cenas (trecho do roteiro, tempo, cena ou imagem, texto na tela). Falta de material é apontada aqui.
3. **Quadros-chave:** o Claude gera 4 a 6 quadros em tamanho real (gancho, um cartão de conteúdo, um alerta, a chamada, o fechamento), com a régua aplicada e uma cópia com a máscara de zona segura, para aprovação da identidade. Junto vai uma prévia curta de áudio (voz, trilha e um efeito).
4. **Montagem e finalização:** com os quadros aprovados, o Claude monta a base, aplica régua, narração, trilha e efeitos, mixa e renderiza.
5. **Revisão:** a equipe aponta ajustes pelo tempo do vídeo (ex.: "0:23, trocar ícone"). Ajustes são refeitos por cena.
6. **Versões finais:** aprovado o vídeo, o Claude gera a capa e, se pedidos, a outra proporção e o `.srt`.
7. **Arquivo:** vídeo e capa ficam em `renderizando/` com o nome padrão (seção 2); arquivos de trabalho em `renderizando/_claude/`.

### Checklist antes de entregar

- [ ] Resolução, fps, codec e duração conforme a seção 2
- [ ] Áudio em −14 LUFS, pico ≤ −1 dBTP, voz sempre inteligível sobre a trilha
- [ ] Palavras-chave idênticas ao roteiro aprovado, sem erros de digitação
- [ ] Nenhuma informação importante (texto, número, alerta, rosto) fora da zona segura
- [ ] Cores e fontes do kit de marca; contraste ≥ 4,5:1
- [ ] Números, doses e sinais de alerta conferidos com o roteiro e o parecer
- [ ] Régua do parceiro certo do primeiro ao último quadro, sem alteração
- [ ] Fechamento com o logo animado (+ assinaturas de parceiros)
- [ ] Licenças de trilha, efeitos e imagens registradas
- [ ] Capa (e `.srt`, se pedido) entregue com o nome padrão
- [ ] Vídeo assistido do início ao fim no celular, com e sem som

## 12. Pendências para a equipe

O manual vira norma quando estes itens forem preenchidos; os quatro primeiros bloqueiam o primeiro vídeo.

- [x] Enviar cores em HEX e arquivos das fontes (15/11/2026)
- [ ] Enviar os logos em .svg ou .png e o arquivo da fonte condensada dos números grandes, se houver
- [ ] Definir como é feito o crédito da fonte Computer Says No (licença CC BY-SA)
- [x] Enviar vídeos já publicados como referência (22 vídeos analisados em 15/11/2026)
- [ ] Enviar o logo animado do fechamento e o som de logo, em arquivo
- [ ] Enviar as réguas de marca de cada parceiro (9:16 e 16:9)
- [ ] Confirmar a lista e a ordem das assinaturas de parceiros no fechamento
- [ ] Definir se haverá janela de Libras
- [ ] Definir a política de rótulo de conteúdo gerado por IA nas publicações
- [ ] Escolher a trilha (ou biblioteca licenciada) padrão da série
- [ ] Definir as hashtags e o modelo de texto do post

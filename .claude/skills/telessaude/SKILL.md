---
name: telessaude
description: Use ao editar ou animar qualquer vídeo do Telessaúde Maranhão (NTS-UFMA), vertical 9:16 ou horizontal 16:9 — teleorientação, campanhas de datas de saúde, institucionais (projetos, retrospectivas) e registros de ações em campo — inclusive para reconstruir em 16:9 um vídeo vertical já publicado. Aplica a identidade da marca por cima da skill geral motion e aponta para as regras de cada formato (formatos/) e de cada tipo de vídeo (tipos/).
---

# Telessaúde Maranhão — perfil da marca

Sub-skill da skill `motion`. Leia antes `motion/SKILL.md`. Aqui fica o que vale para **todo** vídeo do Telessaúde, em qualquer formato e de qualquer tipo.

## Papel do Claude: o vídeo inteiro

O Claude **monta a base** (o que antes era feito no Canva: telas, textos, animação, transições) e **finaliza** (o que antes era feito no Premiere: régua, narração, trilha, efeitos sonoros, mixagem, exportação). Passo a passo em `producao.md`. Os elementos visuais e de marca vêm do usuário; o Claude compõe, anima e posiciona.

## Regra fixa: elementos de marca vêm prontos

**O Claude não cria elementos de marca.** Régua de marca, logos, logo animado, som de logo, assinaturas de parceiros e demais elementos visuais da identidade são fornecidos pelo usuário em cada vídeo. O trabalho é **colocá-los no lugar certo, sem alteração**: a régua centralizada e encostada na base (barra inferior), o logo no fechamento, as assinaturas onde o arquivo do formato indicar. Faltando algum, pergunte; não desenhe, não redesenhe, não recolora, não estique.

A identidade visual ainda está em construção pela equipe: o que este perfil descreve é tendência observada, e o kit de marca entregue pelo usuário tem prioridade sobre ele.

### Conferir régua e fechamento em todo vídeo (regra do usuário, 15/11/2026)
A régua e a tela de fechamento **mudam com a parceria**: vídeo próprio do Telessaúde, PET-Saúde, SEMUS, odontologia, outros projetos. **Nunca reaproveite os de outro vídeo por conta própria.** No primeiro passo de todo vídeo, confira se a régua e o fechamento estão na pasta do vídeo; se não estiverem, **pergunte e espere**. Mesmo presentes, confirme a parceria quando o roteiro sugerir outra.

**Biblioteca primeiro (21/11/2026).** Antes de pedir qualquer asset, consulte `biblioteca/` (catálogo em `biblioteca/README.md`; busca com `py ferramentas/da_biblioteca.py --listar <termo>`) e **copie** para a pasta do vídeo o que já existir (`py ferramentas/da_biblioteca.py "<item>" "<pasta do vídeo>"`). O vídeo usa sempre a cópia dele. Na lista de assets, marque o que veio da biblioteca e peça só o resto. Item novo reutilizável que o usuário entregar (ou que for baixado com o ok dele) também é copiado para a biblioteca e registrado no README dela.

**Sempre pedir todos os assets ao começar a produzir (regra do usuário, 20/11/2026).** Ao iniciar a produção de qualquer vídeo, liste e **peça ao usuário todos os assets necessários** que não estiverem na biblioteca para aquele vídeo (personagens, cenas do Flow, ícones, mapas, logos de parceiros, fotos, régua, fechamento, trilha), cena a cena, a partir do roteiro. Se algum não existir ou não for encontrado, **pesquise opções e mostre como sugestão** (link, fonte e licença); com o ok do usuário, baixe para `elementos/` da pasta do vídeo e, se servir a outros vídeos, também para a biblioteca. Elementos de marca (régua, logos do Telessaúde, logo animado, assinaturas) continuam só do usuário: nunca baixar nem criar substitutos.

**Sempre confirmar os itens obrigatórios com o usuário (regra do usuário, 15/11/2026).** Ao fim da conferência do pacote, liste os itens obrigatórios (checklist em `organizacao.md`) com o arquivo exato que pretende usar em cada um (régua, logo animado do fechamento, som de logo, assinaturas, trilha, narração) e **espere o usuário confirmar antes de montar**. Isso vale mesmo quando o arquivo está na pasta do vídeo; achar um arquivo parecido em outra pasta ou em outro vídeo nunca é confirmação. O IAM e o AVC não confirmam nada para o vídeo seguinte.

## Organização de pastas

Todo vídeo segue a estrutura de `organizacao.md` (tema › parte › audios, roteiro, elementos, trilha sonora, renderizando). Leia antes de abrir ou gravar qualquer arquivo.

## Como o perfil se organiza: formato × tipo

Todo vídeo tem um **formato** e um **tipo**. Leia os dois arquivos antes de planejar:

- `formatos/vertical.md` ou `formatos/horizontal.md`: tela, área segura, composição, tamanhos de texto, régua, capa. O horizontal inclui a **reconstrução de vídeos verticais em 16:9**.
- `tipos/<tipo>.md`: estrutura, duração, tom, efeitos preferidos.

Exemplo: campanha do glaucoma para o YouTube = este arquivo + `formatos/horizontal.md` + `tipos/campanha.md`.

## Origem do material

| Origem | Tipos | O que muda |
| --- | --- | --- |
| **Digital** (animação: ilustração, ícones, texto, cenas geradas por IA) | teleorientação, campanha, institucional | tudo é composto; a identidade vem dos grafismos |
| **Captação real** (filmagem de campo, celular) | registro | a identidade vem da legenda, do mapa e da assinatura; os grafismos são poucos |

Institucionais (Kits, Retrospectiva) são digitais mas podem ter **fotos reais** de eventos e equipes em colagem; é a única exceção dentro do digital. Fotos e filmagens só entram se vierem no pacote do vídeo.

**Perfil é tendência, não regra.** Cada vídeo deve variar (cor do tema, personagens, recursos de movimento) sem sair da identidade descrita aqui. Base: análise de 22 vídeos aprovados em `analise-referencias/RELATORIO-ANALISE.md`.

## Tipos de vídeo (leia o arquivo do tipo antes de planejar)

| Tipo | Arquivo | Exemplos nas referências |
| --- | --- | --- |
| Teleorientação | `tipos/teleorientacao.md` | Hipertensão, Hanseníase, Câncer de Pênis, Retinopatia, série PET-Saúde (Dengue, Diabetes, Obesidade…) |
| Campanha de data | `tipos/campanha.md` | Dia Nacional de Combate ao Glaucoma, Prevenção do Câncer de Pênis |
| Institucional | `tipos/institucional.md` | Kits de Telessaúde (Novo PAC), Retrospectiva 2025 |
| Registro de ação | `tipos/registro.md` | Ação em Tauá-Mirim |

Se o pedido não se encaixar em nenhum, use só este arquivo e pergunte o tipo. Para um tipo novo que se repita, crie `tipos/<nome>.md` com o mesmo formato.

## Entrega (todos os formatos)

- 30 fps, H.264, AAC 48 kHz, −14 LUFS, pico −1 dBTP. Resolução, área segura e capa: ver o arquivo do formato.
- Pergunte o formato se o pedido não disser. Quando o mesmo vídeo sair nos dois, um é o principal (animado primeiro) e o outro é **recomposto**, nunca só recortado.

## Identidade

### Régua de marca
- Arquivo pronto entregue em `elementos/` do próprio vídeo, sem alteração, centralizado e encostado na base, **o vídeo inteiro** (decisão de 15/11/2026). Cada formato tem o seu PNG (detalhes no arquivo do formato).
- Há versões por parceiro; use a que vier no pacote do vídeo:
  1. Telessaúde + Gov. Maranhão/SES + sted + SUS Digital + Brasil (padrão).
  2. Telessaúde + sted + PET-Saúde + Prefeitura de São Luís + Ministério da Saúde (projeto PET-Saúde).
  3. Variante com o logo "MARANHÃO" do governo em primeiro (ações com a SES).
- Registro de ação com filmagem real pode dispensar a régua (ver `tipos/registro.md`).

### Fechamento
- Logo animado: o hexágono entra, depois "TELESSAÚDE" e "Maranhão UFMA" em azul, 3–5 s, fundo branco. Com parceiros, assinaturas empilhadas abaixo com fio separador fino.
- Som de logo padrão nos segundos finais. Logo animado e som de logo são arquivos do usuário; se o vídeo-base do Canva já os tiver, não duplicar.

### Cor
- **Paleta oficial em `cores.md`** (guia de cores do portal): Primary `#365DCC`, Brand Strong `#1C306A`, Secondary `#19756F`, textos `#101828`/`#475467`, fundos `#FFFFFF`/`#F8F9FC`, feedback Success/Warning/Error. Os **tons de azul podem variar** dentro da família da marca, como nos vídeos de referência. Fundo predominante branco/gelo.
- **Cor do tema (decisão de 15/11/2026):** cada vídeo pode ter uma cor de destaque ligada ao assunto (roxo na hanseníase, amarelo na dengue, vermelho na hipertensão, cor da campanha do mês), mas **usada pontualmente**: palavra-chave, ícone, faixa, uma tela de impacto. **O padrão é o azul da marca**, e todo vídeo, mesmo com cor do tema, mantém **algo azul visível** (título, barra, cartão, fundo de bloco), porque o azul remete à identidade do núcleo. Evite telas inteiras na cor do tema em sequência, como nas referências antigas de hanseníase; prefira fundo claro + azul + toques da cor do tema.
- Alerta sempre com cor **e** texto ("ATENÇÃO", triângulo). Contraste ≥ 4,5:1.
- Nunca usar a paleta de um preset de `motion/estilos/` no lugar da marca; do preset vale só movimento, composição e acabamento.

### Tipografia
- **Poppins** é a voz principal (Regular a Bold Italic). Hierarquia típica: linha pequena e leve + palavra-chave grande e pesada ("Você tem / **DIABETES?**").
- Apoios usados com moderação: Exo 2 (logo), condensada tipo Bebas Neue/Oswald (números e institucionais), monoespaçada (texto "técnico"), contorno sem preenchimento para interjeições, manuscrita/script para um toque humano. Outras fontes do usuário: Glacial Indifference, Inter.
- Preferência: Poppins + uma de apoio, além do logo. Mais famílias ou outra base são possíveis com motivo e aprovação do usuário (regra 11 de `motion/SKILL.md`). **Arquivos em `biblioteca/marca/fontes/`** (raiz do projeto); usos, licenças e lacunas em `fontes.md`. A fonte "Computer" é a **Computer Says No** (CC BY-SA: pede atribuição).

### Imagem e personagens
- Ilustração vetorial 2D, pessoas recortadas com sombra suave (efeito adesivo) sobre fundo claro, ou cenas ilustradas completas. Ícones de apoio 3D/flat coloridos.
- **Cenas geradas por IA (Google AI Studio / Flow):** o estilo padrão pedido pelo usuário é **motion design + flat design**. Ao escrever o prompt de uma cena (`motion/metodo-referencia.md`, seção 5), inclua esse estilo, o mesmo personagem de referência, fundo claro e liso (facilita recorte e reenquadramento) e a proporção do formato final (9:16 ou 16:9). Evitar: fotorrealismo, 3D realista, texto dentro da cena (o texto é composto na edição), logos. Para escrever os prompts de um roteiro, use a skill `prompts-flow` (triagem Flow × motion gráfico, estrutura do prompt e entrega).
- **Personagens do Flow sem recorte (decisão do usuário, 20/11/2026):** use o clipe original de fundo branco com `mix-blend-mode: multiply` sobre fundo claro (o vídeo fica na raiz da página, sem `transform`/`z-index` em contêiner entre ele e o fundo, senão o multiplicar não enxerga o fundo). Nada colorido atrás do personagem (mapa, painel azul, faixas): o multiplicar mostra através do corpo. Em cena de fundo escuro, o personagem não entra. Recorte automático foi testado e rejeitado (bordas e roupa comidas).
- **Pessoas não são desenhadas pelo Claude em SVG (devolutiva do Telediagnóstico v1, 20/11/2026: o médico em SVG ficou "horroroso").** Personagem humano vem do Flow (skill `prompts-flow`) ou de ilustração/animação pronta pesquisada na internet, mostrada ao usuário com link e licença antes de baixar. O SVG do Claude fica para ícones, objetos e grafismos.
- Diversidade de idade, cor de pele, corpo e território, incluindo o interior do Maranhão. Nenhuma imagem de medo, culpa ou estigma.
- Dados com fonte citada na tela (IBGE, Ministério da Saúde, OMS).

### Linguagem
- Próxima e maranhense quando o tipo permite ("Ei comadre", "Vish", "Éguas", "Rapaz…"). Texto na tela = palavra-chave da fala, exato.
- O texto na tela só diz o que o roteiro aprovado diz.
- **Série de vídeos: cada um com gancho próprio (devolutiva de 18/11/2026).** Uma abertura-fórmula repetida em todos os vídeos da série (ex.: "Teleconsulta, teleconsultoria… Parece tudo igual, né? Hoje a gente explica…") fica genérica e cansa. A mesma ideia pode servir num vídeo (onde ela é o assunto), não em todos. Cada gancho parte de uma situação ou pergunta ligada ao tema daquele vídeo.

### Movimento (gramática da marca)
Recursos que se repetem e identificam a marca — escolha alguns por vídeo, não todos:
`type-on` (máquina de escrever), entrada com blur, `stagger-in` em listas, `pop-in` de ícones em volta do personagem, `palavra-destaque` (marca-texto amarelo), risco/X vermelho sobre palavra, troca de pose com dissolução, push-in no rosto, empurrão do layout, cortina de faixas coloridas, wipe circular, dessaturar e voltar a cor, papel rasgado, `contador`.
**Curva preferida: mola (spring) no estilo das interfaces da Apple** (`mola`, `molaViva` em `ts-anim.js`): chega rápido, passa um pouco do alvo e assenta. Use em entradas de cartões, etiquetas, ícones, títulos e painéis; ao explicar, nomeie "mola" e os parâmetros (o usuário quer aprender).
**Efeitos: sentido primeiro, criatividade sempre (ajustado em 16/11/2026).** Sugestões de efeito do usuário são opções, não lista obrigatória.
- Quando a fala traz uma imagem clara, o efeito a reforça (relógio na fala do tempo, gotas no sangramento). No mapa de cenas, diga qual trecho da fala ele ilustra.
- Quando a fala não pede nada visual (frase de ligação, trecho pouco interessante), **não deixe a tela parada:** use um efeito criativo, sobretudo de transição — arrastar elementos para os lados, faixas que cortam o vídeo, cortinas, wipes. O usuário é a favor desses efeitos mesmo sem relação literal com a fala.
- O limite: o efeito não pode competir com a informação de saúde, cobrir texto importante nem sugerir algo que o roteiro não diz.
**Devolutiva do AVC v1 (15/11/2026), vale para todo vídeo:**
- **Uma cena puxa a outra.** Prefira elementos que se reposicionam e viram o próximo (metamorfose, elemento compartilhado: o cronômetro vira o relógio, o título vira cabeçalho) a cortes entre telas sem ligação.
- **Transições de mesclagem: assinatura do usuário (16/11/2026).** Ele mesmo as fazia no Canva e quer que sejam consideradas **já no mapa de cenas**, em todo vídeo. Para cada troca de cena, escolha uma das três antes de pensar em corte ou dissolução (receitas em `motion/efeitos.md`, "Transições de mesclagem"):
  1. **`continuidade`:** um elemento que já está na tela **muda de posição ou de tamanho** e fica; a cena "continua a mesma", o resto limpa e entram elementos novos em volta dele.
  2. **`metamorfose`:** uma coisa **se transforma** na outra (silhueta → corpo-cidade, coração do título → coração da cena).
  3. **`arrasto`:** tudo é **arrastado para um lado** e os novos elementos entram arrastados pela direção oposta (direita ↔ esquerda, baixo ↔ cima); varie a direção ao longo do vídeo.
  Exemplos no vertical/horizontal do Canva da Hipertensão parte 1 (`REFAZENDO-VIDEOS/hipertensao 1/video horizontal canva/`): silhueta que vira corpo-cidade e depois paisagem (13–17 s); gota que fica e encolhe ao lado do medidor (23–29 s); a cena da aferição que fica enquanto o cartão "Pressão alta" troca (31–36 s); "Você acha que a pressão alta é rara?" que vai para o canto e abre espaço ao Brasil e às silhuetas (48–55 s); o cartão "A pressão alta dá pra controlar" fixo no canto enquanto os itens mudam (80–97 s).
- **Nada de layout estático, e tudo sempre legível.** Listas e grades: o item novo entra **grande numa área livre** (centro no primeiro; depois um canto, ex. inferior direito, junto da área segura) **sem cobrir nenhum outro**; quando chega o próximo, o anterior encolhe para o seu lugar numa grade provisória menor; no fim, a grade toda cresce para o tamanho final. **Nunca** apagar, esmaecer ou cobrir itens já mostrados (devolutiva da v2).
- **Escala dinâmica (regra central do usuário, 16/11/2026): quanto menos elementos na tela, maiores eles são; a cada elemento novo, todos se redimensionam e se reposicionam** com mola para abrir espaço. Nunca o contrário (algo crescer quando outro entra, ou um espaço vazio esperando a próxima animação). Ex.: o enfermeiro começa grande e diminui quando o cérebro e o texto entram; o relógio entra grande e encolhe enquanto "em até / 4 horas / e 30 minutos" aparecem; cartões com escala e espaçamento que mudam a cada etapa. Grades não precisam ser rígidas nem alinhadas à esquerda: posições alternadas (1º acima à esquerda, 2º um pouco mais abaixo à direita etc.), com folga entre si e do título.
- **Deslocamento suave para abrir espaço (devolutiva da Hipertensão parte 2, 15/11/2026):** a escala dinâmica vale também para a **posição**. O que está sozinho fica centralizado (na horizontal e na vertical). Quando algo entra **acima**, o conjunto desce um pouco; quando algo entra **abaixo**, ele sobe um pouco. Dois blocos que vão receber um elemento entre eles começam próximos e **se afastam** para abrir espaço a ele (ex.: "mais raros" e "pode ser causada por outras doenças" se afastam e a faixa "Hipertensão secundária" entra no meio). Movimentos sempre curtos e com mola (~0,8 s). Ao montar o mapa de cenas, procure esses momentos no vídeo inteiro, não só onde o usuário apontou. Implementação: `data-k="t:dx,dy,escala;..."` em `REFAZENDO-VIDEOS/hipertensao 2/renderizando/_claude/animacao/hipertensao2_h.html`.
- **Fundo branco nunca "frio" (devolutiva da Hipertensão parte 2, 15/11/2026):** cenas de fundo claro ganham um **fundo vivo sutil**: 2–3 manchas de cor bem diluídas (7–13% de opacidade) que se movem devagar como líquido, no azul do núcleo + a cor do tema da cena, e uma textura de pontos azuis leves só nas bordas, deslizando. Fica por baixo de tudo e não compete com o conteúdo. Implementação: `data-fundo="quente|misto|azul|verde"` na cena, na mesma página `hipertensao2_h.html`.
- **Impactos pontuais:** onda de choque, faíscas e tremor curto só em palavras de peso (o pico da pressão, "elevados", alerta), como no gancho da Hipertensão parte 2 e no IAM v5; nunca em toda entrada.
- **Objeto que sai pela borda mostra o que importa:** ao crescer e sair do quadro (celular), gire para que a parte com a informação (o número na tela) continue visível.
- **Lista que cresce sobe junto:** quando entra um item, título e itens sobem um pouco com mola (elástico).
- **Personagem auxiliar:** pode ficar grande, junto da borda, saindo do quadro (só parte do corpo); **nunca** sobre o texto. Animação por **escala** (cresce/diminui com mola) e **troca de pose com dissolução**; **não espelhar/virar de um lado para o outro** (o usuário não gostou).
- **Espaço da tela:** use a tela toda; textos e elementos podem se espalhar e passar um pouco da área segura em vez de ficarem apertados no centro.
- **Tela toda ocupada, sempre (devolutiva da Teleorientação v1, 20/11/2026):** o vídeo também é enviado por **WhatsApp, que não tem margem**. A área segura vale só para a **informação importante** (texto, título, rosto); o resto do quadro (topo, laterais, faixa entre y 1248 e a régua) **não pode ficar vago**: personagens grandes com o pé junto à régua, celular/objeto grande que pode passar da borda, fundo com **marca d'água em movimento** (ex.: mapa do Brasil bem diluído, com deriva lateral e zoom lento contínuos, mesmo sem relação com a fala). Elementos parados ganham movimento leve constante (flutuar, balançar, respirar). Ao checar quadros de prova, procure faixas vazias, não só invasão da margem. Centralize a informação no meio da área segura (x ≈ 480), não em 540.
  - **Como a Teleorientação v1 → v2 resolveu isso (o que o usuário aprovou; análise de 20/11/2026):** a v2 não inclinou textos nem espalhou peças; ela **aumentou o protagonista de cada cena e o ancorou na base**. O celular passou de ~45% para ~75% da altura e desceu até a régua; quando não era o foco, **ficou espiando por baixo do título** em vez de sumir. As pessoas cresceram até ter o **pé na régua** e ficaram até o fecho. O Maranhão cresceu e **saiu pelas bordas**. O texto continuou no alto, dentro da área segura. Ou seja: o espaço é ocupado pelo **assunto da cena, grande**, e não por enfeite, etiqueta cortada ou objeto sem sentido na borda.
  - **Erro repetido do Claude (Telediagnóstico v1, 20/11/2026: "tudo no centro, sem movimento, sem personalidade, robótico"):** montar a cena como uma pilha pequena no meio da área segura, com o resto vazio. Antes de qualquer quadro de prova, pergunte para cada cena: **qual é o protagonista, e ele está grande, ancorado na base ou saindo pela borda?** O que já foi falado pode sair da área segura, mas só para um lugar que **faça sentido** (virar cabeçalho, espiar por baixo, ficar no fecho), nunca como texto cortado na borda. Na Telediagnóstico v2, deixar etiquetas e cartões já falados cortados nas bordas e alfinetes pela metade foi rejeitado como incoerente.
- **Devolutiva do Telediagnóstico v2 (20/11/2026), vale para todo vídeo:**
  - **Nada de fundo mexendo sem motivo:** mapa de marca d'água indo de um lado para o outro o tempo todo foi rejeitado. Fundo pode respirar devagar, mas não "passear".
  - **Alfinete só marca lugar de verdade:** alfinetes soltos sobre o mapa, sem lugar real, parecem marcar algo que não existe. Para "nos municípios", prefira a cobertura se espalhando a partir de um ponto real (ex.: São Luís, onde fica o núcleo).
  - **Título nunca cortado por linha ou traço da mesma cor.** O título vai numa faixa ou num espaço próprio.
  - **Logo de parceiro: só o logo, grande e animado** (as partes entram em sequência), nunca pequeno com a sigla escrita ao lado. Embuta o SVG na página para animar parte por parte; confira se o arquivo não traz mais de um logo (o da UFMG traz dois, um fora do quadro original).
  - **Não repetir o mesmo formato cena após cena** (ex.: tudo em cartão branco, só trocando o nome): quem assiste cansa e pula. Cada bloco ganha uma linguagem própria (tela dividida, aproximação na pessoa, tipografia, ilustração em tela cheia, metamorfose de uma cena na outra) e o cartão fica para quando ajuda.
- **Devolutiva do Telediagnóstico v3 (20/11/2026), vale para todo vídeo:**
  - **Personagem do Flow cortado na cintura: esmaecer a parte de baixo** (máscara em degradê, cerca dos 15–25% finais do corpo), em vez de corte seco no meio da tela ("margem fantasma de novo, não gosto"). Encostado na régua, o corte pode ficar, mas um esmaecimento leve ainda é melhor.
  - **Nada aparece direto na posição final.** Item novo entra grande no meio do espaço livre e depois vai para o seu lugar; a lista sobe para recebê-lo; o vizinho vibra, encolhe ou se afasta com mola. É a regra da escala dinâmica, que o Claude esqueceu de aplicar.
  - **Frase curta da fala pode ir inteira na tela** ("o exame foi feito / aqui"), com a palavra-chave maior e em cor; palavras soltas demais ("o exame / aqui") ficaram secas.
  - **Etiqueta nunca sobre o rosto da pessoa:** meça a largura do texto e deixe folga até o rosto.
  - **Cenas rejeitadas podem ir para outra IA:** quando o usuário pedir, escreva um documento com a descrição de todas as cenas (regras, narração com tempos, elementos disponíveis, cena a cena) e um prompt detalhado para outra IA propor as cenas rejeitadas (modelo em `CRIANDO-VIDEOS/SERVIÇOS NTS/TELEDIAGNÓSTICO/renderizando/_claude/02-descricao-das-cenas.md`).
- **Não usar enfeites genéricos** (cruzes, meios-círculos, pontinhos, confetes espalhados pelo vídeo): o usuário rejeitou na v2. Borda vazia se resolve com o conteúdo real maior e mais espalhado, ou com um elemento do tema.
- **Quebra de linha equilibrada (devolutiva do AVC v4):** nada de palavra sozinha numa linha nem linha longa seguida de uma curtinha ("Se você perceber esses / sinais,"). Quebre à mão (`<br>` + `white-space: nowrap`) para as linhas terem tamanhos parecidos ("Se você perceber / esses sinais,"), ou reduza o corpo e deixe numa linha só. Conferir em todo quadro de prova.
- **Pesos de fonte:** quando ajudar a hierarquia, varie o peso da Poppins (ExtraLight/Light na linha de apoio, SemiBold, Bold, ExtraBold/Black na palavra-chave). Só quando fizer sentido.
- **Transição de clipe para clipe:** desfoque com zoom costuma funcionar melhor que empurrão. **No bloco de avaliação, comentário sobre transição em `mtN` refere-se à saída daquele motion** (na dúvida, pergunte); não mexer na entrada que já foi aprovada.
- **Objeto que vira o próximo:** quando a cena seguinte mostra o mesmo objeto (cérebro do clipe → cérebro do cartão; aparelho de pressão do clipe → ícone da lista), meça o objeto no quadro do clipe e leve-o com câmera ou camada até o lugar e o tamanho exatos do próximo, com dissolução no fim.
- **Etiqueta retangular como padrão (gosto do usuário, 17/11/2026):** palavras-chave e listas vão de preferência em etiquetas retangulares com cantos levemente arredondados (raio ~15–20% da altura). Pílula (cápsula) pode aparecer pontualmente; o que o usuário rejeita é o excesso, pílula em tudo, que deixa o vídeo genérico e "com cara de IA". Detalhes em `motion/principios.md`.
- **Destaque de palavra:** etiqueta (retangular, levemente inclinada) ou marca-texto passando atrás são boas opções para palavras-chave curtas ("de repente").
Ritmo: um elemento novo a cada ~2 s; layout muda a cada 4–8 s. Movimento calmo; nada de shake, glitch ou flash.

### Som
- Trilha contínua sob a narração, **audível no celular** (o usuário não ouviu a trilha do AVC v1, que estava a −12 dB: ~15 dB abaixo da voz nas pausas e ~21 dB sob a voz). Ponto de partida no `ferramentas/mixar.py`: `"db": -11` com `"ducking": {"reducao_db": 5}` (−9 já ficou audível no AVC v2; o usuário pediu ~2 dB a menos) (cerca de 6 dB abaixo da voz nas pausas e 11 dB sob a voz, para uma trilha de ~−15 LUFS). Se a música tiver introdução baixa, comece na parte cheia com `"desde"`; se a música for curta para isso (o `mixar.py` avisa), comece do início com `"realce": {"db": 6, "ate": 11, "rampa": 3}` (IAM v4.1/v5.1). **Meça** antes de entregar: nas pausas e no trecho sem voz a trilha deve ficar entre −20 e −24 LUFS momentâneo no arquivo final. Termina antes do fechamento quando o fechamento tem som próprio (`"ate"`).
- **Efeitos sonoros discretos** (pedido do usuário, 15/11/2026: estavam incomodando): marcam a transição sem chamar atenção; partir de `"sfx_db_extra": −5` sobre os valores de cada efeito.
- **Sons de interface durante o vídeo, não só nas transições** (pedido do usuário): digitação nos textos digitados, swish no marca-texto e em etiquetas, tique em itens de lista. **Sem pop, bolha ou blob** (devolutiva da Hipertensão parte 1, 16/11/2026: o usuário achou o "bloob" estranho e repetitivo; `pop*.wav`, `pop_grave`, `bolha`, `blob` ficam fora). **Coisa que arrasta, desliza ou entra = whoosh/swish suave**, com cuidado na quantidade e no volume (referência: 40 efeitos em 1 min 42 s, com `"sfx_db_extra": -5`). Biblioteca em `biblioteca/sfx/sintetizados/` (`ferramentas/sfx.py`); com a pasta de efeitos do usuário, preferir a dele. Nível de fundo (−15 a −18 dB antes do ajuste geral): imersão, não protagonismo.
- **Densidade (devolutiva do AVC v3):** efeitos demais em sequência curta incomodam (a cena do 192 tinha 13 em 3 s). Um som por gesto que importa; no máximo ~1 efeito a cada 0,7 s; whoosh só nas transições; **sem som** para movimentos secundários (cartões que se reorganizam, ícone que voa, objeto que cresce). Referência: o AVC final tem ~50 efeitos em 66 s (a v3 tinha 85).
- Som de logo no fechamento. Mix final em −14 LUFS e pico ≤ −1 dBTP, em duas passadas (as referências variam de −22 a −10; padronizar).

## Cuidados com conteúdo de saúde (todos os tipos)
- Nunca alterar o sentido das orientações. Números, doses, prazos e sinais de alerta conferidos contra o roteiro antes de cada render.
- Cena gerada com procedimento errado é substituída, não disfarçada.

## Decisões do usuário (15/11/2026)

| Tema | Decisão |
| --- | --- |
| Área segura | **Informação importante** (texto, números, alertas, chamada, rosto) sempre dentro da área segura. Elementos secundários (decoração, ícones de apoio, parte do personagem, fundo) podem encostar ou passar um pouco da margem. |
| Vinheta de abertura | **Nenhuma.** O vídeo abre direto no gancho; a marca aparece na régua e no fechamento. |
| Duração | **Livre:** a narração define. Temas longos podem continuar em parte 1 e parte 2. |
| Legenda | **Teleorientação, campanha e institucional (estilo digital): só palavras-chave animadas**, sem legenda completa. **Registro de ação (captação real): legenda completa** dinâmica. |
| Fechamento | **Só o logo animado** (+ assinaturas de parceiros quando houver), como hoje. Sem cartela com fonte, aviso, redes ou site. |
| Transições | **Livres**, quantos tipos o vídeo pedir, dentro da gramática da marca. |
| Régua | **O vídeo inteiro**, do primeiro ao último quadro. No registro de ação, só se o usuário pedir. |
| Cores | **Azul da marca é o padrão** (tons podem variar). Cor do tema por vídeo permitida, **só em pontos de destaque**; todo vídeo mantém algo azul. |
| Loudness | −14 LUFS, pico −1 dBTP (padroniza a variação das referências). |

O `MANUAL-EDICAO-TELEORIENTACAO.md` traz estas decisões (versão de 15/11/2026); a cópia do repositório é a que vale.

## Antes de entregar
Rode a checagem final de `motion/SKILL.md` e o checklist do tipo de vídeo.

# Análise dos vídeos de referência — Telessaúde Maranhão

Análise de 22 vídeos e 12 capas da pasta `biblioteca/videos-publicados/`, feita em 15/11/2026. Ela serve de base para o perfil "telessaude" do fluxo de edição. **O perfil é tendência, não regra:** o objetivo é variar entre vídeos sem sair da identidade.

Material gerado nesta pasta:
- `folhas/`: folhas de contato com um quadro a cada 2 s, com o tempo marcado.
- `area-segura/`: quadros em tamanho real com a máscara da área segura sobreposta.
- `dados/`: inventário técnico, paletas, medidas de régua e áudio (JSON).
- `scripts/`: scripts que geraram tudo isso, para reaplicar a novos vídeos.

---

## 1. Inventário técnico

| Grupo | Vídeos | Duração | Formato |
| --- | --- | --- | --- |
| Teleorientação "SUS Digital" | Hipertensão, Hanseníase pt 1 e 2, Câncer de Pênis pt 1 e 2, Retinopatia | 65–98 s | 1080×1920, 30 fps |
| Teleorientação PET-Saúde | Dengue 1 e 2, Diabetes 1 e 2, Hanseníase Outubro 1 e 2, Hipertensão PET 1 e 2, Obesidade Infantil 1 e 2 | 73–144 s | 1080×1920, 30 fps |
| Campanhas | Glaucoma (26/05), Prevenção do Câncer de Pênis | 40–73 s | 1080×1920, 30 fps |
| Institucionais | Kits de Telessaúde (Novo PAC), Retrospectiva 2025, Ação em Tauá-Mirim (completo e curto) | 26–136 s | 1080×1920, 30 fps (a Retrospectiva está em 60 fps) |

- Todos são verticais 9:16. Nenhum 16:9 foi enviado.
- A duração mediana da teleorientação é cerca de 78 s. Os temas longos são divididos em "parte 1" e "parte 2", em vez de cortados para 60 s.
- Exportação do Canva: H.264 e AAC, com bitrate de 9 a 17 Mbps.

## 2. Identidade comum (o que se repete em todos)

### Marca e assinatura
- **Régua de marca aparece o vídeo inteiro** em 20 dos 22 vídeos. Fica numa faixa branca de 80 a 140 px colada na base, com os logos de x ≈ 50 a 1030. As exceções são Tauá-Mirim (filmagem real) e o cartão final do Glaucoma.
- **Existem três versões da régua**, conforme o parceiro:
  1. Telessaúde + Gov. Maranhão/SES + sted + SUS Digital + Brasil (série SUS Digital, campanhas e institucionais).
  2. Telessaúde + sted + PET-Saúde + Prefeitura de São Luís + Ministério da Saúde (série PET-Saúde).
  3. Uma variante com o logo "MARANHÃO" do governo em primeiro (Hanseníase SES).
- **Fechamento padrão:** o hexágono do logo entra sozinho. Depois aparece "TELESSAÚDE" em cinza e em seguida "Maranhão UFMA" em azul, por volta de 3 a 5 s. Na série PET-Saúde vêm empilhadas, logo abaixo, as assinaturas da Prefeitura de São Luís e do PET-Saúde, com fio separador fino.
- **Não há vinheta de abertura.** Todos começam direto no gancho, com a narração a partir de 0 s. A marca aparece só na régua e no fechamento.

### Cor
- **Azul do logo:** cerca de **#3149BB**. Foi medido no cartão final, mas é aproximado por causa da compressão; confirme com o kit de marca.
- **Fundo dominante:** branco ou branco gelo (#FDFDFD / #F4F4F4), em 40 a 70% dos quadros de teleorientação.
- **Cada tema tem a sua cor de destaque, e ela muda a cada vídeo.** É aqui que está a variação:

| Tema | Cor de destaque (aprox.) | Papel |
| --- | --- | --- |
| Hanseníase | roxo #7A18AE / #8621B7 | fundos inteiros, títulos |
| Câncer de Pênis | violeta #A92BEB | fundos, palavras-chave |
| Dengue | amarelo #F8DD55 | fundo dos blocos de alerta |
| Hipertensão / Diabetes / Obesidade | vermelho #AB121F a #E53935 | títulos, faixa de chamada |
| Glaucoma, Kits, Retrospectiva | azul #1A4FB7 → #3165D6 em degradê | fundo institucional |

- Para alertas, a cor vem sempre com o triângulo amarelo e a palavra "ATENÇÃO". Isso cumpre a regra "cor e texto".
- **Faixa de chamada recorrente** (série PET): uma barra vermelha de largura total com "Procure o posto de saúde", seguida de "Cuidar da sua saúde é cuidar da sua vida!".

### Tipografia (identificada visualmente; confirmar com os arquivos)
| Uso | Fonte provável | Onde |
| --- | --- | --- |
| Títulos e textos | **Poppins** (Regular, SemiBold, Bold e Bold Italic) | quase todos os vídeos; é a voz principal |
| Logo "TELESSAÚDE" | **Exo 2** Bold (ou parecida) | cartão final |
| Números grandes e títulos institucionais | sans condensada, tipo **Bebas Neue / Oswald** | Retrospectiva, Kits |
| Texto "técnico", espaçado | **monoespaçada**, talvez a fonte "Computer" | Diabetes pt 2 ("Glicemia em jejum", "um simples exame…") |
| Palavra de impacto | **contorno sem preenchimento** (outline) | "Lepra?", "BOA!", "ÉGUAS", "RAPAZ…", "BRASIL" |
| Toque humano | manuscrita ou script | "Hanseníase" (Outubro), "maranhão" (Glaucoma), "ATENÇÃO!" de marcador (Kits, Hipertensão) |

Padrão de hierarquia: uma linha pequena e leve com a palavra-chave grande e pesada embaixo. Exemplos: "Você tem / **DIABETES?**", "O acompanhamento é / **ESSENCIAL**", "Exame de / **Fundo de Olho**". Títulos de tema às vezes vêm quebrados em sílabas empilhadas: "HAN/SE/NÍA/SE", "PRE/VE/NIR", "HIPER/TENSÃO".

### Personagens e imagens
- **Ilustração vetorial 2D** de pessoas recortadas sobre fundo claro, com sombra suave projetada (efeito de adesivo). Cada vídeo tem um ou dois protagonistas fixos que trocam de pose: apontar, mão no queixo, mãos abertas, polegar para cima.
- **Diversidade real:** pessoas negras e brancas, crianças, idosos, famílias, homens e mulheres de várias idades.
- A série PET às vezes usa **cenas ilustradas completas** (quintal, rua, UBS) no lugar do recorte, como em Dengue e Obesidade.
- Ícones de apoio em estilo 3D ou flat colorido aparecem ao redor do personagem: termômetro, coração, rim, cérebro, celular.
- Dados reais aparecem com fonte citada (gráfico do IBGE, Weekly Epidemiological Record).

### Linguagem
- **Voz maranhense e coloquial no gancho:** "Ei comadre", "Ei Mermã", "Ei meu parceiro", "Ei mano", "Vish", "Éguas", "Rapaz…", "Povo tem vergonha de falar disso, siô", "Tu tá é pálido".
- **Diálogo entre dois personagens:** um pergunta, o outro orienta. Isso aparece em Hipertensão, Hanseníase e Câncer de Pênis.
- **O texto na tela é a palavra-chave da fala, não a frase inteira.**

## 3. Estrutura narrativa observada (teleorientação)

| Bloco | Tempo típico | O que acontece |
| --- | --- | --- |
| Gancho | 0–6 s | personagem + chamada regional ou "Você sabia?"; texto entra com máquina de escrever |
| Nome e definição | 6–20 s | nome do tema gigante (às vezes em sílabas) + uma linha de definição |
| Orientação | 20 s – final −20 s | sintomas, causas, transmissão e exames em listas com marcadores; ícones surgem em volta do personagem |
| Alerta | ~ 70% do vídeo | troca de cor de fundo, triângulo, "ATENÇÃO" ou "Sinais de alarme" |
| Chamada | últimos 15–20 s | "Procure o posto de saúde / UBS" + app Meu SUS Digital (celular com botão "BAIXAR") na série SUS Digital |
| Fechamento | 3–6 s | logo animado; na série PET, mais as assinaturas |

Não aparecem nas referências: fonte da orientação na tela, frase "não substitui o atendimento", perfis das redes e site.

## 4. Gramática de movimento (efeitos que se repetem)

| Efeito observado | Exemplos | Nome no catálogo (`efeitos.md`) |
| --- | --- | --- |
| Máquina de escrever, letra a letra | "Milh…", "Sintomas: … equilíbrio", "DAS" | `type-on` |
| Texto entra desfocado e assenta | "Ei comadre", "1,7 milhões" | entrada com blur + fade |
| Itens de lista entram um a um | sintomas, causas, "Pelo APP você pode" | `stagger-in` |
| Ícones pipocam em volta do personagem | dengue (sintomas em círculos), hanseníase | `pop-in` + `stagger-in` |
| Marca-texto amarelo na palavra-chave | "não causa sintomas", "embaçar a visão" | `palavra-destaque` |
| Risco ou X vermelho sobre a palavra | "TRANSMISSÃO", "informação", "Saúde dos olhos" | (não catalogado: `risco`) |
| Personagem troca de pose com dissolução | todos | crossfade curto |
| Zoom no rosto (corte para close) | Hipertensão, Hanseníase Outubro | push-in / corte de escala |
| Layout inteiro empurrado para o lado | "HIPER TENSÃO" (Hipertensão 0:34) | slide / push |
| Cortina de barras coloridas | Hanseníase Outubro 0:34 (azul, lilás, roxo) | wipe em faixas |
| Revelação circular | final dos Kits | wipe circular |
| Dessaturar e voltar a cor | Obesidade pt 2 (alimentos cinza → coloridos) | (não catalogado: `cor-volta`) |
| Papel rasgado como moldura | Obesidade, Diabetes | textura de transição |
| Contador e números grandes | Retrospectiva, Kits | `contador` |
| Fotos tipo polaroide inclinadas | Retrospectiva, Kits | colagem |
| Legenda dinâmica palavra a palavra, com destaque | Tauá-Mirim | legenda estilo CapCut |
| Rota animada em mapa | Tauá-Mirim | traçado de rota |

**Ritmo:** a tela ganha um elemento novo a cada 1,5 a 2,5 s, e o layout inteiro muda a cada 4 a 8 s. A detecção automática de corte quase não achou cortes secos, porque as transições são suaves (dissolução, blur, empurrão) sobre fundo claro.

## 5. Som

- **Trilha contínua sob toda a narração:** não há silêncio acima de 0,8 s a −45 dB em nenhum vídeo, exceto no último segundo.
- **Os 6 s finais medem exatamente −15,8 LUFS** em Glaucoma, Kits, Retrospectiva e Tauá-Mirim. Isso indica um **som de logo padrão** no fechamento; vale pedir esse arquivo.
- **O loudness integrado varia muito: de −22 a −10 LUFS** (média de cerca de −16,5). Não existe um padrão hoje. O alvo de −14 LUFS do manual vai deixar o volume uniforme entre vídeos.

## 6. Área segura: o principal ponto de atenção

Com a máscara x 65–888 e y 288–1248 sobreposta (`area-segura/_painel.jpg`), **nenhuma referência respeita a área segura:**
- Os títulos ficam no topo, entre y ≈ 60 e 250, acima do limite de 288 px.
- O texto e os ícones passam da borda direita (x > 888).
- O rosto ou o corpo do personagem descem abaixo de 1248 px, na faixa que as redes cobrem com legenda e botões.

Seguir a área segura vai **mudar a cara dos vídeos.** Os títulos descem cerca de 230 px e o conteúdo se concentra num retângulo de 823 × 960. É possível manter a identidade assim: o fundo, o cenário e o corpo do personagem continuam usando a tela toda, e só o texto e o rosto entram no retângulo.

## 7. Divergências entre o manual e a prática

| Tema | Manual | Referências | Sugestão |
| --- | --- | --- | --- |
| Vinheta de abertura | 0–3 s com logo e trilha | não existe; o vídeo abre no gancho | seguir a prática: sem vinheta, logo só no fechamento (o próprio manual já admite isso no Reels e no Shorts) |
| Duração | 60 s | 65–144 s, em partes 1 e 2 | decidir se o alvo passa a ser 60–90 s |
| Legenda | legenda completa fixa em todo vídeo | não há legenda; só palavras-chave cinéticas (exceto Tauá-Mirim) | decidir: legenda completa, palavras-chave ou as duas |
| Fechamento | fonte, aviso, assinaturas, redes, site, 6–7 s | só logo animado (+ assinaturas PET), 3–6 s | decidir se a cartela ganha fonte, aviso e redes |
| Transições | corte seco + no máximo 2 tipos | 4 a 6 tipos por vídeo | manter a variedade como estilo ou limitar |
| Paleta | 3 cores por quadro, destaque só no alerta | cor do tema forte em fundos inteiros | registrar a "cor do tema" como papel da paleta |
| Régua | posição definida; duração em aberto | o vídeo inteiro | **pendência resolvida pela prática: o vídeo inteiro** (só confirmar) |
| Loudness | −14 LUFS | −22 a −10 | manter o manual |
| Área segura | x 65–888, y 288–1248 | não respeitada | manter o manual e adaptar o layout (ver seção 6) |

## 8. Estilo transferível × conteúdo das referências

**Estilo para levar adiante:** fundo claro com cor do tema; personagem 2D recortado com sombra suave; Poppins com hierarquia leve/pesada; texto de palavra-chave com máquina de escrever; marca-texto e risco; ícones que pipocam ao redor; chamada regional no gancho; régua o vídeo inteiro; fechamento com o logo montando; trilha contínua com som de logo no fim.

**Conteúdo que fica de fora:** os textos, dados, personagens específicos e a sequência de cenas de cada vídeo. Um vídeo novo usa os mesmos recursos com o roteiro dele.

## 9. Pendências que esta análise gerou

1. Arquivos das fontes: Poppins, Exo 2 (logo), a condensada da Retrospectiva e a monoespaçada ("Computer"?).
2. Os três PNGs da régua, um por parceiro.
3. O logo animado do fechamento e o som de logo, como arquivos, para não recriar.
4. As decisões da seção 7: vinheta, duração, legenda, cartela, transições e área segura.

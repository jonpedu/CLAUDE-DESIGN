# AVC (Acidente Vascular Cerebral): estudo da edição

Versão final: **AVC v4.1** (`renderizando/AVC v4.1.mp4`), 16/11/2026, com a capa `CAPA AVC v4.1.png` (a capa aprovada na v1). A v4.1 é a v4 com a quebra de linha "Se você perceber / esses sinais," corrigida, refeita só no trecho 21,87–30,20 s com `ferramentas/trocar_trecho.py` (o resto do vídeo é idêntico à v4, sem recodificação).
Este documento registra o que entrou no vídeo, quando e com que técnica, e o que mudou em cada revisão, para servir de estudo e para pedidos mais precisos nos próximos vídeos. Tempos em segundos do vídeo final (ex.: `13,48` = 0:13,48).

---

## 1. Ficha técnica

| Item | Valor |
|---|---|
| Formato | 9:16, 1080×1920, 30 fps, H.264 (CRF 12, preset slow, quadros capturados em PNG), AAC 320 kbps, 48 kHz |
| Duração | 65,6 s (narração original: 53,0 s) |
| Volume | −14 LUFS integrado, pico ≈ −1,3 dBFS (loudnorm em duas passadas) |
| Cenas | 13 (C1 a C11, com C8 e C9 divididas em a/b) |
| Fonte da animação | `renderizando/_claude/animacao/completo_v4.html` |
| Mixagem | `animacao/mix_v4.json`, gerada por `gera_mix_v4.py` |
| Narração | `animacao/narracao_v4.wav` = `audio completo avc.wav` editado (`ferramentas/narracao.py`) + take **v2** de "reconhecer os sinais pode salvar vidas" |
| Régua e fechamento | `elementos/Ajustada TELE e PETSAUDE Digital.png` e `elementos/Intro NTS e PETSAUDE.mp4` (PET-Saúde, fornecidos pela equipe, sem alteração) |
| Trilha | `Balanced Learning Loop (Remix) v2.mp3`, −11 dB, ducking de 5 dB, a partir dos 12 s da música |
| Ferramentas | `animar.mjs` (motor), `ts-anim.js`, `telessaude.css`, `transcrever.py`, `narracao.py`, `bordas.py`, `recortar.py`, `sfx.py`, `mixar.py`, `folha.py` |

### Pipeline

1. **Transcrição com tempo por palavra** (`transcrever.py`).
2. **Edição do tempo da narração** (`narracao.py`): corta só dentro dos silêncios e devolve a função `N(t)`, que converte o tempo de uma palavra no áudio original para o tempo do vídeo. Todo evento da página é escrito como `N(palavra)`, então mudar uma pausa não desalinha nada.
3. **Página HTML como linha do tempo** (`render(t)` determinístico) → motor `animar.mjs` (Chrome quadro a quadro, workers em paralelo, cópias de busca rápida dos clipes).
4. **Quadros de prova** (`FOTOS="t1,t2"` + `folha.py`, com a área segura sobreposta) antes de cada render completo.
5. **Mixagem** (`mixar.py`): narração, trilha com ducking, efeitos sonoros, áudio do fechamento, −14 LUFS.

---

## 2. Narração (tempo editado)

| Onde (áudio original) | Mudança | Por quê |
|---|---|---|
| início | silêncio inicial aparado (0,2 s): a voz começa em 0,07 s | a narração já abre no assunto; o gancho visual vem junto (pedido da v3) |
| 3,00 s (depois de "ou AVC,") | +0,6 s | compensa o início antecipado e dá tempo à íris que entra no cérebro |
| 10,70 s (fim de "…no cérebro.") | +0,5 s | o cartão do sangramento respira |
| 13,30 s (depois de "de repente") | +0,8 s | o título "Atenção aos sinais" viaja até o topo antes do 1º cartão |
| 22,35 s (fim de "…entender.") | +0,5 s | a grade final dos sinais fica 1 s inteira na tela |
| 37,00 s (fim de "…30 minutos.") | +0,6 s | o relógio fecha a janela das 4h30 |
| 44,10 s (fim de "…192.") | +0,5 s | o 192 e a ambulância ficam na tela |
| 57,01 s | take v2 de "reconhecer os sinais pode salvar vidas" | o texto final do roteiro ganhou voz (v2: −17,0 LUFS, igual à narração; o v1 estava 5 dB mais alto e com pico acima de 0 dB) |

---

## 3. Linha do tempo cena a cena

| Cena | Tempo | Fala | Base visual | Saída / transição (e por quê) |
|---|---|---|---|---|
| **C1** gancho | 0,00–3,85 | "O Acidente Vascular Cerebral, ou AVC," | tela azul; cérebro recortado; "Você sabe o que é" (Light) fica; "AVC?" se abre em **A**cidente / **V**ascular / **C**erebral; em "ou AVC" as iniciais ficam amarelas | **íris que fecha no cérebro** (3,05): entramos no cérebro |
| **C2** | 3,05–8,40 | "…acontece quando uma parte do cérebro deixa de receber sangue…" | T03 (personagem apresenta o cérebro, a artéria entope) | **o cérebro do clipe vira o cérebro do cartão** (7,70–8,40): a câmera leva o cérebro ao lugar e ao tamanho exatos do cartão seguinte, com dissolução |
| **C3** | 7,90–11,50 | "…ou quando ocorre um sangramento no cérebro" | cartão "deixa de receber sangue" + "ou" + cartão "sangramento" (gotas que saltam) | **cartão azul que sobe** com mola |
| **C4** | 10,85–15,45 | "Os sinais costumam surgir de repente" | triângulo amarelo, "Atenção / aos sinais", "costumam surgir" (Light, digitado), **etiqueta** amarela inclinada "de repente" | **painel que sobe** + o título viaja até o topo da C5 (elemento compartilhado) |
| **C5** | 14,85–25,20 | boca torta · fraqueza em um lado do corpo · parte do corpo "pesada" · dificuldade para falar ou entender | 4 cartões com pessoas recortadas, em **5 etapas de escala e posição** (ver 4.3) | **empurrão para a esquerda** |
| **C6** | 24,60–31,30 | "Se você perceber esses sinais, não espere melhorar e procure atendimento imediatamente" | T05 (o familiar pega o telefone) | **varredura de relógio** (a próxima fala é sobre tempo) |
| **C7** | 30,60–39,50 | "A chance de um tratamento… sem sequelas… em até 4 horas e 30 minutos" | enfermeiro grande que diminui, cérebro com lupa, check verde → enfermeiro com prancheta grande no centro → **ampulheta que gira e vira o relógio** grande, que encolhe enquanto o texto aparece | **empurrão para a esquerda** |
| **C8a** | 38,90–43,40 | "Em caso de suspeita, procure um serviço de urgência" | T02 (aponta a unidade de urgência) | **corte com soco** + borda vermelha de sirene |
| **C8b** | 43,40–47,40 | "…ou acione o SAMU pelo número 192" | "SUSPEITA DE **AVC?**", celular discando 1-9-2, SAMU / LIGUE / **192**; ambulância passa, volta e para; o celular cresce girando, com a base saindo pela borda | **empurrão para cima** |
| **C9a** | 46,80–52,30 | "Para prevenir o AVC, controle a pressão arterial, não fume" | T01 (caminha; o aparelho de pressão e o cigarro surgem no clipe no tempo da fala) | **desfoque com zoom** + o **aparelho de pressão do clipe vira o 1º item da lista** |
| **C9b** | 51,75–57,10 | "…pratique atividade física e mantenha uma alimentação saudável" | "Prevenir é cuidar da saúde"; lista com check verde; tênis e prato entram grandes e encolhem até a linha; a lista sobe com mola | **painel azul que sobe** |
| **C10** | 56,46–61,70 | "reconhecer os sinais pode salvar vidas" (take v2) | cérebro, "AVC:", "reconhecer os sinais" (Light), "pode **salvar vidas**" (marca-texto amarelo) | **íris branca que abre** o fechamento |
| **C11** | 60,96–65,56 | — | fechamento da equipe (vídeo e som) | fim |

A régua fica por cima de tudo, do primeiro ao último quadro. O quadro 0 é a capa aprovada.

---

## 4. Técnicas (catálogo)

### 4.1 Curvas
Mola (`mola`, `molaViva`) em quase todas as entradas e reposicionamentos; `inOut` em câmera e transições; `in` nas saídas. Ver o estudo do IAM para a definição de cada curva.

### 4.2 Elemento que vira o próximo (metamorfose)
| Onde | De → para | Como |
|---|---|---|
| C1 → C2 | cérebro do gancho → cena do cérebro | íris centrada no cérebro |
| C2 → C3 | cérebro do clipe → cérebro do cartão 1 | cérebro **medido no quadro do clipe** (centro 776×850, 522 px); câmera com origem nele, escala 522 → 330 px e translação até o centro do cartão; dissolução nos últimos 0,3 s |
| C4 → C5 | título "Atenção / aos sinais" (2 linhas, branco) → cabeçalho (1 linha, azul) | as duas palavras viajam separadas, com 0,18 s de defasagem para não se cruzarem; cor interpolada |
| C7 | ampulheta → relógio | a ampulheta surge onde estava o cérebro, gira 180° (o tempo corre), voa em arco para o centro crescendo e se dissolve no relógio |
| C9a → C9b | aparelho de pressão do clipe → ícone do 1º item | aparelho medido no quadro (281 px, centro 801×653); a camada `#morph` com o ícone da folha nasce sobre ele, voa em arco e encolhe até o círculo da linha 1 |

### 4.3 Escala dinâmica: quanto menos elementos, maiores
Regra central do usuário: cada elemento novo faz os outros se redimensionarem e se reposicionarem; nada cresce quando outro entra; nada fica esperando com espaço vazio.

- **C5, cartões em 5 etapas** (centro x, centro y, escala):

| Etapa | Cartão 1 | Cartão 2 | Cartão 3 | Cartão 4 |
|---|---|---|---|---|
| 1 (boca torta) | 540, 820, 135% | | | |
| 2 (fraqueza) | 330, 640, 100% | 720, 1020, 100% | | |
| 3 ("pesada") | 300, 565, 85% | 750, 690, 85% | 400, 1060, 105% | |
| 4 (falar/entender) | 290, 545, 78% | 760, 600, 78% | 290, 935, 78% | 720, 1060, 102% |
| final | 350, 612, 90% | 730, 690, 90% | 350, 1015, 90% | 730, 1095, 90% |

A grade final é **alternada** (coluna direita mais baixa). Nenhum cartão cobre outro em nenhum momento; na etapa final, os de baixo se movem primeiro.
- **C7, enfermeiro:** 120% sozinho → 105% quando o cérebro entra → 90% em "sem sequelas"; o texto sai e o enfermeiro da prancheta cresce no centro (120%); sai antes de o relógio entrar.
- **C7, relógio:** entra a 145% no centro e encolhe e sobe a cada linha ("em até" 120%, "4 horas" 110%, "e 30 minutos" 100%); o texto acompanha a base do relógio.
- **C9b, lista:** os ícones novos entram a 200% abaixo da lista, encolhem até a linha e o texto sai deles; a lista inteira sobe 36 px com mola a cada item novo; tudo a 100% de opacidade.
- **C8b, celular:** depois de discar, cresce 30% girando no sentido horário, com a base saindo pela borda e o 192 visível.

### 4.4 Texto
- **Pesos da Poppins:** Light (300) nas linhas de apoio ("Você sabe o que é", "costumam surgir", "Se você perceber…", "em até", "LIGUE", "reconhecer os sinais"); Light Itálico em "A chance de um tratamento"; ExtraBold/Black nas palavras-chave (AVC, sangue, sangramento, sem sequelas, 192).
- **Destaques:** marca-texto ("sangue", "pesada", "imediatamente", "sem sequelas", "urgência", "saúde", "salvar vidas"), **etiqueta** inclinada ("de repente"), digitação ("Você sabe o que é", "cidente / ascular / erebral", "costumam surgir").
- **Cores:** azul da marca na estrutura; vermelho só em sangue, sangramento, "não espere", urgência, "e 30 minutos", SAMU; amarelo em detalhes (iniciais A·V·C, triângulo, etiqueta, "AVC?" do título do SAMU, marca-texto final); verde Secondary nos checks da prevenção.

### 4.5 Clipes e recortes
- **Clipes do Flow** (todos em largura cheia, porque tocam laterais ou base; `bordas.py`): T03 cérebro (C2), T05 familiar com telefone (C6), T02 unidade de urgência (C8a), T01 prevenção (C9a). O T04 (personagem com homem de camiseta azul) não entrou.
- **Recortes** (`recortar.py`, `CHROMA=1`) em `_claude/camadas/`: cérebros (`cerebro_raio`, `cerebro_bloqueio`, `cerebro_sangra`, `cerebro_lupa`), pessoas dos sinais (`idoso_cadeira`, `mulher_braco`, `idoso_curvado`, `homem_sofa`), enfermeiros (`enf_aponta`, `enf_prancheta`, `enf_bracos`), `ampulheta`, `relogio430`, `ambulancia2`, ícones de prevenção (`pressao`, `nao_fume`, `tenis`, `prato`). O sofá foi cortado antes da pessoa ao lado na folha, e o corte fica colado na borda do cartão (margem fantasma).
- **Gráficos em código:** relógio com setor vermelho que cresce até 4h30, celular com teclado, triângulo, telefone, ondas, check verde, gotas.

---

## 5. Som

| Camada | Tratamento |
|---|---|
| Narração | `narracao_v4.wav`, 0 dB (referência) |
| Trilha | −11 dB, começa aos 12 s da música (a introdução é 7 dB mais baixa), ducking de 5 dB; nas pausas fica entre −22 e −27 LUFS; cruza com o som do fechamento |
| Fechamento | áudio do `Intro NTS e PETSAUDE.mp4`, −2 dB, entrada de 0,6 s |
| Efeitos | **51** eventos sintetizados (`biblioteca-sfx/sintetizados/`), −5 dB gerais |

**Regra de densidade (devolutiva da v3):** um som por gesto que importa, no máximo ~1 efeito a cada 0,7 s, whoosh só nas transições, nenhum som para movimento secundário. Na cena do 192, eram 13 efeitos em 3 s e ficaram 6: soco da entrada, SAMU, ambulância (uma vez) e as três teclas.
Sons de interface usados: digitação gerada do próprio texto (`sfx.py --digitar`), pop em escala nos cartões, tiques a cada hora que o ponteiro passa, swish nos marca-textos.

---

## 6. Histórico das revisões

| Versão | Pedido do usuário | O que mudou | Virou regra? |
|---|---|---|---|
| v1 → v2 | gancho com 2,5 s de silêncio antes da voz | voz em 0,4 s; a pergunta se funde à 1ª frase | sim (teleorientacao.md) |
| v1 → v2 | cartões de sinais lentos, espaço vazio | cartão entra grande no centro e vai para a grade | revisada na v3 |
| v1 → v2 | enfermeiro parado | elementos que interagem, cronômetro → relógio | sim |
| v1 → v2 | 192: ambulância, celular discando | celular com teclado e ambulância | — |
| v1 → v2 | lista estática | ícone grande que encolhe até a linha | sim |
| v1 → v2 | texto final sem voz | take v2 narrado | — |
| v1 → v2 | trilha inaudível | −12 → −9 dB, ducking 5 dB, `"desde"`; bug do `mixar.py` (a trilha parava quando a narração acabava) corrigido com `apad` | sim (SKILL.md, som.md) |
| v2 → v3 | enfeites de borda: "odiei" | removidos | sim: nada de enfeite genérico |
| v2 → v3 | cartões cobriam uns aos outros | novo cartão em área livre; nenhum some ou esmaece | sim |
| v2 → v3 | enfermeiro virando de lado | só escala e troca de pose | sim |
| v2 → v3 | desfoque era na saída da C9a, não na entrada | entrada voltou ao empurrão da v1 | sim: comentário de transição = saída do motion |
| v2 → v3 | pressão do clipe → item da lista; cérebro do clipe → cérebro do cartão | metamorfoses medidas no quadro | sim |
| v2 → v3 | brincar com pesos de fonte; trilha −2 dB | Light/Itálico/Black; −11 dB | sim |
| v2 → v3 | capa v2 ruim | capa da v1 mantida | sim (vertical.md) |
| v3 (quadros) | "quanto menos elementos, maior" | etapas de escala nos cartões, enfermeiro, relógio; celular gira mostrando o 192; ambulância mais baixa | sim: regra central |
| v3 → v4 | voz mais cedo | silêncio inicial aparado, pausa compensada depois de "ou AVC" | — |
| v3 → v4 | enfermeiro da prancheta maior, ao centro | cresce no centro depois que o texto sai | — |
| v3 → v4 | efeitos sonoros demais | 85 → 51 eventos | sim (densidade) |
| v4 → v4.1 | "sinais," sozinho na 2ª linha | quebra manual: "Se você perceber / esses sinais,"; só o trecho refeito | sim: quebra de linha equilibrada; `trocar_trecho.py` |

---

## 7. Vocabulário útil para os próximos pedidos

- **Ligação entre cenas:** "o X do clipe vira o Y da próxima cena" (metamorfose medida), elemento compartilhado, íris a partir de um objeto, varredura de relógio.
- **Layout:** "escala dinâmica" (menos elementos = maiores), "grade provisória" e "grade final", "posições alternadas", "entra grande numa área livre".
- **Personagem auxiliar:** "na borda, saindo do quadro", "troca de pose com dissolução", "diminui quando o texto entra".
- **Texto:** Light na linha de apoio, Black na palavra-chave, etiqueta inclinada, marca-texto.
- **Som:** "um som por gesto", "sem som no movimento secundário".

Exemplo de pedido preciso: *"Na lista, cada ícone novo entra grande abaixo e encolhe até a linha; a lista sobe com mola; sem som na reorganização, só um pop quando o ícone aparece."*

# Hipertensão parte 2 (PET-Saúde), reconstrução horizontal: estudo da edição

Versão final aprovada (15/11/2026): `renderizando/Hipertensão parte 2 - horizontal.mp4`, com a capa `renderizando/CAPA Hipertensão parte 2 - horizontal.png`, que também é o primeiro quadro do vídeo.
É a primeira reconstrução de um vídeo vertical já publicado em 16:9. O vídeo-base (`video base vertical/Hipertensão PET SAUDE parte 2.mp4`) define as cenas, as falas e o tempo. A horizontal mantém as mesmas cenas e a mesma ordem, mas a diagramação é outra e muitos elementos são novos.
Este documento registra o que entrou no vídeo, quando, com que técnica e o que mudou em cada revisão. Serve de estudo e de vocabulário para as próximas reconstruções. Tempos em segundos do vídeo final (ex.: `13,48` = 0:13,48).

---

## 1. Ficha técnica

| Item | Valor |
|---|---|
| Formato | 16:9, 1920×1080, 30 fps, H.264 (CRF 12, preset slow, quadros em PNG), AAC 192 kbps, 48 kHz |
| Duração | 78,3 s, 2349 quadros (vídeo-base: 78,0 s; o fechamento ganhou 0,3 s para a intro horizontal terminar inteira) |
| Volume | −14,0 LUFS integrado, pico −1,3 dBFS (`mixar.py`, loudnorm em duas passadas) |
| Cenas | 11 blocos (A, B, C1, C2, D, E, F, G, H + capa no quadro 0) |
| Fonte da animação | `renderizando/_claude/animacao/hipertensao2_h.html` |
| Mixagem | `renderizando/_claude/render/mix_final.json` |
| Áudio | **Áudio original do vertical** (narração + trilha + efeitos, sem alteração) até 73,8 s; por cima, 69 efeitos novos; no fim, o final da trilha prolongado e o som da intro horizontal |
| Régua | `Ajustada TELE e PETSAUDE Digital.png` como **ilha** branca centralizada na base, a 760 px de largura (redução proporcional autorizada) |
| Fechamento | `Intro NTS e PETSAUDE - horizontal.mp4` em tela cheia, com o **som dele** (o do vídeo-base estava desatualizado) |
| Trilha | `Regulate - Dyalla.mp3` (já embutida no áudio do vertical; usada à parte só para prolongar o final) |
| Ferramentas | `animar.mjs` (agora com `TELA=1920x1080`), `componentes.py` (novo), `trocar_trecho.py`, `mixar.py` (agora com `"ate"` na narração), `faster-whisper` (tempo por palavra), `sfx.py` + `impacto.wav` (novo) |
| Scripts deste vídeo | `renderizando/_claude/decupagem/`: `mapear.py`, `comparar.py`, `placa_vermelha.py`, `recorte_vermelho*.py`, `camadas_ext.py`, `camadas_el.py`, `extra_vermelho.py`, `palavras.txt` |

### 1.1 Pipeline da reconstrução

1. **Conferência do pacote, com confirmação de cada item obrigatório:** régua, fechamento, som e trilha. A regra de sempre confirmar nasceu aqui.
2. **Áudio:** transcrevi a narração avulsa (`audios/audio 1.wav`) e o áudio do vídeo para checar se a fala estava completa (estava, com ~0,1 s de diferença). Depois, tirei o **tempo de cada palavra** (`decupagem/palavras.txt`), que guiou todas as entradas.
3. **Mapa de telas:** `mapear.py` compara cada quadro do vertical (a 10 fps) com as 21 telas do Canva e devolve em que intervalo cada uma aparece. Daí saíram os tempos das cenas.
4. **Camadas.** A fonte melhorou ao longo do trabalho:
   - telas do Canva achatadas (fundo branco): recorte automático por componentes;
   - telas com fundo cinza em degradê: correção de campo plano usando a tela vazia (`17.png`) como placa;
   - telas vermelhas: placa reconstruída por inpaint e transparência pela diferença de cor;
   - PNGs transparentes do Canva (`ext (N).png`, 1,5× maiores);
   - **elementos separados, um a um** (`elementos canva N.png`), a melhor fonte, que permitiu animar cada peça.
5. **Quadros-chave** em 16:9, lado a lado com o vertical e com a área segura de 96 px marcada (`comparar.py`). Aprovação antes de animar.
6. **Animação** por tempo (`render(t)`), num HTML só, com atributos declarativos (seção 4).
7. **Prévias** v1 a v8 (em `_claude/versoes-anteriores/`), uma devolutiva por versão.
8. **Final em qualidade máxima.** Os ajustes pontuais depois da aprovação entraram **só nos trechos alterados**, com `trocar_trecho.py`, sem recodificar o resto.

---

## 2. Narração (tempo por palavra, pontos de ancoragem)

| Tempo | Palavra | O que acontece na tela |
|---|---|---|
| 2,40 | "pressão" | a agulha bate no vermelho: impacto |
| 2,76 | "alta" | "PRESSÃO ALTA" cai com impacto |
| 6,48 / 7,06 | "não causa" / "sintomas" | marca-texto amarelo |
| 10,16 | "silenciosa" | silhueta "shh" + "doença silenciosa" |
| 14,56 | "elevados" | o medidor treme, com faíscas |
| 16,30 · 17,46 · 18,28 · 19,54 | dor de cabeça · tontura · visão · sensação | uma bolha por sintoma |
| 22,24 | "mais raros" | o coração entra grande e batendo |
| 27,08 / 28,30 | "rins" / "hormonais" | cartões |
| 29,86 | "hipertensão secundária" | a faixa azul entra entre os blocos |
| 32,82–34,58 | "o acompanhamento com profissionais de saúde" | digitação + três profissionais |
| 35,28 | "essencial" | "com" vira "é", e "ESSENCIAL" salta |
| 40,92 | "É muito importante" | sirene balançando + ondas |
| 52,04 / 52,90 | "sal" / "industrializados" | sal, depois a gôndola |
| 54,28 | "aumentar" | o medidor treme, com faíscas |
| 55,64 | "Já" | o verde varre da direita (virada ruim → bom) |
| 60,26 | "proteger o coração" | coração anatômico batendo + escudo + ondas verdes |
| 66,62 | "é possível controlar" | o título entra e os cartões descem |
| 70,54 | "garantindo" | a frase final, faíscas verdes; os cartões sobem |
| 73,00 | "vida." | fim da narração; fechamento a partir de 73,6 (som) / 73,9 (imagem) |

---

## 3. Linha do tempo cena a cena

| Cena | Intervalo | Fala | Diagramação 16:9 | Técnicas |
|---|---|---|---|---|
| **Capa** | quadro 0 | — | "PRESSÃO ALTA" gigante em degradê + "É possível **controlar**" com marca-texto + pílulas *sintomas · tratamento · alimentação* à esquerda; medidor no vermelho com o coração à direita; anéis e brilho vermelho | miniatura do WhatsApp; `padding-top` no título para o til não ser cortado |
| **A · gancho** | 0,0–4,6 | "Mesmo depois de entender o que é a pressão alta…" | medidor SVG grande no centro → encolhe para a esquerda; à direita, aferição + gota com raios atrás dos ombros | agulha subindo com tensão; **impacto** (onda, faíscas, tremor, clarão); *slam* do título; agulha vibrando no limite; escala dinâmica em 3,4 s; raios piscando; gota "batendo" |
| **B** | 4,6–11,8 | "…não causa sintomas… doença silenciosa." | cartão de borda "PRESSÃO ALTA"; texto à esquerda; medidor + coração separados à direita (grandes); ícone de mudo no alto | marca-texto desenhado; agulha subindo e vibrando; coração batendo; texto começa centrado e sobe quando "doença silenciosa" entra |
| **C1 (vermelha)** | 11,8–16,5 | "Quando aparecem… níveis muito elevados…" | título à esquerda, seta traçada até "Níveis muito elevados" + medidor; homem grande, cortado pela base, à direita | título começa no meio e sobe; escala do homem em degraus (mola); tremor + faíscas em "elevados" |
| **C2 (vermelha)** | 16,5–21,6 | "…dor de cabeça, tontura, visão embaçada e sensação de cansaço." | painel "Níveis muito elevados" no alto à direita; quatro **bolhas** translúcidas em alturas alternadas, com pílula branca | pop de cada bolha na palavra; ritmo orgânico (alto/baixo) |
| **D** | 21,6–32,25 | "Em alguns casos mais raros… hipertensão secundária." | coração + "Em casos mais raros" à esquerda; dois cartões (rins, hormonal) à direita; a faixa azul de borda entra entre o título e o texto | coração separado do título, grande e batendo, encolhendo em degraus; texto grande que encolhe; os blocos **se afastam** para a faixa entrar no meio; ondas no coração |
| **E1** | 32,25–35,0 | "Por isso, o acompanhamento com profissionais de saúde…" | frase digitada no centro + três profissionais embaixo | **digitação**; "profissionais de saúde" sai; **"com" apagado como digitação e trocado por "é"** |
| **E2** | 35,0–47,3 | "…é essencial… medicamentos… não interromper o tratamento…" | metade esquerda centrada em x 550: "O acompanhamento é / ESSENCIAL", três ícones em círculos, cartão dos medicamentos; metade direita centrada em x 1360: sirene, alerta em 3 linhas, prancheta | título e ícones começam grandes no centro e vão para a esquerda; a prancheta começa no meio e desce quando a sirene entra; sirene balança + 3 ondas |
| **F** | 47,3–61,8 | "As escolhas do dia a dia… sal… industrializados… frutas, verduras… proteger o coração." | abertura: título grande + verduras, exercício e sal em volta; depois a coluna do sal (gôndola, sal, setas, medidor) sobre o vermelho e a coluna das frutas (frutas, verduras, coração anatômico, escudo) sobre o verde | fundo vermelho → **varrida diagonal verde** da direita em "Já"; selos ✕/✓; palavras em vermelho e em verde; setas pulsando; medidor tremendo; coração batendo + ondas verdes; a coluna do sal começa centrada e vai para a esquerda |
| **G** | 61,8–73,9 | "Com o acompanhamento regular, alimentação equilibrada e tratamento adequado, é possível controlar… qualidade de vida." | três cartões (médico, cozinheira, prancheta), título no alto, frase verde embaixo | 1 cartão grande no centro → 2 → 3; descem quando o título entra e sobem quando a frase final entra; faíscas verdes |
| **H · fechamento** | 73,9–78,3 | — | intro horizontal em tela cheia | som da intro a partir de 73,6 (invade o fim de G); trilha prolongada cruzando |

Régua em ilha durante todo o vídeo. Transição padrão entre cenas: a nova entra por cima com fade e um leve recuo de escala (0,45 s).

---

## 4. Técnicas (catálogo)

### 4.1 Motor declarativo (`hipertensao2_h.html`)
Cada elemento descreve a própria animação nos atributos. O `render(t)` compõe tudo num único `transform`.

| Atributo | O que faz |
|---|---|
| `data-in="t"` + `data-fx` | entrada no tempo t: `sobe` (mola + desfoque), `pop` (back), `esq`/`dir` (desliza com mola), `fade`, `varre` (desliza 1100 px), `slam` (cai de 2,3× com quique), `marca` (marca-texto), `traco` (SVG se desenha) |
| `data-k="t:dx,dy,escala;…"` | **escala dinâmica / deslocamento**: estados por tempo, mola de 0,8 s entre eles. Em `.grupo` move um conjunto |
| `data-out="t"` | saída (encolhe e some em 0,4 s) |
| `data-pulso` | batimento (duas batidas por ciclo, ~66 bpm) |
| `data-pisca` | piscar irregular (raios) |
| `data-treme="t:amp;…"` | tremor de impacto que decai; vale para a cena inteira ou para um elemento |
| `data-alerta="t"` | balanço que amortece (sirene) |
| `data-sobe-loop` | sobe e desce sem parar (setas) |
| `data-dig` / `data-troca` | digitação e apagamento; troca de uma palavra por outra ("com" → "é") |
| `data-fundo="quente|misto|azul|verde"` | fundo vivo da cena |

### 4.2 Escala dinâmica e deslocamento suave
- O que está sozinho na tela fica **grande e centralizado**. A cada elemento novo, o conjunto encolhe e vai para o lugar final, com mola.
- Quando algo entra **acima**, o conjunto desce; quando algo entra **abaixo**, ele sobe (cartões de G, prancheta de E2, texto de B).
- Dois blocos que vão receber algo entre eles começam **próximos e se afastam** (D: título e texto, com a faixa no meio).

### 4.3 Medidor em SVG
O medidor das telas tinha a agulha "pintada", sem como animar. Redesenhei em SVG (arcos verde/amarelo/vermelho com as mesmas cores, pontas arredondadas e a agulha num grupo separado). Ângulo por tempo:
- **A:** a agulha sobe acelerando (cúbica) e treme cada vez mais, até bater em "pressão".
- **B:** a agulha sobe em 0,9 s e fica vibrando no limite (soma de dois senos).

### 4.4 Impactos pontuais
Ficam numa camada SVG redesenhada a cada quadro: **onda de choque** (anel que cresce e some), **faíscas** (pontos que se espalham e caem) e **tremor** da cena ou do elemento. Só entram em palavras de peso: "pressão", "elevados", "mais raros", "É muito importante", "aumentar", "proteger", "garantindo". O som é o `impacto.wav` sintetizado (baque grave + estalo).

### 4.5 Fundo vivo
Três manchas de cor bem diluídas (7–13%) se movem devagar como líquido, no azul do núcleo mais a cor do tema da cena, com uma textura de pontos azuis só nas bordas. Entra nas cenas claras e na capa. Tira o "branco frio" sem competir com o conteúdo.

### 4.6 Contraste ruim × bom (F)
- O fundo fica vermelho claro com o sal. Em "Já", um verde **varre da direita** num corte diagonal com filete branco.
- Selos ✕ e ✓ aparecem nos cantos.
- As palavras-chave ficam coloridas ("consumo excessivo" e "Aumento da pressão" em vermelho, "alimentos naturais" e "Protege o coração" em verde).
- O texto continua sendo só o do roteiro: o contraste fica na cor, nos símbolos e no movimento.

### 4.7 Bolhas dos sintomas (C2)
Círculos translúcidos (borda branca a 45%, sombra) com a figura recortada dentro e o rótulo numa pílula branca. As alturas são alternadas para um ritmo mais orgânico.

### 4.8 Texto digitado e troca de palavra (E1)
A frase completa da fala ("O acompanhamento com / profissionais de saúde") é digitada, para a tela não ficar parada enquanto a narração anda. A digitação usa `visibility` (a linha não pula). A saída é um apagamento: o "com" sai letra a letra, o "é" entra no lugar e o resto da linha continua, emendando na cena seguinte.

### 4.9 Recortes e camadas
- **Ordem de qualidade:** elementos separados do Canva > PNG transparente da tela > recorte de tela achatada > recorte de quadro do vídeo.
- `componentes.py` separa figuras por transparência (quando o PNG já é transparente), pelo branco ligado às bordas, por placa (campo plano ou diferença) ou pela matiz do fundo. Também gera uma folha numerada para escolher.
- **Recorte com borda cortada** (frutas, gôndola que saíam do quadro vertical) nunca fica solto: entra num **quadro** com o corte escondido na borda. Quando os elementos separados chegaram, os quadros deixaram de ser necessários.
- Personagem com contorno branco sobre degradê (médico, cozinheira): a correção de campo plano deixa o fundo branco puro, e o cartão branco absorve.

### 4.10 Régua, capa e fechamento
- **Régua em ilha:** 760 px, cantos de cima arredondados e sombra leve, por cima de tudo.
- **Capa:** é uma cena própria exibida só quando `t < 1/30` (substitui o quadro 0, sem deslocar o áudio).
- **Intro horizontal:** em tela cheia, sincronizada com o áudio dela (`busca(intro, t − 73,6)`).

---

## 5. Som

| Camada | Como entrou |
|---|---|
| Base | áudio original do vertical (narração, trilha e efeitos), sem alteração, até 73,8 s; corte com fade de 0,2 s logo depois de "vida." (`"narracao": {"ate": 73.8}`) |
| Efeitos novos | 69 efeitos, de −8 a −17 dB: pop nas entradas, whoosh nos deslocamentos e na varrida, swish no marca-texto, nas setas e na seta traçada, tique nos ícones e no "é", digitação na frase de E1, `impacto.wav` nos impactos (−8 dB no gancho, −14/−15 nos outros) |
| Final da trilha | `Regulate - Dyalla.mp3` alinhado ao áudio-base por correlação cruzada (**atraso de 0,021 s**, nível ≈ −24 dB no áudio-base); trecho de 1,8 s a partir de 73,6 s, com entrada de 0,2 s e saída de 1,4 s, cruzando com a intro |
| Fechamento | áudio da `Intro NTS e PETSAUDE - horizontal.mp4` a partir de 73,6 s (0,3 s antes da imagem), entrada de 0,3 s |
| Final | −14,0 LUFS, pico −1,3 dBFS |

---

## 6. Histórico das revisões

| Versão | Pedido do usuário | O que mudou |
|---|---|---|
| quadros-chave 1 | — | 6 quadros em 16:9 ao lado do vertical; régua em ilha |
| quadros-chave 2 | mão do médico mal recortada; a cena vermelha não pode sumir; afastar as coisas das bordas | médico por campo plano; cena vermelha refeita com placa reconstruída e depois com os PNGs transparentes; conteúdo entre x 200 e 1720 (depois virou regra de **distribuição**, não de margem fixa) |
| v1 | primeira versão | animação no tempo da fala; frutas em quadros |
| v2 | quanto menos elementos, maiores; mais efeitos sonoros | escala dinâmica em D, E, F e G; 38 efeitos |
| v3 | deslocamentos suaves (prancheta, cartões, título e texto se afastando) | `data-k` com vários estados; mesmo movimento aplicado em B, C1 e F |
| v4 | coração solto e batendo; textos sobrepostos; ruim × bom mais enfático | coração separado; texto sem sobreposição; fundo vermelho + varrida verde + selos |
| v5 | gancho sem graça; medidor e coração separados; impactos como no IAM | medidor SVG com agulha animada; impacto no gancho; impactos pontuais |
| v6 | coração maior; alerta largo demais e ícones desalinhados; elementos novos em F; régua e intro novas | ESSENCIAL reorganizado; F com elementos separados; régua Digital e intro horizontal |
| v7 | fundo branco frio | fundo vivo |
| v8 / final | gancho e cena 2 melhor distribuídos; homem novo; abertura "profissionais de saúde"; ícones centrados; sintomas mais bonitos | elementos separados no gancho; bolhas; digitação em E1; coluna esquerda de E2 centrada |
| final (ajustes pontuais) | raios atrás da gota; "Aumento da pressão" alinhado; passagem "com" → "é" | só os trechos 0:00–0:08, 0:26–0:43 e 0:52–1:08 re-renderizados com `trocar_trecho.py`; som da intro horizontal no fechamento; trilha prolongada |

---

## 7. Lições para as próximas reconstruções

- **Pedir os elementos separados do Canva logo no começo.** Eles resolveram de uma vez qualidade, recortes ruins e a liberdade de animar cada peça. O recorte de tela achatada é só um paliativo.
- **Confirmar com o usuário cada item obrigatório** (régua, fechamento, som de logo, trilha) com o nome exato do arquivo, mesmo quando ele está na pasta.
- **O som de logo do vídeo-base pode estar desatualizado:** use o do arquivo de intro entregue e prolongue a trilha para ela não parar seco.
- **Tempo por palavra** antes de animar: entradas na palavra certa evitam várias rodadas.
- **Aplicar as regras da skill desde a primeira versão** (escala dinâmica, deslocamento, fundo vivo, impacto pontual, bloco de avaliação), sem esperar o usuário apontar.
- **Distribuir pela cena inteira:** nada nas extremidades com o meio vazio; centralizar o que está sozinho.
- **Só o final aprovado vai para `renderizando/`;** prévias ficam em `_claude/versoes-anteriores/`.
- **Ajuste depois da aprovação = `trocar_trecho.py`:** re-renderiza só o intervalo entre quadros-chave (cerca de 8 s por trecho) em qualidade máxima.

---

## 8. Vocabulário útil para os próximos pedidos

- **Escala dinâmica / deslocamento suave:** "começa grande no centro e vai para o canto quando X entra"; "desce quando o título entra"; "se afastam para X entrar no meio".
- **Impacto:** onda de choque, faíscas, tremor, clarão, *slam* (cair com impacto).
- **Varrida diagonal:** uma cor nova atravessa a tela num corte inclinado e toma metade dela.
- **Fundo vivo:** manchas líquidas + textura de pontos nas bordas.
- **Bolha:** círculo translúcido com figura e pílula de rótulo.
- **Troca por digitação:** apagar uma palavra letra a letra e digitar outra no lugar.
- **Ilha (régua):** régua num cartão branco centralizado na base, sem ocupar a largura toda.
- **Quadro (para recorte):** moldura arredondada que esconde a borda cortada de um elemento.

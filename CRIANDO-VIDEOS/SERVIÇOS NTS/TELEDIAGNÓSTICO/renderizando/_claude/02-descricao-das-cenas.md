# Telediagnóstico: descrição das cenas (v4, 20/11/2026)

> **Atualização (20/11/2026):** a proposta do ChatGPT para as cenas 5, 6, 7, 9 e 10 chegou e está resumida em `03-proposta-chatgpt-cenas-5-6-7-9-10.md` (5A + 6A + 7A + 9A + 10A, com as adaptações do Claude). Ela vai substituir as descrições "a refazer" abaixo assim que for implementada. A cena 2 também mudou na v4: a faixa do título subiu (y 190) e entrou uma cota "a distância" entre o texto e o exame.

Vídeo institucional da série **Serviços do NTS** (Telessaúde Maranhão, NTS-UFMA). Formato vertical 9:16 (1080 × 1920 px, 30 fps), cerca de 62 s: 57,8 s de narração e depois o logo animado do Telessaúde.

**Situação das cenas**

| Cena | Situação |
| --- | --- |
| 1, 2, 3, 4 e 8 | refeitas pelo Claude na v4, a partir da devolutiva da v3 |
| 5, 6, 7, 9 e 10 | **a refazer**: o usuário não gostou da v3. O prompt da seção 5 pede uma proposta nova ao ChatGPT |
| 11 (logo) | aprovada |

Arquivos de referência:
- Página da animação: `animacao/telediagnostico_v4.src.html`.
- Quadros: `quadros/folha_v4.jpg`.
- Prévias:
  - `versoes-anteriores/Telediagnostico_previa_v4.mp4`, com as cenas 1, 2, 3, 4 e 8 novas;
  - `Telediagnostico_previa_v3.mp4`, com as cenas 5, 6, 7, 9 e 10 como estão hoje.

---

## 1. O que o vídeo precisa seguir

**Identidade**
- **Fundo:** branco ou gelo (`#FFFFFF`, `#F3F6FE`), com manchas de cor bem diluídas que respiram devagar.
- **Azuis:** `#365DCC` (principal) e `#1C306A` (escuro).
- **Verde-azulado:** `#19756F`, para o laudo e o "ok".
- **Fonte:** Poppins, com linha leve (300) e palavra-chave pesada (800).
- **Régua de marca:** fica fixa na base, de y 1760 a 1920, do primeiro ao último quadro. Nada importante passa por cima dela.
- **Área segura:** retângulo x 65–888, y 288–1248. Todo texto e toda informação **no momento em que é falada** fica dentro dela. Depois de falada, pode sair dela, mas só para um lugar que faça sentido (virar cabeçalho, ficar como marca, sair da tela).

**Regras do usuário (devolutivas)**
1. **Tela toda ocupada.** O vídeo também vai por WhatsApp, que mostra a tela inteira. O espaço é ocupado pelo **assunto da cena, grande**, ancorado na base ou saindo pela borda, e não por enfeite. Áreas vazias grandes são o erro mais criticado.
2. **Nada robótico nem centralizado em pilha.** O usuário não quer tudo pequeno no meio, parado.
3. **Tudo que entra afeta o que já está na tela.** Os vizinhos vibram, se deslocam ou encolhem com efeito de mola para abrir espaço. Listas: o item novo entra **grande no meio** e depois vai para o lugar dele, e a lista sobe para receber o próximo. Nada aparece direto na posição final.
4. **Não repetir o mesmo formato cena após cena** (ex.: tudo em cartão branco, só trocando o nome). Quem assiste cansa e pula. Cada trecho pede uma linguagem própria.
5. **Uma cena puxa a outra.** As transições preferidas:
   - **continuidade:** um elemento fica e muda de lugar ou de tamanho;
   - **metamorfose:** uma coisa vira a outra;
   - **arrasto:** tudo sai para um lado e o novo entra pelo outro.
6. **Fundo não passeia.** Mapa de marca d'água indo de um lado para o outro foi rejeitado.
7. **Alfinete só marca lugar de verdade.**
8. **Título nunca cortado por linha ou traço.**
9. **Logos de parceiros (UFG, UFMG): só o logo, grande e animado**, sem a sigla escrita ao lado.
10. **Pessoas vêm dos clipes do Google Flow.** O Claude não desenha pessoas.
    - Os clipes têm fundo branco e entram em modo "multiplicar". Por isso **nada colorido pode passar atrás da pessoa**.
    - A parte de baixo do jaleco **esmaece** (sem corte seco). Encostar na régua também é aceito.
11. **Efeitos sonoros discretos**, sem pop nem bolha: whoosh nas viradas, swish nas entradas, tique em itens de lista.
12. **O texto na tela só diz o que a narração diz.**

**Elementos disponíveis**

| Elemento | Detalhe |
| --- | --- |
| Doutor (clipe do Flow, vertical) | da cintura para cima, segura e toca um tablet; 3,9 s em vaivém |
| Doutora (clipe do Flow, vertical) | da cintura para cima, toca um tablet; 3,9 s |
| Logos (SVG) | UFG (hexágonos azuis + "UFG"), UFMG ("UFmG" com o "m" e a barra vermelhos), Telessaúde (vertical e horizontal) |
| Mapa (SVG) | Maranhão (dá para recortar de um mapa do Brasil com estados) |
| Desenhos do Claude (SVG) | papel de exame com traçado de ECG, laudo com check verde, olho/retina, fita de ECG, pulmão, relógio, ícones (gráfico, imagem, dados, sinal de wi-fi, lupa, casa/UBS, setas) |
| Fechamento | `Intro Telessaude.mp4` (logo animado com som) |

---

## 2. Narração, com tempos

| Cena | Tempo (s) | Fala |
| --- | --- | --- |
| 1 | 0,0–8,1 | O exame foi feito aqui, mas quem vai dar o laudo está em outro lugar. Como resolver? Com o telediagnóstico. |
| 2 | 8,6–11,8 | É um serviço feito a distância, com o apoio da tecnologia. |
| 3 | 12,6–18,2 | Gráficos, imagens e dados são enviados a um profissional de saúde, que emite um laudo ou um parecer. |
| 4 | 19,0–23,2 | O Telessaúde Maranhão oferece serviços de telediagnóstico, |
| 5 | 23,2–26,4 | como a telerretinografia, em parceria com a UFG, |
| 6 | 26,4–29,4 | e o eletrocardiograma, em parceria com a UFMG. |
| 7 | 29,4–36,5 | Ampliando essa oferta, o núcleo avança na incorporação da tele-espirometria, também em parceria com a UFMG. |
| 8 | 37,1–45,9 | Essas iniciativas contribuem para ampliar o acesso aos exames, qualificar o diagnóstico e fortalecer a Atenção Primária à Saúde nos municípios maranhenses. |
| 9 | 46,6–53,6 | Ah, e essa distância pode ser de lugar, quando quem analisa está em outro local, ou de tempo, quando a análise é feita em outro momento. |
| 10 | 54,7–57,5 | Telediagnóstico: o laudo chega, mesmo a distância. |
| 11 | 57,9–62,3 | (logo animado do Telessaúde) |

**Palavras-âncora (s):**

| Cena | Âncoras |
| --- | --- |
| 1 | exame 0,42 · aqui 1,28 · quem 2,18 · laudo 2,86 · lugar 3,84 · Como resolver 4,84 · telediagnóstico 6,72 |
| 2 | distância 9,66 · tecnologia 11,18 |
| 3 | gráficos 12,60 · imagens 13,26 · dados 13,86 · enviados 14,4 · profissional 15,12 · laudo 17,16 · parecer 17,92 |
| 4 | Telessaúde 19,14 · Maranhão 19,86 · oferece 20,36 · telediagnóstico 21,56 |
| 5 | telerretinografia 23,18 · UFG 25,34 |
| 6 | eletrocardiograma 26,44 · UFMG 28,56 |
| 7 | Ampliando 29,40 · núcleo 31,5 · incorporação 32,38 · tele-espirometria 33,20 · UFMG 35,80 |
| 8 | ampliar 38,82 · qualificar 40,76 · fortalecer 42,38 · municípios 44,82 |
| 9 | distância 47,36 · lugar 48,38 · local 50,32 · tempo 51,30 · momento 53,28 |
| 10 | Telediagnóstico 54,68 · laudo 55,66 · chega 55,94 · distância 57,02 |

---

## 3. Cenas como estão na v4

### Cena 1: gancho (0,0–8,1 s), refeita
- **0,0–2,0 s:** tela única. O papel de um exame (folha com grade e traçado de ECG) sobe de baixo, grande, ancorado na régua, e o traçado se desenha. No alto, centralizados, "o exame foi feito" (leve, 68 px) e logo abaixo "aqui" (210 px, peso 800, azul-escuro).
- **2,0 s:** a tela se divide numa linha pontilhada em y 960.
  - **Metade de baixo ("aqui"):** fundo azul bem claro, o papel à direita e o texto à esquerda.
  - **Metade de cima ("lá"):** o doutor do Flow desce à direita, com o jaleco esmaecendo antes da divisa. À esquerda, entram um a um: "quem dá" (leve), "o laudo," (peso 800) e "lá" (250 px, azul). Quando entra "lá", as linhas de cima sobem um pouco e o doutor cresce de leve, com mola.
- **4,84 s, "Como resolver?":** um "?" grande (círculo branco de 300 px) aparece na divisa, à direita, balançando. As duas metades se afastam um pouco com mola e voltam.
- **6,62 s, "telediagnóstico":** o "?" some, e da divisa nasce uma **faixa azul** de ponta a ponta, levemente inclinada, com "Telediagnóstico" em branco. A faixa é a ponte entre o aqui e o lá. As metades se ajeitam para abrir espaço.
- **Capa sugerida:** cerca de 7,6 s.

### Cena 2: o que é (8,6–11,8 s), refeita
- **8,7 s:** a faixa sobe e vira uma **barra no alto** (y 300) com o título menor. Ela fica até o fim da cena 3. O doutor vai para o alto à direita, e o exame desce para a parte de baixo à esquerda, maior. A divisão de tela se desfaz.
- **9,66 s, "a distância":** entra "a distância" à esquerda, ao lado do doutor. O doutor e o exame se afastam mais um pouco, com mola.
- **10,45 s, "com o apoio da tecnologia":** um **círculo de sinal (wi-fi)** entra embaixo à direita, entre o exame e o doutor.
- **11,25 s:** quadradinhos de dados saem do exame, passam pelo sinal e sobem até o tablet do doutor.

### Cena 3: como funciona (12,6–18,2 s), refeita
- **12,0 s:** aproximação. O doutor cresce até ficar grande à direita, encostado na régua. O exame continua pequeno embaixo à esquerda.
- **12,60, 13,26 e 13,86 s:** "gráficos", "imagens" e "dados" (cada um com ícone) entram um a um, grandes, no mesmo lugar livre à esquerda. A cada palavra nova, as anteriores sobem com mola, formando a lista.
- **14,4 s, "enviados":** os ícones voam em arco até o tablet do doutor, e o tablet pulsa ao receber.
- **15,12 s, "profissional de saúde":** o doutor reage (cresce de leve).
- **17,1 s, "laudo":** um laudo (folha com check verde) sai do tablet e voa até pousar sobre o exame, embaixo à esquerda. A lista encolhe e sobe para abrir espaço, e a etiqueta verde "laudo ou parecer" entra acima do laudo.
- **18,45 s:** tudo sai (arrasto).

### Cena 4: Telessaúde Maranhão (19,0–23,2 s), refeita
- **19,14 s, "Telessaúde":** o hexágono do logo do Telessaúde (arquivo da marca, sem alteração) entra grande no centro, girando com mola.
- **19,86 s, "Maranhão":** o nome "TELESSAÚDE / Maranhão UFMA" sobe por baixo do hexágono.
- **20,36 s, "oferece":** o logo sobe e encolhe, e entra "oferece serviços de".
- **21,56 s:** o logo sobe mais e entra "telediagnóstico" grande, com marca-texto amarelo.
- **20,6 a 21,0 s:** três círculos grandes (ECG, olho, pulmão) sobem pela base e ficam espiando, cortados pela régua.

### Cena 5: telerretinografia + UFG (23,2–26,4 s), a refazer
- **23,0 s:** o círculo do olho cresce até ocupar a tela (círculo azul-claro com um olho grande).
- **23,18 s:** "telerretinografia" no alto.
- **23,6 s:** uma varredura passa pelo olho, e em 24,55 s há um flash de foto.
- **25,25 s:** o logo da UFG entra animado (os hexágonos giram, as letras sobem).
- **Devolutiva da v3:** não gostou.

### Cena 6: eletrocardiograma + UFMG (26,4–29,4 s), a refazer
- **26,4 s:** a câmera mergulha na pupila (flash), e aparece uma fita de ECG em papel quadriculado ocupando a parte de baixo. O traçado vermelho se desenha da esquerda para a direita.
- "eletrocardiograma" fica no alto.
- **28,5 s:** o logo da UFMG entra grande, com as letras subindo e a barra vermelha se desenhando.
- **Devolutiva da v3:** não gostou.

### Cena 7: tele-espirometria (29,4–37,1 s), a refazer
- **29,4 s:** a fita encolhe para a base, e o traçado do ECG vira uma onda lenta (a respiração). O olho e o ECG viram dois selos pequenos nos cantos do alto, e o logo da UFMG vai pequeno para o canto de baixo.
- **30,0 s:** um "+" tracejado aparece no meio.
- **32,38 s:** o "+" cresce e vira um círculo tracejado, com a etiqueta "em incorporação".
- **33,2 s:** o círculo se preenche com um pulmão que respira, e "tele-espirometria" entra no alto.
- **35,75 s:** o logo da UFMG volta grande.
- **37,06 s:** o círculo abre a cena seguinte (abertura circular).
- **Devolutiva da v3:** não gostou.

### Cena 8: Maranhão + as três frases (37,1–45,9 s), refeita
- **Mapa:** o Maranhão grande, parado, na metade de baixo, saindo pela borda direita e pela base.
- **Cobertura:** a partir de 38 s, uma mancha azul se espalha a partir de **São Luís** (o núcleo) e, à medida que chega, **acende os alfinetes dos municípios** (ilustrativos), que caem com mola.
- **Fundo:** ondas largas e diluídas saem de São Luís pela tela toda (o alcance).
- **Frases:** cada uma entra **grande no meio** do espaço livre acima do mapa e depois vai para a lista à esquerda. A lista sobe para receber a próxima, e o mapa pulsa quando cada frase pousa:
  - "ampliar o acesso aos exames" (38,82 s);
  - "qualificar o diagnóstico" (40,76 s);
  - "fortalecer a Atenção Primária à Saúde" (42,38 s).

### Cena 9: lugar ou tempo (46,6–53,6 s), a refazer
- **46,4 s:** a doutora do Flow sobe pela base, à esquerda, grande.
- **48,38 s:** à direita entra "de lugar" com um alfinete, e embaixo dele uma rota pontilhada com um ponto viajando entre dois lugares.
- **50,6 s:** um relógio grande sobe na parte de baixo à direita, com os ponteiros girando rápido e depois assentando.
- **51,3 s:** entra "de tempo".
- **Devolutiva da v3:** tudo aparece direto na posição final, sem movimento; o relógio fica sobre a doutora (sobre o tablet); há muito espaço vazio.

### Cena 10: fecho (54,7–57,5 s), a refazer
- **54,3 s:** o papel do exame da cena 1 volta pela base, e a faixa azul com "Telediagnóstico" nasce no alto.
- **55,66 s, "o laudo chega":** o laudo vem de fora da tela e pousa sobre o exame. O check verde aparece em 56,3 s.
- **Devolutiva da v3:** não gostou do laudo pousando sobre outro papel nem da faixa com o nome.

### Cena 11: logo (57,9–62,3 s), aprovada
- `Intro Telessaude.mp4`, sem alteração.

---

## 4. Som (aprovado)

- **Trilha:** marimba (0–13,6 s) → trilha de tecnologia (12,6–46,8 s) → marimba até o logo.
- **Volume:** a trilha fica 11 dB abaixo da voz e abaixa mais 5 dB quando há fala.
- **Efeitos:** whoosh, swish e tique discretos. O final fica em −14 LUFS.
- **Cenas novas:** cada uma deve indicar onde vai cada efeito.

---

## 5. Prompt para o ChatGPT (copiar e colar, junto com este documento)

```
Você é diretor de motion design de vídeos curtos de saúde pública para redes sociais (Reels/Shorts/WhatsApp). Anexei a descrição completa de um vídeo vertical (1080×1920, 30 fps, ~62 s) do Telessaúde Maranhão sobre o serviço de TELEDIAGNÓSTICO: identidade visual, regras do cliente, narração com o tempo de cada palavra, elementos disponíveis e a descrição de cada cena como está hoje.

TAREFA: reimagine, com criatividade e de um jeito bem diferente do que está descrito, as CENAS 5, 6, 7, 9 e 10. As cenas 1, 2, 3, 4, 8 e 11 ficam como estão: use-as só para garantir que as suas cenas entram e saem ligadas a elas (a cena 5 começa logo depois da 4, a 9 depois da 8, a 10 termina no logo da cena 11).

O cliente rejeitou nas versões anteriores: tudo pequeno e centralizado; áreas vazias; elementos que aparecem direto na posição final; o mesmo formato repetido cena após cena (ex.: cartões brancos só trocando o nome); mapa de fundo passeando; alfinetes sem sentido; título cortado por linha; logo pequeno com a sigla escrita ao lado; relógio por cima da personagem.

O cliente gosta de: tela toda ocupada pelo assunto da cena, grande, ancorado na base ou saindo pela borda; movimento com mola (passa um pouco do alvo e assenta); tudo que entra empurra, encolhe ou faz vibrar o que já está na tela; itens que entram grandes no meio e depois vão para o lugar deles; uma cena que vira a outra (continuidade, metamorfose, arrasto); variedade de linguagem (tela dividida, tipografia, ilustração em tela cheia, câmera que se aproxima, objetos que se transformam).

Restrições técnicas:
- Animação feita em HTML/CSS/SVG controlada por tempo (sem vídeo novo além dos clipes já disponíveis). Ilustrações são SVG simples, flat, nas cores da marca. Não invente pessoas novas: só o doutor e a doutora dos clipes (fundo branco em modo multiplicar; nada colorido atrás deles; a parte de baixo do jaleco esmaece).
- Texto na tela: só palavras-chave ditas na narração, exatamente como foram ditas. Fonte Poppins. Todo texto e informação, no momento em que é falado, dentro da área segura (x 65–888, y 288–1248). A régua da marca ocupa y 1760–1920 o tempo todo.
- Logos da UFG e da UFMG: só o logo, grande, entrando animado. Cores: #365DCC, #1C306A, #19756F, branco/gelo; vermelho só no ECG e no logo da UFMG.
- Sem pop/bolha nos sons; whoosh, swish e tique discretos.

Para CADA uma das cenas 5, 6, 7, 9 e 10, entregue DUAS opções diferentes entre si. Para cada opção:
1. Ideia em uma frase (o conceito visual e por que combina com a fala).
2. Linha do tempo em segundos do vídeo (use os tempos das palavras-âncora): o que entra, de onde, como (efeito e curva), onde fica (posição aproximada em px num quadro de 1080×1920 e tamanho), e como reage ao que entra depois.
3. Texto exato na tela e o momento de cada um.
4. Transição de entrada (como nasce da cena anterior) e de saída (como vira a próxima).
5. Como a tela fica ocupada (o que preenche a parte de cima, o meio e a parte de baixo).
6. Efeitos sonoros: tipo e segundo.
7. Um esboço do quadro mais cheio da cena em texto (o que está em cada região da tela).

No fim, diga qual das duas opções você recomenda para cada cena e por quê, e confirme que nenhuma regra foi quebrada.
```

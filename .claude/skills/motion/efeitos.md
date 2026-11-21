# Catálogo de efeitos

Use estes nomes nas conversas ("usa um `card-rise` aqui", "troca o `pop-in` por `type-rise`"). Durações em frames a 30 fps. Curvas em `principios.md`.

## Entradas e saídas

| Efeito | Para quê | Duração | Receita |
| --- | --- | --- | --- |
| `pop-in` | ícone, selo, botão, número pequeno | 8–10 | escala 0 → 1,08 → 1 (easeOutBack), opacidade 0 → 1 nos primeiros 4 frames |
| `type-rise` | título, frase-chave | 10–12 | sobe 40–60 px, blur 8 → 0 px, opacidade 0 → 1 (easeOutExpo); palavras com stagger de 3 frames |
| `card-rise` | painel ou cartão de informação | 14–18 | sobe da base, com rotação de −3° → 0°; sombra cresce junto; cobre a cena anterior (oclusão) |
| `stagger-in` | listas, linhas de painel, datas | 3–5 por item | cada item usa `pop-in` ou `type-rise`, com intervalo de 3–5 frames |
| `stagger-out` | limpar a tela antes do próximo bloco | 2–3 por item | ordem inversa, escala 1 → 0,9 e opacidade 1 → 0 (easeInCubic) |
| `pill-expand` | botão que vira barra ou título | 12–15 | etiqueta pequena (de preferência retangular com cantos levemente arredondados; cápsula só pontualmente, ver `principios.md`) faz `pop-in` e depois estica na horizontal até a largura do texto; texto entra 3 frames depois |
| `check-pop` | "faça isso", item concluído | 9 | círculo `pop-in` e traço do check desenhado em 6 frames; brilho curto opcional |
| `notificacao` | alerta de celular, lembrete | 12 | desce do topo da área segura com overshoot leve e fica 2–3 s |

## Ênfase

| Efeito | Para quê | Duração | Receita |
| --- | --- | --- | --- |
| `palavra-destaque` | uma palavra-chave da frase | 6–8 | só a cor muda para a cor de destaque, com escala 1 → 1,05 → 1 |
| `underline-draw` | sublinhar um termo | 8–10 | linha desenhada da esquerda para a direita (easeOutCubic) |
| `contador` | números, porcentagens, doses | 18–30 | conta de 0 até o valor (easeOutExpo); o valor final faz `pop-in` leve; o número final vem do roteiro |
| `alerta-pulso` | sinal de alerta, "procure atendimento" | 12 por pulso | escala 1 → 1,06 → 1 com halo que expande e some; no máximo 2 pulsos, nunca piscar |
| `linha-de-pulso` | fundo de título, tema de saúde, ritmo | 20–30 | traço tipo ECG desenhado da esquerda para a direita, fino e discreto, atrás do texto |
| `sparkle` | acento num ponto de interseção | 6–8 | brilho de 4 pontas que aparece e some; no máximo 3 por cena |
| `grid-guides` | composição de texto "de designer" | 15–20 | linhas guia pontilhadas desenham, texto encaixa, nós quadrados nas interseções; somem antes da próxima cena |

## Transições guiadas por objeto

| Efeito | Para quê | Duração | Receita |
| --- | --- | --- | --- |
| `occlusion-wipe` | trocar de cena sem corte | 12–15 | um cartão ou forma grande atravessa a tela e, ao sair, revela a nova cena |
| `slide-tilt` | passar de um painel para outro | 15–18 | painel atual desliza e gira 3–5° para um lado; o novo entra pelo outro em paralaxe |
| `shape-to-scene` | gancho → conteúdo | 15–20 | uma forma simples (círculo, pílula) cresce e vira o fundo ou a moldura da próxima cena |
| `type-punch` | frase final, impacto | 10–14 | texto entra enorme com blur direcional, encolhe até o tamanho final e assenta nítido; os últimos 0,5 s ficam parados |
| `dissolve` | troca suave entre blocos | 9–15 | fusão simples; use quando nenhum objeto puder fazer a transição |
| `push` | mudança de assunto | 12 | a cena inteira empurra a anterior para fora, na cor primária |

## Transições de mesclagem (uma cena se funde na outra)

Considere estas **primeiro**, ainda no mapa de cenas, para cada troca de cena: elas dão a sensação de um vídeo contínuo em vez de telas cortadas.

| Efeito | Para quê | Duração | Receita |
| --- | --- | --- | --- |
| `continuidade` | o assunto avança sem trocar de "lugar" | 15–24 | um elemento que já está na tela fica e **muda de posição/escala** com mola (ex.: vai para um canto e encolhe); o resto sai com `stagger-out` e os novos elementos entram em volta dele. O elemento que fica é a ponte |
| `metamorfose` | uma ideia vira a seguinte | 15–30 | o objeto A **se transforma** no B: dissolução cruzada no mesmo lugar e tamanho, ou forma que muda (silhueta → corpo detalhado → paisagem; coração do título → coração da cena) |
| `arrasto` | mudança de bloco com energia | 12–18 | tudo é **arrastado para um lado** (com leve atraso entre camadas, em paralaxe) e os novos elementos chegam arrastados pelo lado oposto: direita ↔ esquerda, baixo ↔ cima. Varie a direção ao longo do vídeo; som de whoosh/swish suave |
| `cena-vira-card` | mostrar que a cena é uma entre várias (estilos, serviços, vídeos anteriores) | 18–30 | também chamada de *shared element* ou *hero transition*. A cena em tela cheia **encolhe com mola** até virar um cartão (cantos arredondados crescem junto: 0 → 24–40 px, sombra aparece) e encaixa no lugar dela numa fileira; os vizinhos entram pelos lados, já em movimento. O conteúdo **continua tocando** dentro do cartão: é a mesma camada, só com escala, posição e máscara mudando, nunca um corte para outra imagem. Variante inversa: um cartão do carrossel cresce e vira a cena seguinte |

Combine-as: `continuidade` dentro de um bloco, `arrasto` ou `metamorfose` entre blocos, e `dissolve` só quando nada disso couber.

## Movimento contínuo e câmera

| Efeito | Para quê | Duração | Receita |
| --- | --- | --- | --- |
| `drift` | evitar tela congelada | contínuo | flutuação de 4–8 px e rotação de ±1° em ciclo de 2–4 s, em senoide |
| `ken-burns` | imagem estática | duração do plano | zoom de 3–5% em toda a duração, com leve deslocamento lateral |
| `paralaxe` | profundidade entre camadas | contínuo | fundo move 30–50% do que move o primeiro plano |
| `push-in` | aproximar num momento-chave | 18–30 | zoom de 5–10% da câmera inteira, uma vez por bloco |
| `carrossel` | vários exemplos ao mesmo tempo, sem lista estática | contínuo | fileira de cartões que **desliza sem parar** em velocidade constante suave (a única exceção à regra "nada em velocidade constante", porque é um fluxo, não um gesto); pode ter duas fileiras em sentidos opostos. Cada cartão é uma **moldura com vídeo tocando** dentro (não print). O cartão central ou o que a fala cita cresce 5–10% e ganha brilho; os das bordas esmaecem ou desfocam um pouco |

## Material e superfície

| Efeito | Para quê | Receita |
| --- | --- | --- |
| `vidro` | cartões e barras com cara de interface Apple (*glassmorphism*; na Apple, *Liquid Glass*) | painel semitransparente sobre um fundo **com cor e movimento** (sem fundo vivo, o vidro não aparece): `backdrop-filter: blur(24–40px) saturate(160–180%)`, fundo branco a 15–35% (ou escuro a 20–40% em cena escura), borda de 1 px branca a 40–60% em cima e mais fraca embaixo (luz vindo de cima), sombra difusa grande e leve, cantos 24–40 px. Reflexo opcional: um degradê diagonal branco bem fraco que desliza devagar. Texto sobre vidro sempre com contraste ≥ 4,5:1 |
| `profundidade` | separar camadas como na interface da Apple | primeiro plano nítido e maior; o que fica atrás encolhe 3–6%, desfoca 4–10 px e escurece ou clareia um pouco quando algo entra na frente; volta quando sai |

**Na prática do motor (HTML + Playwright):** `backdrop-filter` funciona no Chrome e sai no render quadro a quadro. Vídeo dentro de cartão (carrossel, `cena-vira-card`) entra como **sequência de quadros JPG** do trecho, trocada pelo tempo `t` da página, e não como `<video>`, que trava a busca no render (problema visto na Teleorientação; solução em `CRIANDO-VIDEOS/SERVIÇOS NTS/TELEORIENTAÇÃO/renderizando/_claude/animacao/teleorientacao_v3.html`). Muitos cartões com vídeo pesam: use quadros pequenos (a largura do cartão) e só os cartões visíveis.

**Marca:** no Telessaúde, vidro e carrossel são recursos de linguagem, não troca de identidade: fundo claro, azul da marca presente e as regras de legibilidade de `telessaude/SKILL.md` continuam valendo.

## Combinações prontas

- **Abertura de tema:** `pill-expand` → `type-rise` no título → `linha-de-pulso` atrás.
- **Lista de passos:** `card-rise` do painel → `stagger-in` dos itens com `check-pop` em cada um.
- **Número de impacto:** `contador` → `palavra-destaque` na unidade → `drift` enquanto a fala continua.
- **Alerta:** limpa a tela com `stagger-out` → selo com `pop-in` → `alerta-pulso` 2 vezes.
- **Final:** `stagger-out` de tudo → `type-punch` na mensagem → cartela fixa.
- **Vitrine de exemplos:** um exemplo em tela cheia → `cena-vira-card` → `carrossel` com os outros exemplos (cada um tocando no seu cartão) → o cartão citado na fala cresce e vira a próxima cena.

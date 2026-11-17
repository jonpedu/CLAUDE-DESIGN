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
| `pill-expand` | botão que vira barra ou título | 12–15 | pílula pequena faz `pop-in` e depois estica na horizontal até a largura do texto; texto entra 3 frames depois |
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

## Movimento contínuo e câmera

| Efeito | Para quê | Duração | Receita |
| --- | --- | --- | --- |
| `drift` | evitar tela congelada | contínuo | flutuação de 4–8 px e rotação de ±1° em ciclo de 2–4 s, em senoide |
| `ken-burns` | imagem estática | duração do plano | zoom de 3–5% em toda a duração, com leve deslocamento lateral |
| `paralaxe` | profundidade entre camadas | contínuo | fundo move 30–50% do que move o primeiro plano |
| `push-in` | aproximar num momento-chave | 18–30 | zoom de 5–10% da câmera inteira, uma vez por bloco |

## Combinações prontas

- **Abertura de tema:** `pill-expand` → `type-rise` no título → `linha-de-pulso` atrás.
- **Lista de passos:** `card-rise` do painel → `stagger-in` dos itens com `check-pop` em cada um.
- **Número de impacto:** `contador` → `palavra-destaque` na unidade → `drift` enquanto a fala continua.
- **Alerta:** limpa a tela com `stagger-out` → selo com `pop-in` → `alerta-pulso` 2 vezes.
- **Final:** `stagger-out` de tudo → `type-punch` na mensagem → cartela fixa.

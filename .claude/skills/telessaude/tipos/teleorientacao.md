# Tipo: teleorientação

Orientação de saúde para a população: um tema por vídeo (doença, prevenção, exame), narrado, com personagens. Aplique por cima de `telessaude/SKILL.md`.

## Norma

- `MANUAL-EDICAO-TELEORIENTACAO.md`, na raiz do projeto, é a norma deste tipo (versão de 15/11/2026, já com as decisões do usuário). Se algo aqui divergir do manual, vale o manual; avise o usuário.
- **Sem legenda completa:** o texto na tela são palavras-chave animadas, copiadas exatamente do roteiro final narrado. O roteiro original e o parecer servem para conferir o sentido. `.srt` só se pedido.

## Séries observadas

| Série | Traços | Régua |
| --- | --- | --- |
| SUS Digital (Hipertensão, Hanseníase, Câncer de Pênis, Retinopatia) | fundo branco, 1–2 personagens em diálogo regional, chamada final para o app Meu SUS Digital (celular + botão "BAIXAR") | padrão ou SES |
| PET-Saúde (Dengue, Diabetes, Hanseníase Outubro, Hipertensão, Obesidade) | tom mais formal, fundos coloridos, texturas (papel rasgado), gráficos com fonte, cenas ilustradas completas; faixa vermelha "Procure o posto de saúde / Cuidar da sua saúde é cuidar da sua vida!" | PET-Saúde, com assinaturas no fechamento |

## Duração e estrutura

- **Duração livre** (decisão de 15/11/2026): a narração define. Referências: 65–144 s (mediana ~78 s); temas longos viram parte 1 e parte 2.
- **Sem vinheta de abertura:** o vídeo começa no gancho.
- Estrutura observada (proporções, não segundos fixos):

| Bloco | Proporção | Conteúdo |
| --- | --- | --- |
| Gancho | 0–6 s | personagem + chamada regional ou "Você sabia?"; `type-on` |
| Nome e definição | ~10–20% | nome do tema gigante (às vezes em sílabas empilhadas) + uma linha |
| Orientação | ~50–60% | sintomas, causas, transmissão, exames: listas com `stagger-in`, ícones com `pop-in` ao redor do personagem |
| Alerta | ~10% | troca de cor de fundo, triângulo, "ATENÇÃO" / "Sinais de alarme" |
| Chamada | ~10–15% | "Procure o posto de saúde / UBS", app Meu SUS Digital quando couber |
| Fechamento | 3–5 s | logo animado (+ assinaturas PET) |

- **Gancho e narração:** se a narração já abre no assunto ("O Acidente Vascular Cerebral…"), não acrescente silêncio antes para um gancho só visual; o texto de gancho do roteiro ("Você sabe o que é AVC?") entra junto com a primeira frase e se funde a ela (devolutiva do AVC v1).
- Como a duração é livre, use as proporções acima; o bloco de orientação é o que estica ou encolhe.

## Formato

- As referências são todas verticais. Para o horizontal (vídeo novo ou reconstrução), a estrutura e o texto são os mesmos; muda só a composição (`formatos/horizontal.md`): personagem num terço, conteúdo nos outros dois, diálogo com um personagem de cada lado.
- O manual pede as duas versões de todo vídeo (9:16 principal, 16:9 para o YouTube).

## Cenas geradas = takes

As cenas com personagens (clipes de ~10 s gerados no Google AI Studio/Flow) são **takes**, não cenas prontas. Siga `motion/takes.md`: decupagem em trechos com tags, uso de partes do clipe, reuso permitido (personagem acenando ou com uma expressão específica pode voltar várias vezes) e sincronia de gestos e boca com a narração sempre que possível. Nas pausas, use trechos com a boca fechada.

## Efeitos preferidos

| Momento | Efeitos |
| --- | --- |
| Gancho | `type-on` ou `pill-expand` com a pergunta do tema, `type-rise` no título |
| Passos e cuidados | `card-rise` + `stagger-in` com `check-pop` em cada item (até 4 itens); `palavra-destaque` na palavra-chave |
| Números, doses, prazos | `contador` + `palavra-destaque` na unidade; o valor é sempre copiado do roteiro |
| Mito/erro | risco ou X vermelho sobre a palavra |
| Sinais de alerta | `stagger-out` para limpar a tela, selo com `pop-in`, `alerta-pulso` (no máximo 2) |
| Onde procurar ajuda | ícone de UBS ou SAMU com `pop-in`, `notificacao` para lembretes |
| Fechamento | `stagger-out` → mensagem com `type-punch` → logo animado (só o logo, + assinaturas de parceiros) |

## Tom

Movimento calmo e confiável; exagero só no alerta e na chamada. Exagero visual de humor (interjeições em contorno, "Vish", "Éguas") cabe no gancho, nunca no alerta.

## Antes de entregar

Checagem final de `motion/SKILL.md` + checklist da seção 11 do manual.

---
name: teleorientacao
description: Use ao editar ou animar vídeos de teleorientação do Telessaúde Maranhão (Reels, Shorts e YouTube). Aplica o manual de edição do projeto, a identidade da marca e os cuidados com conteúdo de saúde por cima da skill geral motion.
---

# Teleorientação — Telessaúde Maranhão

Sub-skill da skill `motion`. Leia antes `motion/SKILL.md`; aqui ficam só as regras específicas desta série.

## Fonte da verdade

- `MANUAL-EDICAO-TELEORIENTACAO.md`, na raiz do projeto, é a norma. Se algo aqui divergir do manual, vale o manual. Avise o usuário da divergência.
- Fontes de uso frequente: Poppins, Glacial Indifference, Exo 2, Inter. No máximo duas famílias por vídeo.
- Identidade visual (cores, fontes, logos) vem do kit de marca na pasta de referências e do perfil "telessaude", quando existir. **Nunca use paleta de um preset de `motion/estilos/` no lugar da marca:** do preset, aproveite só movimento, composição e acabamento.

## Regras específicas da série

- **Formatos:** 9:16 principal (Reels e Shorts), 16:9 derivado para o YouTube. Duração de 50 a 75 s, ideal 60 s.
- **Área segura 9:16:** x 65–888, y 288–1248. Texto, legenda, logos e rostos sempre dentro dela.
- **Régua de marca:** arquivo pronto da pasta de referências, sem alteração, centralizado e encostado na margem inferior. Se ela aparece no vídeo inteiro ou só no fechamento ainda está em aberto: pergunte se o plano não disser.
- **Roteiro original** fica em referências e serve para conferir o sentido. A legenda segue o roteiro final narrado, palavra por palavra.
- **Estrutura de 60 s:** vinheta 0–3 s · gancho 3–8 s · orientação 8–45 s · alerta 45–53 s · fechamento 53–60 s. Só a orientação estica ou encolhe.

## Cenas geradas = takes

As cenas com personagens (clipes de ~10 s gerados no Google AI Studio/Flow) são **takes**, não cenas prontas. Siga `motion/takes.md`: decupagem em trechos com tags, uso de partes do clipe, reuso permitido (por exemplo, o personagem acenando ou com uma expressão específica pode voltar várias vezes) e sincronia de gestos e boca com a narração sempre que possível. A narração é separada; nas pausas, use trechos com a boca fechada.

## Efeitos preferidos nesta série

| Momento | Efeitos |
| --- | --- |
| Gancho | `pill-expand` com a pergunta do tema, `type-rise` no título, `linha-de-pulso` discreta atrás |
| Passos e cuidados | `card-rise` + `stagger-in` com `check-pop` em cada item (até 4 itens) |
| Números, doses, prazos | `contador` + `palavra-destaque` na unidade; o valor é sempre copiado do roteiro |
| Sinais de alerta | `stagger-out` para limpar a tela, selo com `pop-in`, `alerta-pulso` (no máximo 2) |
| Onde procurar ajuda | ícone de UBS ou SAMU com `pop-in`, `notificacao` para lembretes |
| Fechamento | `stagger-out` → mensagem com `type-punch` → cartela fixa com fonte, aviso e assinaturas |

## Tom e cuidados de saúde

- Movimento calmo e confiável: exagero só no alerta e no CTA. Nada de shake, glitch ou flash.
- Nenhuma imagem de medo, culpa ou estigma. Pessoas diversas em idade, cor de pele, corpo e território.
- Cena gerada com procedimento errado (máscara, lavagem de mãos, postura) é substituída, não disfarçada.
- Alerta sempre com cor **e** texto; nunca só cor.
- O texto na tela só diz o que o roteiro aprovado diz. Números, doses e sinais de alerta são conferidos contra o roteiro antes de cada render.

## Antes de entregar

Rode a checagem final de `motion/SKILL.md` e o checklist da seção 11 do manual.

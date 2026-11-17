# Paleta do Telessaúde

Fonte: guia de cores do portal, em `cores hex/` (versão clara e escura), entregue pelo usuário em 15/11/2026. Os valores foram **medidos nos quadrados** (`analise-referencias/scripts/amostrar_paleta.py`), porque alguns rótulos da imagem estão errados: Success, Warning e Error repetem os HEX de texto, e a versão escura repete os rótulos da clara.

**Regra do usuário:** a base é esta paleta, mas **os tons de azul podem variar**, como já acontece nos vídeos de referência (degradês de azul nos institucionais, azul mais claro ou mais escuro conforme o fundo). Varie dentro da família azul da marca; não troque o azul por outro matiz.

## Paleta clara (padrão dos vídeos: fundo branco)

| Papel | Nome | HEX | Uso no vídeo |
| --- | --- | --- | --- |
| Marca | Primary | `#365DCC` | títulos de destaque, barras, botões, ícones da marca |
| Marca | Primary Hover | `#3052B4` | variação de azul (segundo tom, degradês) |
| Marca | Primary Pressed | `#29479B` | azul mais escuro (sombra, degradê, texto azul sobre claro) |
| Marca | Primary Subtle | `#E3E8F8` | fundo de cartão ou bloco azul-claro |
| Marca | Brand Strong | `#1C306A` | azul-marinho: fundos escuros institucionais, texto forte |
| Secundária | Secondary | `#19756F` | verde-petróleo: destaque secundário, "sucesso/cuidado" |
| Secundária | Secondary Hover | `#165E5A` | variação |
| Secundária | Secondary Pressed | `#164B48` | variação escura |
| Secundária | Secondary Subtle | `#ECF8F7` | fundo de cartão verde-claro |
| Texto | Primary | `#101828` | texto principal sobre claro |
| Texto | Secondary | `#475467` | texto de apoio, linha leve da hierarquia |
| Texto | Inverse | `#F8F9FC` | texto sobre fundo escuro |
| Superfície | Page | `#F8F9FC` | fundo gelo |
| Superfície | Default | `#FFFFFF` | fundo branco |
| Superfície | Subtle | `#F1F3F7` | fundo de bloco discreto |
| Borda | Default | `#E2E6ED` | contorno de cartão |
| Borda | Strong | `#CDD3DD` | contorno forte, divisores |
| Feedback | Success | `#027A48` | confirmação, check, "faça isso" |
| Feedback | Success Subtle | `#ECFDF3` | fundo de bloco positivo |
| Feedback | Warning | `#C99B00` | atenção, triângulo de alerta (com texto) |
| Feedback | Warning Subtle | `#FFFAEB` | fundo de bloco de atenção |
| Feedback | Error | `#B42318` | alerta grave, "procure atendimento", X de erro |
| Feedback | Error Subtle | `#FEF3F2` | fundo de bloco de alerta |

## Paleta escura (fundos escuros: institucionais, telas de impacto)

| Papel | HEX |
| --- | --- |
| Primary / Hover / Subtle | `#728EDB` / `#A5B6E8` / `#1C306A` |
| Secondary / Hover / Pressed / Subtle | `#42ADA5` / `#75C9C1` / `#A9E0DA` / `#143E3C` |
| Texto Primary / Secondary / Link | `#F8F9FC` / `#CDD3DD` / `#A5B6E8` |
| Superfície Page / Default / Subtle / Inverse | `#080F1E` / `#101828` / `#1D2939` / `#344054` |
| Superfície Brand / Brand Strong | `#233C83` / `#1C306A` |
| Borda Default / Strong | `#344054` / `#475467` |
| Success / Subtle | `#32D583` / `#054F31` |
| Warning / Subtle | `#FFE34D` / `#574300` |
| Error / Subtle | `#F97066` / `#7A271A` |

## Como usar

- O azul do logo medido nos vídeos (≈ `#3149BB`) está entre Primary e Primary Hover: os vídeos já variavam o azul. O logo e a régua usam sempre o arquivo do usuário, nunca recoloridos.
- Fundos institucionais em degradê: de `#29479B` ou `#1C306A` até `#365DCC` (ou o azul mais claro da paleta escura, `#728EDB`), como nos Kits e na Retrospectiva.
- Alerta sempre com cor **e** texto; contraste ≥ 4,5:1 (texto `#101828` sobre claro; `#F8F9FC` sobre azul e marinho).
- **Cor do tema por vídeo** (roxo na hanseníase, amarelo na dengue, vermelho na hipertensão, cor da campanha do mês): permitida, mas **pontual** (palavra-chave, ícone, faixa, uma tela de impacto). O azul continua sendo o padrão e aparece em todo vídeo. Escolha o tom do tema com contraste ≥ 4,5:1 contra o fundo onde vai o texto. Regra completa em `SKILL.md`.

## Tokens para render (CSS)

```css
:root {
  --ts-primary: #365DCC; --ts-primary-hover: #3052B4; --ts-primary-pressed: #29479B;
  --ts-primary-subtle: #E3E8F8; --ts-brand-strong: #1C306A;
  --ts-secondary: #19756F; --ts-secondary-hover: #165E5A; --ts-secondary-pressed: #164B48; --ts-secondary-subtle: #ECF8F7;
  --ts-text: #101828; --ts-text-2: #475467; --ts-text-inverse: #F8F9FC;
  --ts-page: #F8F9FC; --ts-surface: #FFFFFF; --ts-surface-subtle: #F1F3F7;
  --ts-border: #E2E6ED; --ts-border-strong: #CDD3DD;
  --ts-success: #027A48; --ts-success-subtle: #ECFDF3;
  --ts-warning: #C99B00; --ts-warning-subtle: #FFFAEB;
  --ts-error: #B42318; --ts-error-subtle: #FEF3F2;
}
```

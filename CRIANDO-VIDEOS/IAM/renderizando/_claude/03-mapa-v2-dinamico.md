# IAM — mapa de cenas v2 (dinâmico) · 15/11/2026

Pedido do usuário: vídeo dinâmico, como nos virais de TikTok/Reels — telas cheias de texto e grafismo **sem a personagem**, **movimento de câmera** e **elementos presos ao corpo** por rastreamento. Fechamento = `elementos/Intro NTS e PETSAUDE.mp4` (4,6 s, com som próprio), sem alteração; régua por cima.

Recursos novos (gramática da v2):
- **Tela cheia (TC):** fundo azul em degradê `#1C306A → #365DCC`, tipografia grande branca, linha de ECG animada, sem personagem. Usada em ganchos, título e alertas.
- **Câmera:** push-in lento (1,00 → 1,08), zoom rápido para um ponto (match cut), pull-out revelando o corpo, pan lateral.
- **Rastreamento:** pontos do corpo (peito, pescoço, mandíbula, braço) rastreados no clipe (fluxo óptico); etiquetas com linha-guia seguem esses pontos, mesmo com a câmera se movendo.
- **Transições (variadas):** painel que sobe, zoom para dentro do coração, revelação circular, cortina de faixas azuis, corte seco no tempo da fala.

**Critério (usuário, 15/11/2026):** os recursos acima são sugestões. Cada efeito só entra se reforçar a fala daquele trecho; o resto fica de fora (ex.: a cortina de faixas saiu por ser só decorativa).

## Prévia 0:00–0:35 (cenas 1–6)

| # | Tempo | Tipo | Conteúdo e movimento | Transição de saída |
| --- | --- | --- | --- | --- |
| 1 | 0,0–4,2 | **TC** | "Você sabia?" entra grande (0,0) · ECG desenha de lado a lado · pílula "Sociedade Brasileira de Cardiologia" (1,7) | painel azul sobe e revela a cena 2 (whoosh) |
| 2 | 4,2–9,0 | T07 4,0–8,8 | "uma pessoa sofre **um infarto**" (5,0) · "a cada poucos minutos" com marca-texto vermelho desenhando (6,8) · câmera: push-in lento em direção ao coração | **zoom para dentro do coração** |
| 3 | 9,0–13,9 | T08 4,1–9,0 | "Muitas vidas poderiam ser salvas" (9,0) · "se os sinais fossem reconhecidos **a tempo**" (10,9) · câmera: pan lento para o coração que brilha | corte para tela cheia |
| 4 | 13,9–18,4 | **TC** | "Hoje vamos falar sobre o" (14,1) · "Infarto" (15,8) · "Agudo" (16,3) · "do Miocárdio" (17,0), palavra por palavra · ECG pulsa em vermelho | **revelação circular** a partir do coração |
| 5 | 18,4–26,6 | T06 3,0–9,0 + congelado | "uma artéria que leva sangue ao coração fica" (19,9) · **"bloqueada"** vermelho com pop (22,5) · "impedindo que o músculo cardíaco receba oxigênio" (23,5) · câmera: **push-in na lupa** da artéria entupida | dissolução (0,4 s) |
| 6 | 26,6–35,4 | T04 1,5–10,0 | câmera começa em close no peito e **abre** quando a dor se espalha (30,7) · "Dor ou aperto no peito" (27,9) · etiquetas **rastreadas** com linha-guia: "braço esquerdo" (31,4), "pescoço" (32,5), "costas" (33,6), "mandíbula" (34,5) | (fim da prévia) |

## Cenas 7–16 (implementadas em `animacao/completo.html`)

| # | Tempo | Tipo | Conteúdo e movimento (por que) | Saída |
| --- | --- | --- | --- | --- |
| 7 | 35,7–40,0 | TC | triângulo amarelo pulsando + "Mas atenção:"; "os sinais nem sempre são / iguais para todo mundo" digitado (virada da fala) | empurrada para a esquerda (0,6 s) |
| 8 | 40,0–45,0 | T05 (largura cheia, 1,5× até as três pessoas entrarem) | "Em mulheres, idosos e pessoas com diabetes," com marca-texto e **círculo no rosto de cada pessoa quando é nomeada** | o grupo desce e abre espaço |
| 9 | 45,0–54,7 | T05 congelado embaixo | "o infarto pode se manifestar com" + pílulas no tempo de cada palavra (atípicos em vermelho) | corte em "Fique" |
| 10 | 54,7–66,4 | T01 (colado à esquerda) | selo "Fique atento a:" + lista: cada item entra quando é dito e fica em destaque; os anteriores esmaecem | corte em "Se" |
| 11 | 66,4–72,9 | T03 (largura cheia) | entrada com leve zoom; **câmera aproxima do rosto em "não espere"**, que pulsa em vermelho | corte |
| 12 | 72,9–76,3 | T02 | "Suspeitou de infarto?" · "Ligue imediatamente para o SAMU" (celular + ambulância) | corte |
| 13 | 76,3–78,5 | TC | telefone vibrando, pílula "SAMU", **"1-9-2" entrando dígito a dígito como é falado** | zoom de saída |
| 14 | 78,5–81,0 | T02 | "Não dirija até o hospital sozinho" (carro riscado), "sozinho" em vermelho | corte |
| 15 | 81,0–84,0 | T02 | "Cada minuto conta!" (cronômetro), assenta | dissolução (0,6 s) |
| 16 | 83,6–88,2 | fechamento | `Intro NTS e PETSAUDE.mp4` sem alteração, régua por cima, som próprio | fim |

## Restante (planejamento original, já substituído pela tabela acima)
- 35,4–40,2 **TC de alerta**: "Mas atenção" com triângulo pulsando, fundo branco→amarelo pontual.
- 40,2–54,6 T05 com **pan** pelo grupo (mulher, idosa, homem com glicosímetro) e pílulas; sinais atípicos em **TC** com pílulas que pipocam.
- 54,6–66,4 T01 com lista "Fique atento a:" e ícones rastreados.
- 66,4–72,9 T03 com push-in no rosto, "não espere" pulsando.
- 72,9–80,6 **TC "192"** gigante (contador) → T02 com "Não dirija até o hospital sozinho".
- 80,6–83,5 "Cada minuto conta!" com relógio → **fechamento** (vídeo da equipe, 4,6 s).

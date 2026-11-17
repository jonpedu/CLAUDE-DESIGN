# Som

O som confirma o que o olho vê. Nenhum efeito sonoro pode encobrir a voz.

## Camadas e níveis

| Camada | Nível | Regra |
| --- | --- | --- |
| Voz / narração | referência (−16 a −14 LUFS) | conduz o tempo do vídeo |
| Trilha | 18–22 dB abaixo da voz durante a fala | sobe só na abertura e no final; fade de 1 s |
| Efeitos sonoros | 6–12 dB abaixo da voz | curtos; no máximo 1 a cada 3–4 s |
| Final mixado | −14 LUFS integrado, pico −1 dBTP | normalizar no fim (ffmpeg `loudnorm`, duas passadas) |

## Mapa de micro-efeitos (som ↔ efeito visual)

| Visual | Som |
| --- | --- |
| `pop-in`, `check-pop` | pop curto e suave |
| `pill-expand`, toggle | clique leve |
| `card-rise`, `slide-tilt` | swish curto |
| `occlusion-wipe`, `push` | whoosh baixo |
| `contador` | tique leve a cada passo, ou só um "ding" no valor final |
| `alerta-pulso` | tom grave curto (não sirene) |
| CTA, `type-punch` | thump grave ou estalo |
| `sparkle` | brilho discreto, raro |

## Sincronia

- O som marca o **impacto** (o frame em que o objeto assenta), não o início do movimento. Adiante 0–1 frame.
- Não ponha som em toda animação. Escolha os 4–8 momentos mais importantes de um vídeo de 1 min.
- Abaixe a trilha (ducking) sempre que a voz entra; nunca o contrário.
- Guarde a licença de toda trilha e de todo efeito junto do projeto.

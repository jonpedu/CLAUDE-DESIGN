# Telediagnóstico: prompts para o Google Flow

**Série:** Serviços do NTS · **Roteiro:** v2 aprovado (20/11/2026) · **Gerado com:** skill `prompts-flow`

Só o **profissional de saúde da cena 03** vai para o Flow. O médico feito em SVG foi recusado pelo usuário em 20/11/2026. O resto do vídeo continua em motion gráfico: alfinetes, linha, ícones, cartões dos exames, mapa do Maranhão, relógio e laudo.

## Cena 03: "...são enviados a um profissional de saúde, que emite um laudo ou um parecer." (~3,5 s, de 15,1 a 18,5 s)

**Como vai ser montada:** o profissional fica no **alto da tela**, na ponta de cima da linha. Os ícones de gráficos, imagens e dados sobem pela linha e chegam até ele. Ele olha o tablet, analisa e confirma com a cabeça, e o laudo desce pela linha com o check verde. Uso o clipe original com fundo branco em **modo multiplicar** (sem recorte, como no piloto). Por isso a linha termina embaixo dele e nada colorido passa por trás.

O enquadramento é **da cintura para cima**, porque ele ocupa só o terço de cima da tela. A ação principal (olhar, analisar, confirmar) precisa acontecer **nos primeiros 3 s**.

**Personagem recorrente da série:** este é o "médico especialista a distância" do elenco da série. Se o clipe for aprovado, a mesma descrição (palavra por palavra) serve para a teleconsultoria e a teleinterconsulta, e o clipe pode virar a imagem de referência (*Ingredients to Video*).

**Configuração no Flow:** modo texto para vídeo (*Text to Video*), proporção **9:16 (retrato)**, a melhor qualidade disponível, 2 variações por prompt. O áudio do clipe não é usado.

---

### Clipe A: médico analisando os exames no tablet

```
Flat design 2D vector animation, motion design style, clean and friendly health-education look. Pure solid white background (#FFFFFF), no scenery, no desk, no furniture.

A Brazilian male doctor, around 40 years old, medium brown skin, short black hair neatly combed, a short well-trimmed beard, rectangular dark-framed glasses, wearing a clean white lab coat over a light-blue shirt, a stethoscope around his neck. Framing: waist-up, centered in the frame, the character fills the middle 55% of the frame height with generous empty white space above and below, both hands visible.

Action: he holds a tablet at chest height with one hand, the screen is on with no light rays or glow around it (no readable content). In the first second he looks down at the tablet attentively and slides a finger across the screen, analyzing. Around the second second he gives a confident, small nod and taps the screen once, as if confirming a report. Then he looks up toward the viewer with a calm, reassuring smile and keeps a relaxed idle pose with subtle breathing.

Camera: static, locked-off, straight-on medium shot, no zoom, no pan, no cuts. Lighting: flat, even, no dramatic shadows. Colors: soft pastel tones with blue accents. Smooth, simple character animation at a natural pace.

Avoid: text, letters, numbers, logos, watermarks, UI elements on the tablet, photorealism, 3D rendering, caricature or exaggerated features, extra characters, background objects, desk, camera movement.
```

### Clipe B (opcional): médica, mesma ação

Para variar o elenco da série, ou para usar no lugar do A se ficar melhor.

```
Flat design 2D vector animation, motion design style, clean and friendly health-education look. Pure solid white background (#FFFFFF), no scenery, no desk, no furniture.

A Brazilian female doctor, around 35 years old, dark brown skin, black curly hair tied back in a low bun, small round earrings, wearing a clean white lab coat over a teal scrub top, a stethoscope around her neck. Framing: waist-up, centered in the frame, the character fills the middle 55% of the frame height with generous empty white space above and below, both hands visible.

Action: she holds a tablet at chest height with one hand, the screen is on with no light rays or glow around it (no readable content). In the first second she looks down at the tablet attentively and slides a finger across the screen, analyzing. Around the second second she gives a confident, small nod and taps the screen once, as if confirming a report. Then she looks up toward the viewer with a calm, reassuring smile and keeps a relaxed idle pose with subtle breathing.

Camera: static, locked-off, straight-on medium shot, no zoom, no pan, no cuts. Lighting: flat, even, no dramatic shadows. Colors: soft pastel tones with blue accents. Smooth, simple character animation at a natural pace.

Avoid: text, letters, numbers, logos, watermarks, UI elements on the tablet, photorealism, 3D rendering, caricature or exaggerated features, extra characters, background objects, desk, camera movement.
```

---

## Ao gerar

- **Escolha** a variação em que o aceno com a cabeça aparece cedo, as mãos estão inteiras e o tablet fica sem texto.
- **Mesmo traço do piloto:** o estilo deve combinar com as pessoas da Teleorientação (vetor flat, cores pastel). Se sair 3D ou detalhado demais, gere de novo.
- **Onde salvar:** em `TELEDIAGNÓSTICO/elementos/`. Pode deixar o nome que o Flow dá.
- **Se der errado:** me diga o que saiu errado (estilo, corpo cortado, texto na tela, gesto estranho) que eu ajusto o prompt.

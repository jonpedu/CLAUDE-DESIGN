# Teleorientação: prompts para o Google Flow

**Série:** Serviços do NTS · **Roteiro:** v2 aprovado (20/11/2026) · **Gerado com:** skill `prompts-flow`

Só a **cena 02** usa o Flow. As cenas 01 e 03 são motion gráfico feito pelo Claude, e a 04 é o fechamento da marca.

## Cena 02: "É uma ação de conscientização feita para o cidadão." (~4 s)

**Roteiro:** pessoas diversas (idade, cor de pele, território, incluindo o interior do Maranhão) olhando o celular.

**Como vai ser montada:** cada pessoa é gerada **sozinha, de corpo inteiro, em fundo branco**. Na edição, eu recorto as pessoas e faço elas entrarem uma a uma, lado a lado, sobre um fundo da marca (depois pode entrar o mapa do Maranhão em SVG). As etiquetas "conscientização" e "para o cidadão" entram por cima. De cada clipe uso de 1 a 2 s, então o ideal é que a ação principal (olhar o celular e sorrir) aconteça **nos primeiros 3 s**.

**Gere os clipes A, B e C.** O D é opcional, para trocar por um dos três ou para ter 4 pessoas.

**Configuração no Flow:** modo texto para vídeo (*Text to Video*), proporção **9:16 (retrato)**, a melhor qualidade disponível, 2 variações por prompt. Cole o prompt inteiro, em inglês. Se o Flow gerar som, não tem problema: o áudio do clipe não é usado.

---

### Clipe A: idosa da cidade

```
Flat design 2D vector animation, motion design style, clean and friendly health-education look. Pure solid white background (#FFFFFF), no scenery, no floor line, only a very soft contact shadow under the feet.

A Brazilian elderly woman, around 70 years old, warm brown skin, short wavy gray hair, round reading glasses, wearing a light-blue floral blouse and a navy skirt, comfortable flat shoes. Full body, standing, centered in the frame, the character fills the middle 60% of the frame height with generous empty white space above and below.

Action: she holds a smartphone at chest height with both hands, the phone screen glows softly with plain light (no readable content). In the first two seconds she lifts her eyes slightly to the screen, her face lights up with a gentle, warm smile, and she gives a small approving nod. Then she keeps a calm idle pose with subtle breathing.

Camera: static, locked-off, straight-on medium-long shot, no zoom, no pan, no cuts. Lighting: flat, even, no dramatic shadows. Colors: soft pastel tones with blue accents. Smooth, simple character animation at a natural pace.

Avoid: text, letters, numbers, logos, watermarks, UI elements on the phone, photorealism, 3D rendering, extra characters, background objects, camera movement.
```

### Clipe B: agricultor do interior do Maranhão

```
Flat design 2D vector animation, motion design style, clean and friendly health-education look. Pure solid white background (#FFFFFF), no scenery, no floor line, only a very soft contact shadow under the feet.

A Brazilian man from the rural interior of Maranhão, around 45 years old, dark brown skin, short black hair and a short beard, wearing a woven straw hat, a simple short-sleeved green t-shirt, rolled-up beige work trousers and rubber sandals. Full body, standing, centered in the frame, the character fills the middle 60% of the frame height with generous empty white space above and below.

Action: he holds a smartphone in one hand at chest height, the screen glows softly with plain light (no readable content). In the first two seconds he looks down at the phone, raises his eyebrows with interest, then smiles broadly and tips the brim of his hat slightly with his free hand. Then he keeps a relaxed idle pose with subtle breathing.

Camera: static, locked-off, straight-on medium-long shot, no zoom, no pan, no cuts. Lighting: flat, even, no dramatic shadows. Colors: soft pastel tones with blue accents. Smooth, simple character animation at a natural pace.

Avoid: text, letters, numbers, logos, watermarks, UI elements on the phone, photorealism, 3D rendering, caricature or exaggerated stereotypes, extra characters, background objects, camera movement.
```

### Clipe C: jovem estudante

```
Flat design 2D vector animation, motion design style, clean and friendly health-education look. Pure solid white background (#FFFFFF), no scenery, no floor line, only a very soft contact shadow under the feet.

A Brazilian young woman, around 20 years old, light brown skin, long curly dark hair tied in a high ponytail, wearing a yellow t-shirt, light-blue jeans, white sneakers and a small backpack on one shoulder. Full body, standing, centered in the frame, the character fills the middle 60% of the frame height with generous empty white space above and below.

Action: she holds a smartphone with both hands, the screen glows softly with plain light (no readable content). In the first two seconds the phone gives a small vibration, she looks at it, smiles with curiosity and gives a quick, light thumbs-up with one hand before returning both hands to the phone. Then she keeps a relaxed idle pose with subtle breathing.

Camera: static, locked-off, straight-on medium-long shot, no zoom, no pan, no cuts. Lighting: flat, even, no dramatic shadows. Colors: soft pastel tones with blue accents. Smooth, simple character animation at a natural pace.

Avoid: text, letters, numbers, logos, watermarks, UI elements on the phone, photorealism, 3D rendering, extra characters, background objects, camera movement.
```

### Clipe D (opcional): quebradeira de coco babaçu

Figura típica do Maranhão. Reforça o "território" sem precisar de cenário.

```
Flat design 2D vector animation, motion design style, clean and friendly health-education look. Pure solid white background (#FFFFFF), no scenery, no floor line, only a very soft contact shadow under the feet.

A Brazilian woman from rural Maranhão, around 50 years old, deep brown skin, hair covered by a colorful cotton headscarf, wearing a simple orange blouse, a long patterned skirt and sandals, a small woven straw basket hanging from her forearm. Full body, standing, centered in the frame, the character fills the middle 60% of the frame height with generous empty white space above and below.

Action: she holds a smartphone in her free hand at chest height, the screen glows softly with plain light (no readable content). In the first two seconds she looks at the screen, her expression turns into a proud, open smile and she nods slowly. Then she keeps a calm idle pose with subtle breathing.

Camera: static, locked-off, straight-on medium-long shot, no zoom, no pan, no cuts. Lighting: flat, even, no dramatic shadows. Colors: soft pastel tones with blue accents. Smooth, simple character animation at a natural pace.

Avoid: text, letters, numbers, logos, watermarks, UI elements on the phone, photorealism, 3D rendering, caricature or exaggerated stereotypes, extra characters, background objects, camera movement.
```

---

## Ao gerar

- **Escolha** a variação em que o sorriso aparece cedo e o celular fica sem texto na tela. Se a tela vier com algo escrito, não tem problema: eu cubro com um brilho na edição.
- **Mesmo traço nos três:** se um clipe sair com estilo diferente (mais 3D, mais detalhado), gere de novo. Também dá para usar a imagem de um clipe aprovado como referência (*Ingredients to Video*) nos outros.
- **Nomes dos arquivos:** pode deixar os nomes que o Flow dá. Salve em `TELEORIENTAÇÃO/elementos/`.
- **Se der errado:** me diga o que saiu errado (estilo, corpo cortado, texto na tela, gesto estranho) que eu ajusto o prompt.

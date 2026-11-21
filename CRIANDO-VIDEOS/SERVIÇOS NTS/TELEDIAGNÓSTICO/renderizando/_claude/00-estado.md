# TELEDIAGNÓSTICO: estado

Criado em 17/11/2026. Atualize a cada entrega; o histórico detalhado fica em `TELEDIAGNÓSTICO - estudo da edição.md`.

- **Formato e tipo:** institucional; vertical (9:16) primeiro, depois horizontal (16:9)
- **Roteiro:** v2 aprovado pela Amanda (20/11/2026), `roteiro/roteiro - telediagnóstico.md`, ~45 s
- **Versão atual:** v4 (20/11/2026): `animacao/telediagnostico_v4.src.html` → `py animacao/monta_v3.py v4` gera `telediagnostico_v4.html`; folha `quadros/folha_v4.jpg`; prévia com som `versoes-anteriores/Telediagnostico_previa_v4.mp4` (mix `animacao/mix_v4.json`). Cenas 1, 2, 3, 4 e 8 refeitas pelo Claude; cenas 5, 6, 7, 9 e 10 ainda as da v3 (rejeitadas). Logo do Telessaúde da cena 4: `elementos/logo-telessaude-vertical.svg` (cópia de `Uso marcas Telessaúde/1.svg`).
- **Final aprovado:** nenhum
- **Próximo passo (pronto para outra conta/conversa continuar):**
  1. Implementar na página `animacao/telediagnostico_v4.src.html` as cenas **5A, 6A, 7A, 9A e 10A** da proposta do ChatGPT, com as adaptações do Claude: tudo em `03-proposta-chatgpt-cenas-5-6-7-9-10.md`. Trechos a trocar no script: do bloco `// olho: espia por baixo` até o fim de `C4c/d` (cenas 5–7); de `// ===================== C5` até `FECHAMENTO` (cenas 9–10); passos de 54,x s em `DV`, `painel`, `papel`, `faixa`/`tit` e `doc` (fecho antigo); HTML de `mais`, `tagInc`, `bOlho`, `bEcg`, `rel`, `rota` (sai) e novos elementos. Logo da UFG maior (altura 360).
  2. Gerar o HTML: `py "CRIANDO-VIDEOS/SERVIÇOS NTS/TELEDIAGNÓSTICO/renderizando/_claude/animacao/monta_v3.py" v4`.
  3. Quadros de prova (mostrar antes de renderizar): `FOTOS="23.3,24.6,25.8,26.6,27.4,28.9,29.8,31.7,33.6,34.8,36.2,37.4,47.8,49.2,51.8,53.3,54.9,55.8,56.6,57.5" node ferramentas/animar.mjs "<...>/animacao/telediagnostico_v4.html" "<...>/quadros/v4b"` + `py ferramentas/folha.py "<...>/quadros/v4b" "<...>/quadros/folha_v4b.jpg" 5 300`.
  4. Ajustar os efeitos sonoros das cenas novas em `animacao/mix_v4.json` (lista da proposta; sem pop; `sfx_db_extra` −5).
  5. Prévia (só se o usuário pedir): `PREVIA=1 node ferramentas/animar.mjs <página v4> "<...>/versoes-anteriores/Telediagnostico_previa_v4_semsom.mp4"` e `py ferramentas/mixar.py "<...>/animacao/mix_v4.json"`.
  6. Render final, depois da aprovação: `QUALIDADE=max node ferramentas/animar.mjs <página v4> "<...>/animacao/final_v4_video.mp4"`, capa no quadro 0 (`formatos/vertical.md`; sugestão: quadro de ~7,6 s) e `mixar.py` com um `mix_final_v4.json` (cópia de `mix_v4.json` com `video` = vídeo final e `saida` = `../../TELEDIAGNÓSTICO v4.mp4`).

## Assets (lista entregue em 20/11/2026)

| Cena | Precisa | Quem faz |
| --- | --- | --- |
| Todas | Narração `.wav` (texto "Narração completa" do roteiro, mesma voz do piloto) em `audios/` | usuário (AI Studio) |
| Todas | Régua `regua - tele-sted-sus-govbr.svg` | reaproveitar do piloto (Claude copia) |
| 06 | Fechamento `Intro Telessaude.mp4` (vertical) | reaproveitar do piloto; horizontal ainda falta |
| Todas | Trilha | Claude propõe do banco (`tecnologia/technology-background-atlasaudio-631954.mp3` ou a do piloto, para unidade da série) |
| 01, 05 | Alfinete de mapa, linha de conexão, relógio | Claude (SVG) |
| 02 | Dois pontos e linha que se estica | Claude (SVG) |
| 03 | Ícones gráfico / imagem / dados, documento de laudo, profissional de saúde | Claude (SVG); profissional pode ser clipe do Flow (opcional) |
| 04 | Ícones olho/retina, linha de ECG, pulmão | Claude (SVG) |
| 04 | Logos UFG e UFMG | usuário, se quiser; sem eles, só as siglas |
| 04 | Mapa do Maranhão com pontos | Claude, a partir de `brazil.svg` (`BR-MA`); municípios reais pedem a malha do IBGE |

## Pacote (conferência)

- [x] Narração em `audios/`: `audio telediagnostico.wav` (57,8 s, 24 kHz mono; o roteiro previa 44 a 48 s)
- [x] Roteiro final (v2 aprovado)
- [x] Elementos em `elementos/`: `UFG_logo.svg` e `ufmg-logo.svg` (do usuário, monocromáticos escuros), `brazil.svg` (do piloto)
- [x] Régua `regua - tele-sted-sus-govbr.svg` (copiada do piloto)
- [x] Fechamento `Intro Telessaude.mp4` (vertical, copiado do piloto)
- [x] Trilha `trilha sonora/joyful-marimba-universfield.mp3` (a mesma do piloto)
- [x] Itens obrigatórios confirmados pelo usuário (20/11/2026: régua, fechamento e trilha do piloto)

## Narração medida (etapa 2, 20/11/2026)

Transcrição em `transcricao/` (`palavras.json`, `transcricao.txt`; dica do roteiro em `dica.txt`). Duração 57,8 s.

| Cena | Fala (s) | Âncoras (início da palavra, s) |
| --- | --- | --- |
| 01 Gancho | 0,00–8,14 | "laudo" 2,86 · "lugar" 3,84 · "Como resolver?" 4,84 · "telediagnóstico" 6,72 |
| 02 O que é | 8,58–11,78 | "a distância" 9,66 |
| 03 Como funciona | 12,60–18,16 | "gráficos" 12,60 · "imagens" 13,26 · "dados" 13,86 · "laudo" 17,16 |
| 04 Exames do NTS | 18,98–45,92 | "telerretinografia" 23,18 · "UFG" 25,34 · "eletrocardiograma" 26,44 · "UFMG" 28,56 · "Ampliando" 29,40 · "tele-espirometria" 33,20 · "UFMG" 35,80 · "Essas iniciativas" 37,06 · "ampliar" 38,82 · "qualificar" 40,76 · "fortalecer" 42,38 |
| 05 Lugar ou tempo | 46,60–53,62 | "lugar" 48,38 · "tempo" 51,30 |
| 06 Fecho | 54,68–57,46 | "Telediagnóstico" 54,68 · "laudo" 55,66 · "distância" 57,02 |

Diferenças da fala em relação ao roteiro, **feitas de propósito pelo usuário para soar melhor na voz** (20/11/2026; o sentido não muda): "o núcleo avança na incorporação da tele-espirometria, **também** em parceria com a UFMG" (o "também" mudou de lugar) e um "Ah," antes de "e essa distância" (46,6 s). As palavras-chave da tela não mudam. Os erros do Whisper ("telerdiagnóstico", "Ancliando") são só do reconhecimento.

## Decisões deste vídeo

- 20/11/2026: proposta do ChatGPT para as cenas 5, 6, 7, 9 e 10 recebida e resumida em `03-proposta-chatgpt-cenas-5-6-7-9-10.md` (combinação recomendada 5A+6A+7A+9A+10A). Ainda **não implementada**. O usuário pediu para deixar tudo pronto para outra conta/conversa continuar, sem renderizar.
- 20/11/2026: cena 2 ajustada na v4 (faixa do título em y 190, cota "a distância"), só em quadros (`quadros/folha_v4_cena2.jpg`).

- 20/11/2026, prévia v4 aos 11 s: a faixa do título cobria a cabeça do doutor (subiu para y 190 nas cenas 2 e 3) e faltava algo entre "a distância" e o exame (entrou uma cota vertical que se estica com mola, verde). Só quadros (`quadros/folha_v4_cena2.jpg`); a prévia não foi renderizada de novo, a pedido.

- 20/11/2026, devolutiva da v3: som e logo aprovados. Cena 1: texto completo "o exame foi feito / aqui", mais centralizado, "quem dá / o laudo, / lá" maior e distribuído, "?" bem maior, jaleco do doutor esmaecendo. Cena 2: exame perto e maior, sem vazio ao lado. Cena 3: etiqueta "laudo ou parecer" longe do rosto, elementos reagindo uns aos outros. Cena 4: refeita com o logo do Telessaúde. Cena 8: faltavam alfinetes, fundo e movimento (aplicado na v4). Cenas 5, 6, 7, 9 e 10: "não gostei"; o usuário vai pedir proposta ao ChatGPT com o documento `02-descricao-das-cenas.md`.

- 20/11/2026, som da v3: trilha combinada `animacao/trilha_v3.wav` (marimba do piloto 0–13,6 s → `tecnologia/technology-background-atlasaudio-631954.mp3` 12,6–46,8 s → marimba 45,8 s até o fecho, cruzamentos de 1 s; as duas medem −14,8 LUFS). Mix `animacao/mix_v3.json`: trilha −11 dB, ducking 5 dB, realce +6 dB até 8 s (introdução baixa da marimba), 47 efeitos sintetizados (sem pop), `sfx_db_extra` −5. Resultado: −14,0 LUFS, pico −1,2 dBFS.

- 20/11/2026: v3 refeita do zero depois da devolutiva da v2 (fundo mexendo, alfinetes sem sentido, informação fora da área segura, título cortado pela linha, logos pequenos com sigla, cartões repetidos). Uma linguagem por cena: tela dividida aqui/lá com faixa do título → aproximação no doutor → tipografia → olho em tela cheia (UFG) → mergulho na pupila → fita de ECG (UFMG) → a fita vira a respiração (tele-espirometria) → Maranhão parado com a cobertura saindo de São Luís → doutora com lugar/tempo → o exame recebe o laudo.
- 20/11/2026: o `ufmg-logo.svg` traz dois logos; a página usa só o que fica dentro do quadro original do arquivo.

- 20/11/2026: o usuário prefere avaliar o mapa de cenas **pelos quadros-chave numa folha só**, não pela tabela. O mapa em texto (`01-mapa-de-cenas.md`) fica como referência; a aprovação é pela imagem.

- 20/11/2026: produção começou (segundo da série, depois do piloto Teleorientação).
- 20/11/2026: régua, fechamento e trilha iguais aos do piloto (ok do usuário).
- 20/11/2026: **narração de 57,8 s aprovada pelo usuário** (revisou e não viu incoerência; cabe no vídeo). Não regravar para chegar aos ~45 s do roteiro.
- 20/11/2026: ~~profissional em SVG~~ **recusado** pelo usuário (ficou feio). O profissional da cena 03 vem do **Flow** (prompts em `roteiro/prompts-flow.md`) ou de uma animação pronta da internet que o usuário aprovar.
- 20/11/2026: os pontos do mapa do Maranhão (cena 04) são **ilustrativos**. Se o usuário mandar a lista de municípios, troca pelos reais (malha do IBGE).
- 20/11/2026: logos da UFG e da UFMG entram ao lado das siglas na cena 04.
- 20/11/2026: o "também" que mudou de lugar e o "Ah," da cena 05 são do usuário, de propósito. A narração vale como está.
- 20/11/2026, trilha: base `joyful-marimba` (piloto). O usuário liberou ("me surpreenda") uma segunda trilha se couber. Ideia a testar na prévia de áudio: na cena 03/04 (dados viajando, exames), entrar uma de `tecnologia/` e voltar à marimba no fecho. Decidir na mixagem.

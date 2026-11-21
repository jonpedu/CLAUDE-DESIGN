# Biblioteca geral

A **fonte de onde todos os vídeos bebem**: tudo o que serve a mais de um vídeo (marca, trilhas, efeitos, personagens, mapas, vídeos publicados). Montada em 21/11/2026 a partir do que estava espalhado nas pastas dos vídeos. Lista completa de arquivos, gerada por script: `INVENTARIO.md`.

## Regra de uso (vale para o Claude e para quem editar)

1. **Ao começar um vídeo, consulte a biblioteca antes de pedir qualquer asset.** Na lista de assets cena a cena (`.claude/skills/telessaude/SKILL.md`), marque o que já existe aqui e peça ao usuário só o resto.
2. **Copie, não use daqui.** O item vai para a pasta do vídeo com
   `py ferramentas/da_biblioteca.py "<item>" "<pasta do vídeo>"` (trilhas → `trilha sonora/`, o resto → `elementos/`; nunca substitui o que já existe). A página e a mixagem do vídeo apontam para a cópia, então o vídeo continua igual mesmo se a biblioteca mudar.
   **Exceções**, lidas direto daqui pelo motor: `sfx/` (efeitos sonoros, citados nas mixagens) e `marca/fontes/` (fontes, injetadas pelo `ferramentas/animar.mjs`).
3. **Não edite nem apague nada daqui por conta própria.** Elemento de marca é do usuário: nunca recolorir, redesenhar ou criar substituto.
4. **Item novo que serve a outros vídeos entra aqui** (cópia, com nome descritivo): elemento de marca que o usuário entregar num vídeo, trilha nova, personagem do Flow que pode voltar, SVG baixado com o ok do usuário. Anote na seção certa deste README (com origem e licença) e rode `py ferramentas/da_biblioteca.py --inventario`.
5. **A régua e o fechamento mudam com a parceria.** Mesmo achando aqui, confirme com o usuário qual vale para o vídeo (regra de `telessaude/SKILL.md`).

## O que tem

### `marca/` — identidade (arquivos do usuário)

| Pasta | Conteúdo | Uso |
| --- | --- | --- |
| `reguas/` | `regua - tele-sted-sus-govbr.svg` (Telessaúde + sted + SUS Digital + Gov; padrão dos vídeos próprios do NTS, 1080×160) · `Ajustada TELE e PETSAUDE Digital.png` (parceria PET-Saúde) · `exemplo de uso da regua em ilha (16x9).png` · `regua_ilha.py` (monta a ilha 16:9 a partir do PNG, sem alterar a régua) | régua centralizada na base, o vídeo inteiro (`formatos/vertical.md`, `formatos/horizontal.md`) |
| `fechamentos/vertical/` | `Intro Telessaude.mp4` (só NTS, 4,4 s, com som) · `Intro NTS e PETSAUDE.mp4` | último bloco do vídeo, com o som de logo |
| `fechamentos/horizontal/` | `Intro NTS e PETSAUDE - horizontal.mp4` | 16:9 da parceria PET-Saúde |
| `logos/telessaude/` | `1.svg` a `10.svg` (variações do logo, da pasta "Uso marcas Telessaúde") · `logo-telessaude-vertical.svg` (cópia nomeada do `1.svg`) | logo avulso em cena (ex.: Telediagnóstico, cena 4) |
| `logos/parceiros/` | `UFG_logo.svg`, `ufmg-logo.svg` (monocromáticos escuros; o da UFMG traz dois logos, um fora do quadro) | parceiros dos exames de telediagnóstico; animar parte por parte embutindo o SVG |
| `fontes/` | Poppins (base), Exo 2, Inter, Glacial Indifference, Bebas Neue, Computer Says No (CC BY-SA, pede atribuição) | regras em `.claude/skills/telessaude/fontes.md` |
| `cores/` | guia de cores do portal (clara e escura) | valores e regras em `.claude/skills/telessaude/cores.md` |

### `trilhas/` — trilhas sonoras

Por clima (`animado/`, `corporativo/`, `emocional/`, `suave/`, `tecnologia/`; 20 faixas com LUFS e licença no `trilhas/README.md`) e `usadas-em-videos/` (`Balanced Learning Loop (Remix) v2.mp3`, do AVC e do IAM; `Regulate - Dyalla.mp3`, da Hipertensão PET-Saúde).

### `sfx/` — efeitos sonoros

`sintetizados/`: whoosh, swish, tique, impacto, digitação, notificação de marimba (gerados por `ferramentas/sfx.py`, livres de licença). `pop*`, `bolha` e `blob` ficaram fora do gosto do usuário (`telessaude/SKILL.md`, Som); não use.

### `elementos/` — elementos reutilizáveis

| Pasta | Conteúdo |
| --- | --- |
| `mapas/` | `brazil.svg` (estados com id, ex. `BR-MA`) e `mapa_br.js` (o mesmo mapa pronto para a página) · **`maranhao-municipios.svg`** (os 217 municípios, 1000×1330; cada um é um `<path id="mun-<código IBGE>" data-nome="…" data-regiao-imediata="…">`, ex. São Luís = `mun-2111300`) · `maranhao-municipios-centros.json` (centro de cada município em px do mesmo SVG, para alfinete, rótulo ou a cobertura se espalhando a partir de São Luís, em x 643, y 229) · `maranhao-contorno-ibge.svg` (só o contorno do estado) · `_previa-maranhao-municipios.png`. Fonte: IBGE, malhas territoriais (dados públicos), baixado em 21/11/2026 |
| `icones/phosphor/` | **Phosphor Icons 2.1.1** (licença MIT, `LICENSE.txt`): 1.512 ícones em 4 pesos (`regular/`, `bold/`, `fill/`, `duotone/`), arquivo `<nome>-<peso>.svg`. Usam `currentColor`: a cor vem do CSS da página (azul da marca, cor do tema). O `duotone` combina com o flat dos vídeos. Prévia dos de saúde, tecnologia e cotidiano: `icones/_folha-saude-tecnologia.png` |
| `icones/lucide/` | **Lucide 1.77** (licença ISC, `LICENSE.txt`): 2.410 ícones de traço; `_tags.json` traz palavras-chave em inglês de cada um para busca |
| `personagens-flow/avc/`, `iam/` | clipes do Flow dos vídeos PET-Saúde (personagem enfermeiro/apresentador, gestos, cérebro, coração), fundo claro |
| `personagens-flow/telediagnostico-medico-tablet/` | médico com tablet, 5 clipes, fundo branco |
| `personagens-flow/teleorientacao-pessoas-celular/` | idosa, agricultor e estudante com celular, 16:9, fundo branco (servem aos dois formatos) |
| `folhas-de-elementos/avc/`, `iam/` | folhas de ícones e personagens geradas por IA, para recorte (`ferramentas/recortar.py`) |

Personagens do Flow entram em multiplicar sobre fundo claro, sem recorte (`telessaude/SKILL.md`, "Imagem e personagens"). Para reaproveitar um personagem num vídeo novo, mantenha a mesma descrição física no prompt (`prompts-flow`).

### `videos-publicados/` — vídeos aprovados e capas

Antiga `videos-referencia/`. Finais publicados por tipo (`TELEORIENTAÇÃO/` com a série PET-Saúde, Câncer de Pênis, Hanseníase, Hipertensão, Retinopatia; campanhas; Kits de Telessaúde; Retrospectiva 2025; Ação em Tauá-Mirim), com as capas, e `capas-youtube/` (20 capas dos Shorts, links em `fontes.md`). Servem de referência de estilo (`analise-referencias/`), de vídeo-base para as reconstruções em 16:9 (`planejamento/videos-para-refazer-na-horizontal.md`) e de trechos para citar vídeos anteriores (ex.: cena 03 da Teleorientação).

### Modelos de página (ficam no vídeo, não aqui)

O código das animações fica na pasta de cada vídeo, porque aponta para os arquivos dele. Para começar um vídeo novo, parta de um destes e copie para `renderizando/_claude/animacao/` do vídeo novo:

| Modelo | Arquivo | Serve para |
| --- | --- | --- |
| Horizontal 16:9 (reconstrução) | `REFAZENDO-VIDEOS/hipertensao 2/renderizando/_claude/animacao/hipertensao2_h.html` | deslocamento suave (`data-k`), fundo vivo (`data-fundo`), duas colunas |
| Vertical institucional (série Serviços do NTS) | `CRIANDO-VIDEOS/SERVIÇOS NTS/TELEORIENTAÇÃO/renderizando/_claude/animacao/teleorientacao_v3.html` | notificação como fio condutor, pessoas do Flow em multiplicar, mapa |
| Vertical teleorientação (PET-Saúde) | `CRIANDO-VIDEOS/AVC/renderizando/_claude/animacao/completo_v4.html` | cartões, listas com escala dinâmica, clipes do Flow |

## O que falta (para procurar ou pedir)

Feito em 21/11/2026: mapa do Maranhão por município (IBGE) e bancos de ícones SVG (Phosphor e Lucide), em `elementos/`.

Em ordem de importância para os próximos vídeos:

1. **Fechamento horizontal só do Telessaúde** (`Intro Telessaude` em 16:9). Bloqueia as versões 16:9 da série Serviços do NTS. Do usuário (Canva).
2. **Régua PET-Saúde em SVG** e a **variante com o logo "MARANHÃO" (SES) em primeiro**, citada em `telessaude/SKILL.md`. Hoje só existe o PNG do PET-Saúde. Do usuário.
3. **Som de logo isolado** (`.wav` do fechamento), para quando o fechamento entrar sem o vídeo dele. Do usuário, ou extrair do `Intro*.mp4`.
4. **Logos dos parceiros em SVG:** PET-Saúde, SEMUS São Luís, SES-MA/Governo do Maranhão, Ministério da Saúde, SUS Digital, sted. Hoje só aparecem dentro das réguas. Do usuário.
5. **Efeitos sonoros reais** (pasta de efeitos do usuário e trechos úteis do áudio dos clipes do Flow), para não depender só dos sintetizados.
6. **Páginas do Canva em PNG** dos vídeos a reconstruir em 16:9 (Obesidade infantil, Hanseníase outubro, Diabetes e Dengue, partes 1 e 2; Câncer de pênis, Hanseníase, Hipertensão e Retinopatia próprios do NTS). Do usuário.
7. **Capas do YouTube do AVC e do IAM**, quando forem publicados.
8. **Registro da voz do AI Studio** usada nas narrações (nome da voz e configurações), para manter a mesma voz na série. Do usuário; anotar em `telessaude/tipos/`.

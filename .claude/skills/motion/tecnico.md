# Pipeline técnico local

Tudo roda na máquina do usuário (Windows). Numa máquina ou conta nova, rode `/preparar` (ou `py ferramentas/preparar.py`): confere ffmpeg, Python e pacotes (`requirements.txt`), Node, `playwright-core` e Chrome, e o material de cada vídeo. Instalação no `README.md`.

## Windows (ajustes conhecidos; valem em qualquer máquina Windows, sobretudo com acento no caminho)

- Python é `py` (`python` abre a loja). Pacotes: Pillow, numpy, OpenCV, faster-whisper (`py -m pip install -r requirements.txt`). `PYTHONIOENCODING=utf-8` ao imprimir nomes com acento.
- `cv2.imread`/`imwrite` falham com "Usuário" no caminho: leia e grave imagens com Pillow.
- Playwright: `playwright-core` em `ferramentas/` (`npm install` lá dentro), `channel: 'chrome'`, página por `file://` (não `setContent`); em Node, caminhos com `fileURLToPath`.
- faster-whisper: o áudio entra decodificado pelo ffmpeg (já feito em `transcrever.py`).
- `drawtext` do ffmpeg trava aqui (fontconfig): para folhas de contato, use `ferramentas/folha.py` ou Pillow.

## Ferramentas do projeto (`ferramentas/`)

| Script | Para quê |
| --- | --- |
| `novo_video.py` | cria as pastas de um vídeo novo e o `_claude/00-estado.md` (primeiro comando de todo vídeo) |
| `transcrever.py` | tempo por palavra da narração |
| `narracao.py` | silêncio no início e pausas maiores/menores entre frases (só dentro dos silêncios); imprime a função `N(t)` para a página |
| `bordas.py` | margem fantasma: bordas que cada clipe toca |
| `recortar.py` | recortes PNG de quadros ou folhas (fundo branco, sementes, traço, `CHROMA=1`); no chroma, pedaços de figuras vizinhas que entram na caixa saem sozinhos |
| `animar.mjs` + `ts-anim.js` + `telessaude.css` | motor `render(t)`; `FOTOS="t1,t2"` gera quadros de prova |
| `folha.py` | folha de contato dos quadros de prova com a área segura e o tempo |
| `sfx.py` | efeitos sintetizados; `--digitar nome="texto"@cps` gera a digitação de um texto da página |
| `mixar.py` | narração + trilha com ducking + efeitos + fechamento, −14 LUFS |
| `trocar_trecho.py` | **ajuste pontual sem perder qualidade:** renderiza só entre dois quadros-chave e junta com cópia direta (o resto fica idêntico, sem recodificar). Use em vez de `emendar.py`, que recodifica tudo em CRF 17. Ex. AVC v4.1: 250 quadros em 45 s em vez de ~5 min |
| `editor.mjs` + `editor-ui.js` + `editor_comparar.py` | **editor de quadros-chave** (ver seção abaixo) |
| `emendar.py`, `rastrear.py` | refazer trechos recodificando o vídeo todo (prévias); rastrear o corpo no clipe |

Na página, `TS.$` é `querySelector` (precisa de `#`); para ids, defina `const $ = (id) => document.getElementById(id)`. Texto branco sobre azul: não use a classe `.titulo` (a cor dela vence `.branco`); ponha `color:#fff` no próprio elemento.

## Editor de quadros-chave (devolutiva visual do usuário)

Feito em 16/11/2026, a pedido do usuário: em vez de prints marcados e explicação por texto, ele mexe direto na cena.

- **Abrir:** `node ferramentas/editor.mjs "<página .html>" "t1,t2"` (horizontal: `TELA=1920x1080`; tamanho na tela: `ESCALA=0.42`). Abre um Chrome visível com a cena e um painel ao lado. Dê ao usuário o comando pronto, com os tempos dos quadros-chave.
- **O que ele faz:** clica numa peça e arrasta (Alt+clique alterna entre a peça inteira e as partes dela; clique em área vazia só solta a seleção); puxa o quadrado do canto para mudar o tamanho; `H` oculta; desenha seta, círculo ou nota; escreve uma observação geral; navega no tempo (`,` e `.` = um quadro). A máscara da área segura liga com `M`.
- **Quadros-chave por elemento (16/11/2026):** cada mudança vale a partir do momento em que foi feita. Com um só quadro-chave, vale para o vídeo todo; ajustando o mesmo elemento em outro momento, o editor cria outro quadro-chave e anima entre os dois (`suave`, easeInOutCubic) ou troca de uma vez (`corte`). `0` = "sem ajuste neste momento"; `[` `]` pulam entre os quadros-chave; a trilha sob o tempo mostra os losangos. Ex.: ambulância maior na ida (44,2 s) e normal na volta (45,9 s).
- **Salvar** grava em `renderizando/_claude/quadros/ajustes/<data-hora>/`: `ajustes.json` + `t<tempo>_antes.png`, `_depois.png` e `_comparacao.png` (lado a lado, caixas numeradas).
- **Como aplicar:** leia o `ajustes.json`. Cada ajuste traz o elemento (`#id` ou caminho a partir do id mais próximo), o texto dele, a `transicao` e os `quadros_chave` (tempo, caixas antes/depois em px do vídeo, deslocamento visto na tela e `transform_extra`). Um só quadro-chave: leve a mudança para a **posição de repouso** do elemento (o valor de base, não um transform solto por cima). Vários: escreva na página a animação entre os momentos (escala e posição em função de `t`, com a curva da casa), respeitando `corte` quando for o caso. Confira com quadros de prova nos tempos dos quadros-chave e no meio deles. Anotações (seta, círculo, nota) são pedidos para interpretar, como uma devolutiva escrita.
- **Os ajustes são guia, não tempo exato (regra do usuário, 16/11/2026).** O usuário marca um quadro qualquer em que o elemento aparece, não necessariamente o primeiro. Por isso:
    - **Um quadro-chave** = mudança **global**: aplique a escala e a posição em toda a presença do elemento naquela cena (antes e depois do tempo marcado), ajustando a animação de base, não só a partir daquele quadro.
    - **Vários quadros-chave** = o elemento deve ter tamanhos/posições diferentes em **fases** diferentes da cena. Os tempos dizem qual fase é qual (ex.: a ambulância na ida e na volta), não o quadro exato da mudança: faça a troca no ponto natural da animação (início de um movimento, saída de tela, corte), com a curva da casa.
    - Na dúvida sobre a intenção, mostre um quadro de prova antes e depois da mudança e pergunte.
- **Limites:** dentro de um clipe do Flow não se movem partes (o clipe inteiro sim); antes do primeiro e depois do último quadro-chave vale o valor mais próximo, então confira os outros momentos em que o elemento aparece.
- **Para páginas novas:** dê `id` às peças principais (cartões, títulos, ícones, clipes): o editor e o `ajustes.json` ficam mais claros.

## Ferramentas por tarefa

| Tarefa | Ferramenta |
| --- | --- |
| Grafismos, texto cinético, cartões, ícones | HTML/CSS/SVG (com as fontes da marca) animado por uma função `render(t)` e capturado quadro a quadro com Playwright |
| Reenquadrar cenas de vídeo (16:9 → 9:16), Ken Burns, máscaras | ffmpeg (`crop`, `scale`, `zoompan`, `overlay`) ou OpenCV |
| Legendas estilizadas | arquivo `.ass` queimado com ffmpeg (`subtitles=`), ou desenhadas no HTML |
| Composição, transições, junção, áudio | ffmpeg (`overlay`, `xfade`, `concat`, `amix`, `sidechaincompress`, `loudnorm`) |
| Medir a narração e encontrar pausas | ffmpeg `silencedetect` / `ebur128` |

Se o usuário quiser uma biblioteca (Remotion, GSAP, Lottie), instale localmente no projeto com npm e registre no `CLAUDE.md` do projeto.

## Outras tecnologias (registro para quando precisar)

Conversa de 16/11/2026. A base continua sendo **HTML/CSS/SVG + Playwright** (`render(t)` quadro a quadro), que já é motion de verdade e cobre texto, cartões, ícones e transições. As outras entram só quando um vídeo pedir algo que a base não faz bem:

| Tecnologia | Quando usar | Observações |
| --- | --- | --- |
| **Lottie** (lottie-web) | ícones animados prontos (LottieFiles) ou exportados do After Effects | **primeira a acrescentar**; roda dentro da página atual, no mesmo `render(t)` (avançar o quadro do Lottie pelo tempo) |
| **Blender** (scripts `bpy`) | 3D de verdade: câmera voando, objetos com volume, luz, rastreio 3D de câmera em filmagem | o Claude escreve os scripts; render pesado, escolher a máquina mais forte |
| **Remotion** | o mesmo que a base, em React, com linha do tempo e prévia ao vivo | mais organizado em projetos grandes; **licença paga para empresas acima de certo porte**: conferir antes de usar em trabalho institucional |
| **Motion Canvas** | animação explicativa em código (diagramas, passo a passo) | código aberto |
| **GSAP** | curvas e linhas do tempo complexas dentro do HTML | usar no modo controlado por `t` (pausado, `seek(t)`), nunca no relógio real |
| **Premiere / DaVinci Resolve via XML** | quando o usuário quiser ajustar à mão num editor | o Claude gera o XML (cortes, trilhas, mídia); quem renderiza é o editor. Perde o ciclo "renderizar → olhar o quadro → ajustar" |
| **After Effects** (ExtendScript) | só se um cliente exigir projeto `.aep` | o Claude não vê a interface |

### Vídeo com câmera real (vlog, entrevista, registro)

Ainda não usado; registrar em `video-real.md` quando surgir o primeiro. O fluxo vale para qualquer máquina: o que for pesado está marcado, e o usuário escolhe onde rodar.

| Tarefa | Como |
| --- | --- |
| Cortes de vlog (silêncios, "é…", tropeços) | transcrição com tempo por palavra (`transcrever.py`) e corte pelo texto |
| Legenda dinâmica | página HTML ou `.ass` a partir das palavras |
| Movimento de câmera digital, reenquadrar seguindo o rosto | ffmpeg (`crop`, `zoompan`) + detecção de rosto |
| Estabilização | ffmpeg `vidstab` |
| Cor (balanço de branco, contraste, LUT `.cube`, igualar planos) | ffmpeg (`eq`, `curves`, `colorbalance`, `lut3d`); o usuário aprova pelo olho |
| Áudio (ruído, EQ, compressão, volume) | ffmpeg (`afftdn`, `arnndn`), DeepFilterNet; separar voz com Demucs (pesado) |
| Texto atrás da pessoa, recorte do fundo | segmentação de vídeo (pesado) |
| Foto com efeito 3D (parallax) | estimativa de profundidade + deslocamento (pesado) |
| Material longo ou 4K | cópias leves (proxies) para trabalhar; o original só no render final |

## Organização de um projeto de vídeo

A sub-skill de marca define as pastas de entrada (no Telessaúde, `telessaude/organizacao.md`). Sem sub-skill, use a mesma estrutura:

```
<vídeo>/
  audios/  roteiro/  elementos/  trilha sonora/      entrada (do usuário; o Claude não grava aqui)
  renderizando/                                      só o final aprovado e a capa dele
    _claude/                                         trabalho do Claude
      00-estado.md        estado do vídeo: versão atual, o que falta, decisões
      transcricao/        tempo por palavra
      decupagem/          takes e trechos úteis
      camadas/            recortes e elementos preparados
      animacao/           página HTML (render(t)), mix_vN.json (mixagem), narração editada
      quadros/            quadros de prova e folhas com a área segura
      versoes-anteriores/ prévias e versões em avaliação
  <TEMA> - estudo da edição.md                       registro do vídeo (o que entrou, técnicas, revisões)
```

> **Observação (estrutura antiga, guardada a pedido do usuário em 16/11/2026).** Antes de unificar com `organizacao.md`, este arquivo propunha a estrutura abaixo, provavelmente herdada do repositório **fluxo-de-edicao** (8 etapas) que inspirou o fluxo. Não é a usada hoje, mas **analise-a ao criar estruturas para outros tipos de vídeo ou clientes**: ela separa bem referências, entradas, plano, cenas, provas e saídas.
>
> ```
> <projeto>/
>   referencias/   régua, roteiro original, prints de estilo
>   entrada/       narração, roteiro final, cenas, imagens, trilha
>   plano.md       plano cronometrado (metodo-referencia.md)
>   cenas/         uma pasta por cena: código da animação + mp4 renderizado
>   provas/        quadros-chave PNG e máscara de área segura
>   saida/         vídeos finais, capas, .srt
> ```

`ferramentas/novo_video.py <pasta>` cria essa estrutura e o `00-estado.md`. O motor é sempre o de `ferramentas/`; por vídeo ficam só os **dados**: a página da animação e a mixagem: um `mix_vN.json` lido por `mixar.py` (narração, trilha, efeitos sonoros com tempos e volumes, fechamento). No AVC ele era gerado por um `gera_mix.py`; nos vídeos mais novos é escrito direto.

## Regras de render

- **Determinístico:** a animação é função do tempo `t` (`render(t)`), nunca de relógio real; o mesmo `t` gera o mesmo quadro.
- **Quadros de prova primeiro:** renderize 4–6 PNGs nos momentos de maior densidade e olhe antes do vídeo completo.
- **Uma cena = um arquivo:** cada cena vira um MP4 com as mesmas configurações (resolução, fps, codec, pixel format). Junte com o concat demuxer e `-c copy`, depois acrescente o áudio com `-c:v copy`.
- **Transições dentro da cena:** crossfade e wipes ficam dentro do arquivo da cena, para não reencodar tudo.
- **Nome temporário:** renderize para `cena_03.tmp.mp4` e renomeie para `cena_03.mp4` só se o ffmpeg terminar com código 0.
- **Imagem parada:** `-framerate 30 -i s.png -vf format=yuv420p,loop=-1:1,trim=duration=D` em vez de `-loop 1`.
- **Codificação de trabalho:** `-c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p`; final com o mesmo CRF.
- **Alterar um vídeo pronto:** troque só a cena afetada (e a vizinha, se tiver transição com ela); som novo com `-c:v copy`.

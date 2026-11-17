# Pipeline técnico local

Tudo roda na máquina do usuário (Windows). Na primeira sessão, verifique `ffmpeg -version`, `python --version` (com Pillow, numpy, opencv-python) e `node -v`. Se faltar algo, diga ao usuário o que instalar antes de começar.

## Ferramentas por tarefa

| Tarefa | Ferramenta |
| --- | --- |
| Grafismos, texto cinético, cartões, ícones | HTML/CSS/SVG (com as fontes da marca) animado por uma função `render(t)` e capturado quadro a quadro com Playwright |
| Reenquadrar cenas de vídeo (16:9 → 9:16), Ken Burns, máscaras | ffmpeg (`crop`, `scale`, `zoompan`, `overlay`) ou OpenCV |
| Legendas estilizadas | arquivo `.ass` queimado com ffmpeg (`subtitles=`), ou desenhadas no HTML |
| Composição, transições, junção, áudio | ffmpeg (`overlay`, `xfade`, `concat`, `amix`, `sidechaincompress`, `loudnorm`) |
| Medir a narração e encontrar pausas | ffmpeg `silencedetect` / `ebur128` |

Se o usuário quiser uma biblioteca (Remotion, GSAP, Lottie), instale localmente no projeto com npm e registre no `CLAUDE.md` do projeto.

## Organização de um projeto de vídeo

```
<projeto>/
  referencias/   régua, roteiro original, prints de estilo
  entrada/       narração, roteiro final, cenas, imagens, trilha
  plano.md       plano cronometrado (metodo-referencia.md)
  cenas/         uma pasta por cena: código da animação + mp4 renderizado
  provas/        quadros-chave PNG e máscara de área segura
  saida/         vídeos finais, capas, .srt
```

## Regras de render

- **Determinístico:** a animação é função do tempo `t` (`render(t)`), nunca de relógio real; o mesmo `t` gera o mesmo quadro.
- **Quadros de prova primeiro:** renderize 4–6 PNGs nos momentos de maior densidade e olhe antes do vídeo completo.
- **Uma cena = um arquivo:** cada cena vira um MP4 com as mesmas configurações (resolução, fps, codec, pixel format). Junte com o concat demuxer e `-c copy`, depois acrescente o áudio com `-c:v copy`.
- **Transições dentro da cena:** crossfade e wipes ficam dentro do arquivo da cena, para não reencodar tudo.
- **Nome temporário:** renderize para `cena_03.tmp.mp4` e renomeie para `cena_03.mp4` só se o ffmpeg terminar com código 0.
- **Imagem parada:** `-framerate 30 -i s.png -vf format=yuv420p,loop=-1:1,trim=duration=D` em vez de `-loop 1`.
- **Codificação de trabalho:** `-c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p`; final com o mesmo CRF.
- **Alterar um vídeo pronto:** troque só a cena afetada (e a vizinha, se tiver transição com ela); som novo com `-c:v copy`.

"""Edita o tempo da narração: silêncio no início e pausas maiores (ou menores) entre frases, sem tocar nas palavras.
Uso: py ferramentas/narracao.py <entrada.wav> <saida.wav> <inicio_s> [corte:delta ...]
  inicio_s  silêncio antes da primeira palavra (ex.: 2.0 para um gancho só visual)
  corte:delta  em `corte` (segundos do áudio ORIGINAL, sempre dentro de um silêncio) soma `delta` s de pausa;
               delta negativo encurta a pausa (remove de corte até corte+|delta|).
Exemplo: py ferramentas/narracao.py narr.wav narr_editada.wav 2.0 10.70:0.5 22.35:0.5
Imprime a tabela de deslocamentos: na página, use N(t_original) = t_original + deslocamento do trecho
(função gerada no fim, pronta para colar no HTML). Antes de cortar, confira os silêncios com
ffmpeg -af silencedetect=n=-40dB:d=0.25 — o corte nunca pode cair dentro de uma palavra.
"""
import subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")

ent, sai, ini = sys.argv[1], sys.argv[2], float(sys.argv[3])
cortes = sorted((float(a.split(":")[0]), float(a.split(":")[1])) for a in sys.argv[4:])

# trechos do original: [a, b) com deslocamento acumulado
trechos, a, desl = [], 0.0, ini
for c, d in cortes:
    trechos.append((a, c, desl))
    if d >= 0:
        a, desl = c, desl + d
    else:
        a, desl = c - d, desl + d  # pula |d| s do original
trechos.append((a, None, desl))

fil, rot = [], []
trechos = [x for x in trechos if x[1] is None or x[1] > x[0]]   # corte em 0 com delta negativo = aparar o silêncio inicial
for i, (a, b, dl) in enumerate(trechos):
    tr = f"atrim=start={a}" + (f":end={b}" if b is not None else "")
    fil.append(f"[0:a]{tr},asetpts=PTS-STARTPTS,adelay={int(round((a + dl) * 1000))}:all=1[t{i}]")
    rot.append(f"[t{i}]")
fil.append(f"{''.join(rot)}amix=inputs={len(rot)}:normalize=0:dropout_transition=0[s]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", ent, "-filter_complex", ";".join(fil), "-map", "[s]",
                "-c:a", "pcm_s16le", sai], check=True)

print("trecho original        deslocamento")
for a, b, dl in trechos:
    print(f"  {a:7.2f} – {('fim' if b is None else f'{b:.2f}'):>7}   +{dl:.2f} s")
lim = [b for _, b, _ in trechos[:-1]]
print("\n// cole na página: tempo original da palavra → tempo do vídeo")
print("const N = (o) => o + " + " ".join(f"(o < {b} ? {dl} :" for (_, b, dl) in trechos[:-1])
      + f" {trechos[-1][2]}" + ")" * len(lim) + ";")

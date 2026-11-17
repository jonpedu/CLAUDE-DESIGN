"""Troca só um trecho de um vídeo já renderizado, sem recodificar o resto (cópia direta do fluxo).
Uso: py ferramentas/trocar_trecho.py <pagina.html> <base.mp4> <saida.mp4> <t_ini> <t_fim>
     (variáveis do motor valem: QUALIDADE=max se a base foi feita com QUALIDADE=max; a base precisa ser o vídeo
      SEM áudio que saiu do animar.mjs, com os mesmos parâmetros de codificação)
Como funciona:
  1. acha o quadro-chave da base em ou antes de t_ini e o primeiro em ou depois de t_fim;
  2. renderiza a página só entre esses dois quadros-chave (1 worker, mesma qualidade da base);
  3. corta a base nos quadros-chave com -c copy (segment muxer) e junta antes + trecho + depois com -c copy;
  4. confere o número de quadros. Fora do trecho, os quadros ficam idênticos aos da base (PSNR infinito).
Depois, rode a mixagem (mixar.py) apontando para a nova saída.
"""
import os, subprocess, sys, tempfile
from pathlib import Path

pag, base, saida, ti, tf = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
AQUI = Path(__file__).resolve().parent
fps = 30


def q(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                        "stream=nb_read_frames", "-of", "csv=p=0", str(f)], capture_output=True, text=True, check=True)
    return int(r.stdout.strip().strip(","))


r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-skip_frame", "nokey", "-show_entries",
                    "frame=pts_time", "-of", "csv=p=0", str(base)], capture_output=True, text=True, check=True)
chaves = sorted({round(float(x.strip(",")) * fps) for x in r.stdout.split() if x.strip(",")})
total = q(base)
k0 = max(k for k in chaves if k <= round(ti * fps))
depois = [k for k in chaves if k >= round(tf * fps)]
k1 = depois[0] if depois else total
print(f"quadros-chave: {k0} ({k0 / fps:.2f} s) → {k1} ({k1 / fps:.2f} s); {k1 - k0} quadros a renderizar")

with tempfile.TemporaryDirectory(dir=saida.parent) as tmp:
    tmp = Path(tmp)
    trecho = tmp / "trecho.mp4"
    env = dict(os.environ, WORKERS="1")
    subprocess.run(["node", str(AQUI / "animar.mjs"), pag, str(trecho), repr(k0 / fps), repr(k1 / fps)], env=env, check=True)
    marcas = ",".join(str(k) for k in (k0, k1) if 0 < k < total)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(base), "-map", "0:v", "-c", "copy", "-f", "segment",
                    "-segment_frames", marcas, "-reset_timestamps", "1", str(tmp / "p%d.mp4")], check=True)
    partes = sorted(tmp.glob("p*.mp4"), key=lambda p: int(p.stem[1:]))
    antes = partes[0] if k0 > 0 else None
    depois_p = partes[-1] if k1 < total else None
    lista = [p for p in (antes, trecho, depois_p) if p]
    (tmp / "lista.txt").write_text("\n".join(f"file '{p.name}'" for p in lista), encoding="utf-8")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "lista.txt"),
                    "-c", "copy", "-movflags", "+faststart", str(saida)], check=True)
n = q(saida)
print("ok", saida, n, "quadros", "(igual à base)" if n == total else f"ATENÇÃO: base tem {total}")

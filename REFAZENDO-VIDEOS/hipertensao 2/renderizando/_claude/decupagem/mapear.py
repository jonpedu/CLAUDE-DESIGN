"""Para cada instante do vídeo vertical, qual tela do Canva (PNG) está mais parecida. Saída: trechos tela/tempo."""
import subprocess, sys, numpy as np
from pathlib import Path
from PIL import Image
B = Path(__file__).resolve().parents[3]
vid = B / "video base vertical" / "Hipertensão PET SAUDE parte 2.mp4"
W, H, FPS = 54, 96, 10
pags = {}
for i in range(1, 22):
    im = Image.open(B / "paginas em png" / f"{i}.png").convert("L").resize((W, H), Image.BILINEAR)
    pags[i] = np.asarray(im, np.float32)[:84]  # ignora a faixa da régua
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(vid), "-vf", f"fps={FPS},scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                     capture_output=True, check=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)[:, :84]
res = []
for k, f in enumerate(fr):
    d = {i: float(np.mean(np.abs(f - p))) for i, p in pags.items()}
    best = min(d, key=d.get); res.append((k / FPS, best, d[best]))
# compacta
seg = []
for t, b, e in res:
    if seg and seg[-1][2] == b: seg[-1][1] = t; seg[-1][3] = min(seg[-1][3], e)
    else: seg.append([t, t, b, e])
for a, z, b, e in seg:
    if z - a >= 0.2: print(f"{a:6.1f}-{z:6.1f}  tela {b:2d}  (melhor erro {e:5.1f})")

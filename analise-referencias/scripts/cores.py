"""Resume paletas por vídeo e mede as cores do logo no cartão final.
Uso: py analise-referencias/scripts/cores.py
"""
import io, json, subprocess
from pathlib import Path
import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parents[2]
d = json.loads((RAIZ / "analise-referencias/dados/paletas.json").read_text(encoding="utf-8"))
for k, v in d.items():
    print(k[:50].ljust(50), " ".join(f"{c['hex']}:{c['pct']}" for c in v[:6]))

p = RAIZ / "videos-referencia/TELEORIENTAÇÃO/Hipertensão/Hipertensão.mp4"
r = subprocess.run(["ffmpeg", "-v", "error", "-ss", "97.5", "-i", str(p), "-frames:v", "1",
                    "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
a = np.asarray(Image.open(io.BytesIO(r.stdout)).convert("RGB")).reshape(-1, 3).astype(int)
sat = (a.max(1) - a.min(1)) > 60
cols, cnt = np.unique((a[sat] // 6) * 6, axis=0, return_counts=True)
for i in np.argsort(-cnt)[:8]:
    print("logo", "#%02X%02X%02X" % tuple(cols[i]), cnt[i])

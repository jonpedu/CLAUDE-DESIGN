"""Decupagem de takes: folha de contato (1 quadro por segundo) e áudio de cada clipe.
Uso: py analise-referencias/scripts/decupar.py <pasta_elementos> <pasta_saida>
Saída: <pasta_saida>/takes_N.jpg e <pasta_saida>/takes.json
"""
import io, json, re, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ent, sai = Path(sys.argv[1]), Path(sys.argv[2])
sai.mkdir(parents=True, exist_ok=True)
clipes = sorted(ent.glob("*.mp4"))
TW, TH, COLS, POR_FOLHA = 162, 288, 10, 4
try:
    fonte = ImageFont.truetype("arial.ttf", 16)
except OSError:
    fonte = ImageFont.load_default()


def quadro(p, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t}", "-i", str(p), "-frames:v", "1",
                        "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
    return Image.open(io.BytesIO(r.stdout)).convert("RGB")


def audio(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-vn",
                        "-af", "silencedetect=n=-40dB:d=0.3,volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True, errors="replace")
    ini = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", r.stderr)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    media = re.search(r"mean_volume: (-?[\d.]+) dB", r.stderr)
    pico = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
    return {"media_db": float(media.group(1)) if media else None, "pico_db": float(pico.group(1)) if pico else None,
            "silencios": [[round(a, 1), round(b, 1)] for a, b in zip(ini, fim)]}


info = []
for i in range(0, len(clipes), POR_FOLHA):
    lote = clipes[i:i + POR_FOLHA]
    img = Image.new("RGB", (COLS * TW, len(lote) * (TH + 26)), (20, 20, 20))
    d = ImageDraw.Draw(img)
    for r, p in enumerate(lote):
        n = i + r + 1
        y = r * (TH + 26)
        d.text((4, y + 4), f"T{n:02d}  {p.name[:70]}", fill=(255, 220, 0), font=fonte)
        for c in range(COLS):
            img.paste(quadro(p, c + 0.5).resize((TW, TH)), (c * TW, y + 26))
            d.text((c * TW + 4, y + 30), f"{c + 0.5:.1f}s", fill=(255, 255, 0), font=fonte)
        a = audio(p)
        info.append({"take": f"T{n:02d}", "arquivo": p.name, **a})
        print(f"T{n:02d}", p.name[:60], a, flush=True)
    img.save(sai / f"takes_{i // POR_FOLHA + 1}.jpg", quality=85)
(sai / "takes.json").write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")

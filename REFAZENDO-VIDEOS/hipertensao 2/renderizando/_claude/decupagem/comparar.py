"""Monta, para cada quadro-chave, o vertical original ao lado do horizontal com a área segura (96 px) e salva em renderizando/quadros-chave/."""
import subprocess, io, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
R = Path(__file__).resolve().parents[2]
vid = R.parent / "video base vertical" / "Hipertensão PET SAUDE parte 2.mp4"
tempos = [float(x) for x in sys.argv[1].split(",")]
out = R / "quadros-chave"; out.mkdir(exist_ok=True)
f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 34)
for k, t in enumerate(tempos, 1):
    h = Image.open(R / "_claude" / "quadros" / f"t{t:06.2f}.png").convert("RGB")
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", str(vid), "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    v = Image.open(io.BytesIO(raw)).convert("RGB").resize((608, 1080))
    ov = Image.new("RGBA", h.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    for r in [(0, 0, 1920, 96), (0, 984, 1920, 1080), (0, 96, 96, 984), (1824, 96, 1920, 984)]:
        d.rectangle(r, fill=(255, 0, 60, 60))
    d.rectangle((96, 96, 1824, 984), outline=(255, 0, 60, 255), width=4)
    m = Image.alpha_composite(h.convert("RGBA"), ov).convert("RGB")
    s = Image.new("RGB", (608 + 24 + 1920, 1080 + 60), "white"); s.paste(v, (0, 60)); s.paste(m, (632, 60))
    d = ImageDraw.Draw(s)
    d.text((10, 12), f"{k}. vertical ({t:.1f} s)", font=f, fill="black"); d.text((642, 12), "horizontal (com a área segura de 96 px)", font=f, fill="black")
    s.save(out / f"{k} - {t:.1f}s.png"); h.save(out / f"{k} - {t:.1f}s - limpo.png")
print("ok", out)

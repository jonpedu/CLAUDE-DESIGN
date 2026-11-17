"""Folha de contato de quadros 9:16 com a área segura (x 65–888, y 288–1248) sobreposta e o tempo de cada quadro.
Uso: py ferramentas/folha.py <pasta_com_pngs> <saida.jpg> [colunas=8] [largura_miniatura=270]
"""
import sys, glob, os
from PIL import Image, ImageDraw
pasta, saida = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 8
w = int(sys.argv[4]) if len(sys.argv) > 4 else 270
fs = sorted(glob.glob(os.path.join(pasta, "*.png")))
h = w * 1920 // 1080; s = w / 1080
fol = Image.new("RGB", (cols * w, ((len(fs) + cols - 1) // cols) * (h + 22)), (40, 40, 40))
d = ImageDraw.Draw(fol)
for i, f in enumerate(fs):
    x, y = (i % cols) * w, (i // cols) * (h + 22)
    fol.paste(Image.open(f).convert("RGB").resize((w, h)), (x, y + 22))
    d.rectangle([x + 65 * s, y + 22 + 288 * s, x + 888 * s, y + 22 + 1248 * s], outline=(255, 0, 255), width=2)
    d.text((x + 4, y + 4), os.path.basename(f)[1:-4], fill=(255, 255, 255))
fol.save(saida, quality=88)
print(saida, len(fs), "quadros")

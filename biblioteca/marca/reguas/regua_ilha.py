"""Régua em ilha (igual à Hipertensão parte 2): PNG sem alteração a 760 px de largura, ilha branca
centralizada e encostada na base, cantos de cima com raio 30, padding lateral 34, sombra suave para cima."""
from PIL import Image, ImageDraw, ImageFilter
import sys
reg = Image.open(sys.argv[1]).convert("RGBA")
w = 760; h = round(reg.height * w / reg.width)
reg = reg.resize((w, h), Image.LANCZOS)
W, H, pad, r = 1920, 1080, 34, 30
iw = w + 2 * pad; x0 = (W - iw) // 2; y0 = H - h
out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
# sombra: 0 -6px 26px rgba(16,24,40,.10)
sm = Image.new("L", (W, H), 0); ImageDraw.Draw(sm).rounded_rectangle([x0, y0 - 6, x0 + iw, H + r], r, fill=int(255 * .10))
sm = sm.filter(ImageFilter.GaussianBlur(13))
out = Image.composite(Image.new("RGBA", (W, H), (16, 24, 40, 255)), out, sm)
ilha = Image.new("L", (W, H), 0); ImageDraw.Draw(ilha).rounded_rectangle([x0, y0, x0 + iw - 1, H + r], r, fill=255)
out.paste(Image.new("RGBA", (W, H), (255, 255, 255, 255)), (0, 0), ilha)
out.alpha_composite(reg, (x0 + pad, y0))
out.save(sys.argv[2]); print("ilha", iw, "x", h, "em x", x0, "y", y0)

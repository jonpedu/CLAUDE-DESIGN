"""Separa automaticamente as figuras de uma tela pronta (PNG do Canva ou quadro de vídeo) em camadas PNG com transparência.
Cada grupo de pixels que não é fundo vira uma camada; uma folha numerada mostra todas para escolher.
Uso: py ferramentas/componentes.py <tela.png|video.mp4> <pasta_saida> [--t 3.5] [--placa fundo.png] [--junta 24] [--min 1500] [--corte 1760] [--prefixo p1]
  --matiz   fundo colorido em degradê: matiz do fundo (vermelho = 0) e --tol a tolerância (padrão 8)
  PNG já transparente (ex.: exportado do Canva sem fundo): a transparência dele é usada direto (prefira sempre).
  --placa   imagem do fundo vazio (ex.: tela só com o degradê); sem ela, o fundo é o quase-branco ligado às bordas.
            Fundo claro: a placa é dividida (campo plano) e o fundo vira branco. Fundo colorido: use --dif 14
            (transparência pela diferença de cor para a placa).
  --junta   distância (px) para juntar pedaços próximos na mesma figura (padrão 24)
  --min     área mínima de uma figura, em px (padrão 1500)
  --corte   ignora tudo abaixo desta linha (régua; padrão 1760 para 1080x1920)
Saída: <prefixo>_cNN.png (recorte RGBA) + <prefixo>_cNN.json (posição na tela) + <prefixo>_folha.png
"""
import argparse, io, json, subprocess
from pathlib import Path
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("fonte"); ap.add_argument("saida")
ap.add_argument("--t", type=float, default=0); ap.add_argument("--placa"); ap.add_argument("--junta", type=int, default=24)
ap.add_argument("--min", type=int, default=1500); ap.add_argument("--corte", type=int, default=1760); ap.add_argument("--prefixo", default="tela")
ap.add_argument("--matiz", type=int, help="matiz do fundo colorido (OpenCV 0-179; vermelho = 0)"); ap.add_argument("--tol", type=int, default=8)
ap.add_argument("--dif", type=int, help="com --placa colorida: diferença mínima de cor para ser figura (ex.: 14)")
A = ap.parse_args()
out = Path(A.saida); out.mkdir(parents=True, exist_ok=True)


def abre(f, t=0):
    if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        return np.asarray(Image.open(f).convert("RGB"))
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", f, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                       capture_output=True, check=True)
    return np.asarray(Image.open(io.BytesIO(r.stdout)).convert("RGB"))


rgb = abre(A.fonte, A.t).copy()
H, W = rgb.shape[:2]
alfa_pronto = None
if A.fonte.lower().endswith(".png"):
    _im = Image.open(A.fonte)
    if _im.mode in ("RGBA", "LA") or "transparency" in _im.info:
        _a = np.asarray(_im.convert("RGBA"))[:, :, 3]
        if (_a < 250).mean() > 0.05:  # PNG já transparente (exportado sem fundo): usa a própria transparência
            alfa_pronto = _a.copy()
if alfa_pronto is not None:
    alfa = alfa_pronto
elif A.matiz is not None:
    # fundo colorido em degradê (ex.: vermelho): é fundo o que tem a matiz do fundo e está ligado às bordas
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV).astype(np.int16)
    dh = np.minimum(np.abs(hsv[:, :, 0] - A.matiz), 180 - np.abs(hsv[:, :, 0] - A.matiz))
    quase = ((dh <= A.tol) & (hsv[:, :, 1] >= 70)).astype(np.uint8)
    fundo = np.zeros((H + 2, W + 2), np.uint8)
    for (x, y) in [(x, 0) for x in range(0, W, 20)] + [(x, H - 1) for x in range(0, W, 20)] + \
                  [(0, y) for y in range(0, H, 20)] + [(W - 1, y) for y in range(0, H, 20)]:
        if quase[y, x] and not fundo[y + 1, x + 1]:
            cv2.floodFill(quase, fundo, (x, y), 2, flags=4 | (255 << 8) | cv2.FLOODFILL_MASK_ONLY)
    alfa = np.where(fundo[1:-1, 1:-1] > 0, 0, 255).astype(np.uint8)
    alfa = cv2.morphologyEx(alfa, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    alfa = cv2.erode(alfa, np.ones((3, 3), np.uint8))
elif A.placa and A.dif:
    # fundo colorido com placa: transparência pela diferença de cor para a placa (sombras suaves ficam semitransparentes)
    placa = abre(A.placa).astype(np.int16)
    dif = np.abs(rgb.astype(np.int16) - placa).max(axis=2).astype(np.float32)
    alfa = np.clip((dif - A.dif) * 255 / 40, 0, 255).astype(np.uint8)
    alfa = cv2.morphologyEx(alfa, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
else:
    if A.placa:
        # correção de campo plano: divide pela placa (fundo vazio). O degradê vira branco puro e o resto mantém o
        # contraste relativo (jaleco branco e traços claros sobrevivem); depois segue como fundo branco.
        placa = abre(A.placa).astype(np.float32)
        rgb = np.clip(rgb.astype(np.float32) / np.maximum(placa, 1) * 255, 0, 255).astype(np.uint8)
    quase = (rgb.min(axis=2) >= 236).astype(np.uint8)
    fundo = np.zeros((H + 2, W + 2), np.uint8)
    for (x, y) in [(x, 0) for x in range(0, W, 20)] + [(x, H - 1) for x in range(0, W, 20)] + \
                  [(0, y) for y in range(0, H, 20)] + [(W - 1, y) for y in range(0, H, 20)]:
        if quase[y, x] and not fundo[y + 1, x + 1]:
            cv2.floodFill(quase, fundo, (x, y), 2, flags=4 | (255 << 8) | cv2.FLOODFILL_MASK_ONLY)
    alfa = np.where(fundo[1:-1, 1:-1] > 0, 0, 255).astype(np.uint8)
    alfa = cv2.erode(alfa, np.ones((3, 3), np.uint8))
if alfa_pronto is None:
    alfa = cv2.GaussianBlur(alfa, (3, 3), 0)
alfa[A.corte:] = 0

k = max(1, A.junta)
grupo = cv2.dilate((alfa > 30).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k)))
n, lab, st, _ = cv2.connectedComponentsWithStats(grupo, connectivity=8)
ordem = sorted([c for c in range(1, n) if st[c, cv2.CC_STAT_AREA] >= A.min], key=lambda c: (st[c, 1] // 120, st[c, 0]))
itens = []
for i, c in enumerate(ordem, 1):
    x, y, w, h = st[c, :4]
    a = np.where(lab[y:y + h, x:x + w] == c, alfa[y:y + h, x:x + w], 0).astype(np.uint8)
    ys, xs = np.where(a > 8)
    if len(xs) == 0:
        continue
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    nome = f"{A.prefixo}_c{i:02d}"
    Image.fromarray(np.dstack([rgb[y:y + h, x:x + w], a])[y0:y1, x0:x1], "RGBA").save(out / f"{nome}.png")
    pos = {"x": int(x + x0), "y": int(y + y0), "w": int(x1 - x0), "h": int(y1 - y0)}
    (out / f"{nome}.json").write_text(json.dumps(pos), encoding="utf-8")
    itens.append((nome, pos))

# folha: a tela com as caixas numeradas
folha = Image.fromarray(rgb).convert("RGB")
d = ImageDraw.Draw(folha)
f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 44)
for nome, p in itens:
    d.rectangle([p["x"], p["y"], p["x"] + p["w"], p["y"] + p["h"]], outline=(255, 0, 90), width=6)
    rot = nome.split("_c")[1]
    d.rectangle([p["x"], p["y"], p["x"] + 70, p["y"] + 52], fill=(255, 0, 90))
    d.text((p["x"] + 6, p["y"] + 2), rot, font=f, fill="white")
folha.resize((W // 2, H // 2)).save(out / f"{A.prefixo}_folha.png")
for nome, p in itens:
    print(nome, p)

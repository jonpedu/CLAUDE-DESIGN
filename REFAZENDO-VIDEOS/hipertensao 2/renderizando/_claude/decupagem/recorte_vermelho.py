"""Recorta as figuras das telas vermelhas (4 e 5) por caixas, com transparência pela diferença para a placa (placa_vermelha.py)."""
import os, sys, numpy as np, cv2
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recorte_vermelho_caixas import CAIXAS

P = "paginas em png"; S = os.path.join("renderizando", "_claude", "camadas")
# diferença mínima de cor para ser figura; o medidor e a dor de cabeça pedem mais (senão a borda da caixa aparece)
LIMIAR = {"medidor_v": 45, "s_cabeca": 32}
for n, cx in CAIXAS.items():
    rgb = np.asarray(Image.open(os.path.join(P, n + ".png")).convert("RGB"))
    placa = np.asarray(Image.open(os.path.join(S, f"p{n}_placa.png")).convert("RGB")).astype(np.int16)
    dif = np.abs(rgb.astype(np.int16) - placa).max(axis=2).astype(np.float32)
    for nome, (x0, y0, x1, y1) in cx.items():
        alfa = np.clip((dif - LIMIAR.get(nome, 14)) * 255 / 40, 0, 255).astype(np.uint8)
        alfa = cv2.morphologyEx(alfa, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        alfa = cv2.GaussianBlur(alfa, (3, 3), 0)
        a = alfa[y0:y1, x0:x1]; ys, xs = np.where(a > 10)
        cx0, cx1, cy0, cy1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
        Image.fromarray(np.dstack([rgb[y0:y1, x0:x1], a])[cy0:cy1, cx0:cx1], "RGBA").save(os.path.join(S, f"p{n}_{nome}.png"))
        print(nome, {"x": int(x0 + cx0), "y": int(y0 + cy0), "w": int(cx1 - cx0), "h": int(cy1 - cy0)})

"""Camadas da cena vermelha a partir dos PNGs transparentes enviados pelo usuário (paginas em png/extra).
ext1 = tela 4, ext2 = tela 5 (mesmo layout 1080x1920 das telas), ext3 = três poses do homem de corpo inteiro (deitadas)."""
import os, sys, numpy as np, cv2
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recorte_vermelho_caixas import CAIXAS
X = os.path.join("paginas em png", "extra"); S = os.path.join("renderizando", "_claude", "camadas")

def corta(im, box, nome):
    sub = im.crop(box); a = np.asarray(sub)[:, :, 3]; ys, xs = np.where(a > 8)
    sub = sub.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)); sub.save(os.path.join(S, nome)); print(nome, sub.size)

def tira_painel(im):
    """Desfaz o painel escuro semitransparente (75,75,75 a 92/255) da tela 5 sobre as figuras que ele cobre."""
    arr = np.asarray(im).astype(np.float32); A = arr[:, :, 3] / 255; C = arr[:, :, :3]
    pa, P = 92 / 255, 75.0
    puro = (np.abs(arr[:, :, 3] - 92) <= 1) & (np.abs(C - P).max(axis=2) <= 2)
    ys, xs = np.where(puro); x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    R = np.zeros(A.shape, bool); R[y0:y1, x0:x1] = True
    af = np.clip((A - pa) / (1 - pa), 0, 1)
    Cf = (C * A[:, :, None] - P * pa * (1 - af[:, :, None])) / np.maximum(af[:, :, None], 1e-3)
    out = arr.copy()
    out[R, :3] = np.clip(Cf[R], 0, 255); out[R, 3] = af[R] * 255
    return Image.fromarray(out.astype(np.uint8), "RGBA")

for n, arq in [("4", "ext1.png"), ("5", "ext2.png")]:
    im = Image.open(os.path.join(X, arq)).convert("RGBA")
    if n == "5":
        im = tira_painel(im)
    for nome, box in CAIXAS[n].items():
        corta(im, box, f"x{n}_{nome}.png")
# poses: gira para ficar em pé e separa as três figuras
im = Image.open(os.path.join(X, "ext3.png")).convert("RGBA").rotate(-90, expand=True)
a = (np.asarray(im)[:, :, 3] > 20).astype(np.uint8)
a = cv2.dilate(a, np.ones((25, 25), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(a)
grandes = sorted([c for c in range(1, n) if st[c, 4] > 20000], key=lambda c: st[c, 0])
for k, c in enumerate(grandes, 1):
    x, y, w, h = st[c, :4]; corta(im, (x, y, x + w, y + h), f"x_homem_pose{k}.png")

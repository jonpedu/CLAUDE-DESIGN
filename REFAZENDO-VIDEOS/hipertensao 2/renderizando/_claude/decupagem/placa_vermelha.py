"""Fundo vazio (placa) das telas vermelhas 4 e 5: tira as figuras e preenche com o degradê vizinho (inpaint em escala reduzida)."""
import os, sys, numpy as np, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
P = "paginas em png"; S = os.path.join("renderizando", "_claude", "camadas")
for n in ["4", "5"]:
    rgb = np.asarray(Image.open(os.path.join(P, n + ".png")).convert("RGB"))
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV).astype(np.int16)
    dh = np.minimum(hsv[:, :, 0], 180 - hsv[:, :, 0])
    fundo = (dh <= 6) & (hsv[:, :, 1] >= 90)
    fig = (~fundo).astype(np.uint8)
    fig = cv2.morphologyEx(fig, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    fig = cv2.dilate(fig, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (81, 81)))
    # as caixas das figuras (recorte_vermelho.py) entram inteiras na máscara: pele de tom avermelhado não vira fundo
    from recorte_vermelho_caixas import CAIXAS
    for (x0, y0, x1, y1) in CAIXAS[n].values():
        fig[max(0, y0 - 20):y1 + 20, max(0, x0 - 20):x1 + 20] = 1
    k = 8
    peq = cv2.resize(rgb, (rgb.shape[1] // k, rgb.shape[0] // k), interpolation=cv2.INTER_AREA)
    mpeq = cv2.resize(fig * 255, (peq.shape[1], peq.shape[0]), interpolation=cv2.INTER_NEAREST)
    cheio = cv2.inpaint(peq, mpeq, 12, cv2.INPAINT_TELEA)
    cheio = cv2.GaussianBlur(cheio, (0, 0), 3)
    placa = cv2.resize(cheio, (rgb.shape[1], rgb.shape[0]), interpolation=cv2.INTER_CUBIC)
    placa = np.where(fig[:, :, None] > 0, placa, rgb)
    placa = cv2.GaussianBlur(placa, (0, 0), 2)
    Image.fromarray(placa).save(os.path.join(S, f"p{n}_placa.png"))
print("ok")

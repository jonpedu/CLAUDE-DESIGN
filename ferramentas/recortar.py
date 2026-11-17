"""Recorta elementos de um quadro com fundo branco liso em camadas PNG com transparência.
O fundo é o branco conectado às bordas (flood fill); brancos internos (camisa, olhos) continuam opacos.
Uso (caixas):   py ferramentas/recortar.py <video_ou_png> <tempo_s> <pasta_saida> nome=x0,y0,x1,y1 [...]
Uso (sementes): py ferramentas/recortar.py <video_ou_png> <tempo_s> <pasta_saida> nome=x,y;x,y [...]
  sementes = um ou mais pontos dentro de cada figura; figuras que se tocam são separadas pela fronteira natural.
Cada camada vira <nome>.png recortado no conteúdo, e <nome>.json com a posição no quadro original.
"""
import io, json, subprocess, sys
from pathlib import Path
import numpy as np
import cv2
from PIL import Image

fonte, tempo, saida = sys.argv[1], float(sys.argv[2]), Path(sys.argv[3])
saida.mkdir(parents=True, exist_ok=True)
caixas = {a.split("=")[0]: tuple(map(int, a.split("=")[1].split(","))) for a in sys.argv[4:]
          if len(a.split("=")[1].split(",")) == 4 and ";" not in a}
# nome terminado em * = ícone de traço: transparência pela escuridão do traço (sem erosão, preserva linhas finas)

if fonte.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
    img = Image.open(fonte).convert("RGB")
else:
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(tempo), "-i", fonte, "-frames:v", "1",
                        "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True, check=True)
    img = Image.open(io.BytesIO(r.stdout)).convert("RGB")
rgb = np.asarray(img).copy()
H, W = rgb.shape[:2]

# Modo chroma (fundo verde): CHROMA=1 no ambiente. Transparência pela dominância do verde + remoção do vazamento verde na borda.
import os
if os.environ.get("CHROMA"):
    f = rgb.astype(np.float32)
    chave = f[:, :, 1] - np.maximum(f[:, :, 0], f[:, :, 2])
    a = 1 - np.clip((chave - 35) / 70, 0, 1)
    a = cv2.GaussianBlur(a, (3, 3), 0)
    g_lim = np.maximum(f[:, :, 0], f[:, :, 2])
    f[:, :, 1] = np.where(f[:, :, 1] > g_lim, g_lim, f[:, :, 1])  # despill
    rgb = f.clip(0, 255).astype(np.uint8)
    alfa_chroma = (a * 255).astype(np.uint8)
    for nome_cx in sys.argv[4:]:
        n, v = nome_cx.split("=")
        x0, y0, x1, y1 = map(int, v.split(","))
        sub = alfa_chroma[y0:y1, x0:x1].copy()
        # pedaços de figuras vizinhas que entraram na caixa: componente que toca a borda da caixa e não é a figura
        # principal (a maior) sai. Peças soltas internas (balão de fala, linhas de movimento) ficam.
        nc, lab, st, _ = cv2.connectedComponentsWithStats((sub > 40).astype(np.uint8), connectivity=8)
        if nc > 2:
            princ = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
            hh, ww = sub.shape
            for c in range(1, nc):
                x, y, w_, h_ = st[c, :4]
                borda = x == 0 or y == 0 or x + w_ >= ww or y + h_ >= hh
                if c != princ and (borda or st[c, cv2.CC_STAT_AREA] < 60):
                    sub[cv2.dilate((lab == c).astype(np.uint8), np.ones((5, 5), np.uint8)) > 0] = 0
        ys, xs = np.where(sub > 8)
        cx0, cx1, cy0, cy1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
        rgba = np.dstack([rgb[y0:y1, x0:x1], sub])[cy0:cy1, cx0:cx1]
        Image.fromarray(rgba, "RGBA").save(saida / f"{n}.png")
        print(n, {"w": int(cx1 - cx0), "h": int(cy1 - cy0)})
    sys.exit(0)

# fundo = quase branco conectado à borda
quase_branco = (rgb.min(axis=2) >= 236).astype(np.uint8)
fundo = np.zeros((H + 2, W + 2), np.uint8)
semente = quase_branco.copy()
for (x, y) in [(0, 0), (W - 1, 0), (0, H - 1), (W - 1, H - 1)] + [(x, 0) for x in range(0, W, 40)] + [(x, H - 1) for x in range(0, W, 40)] \
        + [(0, y) for y in range(0, H, 40)] + [(W - 1, y) for y in range(0, H, 40)]:
    if semente[y, x] and not fundo[y + 1, x + 1]:
        cv2.floodFill(semente, fundo, (x, y), 2, flags=4 | (255 << 8) | cv2.FLOODFILL_MASK_ONLY)
eh_fundo = fundo[1:-1, 1:-1] > 0
alfa = np.where(eh_fundo, 0, 255).astype(np.uint8)
# borda suave: encolhe 1 px e desfoca levemente (tira o halo branco)
alfa = cv2.erode(alfa, np.ones((3, 3), np.uint8), iterations=1)
alfa = cv2.GaussianBlur(alfa, (3, 3), 0)

def salvar(nome, a_full, x0=0, y0=0, x1=None, y1=None):
    x1 = x1 or W; y1 = y1 or H
    a = a_full[y0:y1, x0:x1]
    ys, xs = np.where(a > 8)
    if len(xs) == 0:
        print(nome, "vazio"); return
    cx0, cx1, cy0, cy1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    rgba = np.dstack([rgb[y0:y1, x0:x1], a])[cy0:cy1, cx0:cx1]
    Image.fromarray(rgba, "RGBA").save(saida / f"{nome}.png")
    pos = {"x": int(x0 + cx0), "y": int(y0 + cy0), "w": int(cx1 - cx0), "h": int(cy1 - cy0)}
    (saida / f"{nome}.json").write_text(json.dumps(pos), encoding="utf-8")
    print(nome, pos)


# Modo sementes: nome=x,y;x,y — separa figuras que se tocam (watershed a partir de um ou mais pontos por figura)
if caixas == {} and any(";" in a or a.count(",") == 1 for a in sys.argv[4:]):
    pass
sementes = {}
for a in sys.argv[4:]:
    n, v = a.split("=")
    pts = [tuple(map(int, p.split(","))) for p in v.split(";")]
    if all(len(p) == 2 for p in pts):
        sementes[n] = pts
if sementes:
    marc = np.zeros((H, W), np.int32)
    marc[alfa < 10] = 1  # fundo
    nomes = list(sementes)
    for k, n in enumerate(nomes):
        for (x, y) in sementes[n]:
            cv2.circle(marc, (x, y), 9, k + 2, -1)
    cv2.watershed(cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR), marc)
    for k, n in enumerate(nomes):
        reg = (marc == k + 2).astype(np.uint8)
        reg = cv2.dilate(reg, np.ones((3, 3), np.uint8))  # recupera a linha de fronteira do watershed
        salvar(n, (alfa * reg).astype(np.uint8))
    sys.exit(0)

tracos = np.clip((248 - rgb.min(axis=2).astype(int)) * 5, 0, 255).astype(np.uint8)
for nome, (x0, y0, x1, y1) in caixas.items():
    if nome.endswith("*"):
        salvar(nome[:-1], tracos, x0, y0, x1, y1); continue
    a = alfa[y0:y1, x0:x1]
    ys, xs = np.where(a > 8)
    if len(xs) == 0:
        print(nome, "vazio"); continue
    cx0, cx1, cy0, cy1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    rgba = np.dstack([rgb[y0:y1, x0:x1], a])[cy0:cy1, cx0:cx1]
    Image.fromarray(rgba, "RGBA").save(saida / f"{nome}.png")
    pos = {"x": int(x0 + cx0), "y": int(y0 + cy0), "w": int(cx1 - cx0), "h": int(cy1 - cy0)}
    (saida / f"{nome}.json").write_text(json.dumps(pos), encoding="utf-8")
    print(nome, pos)

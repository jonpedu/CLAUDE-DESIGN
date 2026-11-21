"""Recorta os clipes do Flow (fundo branco) em sequências PNG com transparência, recortadas na caixa do personagem.
Fundo = branco conectado às bordas; a sombra de contato vira semitransparente. Uso: py recorta_clipes.py"""
import subprocess, json, sys
from pathlib import Path
import numpy as np, cv2
from PIL import Image
AQUI = Path(__file__).parent; EL = AQUI.parents[2] / 'elementos'
CLIPES = {'idosa': 'Elderly_woman_holding_glowing_sm…_3a553e1c_1080p.mp4',
          'agricultor': 'Man_holding_smartphone_and_smiling_1a88ab62_1080p.mp4',
          'estudante': 'Woman_looking_at_smartphone_be74538f_1080p.mp4'}
W, H, FPS = 1920, 1080, 30
info = {}
for nome, arq in CLIPES.items():
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(EL / arq), '-vf', f'fps={FPS}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                         capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
    alfas = []
    for f in fr:
        w = f.min(axis=2).astype(np.int16); sat = f.max(axis=2).astype(np.int16) - w
        mx = f.max(axis=2).astype(np.int16)
        # fundo: branco neutro OU o creme do brilho do celular (muito claro, levemente amarelado)
        claro = (((w >= 214) & (sat < 22)) | ((w >= 200) & (mx >= 240) & (sat < 42))).astype(np.uint8)
        k = np.ones((3, 3), np.uint8)
        er = cv2.erode(claro, k, iterations=2)                       # fecha frestas finas do contorno (evita furos na roupa)
        n, lab = cv2.connectedComponents(er, connectivity=4)
        borda = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
        fundo_b = np.isin(lab, list(borda))
        # brancos fechados (entre braço, mão e rosto): manchas grandes e bem brancas que não tocam a borda também são fundo
        n2, lab2, st, _ = cv2.connectedComponentsWithStats(claro, connectivity=4)
        borda2 = set(np.unique(np.concatenate([lab2[0], lab2[-1], lab2[:, 0], lab2[:, -1]])))
        for j in range(1, n2):
            if st[j, cv2.CC_STAT_AREA] >= 1800 and j not in borda2:
                m = lab2 == j
                if w[m].mean() >= 243: fundo_b |= m
        fundo = (cv2.dilate(fundo_b.astype(np.uint8), k, iterations=3) > 0) & (claro > 0)
        a = np.ones((H, W), np.float32)
        # ruído quase branco e o brilho claro da luz do celular = transparente; sombra mais escura = parcial
        a[fundo] = np.clip((232 - w[fundo]) / 36.0, 0, 1) ** 1.3
        a = cv2.GaussianBlur(a, (3, 3), 0)
        alfas.append(a)
    al = np.stack(alfas)
    ys, xs = np.where(al.max(axis=0) > 0.35)
    x0, x1, y0, y1 = max(0, xs.min() - 12), min(W, xs.max() + 12), max(0, ys.min() - 12), min(H, ys.max() + 12)
    pasta = AQUI / 'clipes' / nome; pasta.mkdir(parents=True, exist_ok=True)
    for i, (f, a) in enumerate(zip(fr, al)):
        c = f[y0:y1, x0:x1].astype(np.float32); aa = a[y0:y1, x0:x1][..., None]
        fg = np.where(aa > 0.02, (c - (1 - aa) * 255) / np.maximum(aa, 0.02), c)     # tira o branco misturado na borda
        rgba = np.concatenate([np.clip(fg, 0, 255), aa * 255], axis=2).astype(np.uint8)
        Image.fromarray(rgba, 'RGBA').save(pasta / f'{i:03d}.png', optimize=False, compress_level=3)
    info[nome] = {'n': len(fr), 'caixa': [int(x0), int(y0), int(x1), int(y1)], 'w': int(x1 - x0), 'h': int(y1 - y0)}
    print(nome, info[nome])
(AQUI / 'clipes' / 'clipes.json').write_text(json.dumps(info, indent=1), encoding='utf-8')

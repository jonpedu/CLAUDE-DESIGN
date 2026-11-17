"""Margem fantasma: detecta em quais bordas o conteúdo de um clipe encosta (personagem ou objeto cortado pelo quadro).
O clipe deve ser colado nessas mesmas bordas do vídeo final; a base pode ficar escondida sob a régua.
Uso: py ferramentas/bordas.py <clipe.mp4> [<clipe2.mp4> ...]
Saída: para cada borda, os trechos de tempo (s) em que há conteúdo encostado.
"""
import subprocess, sys
import numpy as np

W, H, FAIXA, LIMIAR = 270, 480, 3, 0.04  # análise em 1/4 da resolução; faixa de 3 px; >4% da borda com conteúdo


def bordas(clipe, passo=0.25):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", clipe, "-vf", f"fps={1 / passo},scale={W}:{H}",
                          "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True, check=True).stdout
    q = np.frombuffer(raw, np.uint8).reshape(-1, H, W) < 225  # não branco
    lados = {"esquerda": q[:, :, :FAIXA], "direita": q[:, :, -FAIXA:], "topo": q[:, :FAIXA, :], "base": q[:, -FAIXA:, :]}
    res = {}
    for nome, b in lados.items():
        toca = b.reshape(len(q), -1).mean(axis=1) > LIMIAR
        trechos, ini = [], None
        for i, v in enumerate(list(toca) + [False]):
            if v and ini is None: ini = i
            if not v and ini is not None:
                trechos.append((round(ini * passo, 2), round(i * passo, 2))); ini = None
        res[nome] = trechos
    return res


for c in sys.argv[1:]:
    r = bordas(c)
    tocadas = {k: v for k, v in r.items() if v}
    print(c.split("/")[-1].split("\\")[-1][:48], "->", tocadas if tocadas else "nenhuma borda")

"""Camadas finais a partir dos PNGs transparentes do Canva (paginas em png/extra/ext (N).png, 1620x2880).
Recorta a região inteira de cada componente (componentes.py → _ext/eN_cMM.json), para o cartão levar o conteúdo junto."""
import os, json, numpy as np
from PIL import Image
X = os.path.join("paginas em png", "extra"); C = os.path.join("renderizando", "_claude", "camadas")
MAPA = {  # nome final: (ext N, componente)
    "n_medidor": (2, 5), "n_afericao": (2, 6), "n_coracao_medidor": (4, 8), "n_mudo": (4, 9),
    "n_coracao": (6, 3), "n_rins": (7, 10), "n_hormonal": (7, 16),
    "n_ic1": (8, 1), "n_ic2": (8, 2), "n_ic3": (8, 3),
    "n_cartao_med": (10, 4), "n_sirene": (10, 9), "n_prancheta": (10, 10),
    "n_frutas": (13, 13), "n_verduras": (13, 14), "n_protege": (13, 15),
    "n_medico": (14, 10), "n_chef": (15, 10),
}
REGIAO = {"n_cartao_med"}  # cartão: a região inteira, com ícone e texto de dentro
cache = {}
for nome, (n, c) in MAPA.items():
    if n not in cache:
        cache[n] = Image.open(os.path.join(X, f"ext ({n}).png")).convert("RGBA")
    if nome not in REGIAO:  # só a figura (sem textos vizinhos que caem na mesma caixa)
        Image.open(os.path.join(C, "_ext", f"e{n}_c{c:02d}.png")).save(os.path.join(C, nome + ".png")); print(nome, "figura"); continue
    p = json.load(open(os.path.join(C, "_ext", f"e{n}_c{c:02d}.json"), encoding="utf-8"))
    sub = cache[n].crop((p["x"], p["y"], p["x"] + p["w"], p["y"] + p["h"]))
    sub.save(os.path.join(C, nome + ".png")); print(nome, sub.size)

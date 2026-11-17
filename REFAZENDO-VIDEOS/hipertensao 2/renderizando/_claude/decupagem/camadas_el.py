"""Camadas dos 'elementos canva N.png' (1920x1080, transparentes, enviados pelo usuário em 15/11/2026).
Cada nome junta um ou mais componentes (componentes.py → camadas/_el/kN_cMM.json) e recorta a região do arquivo original."""
import os, json
from PIL import Image
X = os.path.join("paginas em png", "extra"); C = os.path.join("renderizando", "_claude", "camadas")
ARQ = {"k2": "elementos canva 2.png", "k52": "elementos canva 5 (2).png", "k5": "elementos canva 5.png", "k6": "elementos canva 6.png", "k4": "elementos canva 4.png"}
MAPA = {
    "f_verduras": ("k52", [1]), "f_seta_baixo": ("k52", [2]), "f_seta_cima": ("k52", [3]), "f_medidor": ("k52", [4]),
    "f_escudo": ("k52", [5]), "f_frutas": ("k52", [6]), "f_sal": ("k52", [7]), "f_gondola": ("k52", [8]),
    "f_exercicio": ("k52", [9]), "f_coracao": ("k52", [10]),
    "e_ic1": ("k6", [1, 2]), "e_ic2": ("k6", [3]), "e_ic3": ("k6", [4]), "e_par": ("k6", [5, 6]),
    "e_sirene": ("k6", list(range(7, 18))), "e_prancheta": ("k6", [18, 19]), "e_medico": ("k6", [20]),
    "a_casal": ("k2", [1, 2]), "a_gota": ("k2", [3]), "a_afericao": ("k2", [4]), "a_raio1": ("k2", [5]), "a_raio2": ("k2", [9]),
    "a_coracao": ("k2", [6, 7]), "a_silencio": ("k2", [10]),
    "s_cabeca": ("k5", [1, 4]), "s_cansaco": ("k5", [2]), "s_visao": ("k5", [11]), "s_tontura": ("k5", [17]), "g_chef": ("k5", [3]),
    "h_pose1": ("k4", [1]), "h_pose2": ("k4", [2]), "h_pose3": ("k4", [3]),
}
for nome, (k, cs) in MAPA.items():
    if len(cs) == 1:  # só a figura (a região pegaria pedaços de vizinhos)
        Image.open(os.path.join(C, "_el", f"{k}_c{cs[0]:02d}.png")).save(os.path.join(C, nome + ".png")); print(nome, "figura"); continue
    bs = [json.load(open(os.path.join(C, "_el", f"{k}_c{c:02d}.json"), encoding="utf-8")) for c in cs]
    x0 = min(b["x"] for b in bs); y0 = min(b["y"] for b in bs)
    x1 = max(b["x"] + b["w"] for b in bs); y1 = max(b["y"] + b["h"] for b in bs)
    im = Image.open(os.path.join(X, ARQ[k])).convert("RGBA").crop((x0, y0, x1, y1))
    im.save(os.path.join(C, nome + ".png")); print(nome, im.size)

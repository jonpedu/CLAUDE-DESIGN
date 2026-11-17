"""Monta a imagem antes/depois de cada quadro salvo pelo editor de quadros (editor.mjs).
Uso: py ferramentas/editor_comparar.py <ajustes.json>
Antes: caixas laranja onde os elementos estavam. Depois: caixas verdes onde ficaram + anotações em vermelho.
"""
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

arq = Path(sys.argv[1])
D = json.loads(arq.read_text(encoding="utf-8"))
pasta = arq.parent
FONTE = Path(__file__).resolve().parent.parent / "fontes tipograficas" / "Poppins" / "Poppins-Bold.ttf"
fonte = lambda n: ImageFont.truetype(str(FONTE), n) if FONTE.exists() else ImageFont.load_default()
LAR, VER, VERM = (247, 144, 9), (18, 183, 106), (240, 68, 56)


def numero(d, x, y, n, cor):
    d.ellipse([x - 26, y - 26, x + 26, y + 26], fill=cor)
    d.text((x, y), str(n), font=fonte(30), fill="white", anchor="mm")


for q in D["quadros"]:
    t = q["t"]
    antes = Image.open(pasta / q["antes"]).convert("RGB")
    depois = Image.open(pasta / q["depois"]).convert("RGB")
    da, dd = ImageDraw.Draw(antes), ImageDraw.Draw(depois)
    for a in D["ajustes"]:
        for qc in a.get("quadros_chave", [a]):
            if abs(qc["t"] - t) > 0.011:
                continue
            for d, cx, cor in ((da, qc["caixa_antes"], LAR), (dd, qc["caixa_depois"], VER)):
                if cx:
                    d.rectangle([cx["x"], cx["y"], cx["x"] + cx["w"], cx["y"] + cx["h"]], outline=cor, width=6)
                    numero(d, cx["x"], cx["y"], a["n"], cor)
    for a in D["anotacoes"]:
        if abs(a["t"] - t) > 0.011:
            continue
        x1, y1, x2, y2 = a["de"]["x"], a["de"]["y"], a["ate"]["x"], a["ate"]["y"]
        if a["tipo"] == "seta":
            dd.line([x1, y1, x2, y2], fill=VERM, width=10)
            ang = math.atan2(y2 - y1, x2 - x1)
            pts = [(x2, y2)] + [(x2 - 40 * math.cos(ang + s), y2 - 40 * math.sin(ang + s)) for s in (-0.45, 0.45)]
            dd.polygon(pts, fill=VERM)
        elif a["tipo"] == "circulo":
            dd.ellipse([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)], outline=VERM, width=10)
        numero(dd, x1, y1, a["n"], VERM)

    w, h = antes.size
    topo, gap = 110, 40
    tela = Image.new("RGB", (w * 2 + gap, h + topo), (244, 246, 250))
    tela.paste(antes, (0, topo))
    tela.paste(depois, (w + gap, topo))
    d = ImageDraw.Draw(tela)
    d.text((24, 30), f"ANTES  ·  {t:.2f} s", font=fonte(48), fill=(16, 24, 40))
    d.text((w + gap + 24, 30), f"DEPOIS  ·  {t:.2f} s", font=fonte(48), fill=(16, 24, 40))
    tela.save(pasta / q["comparacao"])
    print("ok", q["comparacao"])

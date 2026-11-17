"""Mede a cor real de cada quadrado das paletas em 'cores hex/' (os rótulos de algumas estão errados).
Uso: py analise-referencias/scripts/amostrar_paleta.py
"""
from pathlib import Path
from PIL import Image
import numpy as np

RAIZ = Path(__file__).resolve().parents[2]
ESCALA = 1440 / 1105  # coordenadas medidas na imagem exibida a 1105 px
# (nome, x, y) no centro de cada quadrado, coordenadas da imagem exibida
PONTOS = [
    ("Primary", 225, 390), ("Primary Hover", 388, 390), ("Primary Pressed", 551, 390), ("Primary Subtle", 714, 390),
    ("Secondary", 225, 575), ("Secondary Hover", 388, 575), ("Secondary Pressed", 551, 575), ("Secondary Subtle", 714, 575),
    ("Text Primary", 225, 890), ("Text Secondary", 388, 890), ("Text Inverse", 551, 890), ("Text Link", 714, 890),
    ("Surface Page", 225, 1208), ("Surface Default", 388, 1208), ("Surface Subtle", 551, 1208), ("Surface Inverse", 714, 1208),
    ("Surface Brand", 225, 1392), ("Surface Brand Strong", 388, 1392),
    ("Border Default", 225, 1710), ("Border Strong", 388, 1710),
    ("Success", 225, 2025), ("Success Subtle", 388, 2025),
    ("Warning", 225, 2210), ("Warning Subtle", 388, 2210),
    ("Error", 225, 2395), ("Error Subtle", 388, 2395),
]

for nome_arq, modo in [("Frame 1000003513.png", "claro"), ("Frame 1000003513-1.png", "escuro")]:
    a = np.asarray(Image.open(RAIZ / "cores hex" / nome_arq).convert("RGB")).astype(int)
    print(f"== {modo} ({nome_arq})")
    for nome, x, y in PONTOS:
        X, Y = int(x * ESCALA), int(y * ESCALA)
        bloco = a[Y - 6:Y + 6, X - 6:X + 6].reshape(-1, 3)
        r, g, b = np.median(bloco, axis=0).astype(int)
        print(f"  {nome:22s} #{r:02X}{g:02X}{b:02X}")

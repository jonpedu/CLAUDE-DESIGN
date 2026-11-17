"""Medições em tamanho real: régua de marca, máscara de área segura e áudio por trecho.
Uso: py analise-referencias/scripts/medir.py
Saídas: analise-referencias/dados/medidas.json, analise-referencias/area-segura/*.jpg
"""
import json, re, subprocess, io
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

RAIZ = Path(__file__).resolve().parents[2]
BASE = RAIZ / "analise-referencias"
MASC = BASE / "area-segura"
MASC.mkdir(exist_ok=True)
cortes = json.loads((BASE / "dados" / "cortes.json").read_text(encoding="utf-8"))

# Área segura do projeto (CLAUDE.md / manual seção 9)
SX0, SX1, SY0, SY1 = 65, 888, 288, 1248

# Quadros para conferir a área segura: (id, segundo)
AMOSTRAS = [
    ("teleorientacao-hipertensao-hipertensao", 2), ("teleorientacao-hipertensao-hipertensao", 16),
    ("teleorientacao-hipertensao-hipertensao", 42), ("teleorientacao-pet-saude-dengue-parte-2-dengue-parte-2", 40),
    ("teleorientacao-pet-saude-diabetes-parte-1-diabetes-parte-1", 28),
    ("teleorientacao-hanseniase-parte-2-video-hanseniese-parte-2-logo-ses", 38),
    ("teleorientacao-cancer-de-penis-parte-2-cancer-de-penis-pt-2", 10),
    ("teleorientacao-pet-saude-obesidade-infantil-2-obesidade-infantil-parte-2", 42),
    ("dia-nacional-de-combate-ao-glaucoma-dia-nacional-de-combate-ao-glaucoma", 22),
    ("kits-de-telessaude-novo-pac-kits-novo-pac", 46),
]


def quadro(arquivo, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", str(RAIZ / arquivo), "-frames:v", "1",
                        "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
    return Image.open(io.BytesIO(r.stdout)).convert("RGB")


def regua(img):
    """Mede a faixa da régua: linhas de baixo para cima até achar uma faixa branca alta acima dela."""
    a = np.asarray(img).astype(int)
    h = a.shape[0]
    tinta = (255 - a.min(axis=2)) > 40          # pixel não branco
    linhas = tinta.sum(axis=1)
    # sobe a partir do fundo enquanto houver conteúdo ou pequenos espaços (até 12 px)
    y, vazio, topo = h - 1, 0, h - 1
    while y > h * 0.75:
        if linhas[y] > 3:
            topo, vazio = y, 0
        else:
            vazio += 1
            if vazio > 12 and topo < h - 1:
                break
        y -= 1
    cols = np.where(tinta[topo:].any(axis=0))[0]
    return {"topo_y": int(topo), "altura_px": int(h - topo),
            "x0": int(cols.min()) if len(cols) else None, "x1": int(cols.max()) if len(cols) else None}


def mascara(img, out):
    im = img.copy()
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    W, H = im.size
    for box in [(0, 0, W, SY0), (0, SY1, W, H), (0, SY0, SX0, SY1), (SX1, SY0, W, SY1)]:
        d.rectangle(box, fill=(255, 0, 60, 90))
    d.rectangle((SX0, SY0, SX1, SY1), outline=(255, 0, 60, 255), width=4)
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    im.resize((540, 960)).save(out, quality=88)


def audio(arquivo, dur):
    """Loudness da abertura (0-3 s), do miolo e dos 6 s finais; pausas acima de 0,8 s."""
    def lufs(ss, t):
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-ss", str(ss), "-t", str(t), "-i", str(RAIZ / arquivo),
                            "-vn", "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True, errors="replace")
        m = re.search(r"I:\s+(-?[\d.]+) LUFS", r.stderr.split("Summary:")[-1])
        return float(m.group(1)) if m else None
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(RAIZ / arquivo), "-vn",
                        "-af", "silencedetect=n=-45dB:d=0.8", "-f", "null", "-"], capture_output=True, text=True, errors="replace")
    ini = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", r.stderr)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    return {"lufs_0_3s": lufs(0, 3), "lufs_meio": lufs(dur * 0.3, dur * 0.4), "lufs_6s_finais": lufs(max(0, dur - 6), 6),
            "silencios_45db": [[round(a, 1), round(b, 1)] for a, b in zip(ini, fim)]}


def main():
    med = {}
    for vid, c in cortes.items():
        dur = c["duracao_s"]
        fim = quadro(c["arquivo"], max(0, dur - 0.5))
        med[vid] = {"regua_no_fim": regua(fim), "audio": audio(c["arquivo"], dur)}
        print(vid, med[vid]["regua_no_fim"], flush=True)
    for vid, t in AMOSTRAS:
        mascara(quadro(cortes[vid]["arquivo"], t), MASC / f"{vid}_{t:03d}s.jpg")
    (BASE / "dados" / "medidas.json").write_text(json.dumps(med, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

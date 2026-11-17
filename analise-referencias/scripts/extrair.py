"""Extrai cortes (detecção de cena), amostras a cada 2 s, folhas de contato e paleta dominante.
Uso: py analise-referencias/scripts/extrair.py
Saídas em analise-referencias/: dados/cortes.json, dados/paletas.json, folhas/*.jpg, quadros/<id>/*.jpg
"""
import json, re, subprocess, unicodedata
from pathlib import Path
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parents[2]
REF = RAIZ / "videos-referencia"
BASE = RAIZ / "analise-referencias"
DADOS, FOLHAS, QUADROS = BASE / "dados", BASE / "folhas", BASE / "quadros"
for d in (DADOS, FOLHAS, QUADROS):
    d.mkdir(parents=True, exist_ok=True)

PASSO = 2.0          # segundos entre amostras
LIMIAR = 0.30        # sensibilidade da detecção de corte
COLS, LINHAS = 8, 4  # 32 amostras por folha = 64 s
TW, TH = 216, 384


def ident(p):
    rel = p.relative_to(REF).with_suffix("")
    s = "_".join(rel.parts)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def extrair(p, vid):
    pasta = QUADROS / vid
    pasta.mkdir(exist_ok=True)
    for f in pasta.glob("*.jpg"):
        f.unlink()
    fc = (f"[0:v]scale={TW}:{TH},split=2[s][f];"
          f"[s]select='gt(scene\\,{LIMIAR})',showinfo[so];[f]fps=1/{PASSO}[fo]")
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-filter_complex", fc,
                        "-map", "[so]", "-f", "null", "-",
                        "-map", "[fo]", "-q:v", "3", str(pasta / "%04d.jpg")],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    cortes = [round(float(t), 2) for t in re.findall(r"pts_time:([\d.]+)", r.stderr)]
    return cortes, sorted(pasta.glob("*.jpg"))


def folhas(vid, quadros):
    try:
        fonte = ImageFont.truetype("arial.ttf", 18)
    except OSError:
        fonte = ImageFont.load_default()
    por = COLS * LINHAS
    saidas = []
    for i in range(0, len(quadros), por):
        lote = quadros[i:i + por]
        img = Image.new("RGB", (COLS * TW, LINHAS * (TH + 24)), (20, 20, 20))
        dr = ImageDraw.Draw(img)
        for j, q in enumerate(lote):
            x, y = (j % COLS) * TW, (j // COLS) * (TH + 24)
            img.paste(Image.open(q), (x, y + 24))
            t = (i + j) * PASSO
            dr.text((x + 4, y + 2), f"{int(t // 60)}:{t % 60:04.1f}", fill=(255, 220, 0), font=fonte)
        out = FOLHAS / f"{vid}_{i // por + 1}.jpg"
        img.save(out, quality=85)
        saidas.append(out.name)
    return saidas


def paleta(quadros, k=8):
    px = []
    for q in quadros:
        # OpenCV não lê caminhos com acento no Windows; Pillow lê.
        a = np.asarray(Image.open(q).convert("RGB").resize((54, 96), Image.BOX))
        px.append(a.reshape(-1, 3))
    px = np.concatenate(px).astype(np.float32)
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.5)
    _, rot, cent = cv2.kmeans(px, k, None, crit, 3, cv2.KMEANS_PP_CENTERS)
    cont = np.bincount(rot.ravel(), minlength=k) / len(rot)
    ordem = np.argsort(-cont)
    return [{"hex": "#%02X%02X%02X" % tuple(int(c) for c in cent[o]), "pct": round(float(cont[o]) * 100, 1)} for o in ordem]


def main():
    cortes_all, pal_all = {}, {}
    for p in sorted(REF.rglob("*.mp4")):
        vid = ident(p)
        cortes, quadros = extrair(p, vid)
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                   capture_output=True, text=True).stdout)
        planos = np.diff([0.0] + cortes + [dur])
        cortes_all[vid] = {"arquivo": str(p.relative_to(RAIZ)), "duracao_s": round(dur, 2), "cortes": cortes,
                           "n_planos": len(planos), "plano_medio_s": round(float(planos.mean()), 2),
                           "plano_mediano_s": round(float(np.median(planos)), 2),
                           "folhas": folhas(vid, quadros)}
        pal_all[vid] = paleta(quadros)
        print(vid, len(cortes), "cortes", cortes_all[vid]["plano_medio_s"], "s/plano", flush=True)
    (DADOS / "cortes.json").write_text(json.dumps(cortes_all, ensure_ascii=False, indent=2), encoding="utf-8")
    (DADOS / "paletas.json").write_text(json.dumps(pal_all, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

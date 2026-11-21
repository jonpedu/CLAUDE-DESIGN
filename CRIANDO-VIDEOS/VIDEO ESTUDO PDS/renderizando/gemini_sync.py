"""Usa a narração do Gemini (audios/gemini/a1..a7.wav) no lugar da voz do edge-tts.
Alinha cada fala do roteiro às palavras transcritas (renderizando/_transc/aN/palavras.json), recorta fala por fala,
aplica as pausas do roteiro e reescreve timeline.js + audios/narracao.wav (mesmo formato do tts.py)."""
import json, subprocess, sys, difflib, unicodedata, re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).parent
RAIZ = AQUI.parent
CFG = json.loads((RAIZ / "roteiro" / "narracao.json").read_text(encoding="utf-8"))
FALAS = {f["id"]: f for f in CFG["falas"]}
ARQS = {
    "a1": ["b0", "b1"],
    "a2": ["b2", "b3", "b4", "b5", "b6"],
    "a3": ["b7", "b8", "b9", "b10", "b11", "b12"],
    "a4": ["b13", "b14", "b15", "b16", "b17"],
    "a5": ["b18", "b19", "b20", "b21", "b22", "b23", "b24"],
    "a6": ["b25", "b26", "b27", "b28", "b29", "b30", "p0", "q1", "r1", "q2", "r2"],
    "a7": ["q3", "r3", "q4", "r4", "q5", "r5", "q6", "r6", "q7", "r7", "b31"],
}
INICIO = 0.8
NUM = {"0,8": "zero virgula oito", "0,64": "zero virgula sessenta e quatro", "0,512": "zero virgula quinhentos e doze",
       "1,2": "um virgula dois", "1,44": "um virgula quarenta e quatro", "1,728": "um virgula setecentos e vinte e oito",
       "1": "um", "2": "dois", "3": "tres", "4": "quatro"}


def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn")
    return re.sub(r"[^\w,]", "", w).strip(",")


def expande(w):
    n = norm(w)
    return NUM.get(n, n).split() if n else []


def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True)
    return float(r.stdout)


tmp = RAIZ / "audios" / "gemini" / "_cortes"
tmp.mkdir(exist_ok=True)
linha, lista, t = {}, [], INICIO
sil = tmp / "_ini.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", str(INICIO),
                "-c:a", "pcm_s16le", str(sil)], check=True)
lista.append(sil)

for arq, ids in ARQS.items():
    pw = json.loads((AQUI / "_transc" / arq / "palavras.json").read_text(encoding="utf-8"))
    if arq == "a2":  # o modelo small errou os 7 s iniciais; usa a transcrição do medium nesse trecho
        ini = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if len(sys.argv) > 1 else []
        corte = max(w["fim"] for w in ini) if ini else 0
        pw = ini + [w for w in pw if w["ini"] >= corte]
    # sequência transcrita (tokens expandidos) com tempo
    tx = [(tok, w["ini"], w["fim"]) for w in pw for tok in expande(w["p"])]
    # sequência do roteiro: (fala, índice da palavra original, token)
    rt = []
    for fid in ids:
        for k, w in enumerate(FALAS[fid]["texto"].split()):
            for tok in expande(w):
                rt.append((fid, k, tok))
    sm = difflib.SequenceMatcher(None, [r[2] for r in rt], [x[0] for x in tx], autojunk=False)
    t_ini, t_fim = [None] * len(rt), [None] * len(rt)
    for a, b, n in sm.get_matching_blocks():
        for j in range(n):
            t_ini[a + j], t_fim[a + j] = tx[b + j][1], tx[b + j][2]
    # interpola os não casados
    known = [i for i, v in enumerate(t_ini) if v is not None]
    for i in range(len(rt)):
        if t_ini[i] is None:
            prev = max([k for k in known if k < i], default=None)
            nxt = min([k for k in known if k > i], default=None)
            if prev is None: t_ini[i] = t_fim[i] = t_ini[nxt]
            elif nxt is None: t_ini[i] = t_fim[i] = t_fim[prev]
            else:
                fr = (i - prev) / (nxt - prev)
                t_ini[i] = t_fim[i] = t_fim[prev] + fr * (t_ini[nxt] - t_fim[prev])
    total_arq = dur(RAIZ / "audios" / "gemini" / f"{arq}.wav")
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(RAIZ / "audios" / "gemini" / f"{arq}.wav"), "-af",
                        "silencedetect=n=-42dB:d=0.12", "-f", "null", "-"], capture_output=True, text=True).stderr
    ss = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]
    se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
    sils = list(zip(ss, se + [total_arq] * (len(ss) - len(se))))
    for m, fid in enumerate(ids):
        idx = [i for i, r in enumerate(rt) if r[0] == fid]
        a0 = t_ini[idx[0]]
        b0 = t_fim[idx[-1]]
        # limites: meio do silêncio até a fala vizinha
        prox = [i for i, r in enumerate(rt) if m + 1 < len(ids) and r[0] == ids[m + 1]]
        ant = [i for i, r in enumerate(rt) if m > 0 and r[0] == ids[m - 1]]
        def fronteira(fim_a, ini_b):
            """Maior silêncio real entre duas falas: (onde a 1ª termina, onde a 2ª começa)."""
            cand = [(a, b) for a, b in sils if b > fim_a - 0.6 and a < ini_b + 0.6 and b - a >= 0.12]
            if not cand: mid = (fim_a + ini_b) / 2; return mid, mid
            a, b = max(cand, key=lambda s: s[1] - s[0])
            return a, b
        if ant:
            sa, sb = fronteira(t_fim[ant[-1]], a0); c0 = max(sa, sb - 0.08); a0 = sb
        else:
            c0 = 0.0 if a0 < 0.6 else a0 - 0.15
        if prox:
            sa, sb = fronteira(b0, t_ini[prox[0]]); c1 = min(sb, sa + 0.12); b0 = sa
        else:
            c1 = total_arq; b0 = max(b0, max([a for a, b in sils if a < total_arq - 0.05], default=b0))
        p = FALAS[fid].get("pausa", 0.4)
        w = tmp / f"{fid}.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(RAIZ / "audios" / "gemini" / f"{arq}.wav"),
                        "-af", f"atrim={c0:.3f}:{c1:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,areverse,afade=t=in:d=0.04,areverse,apad=pad_dur={p}",
                        "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(w)], check=True)
        # palavras (do roteiro) com tempo na linha final
        pal, vistos = [], set()
        for i in idx:
            k = rt[i][1]
            if k in vistos: continue
            vistos.add(k)
            pal.append([FALAS[fid]["texto"].split()[k], round(t + (t_ini[i] - c0), 3)])
        linha[fid] = {"ini": round(t + (a0 - c0), 3), "fim": round(t + (b0 - c0), 3), "cena": FALAS[fid]["cena"], "pal": pal}
        lista.append(w)
        t += dur(w)

total = round(t, 2)
lt = tmp / "_lista.txt"
lt.write_text(chr(10).join(f"file '{p.as_posix()}'" for p in lista), encoding="utf-8")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lt),
                "-c:a", "pcm_s16le", str(RAIZ / "audios" / "narracao.wav")], check=True)
(AQUI / "timeline.js").write_text("window.B = " + json.dumps(linha, ensure_ascii=False) +
                                  f";\nwindow.DURACAO = {total};\n", encoding="utf-8")
for fid in ["b2", "b13", "q2", "r2", "b31"]:
    print(fid, linha[fid]["ini"], linha[fid]["fim"], linha[fid]["pal"][:6])
print(f"ok: {len(linha)} falas, {total:.1f} s")

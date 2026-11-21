"""Gera a narração fala por fala (edge-tts), junta com as pausas e escreve a linha do tempo para a página.
Uso: py tts.py   (lê ../roteiro/narracao.json; saídas em ../audios/ e ./timeline.js)
Só refaz o mp3 de uma fala se o texto mudou."""
import asyncio, json, subprocess, sys, hashlib
from pathlib import Path
import edge_tts

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).parent
RAIZ = AQUI.parent
CFG = json.loads((RAIZ / "roteiro" / "narracao.json").read_text(encoding="utf-8"))
AUD = RAIZ / "audios" / "falas"
AUD.mkdir(parents=True, exist_ok=True)
INICIO = 0.8


async def gera(f):
    h = hashlib.sha1((CFG["voz"] + CFG["taxa"] + f["texto"]).encode()).hexdigest()[:10]
    mp3, js = AUD / f"{f['id']}_{h}.mp3", AUD / f"{f['id']}_{h}.json"
    if mp3.exists() and js.exists():
        return mp3, json.loads(js.read_text(encoding="utf-8"))
    com = edge_tts.Communicate(f["texto"], CFG["voz"], rate=CFG["taxa"], boundary="WordBoundary")
    pal = []
    with open(mp3, "wb") as out:
        async for c in com.stream():
            if c["type"] == "audio":
                out.write(c["data"])
            elif c["type"] == "WordBoundary":
                pal.append([c["text"], c["offset"] / 1e7, (c["offset"] + c["duration"]) / 1e7])
    js.write_text(json.dumps(pal, ensure_ascii=False), encoding="utf-8")
    return mp3, pal


def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


async def main():
    res = []
    for f in CFG["falas"]:
        res.append(await gera(f))
    t, linha, lista = INICIO, {}, []
    tmp = AUD / "_wav"; tmp.mkdir(exist_ok=True)
    sil = tmp / "_ini.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", str(INICIO),
                    "-c:a", "pcm_s16le", str(sil)], check=True)
    lista.append(sil)
    for f, (mp3, pal) in zip(CFG["falas"], res):
        w = tmp / (mp3.stem + f"_{f.get('pausa', 0.4)}.wav")
        if not w.exists():
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mp3), "-af", f"apad=pad_dur={f.get('pausa', 0.4)}",
                            "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(w)], check=True)
        d = dur(mp3)
        linha[f["id"]] = {"ini": round(t, 3), "fim": round(t + d, 3), "cena": f["cena"],
                          "pal": [[w_, round(t + a_, 3)] for w_, a_, b_ in pal]}
        lista.append(w)
        t = t + dur(w)
    total = round(t, 2)
    n = len(res)
    lt = tmp / "_lista.txt"
    lt.write_text(chr(10).join(f"file '{p.as_posix()}'" for p in lista), encoding="utf-8")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lt),
                    "-c:a", "pcm_s16le", str(RAIZ / "audios" / "narracao.wav")], check=True)
    (AQUI / "timeline.js").write_text("window.B = " + json.dumps(linha, ensure_ascii=False) +
                                      f";\nwindow.DURACAO = {total};\n", encoding="utf-8")
    print(f"ok: {n} falas, {total:.1f} s")


asyncio.run(main())

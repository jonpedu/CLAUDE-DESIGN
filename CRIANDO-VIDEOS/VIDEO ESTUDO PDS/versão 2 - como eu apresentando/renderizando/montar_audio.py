"""Junta os 4 áudios da v2 com pausas curtas e escreve timeline.js (palavras do Whisper com tempo absoluto)."""
import json, subprocess, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).parent
AUD = AQUI.parent / "audios"
INICIO, GAP, FIM = 1.0, 0.7, 2.0
cenas = {"s1": "slide6", "s2": "slide6", "s3": "slide7", "s4": "slide7"}
dur = lambda p: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                     capture_output=True, text=True).stdout)
B, t, partes = {}, INICIO, []
tmp = AQUI / "_wav"; tmp.mkdir(exist_ok=True)
for i in range(1, 5):
    src = AUD / f"v2-a{i}.wav"
    pw = json.loads((AQUI / "_transc" / f"a{i}" / "palavras.json").read_text(encoding="utf-8"))
    d = dur(src)
    B[f"s{i}"] = {"ini": round(t + pw[0]["ini"], 3), "fim": round(t + pw[-1]["fim"], 3), "cena": cenas[f"s{i}"],
                  "pal": [[w["p"], round(t + w["ini"], 3)] for w in pw]}
    pre = INICIO if i == 1 else GAP
    w = tmp / f"a{i}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-af", f"adelay={int(pre*1000)}:all=1" + (f",apad=pad_dur={FIM}" if i == 4 else ""),
                    "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(w)], check=True)
    partes.append(w)
    t += d + (GAP if i < 4 else FIM)
lt = tmp / "_lista.txt"
lt.write_text(chr(10).join(f"file '{p.as_posix()}'" for p in partes), encoding="utf-8")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lt), "-c:a", "pcm_s16le",
                str(AQUI / "narracao.wav")], check=True)
total = round(dur(AQUI / "narracao.wav"), 2)
(AQUI / "timeline.js").write_text("window.B = " + json.dumps(B, ensure_ascii=False) + f";\nwindow.DURACAO = {total};\n", encoding="utf-8")
for k, v in B.items():
    print(k, v["ini"], v["fim"], " ".join(f"{w}@{tt:.1f}" for w, tt in v["pal"]))
print("total", total)

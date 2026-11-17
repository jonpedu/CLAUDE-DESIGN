"""Emenda trechos re-renderizados num vídeo-base, por intervalo de tempo (quadro exato), sem refazer o resto.
Uso: py ferramentas/emendar.py <base.mp4> <saida.mp4> <fps> <inicio>:<arquivo> [<inicio>:<arquivo> ...]
Cada trecho substitui o base a partir de <inicio> (s) pela sua própria duração. Partes do base sem trecho ficam como estão.
"""
import json, subprocess, sys

base, saida, fps = sys.argv[1], sys.argv[2], float(sys.argv[3])
trechos = sorted((float(a.split(":", 1)[0]), a.split(":", 1)[1]) for a in sys.argv[4:])


def quadros(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                        "stream=nb_read_frames", "-of", "json", f], capture_output=True, text=True)
    return int(json.loads(r.stdout)["streams"][0]["nb_read_frames"])


nb = quadros(base)
ins, partes, cursor, k = ["-i", base], [], 0, 1
for ini, arq in trechos:
    q0 = round(ini * fps); n = quadros(arq)
    if q0 > cursor:
        partes.append(f"[0:v]trim=start_frame={cursor}:end_frame={q0},setpts=PTS-STARTPTS[p{len(partes)}]")
    ins += ["-i", arq]
    partes.append(f"[{k}:v]trim=start_frame=0:end_frame={n},setpts=PTS-STARTPTS[p{len(partes)}]")
    k += 1; cursor = q0 + n
if cursor < nb:
    partes.append(f"[0:v]trim=start_frame={cursor},setpts=PTS-STARTPTS[p{len(partes)}]")
fc = ";".join(partes) + ";" + "".join(f"[p{i}]" for i in range(len(partes))) + f"concat=n={len(partes)}:v=1:a=0,fps={fps}[v]"
subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fc, "-map", "[v]", "-c:v", "libx264",
                "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart", saida], check=True)
print("ok", saida, quadros(saida), "quadros")

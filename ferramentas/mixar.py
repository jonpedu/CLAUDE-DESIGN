"""Mixa narração + trilha + efeitos e junta ao vídeo, com volume final em -14 LUFS / -1 dBTP.
Uso: py ferramentas/mixar.py <plano.json>
plano.json: {
  "video": "...mp4", "saida": "...mp4", "dur": 35.6,
  "narracao": {"arq": "...wav", "ini": 0, "db": 0},
  "trilha": {"arq": "...mp3", "db": -9, "fade_in": 1, "fade_out": 0.8, "desde": 0, "ducking": {"reducao_db": 5}},
  "fim_audio": {"arq": "...mp4", "em": 83.5, "db": 0},          (opcional: áudio de outro arquivo, ex. fechamento)
  "sfx": [{"arq": "...wav", "em": 4.15, "db": -6}, ...]
}
Caminhos relativos ao próprio plano.json.
"""
import json, subprocess, sys
from pathlib import Path

plano_p = Path(sys.argv[1]); P = json.loads(plano_p.read_text(encoding="utf-8")); B = plano_p.parent
a = lambda p: str((B / p).resolve())
dur = P["dur"]
ins, fil, mix = ["-i", a(P["video"])], [], []
k = 1


def add(arq):
    global k
    ins.extend(["-i", a(arq)]); k += 1
    return k - 1


n = add(P["narracao"]["arq"])
# "ate" na narração: corta ali com fade curto (ex.: o áudio do vídeo-base traz um som de logo antigo no fim)
na = P["narracao"].get("ate")
corte = f"atrim=0:{na},afade=t=out:st={na - 0.2}:d=0.2," if na else ""
fil.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,{corte}adelay={int(P['narracao'].get('ini', 0) * 1000)}:all=1,"
           f"volume={P['narracao'].get('db', 0)}dB,apad=whole_dur={dur},atrim=0:{dur},afade=t=out:st={dur - 0.5}:d=0.5,asplit=2[nar][chave]")
mix.append("[nar]")
duck = None
if "trilha" in P:
    T = P["trilha"]; i = add(T["arq"]); ate = T.get("ate", dur)  # "ate": onde a trilha termina (ex.: antes do fechamento)
    desde = T.get("desde", 0)  # "desde": ponto da música onde começar (pular introdução baixa)
    dmus = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", a(T["arq"])],
                                capture_output=True, text=True).stdout.strip() or 0)
    if dmus and desde + ate > dmus:
        print(f"AVISO: a música tem {dmus:.1f} s; começando em {desde} s ela acaba em {dmus - desde:.1f} s do vídeo (precisa ir até {ate}). "
              f"Use 'desde' <= {max(0, dmus - ate):.1f} e, se a introdução for baixa, 'realce'.")
    # "realce": {"db": 6, "ate": 11, "rampa": 3} sobe a introdução baixa da música e volta ao normal numa rampa
    R = T.get("realce")
    realce = (f"volume='if(lt(t,{R['ate']}),1,if(lt(t,{R['ate'] + R.get('rampa', 3)}),1-(t-{R['ate']})/{R.get('rampa', 3)},0))*{10 ** (R['db'] / 20) - 1}+1':eval=frame,"
              if R else "")
    duck = T.get("ducking")  # {"reducao_db": 8, "ataque_ms": 80, "soltura_ms": 900}: trilha abaixa sob a voz e sobe nas pausas
    fil.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,atrim={desde}:{desde + ate},asetpts=PTS-STARTPTS,{realce}volume={T.get('db', -19)}dB,"
               f"afade=t=in:st=0:d={T.get('fade_in', 1)},afade=t=out:st={ate - T.get('fade_out', 0.8)}:d={T.get('fade_out', 0.8)}"
               f"{'[tri0]' if duck else '[tri]'}")
    if duck:
        # razão alta + limiar baixo: com voz, a trilha cai ~reducao_db; sem voz, volta ao nível base
        red = duck.get("reducao_db", 8)
        fil.append(f"[tri0][chave]sidechaincompress=threshold=0.015:ratio={max(2, red)}:attack={duck.get('ataque_ms', 80)}:"
                   f"release={duck.get('soltura_ms', 900)}:knee=4[tri]")
    mix.append("[tri]")
if not duck:
    fil.append("[chave]anullsink")
if "fim_audio" in P:
    F = P["fim_audio"]; i = add(F["arq"])
    fi = F.get("fade_in", 0)  # entrada suave do som do fechamento (cruza com a saída da trilha)
    fil.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,volume={F.get('db', 0)}dB"
               f"{f',afade=t=in:st=0:d={fi}' if fi else ''},adelay={int(F['em'] * 1000)}:all=1[fim]")
    mix.append("[fim]")
extra = P.get("sfx_db_extra", 0)  # ajuste geral de volume dos efeitos (ex.: -5 deixa todos mais discretos)
for j, s in enumerate(P.get("sfx", [])):
    i = add(s["arq"])
    fil.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,volume={s.get('db', -8) + extra}dB,adelay={int(s['em'] * 1000)}:all=1[s{j}]")
    mix.append(f"[s{j}]")
base = f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:dropout_transition=0,atrim=0:{dur}"

# 1ª passada: mede o loudness da mistura
med = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *ins, "-filter_complex",
                      ";".join(fil + [base + ",loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json[a]"]),
                      "-map", "[a]", "-f", "null", "-"], capture_output=True, text=True, errors="replace").stderr
m = json.loads(med[med.rindex("{"):med.rindex("}") + 1])
# 2ª passada: aplica com os valores medidos (linear), alvo -14 LUFS e pico -1,5 dBTP (margem para o AAC)
ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
      f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
fil.append(f"{base},{ln},aresample=48000[a]")
cmd = ["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fil), "-map", "0:v", "-map", "[a]",
       "-c:v", "copy", "-c:a", "aac", "-b:a", f"{P.get('audio_kbps', 192)}k", "-ar", "48000", "-t", str(dur), "-movflags", "+faststart", a(P["saida"])]
subprocess.run(cmd, check=True)
r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", a(P["saida"]), "-af", "ebur128=peak=true", "-f", "null", "-"],
                   capture_output=True, text=True, errors="replace")
print("ok", P["saida"], [l.strip() for l in r.stderr.split("Summary:")[-1].splitlines() if "I:" in l or "Peak:" in l])

"""Inventário técnico dos vídeos de referência: formato, duração, áudio e loudness.
Uso: py analise-referencias/scripts/inventario.py
Saída: analise-referencias/dados/inventario.json
"""
import json, subprocess, re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
REF = RAIZ / "videos-referencia"
SAIDA = RAIZ / "analise-referencias" / "dados"
SAIDA.mkdir(parents=True, exist_ok=True)


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(p)],
                       capture_output=True, text=True, encoding="utf-8")
    return json.loads(r.stdout)


def loudness(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    txt = r.stderr.split("Summary:")[-1]
    def g(pat):
        m = re.search(pat, txt)
        return float(m.group(1)) if m else None
    return {"lufs_i": g(r"I:\s+(-?[\d.]+) LUFS"), "lra": g(r"LRA:\s+(-?[\d.]+) LU"), "true_peak": g(r"Peak:\s+(-?[\d.]+) dBFS")}


def main():
    itens = []
    for p in sorted(REF.rglob("*.mp4")):
        d = probe(p)
        v = next((s for s in d["streams"] if s["codec_type"] == "video"), {})
        a = next((s for s in d["streams"] if s["codec_type"] == "audio"), {})
        num, den = (v.get("r_frame_rate", "0/1").split("/") + ["1"])[:2]
        item = {
            "arquivo": str(p.relative_to(RAIZ)),
            "duracao_s": round(float(d["format"]["duration"]), 2),
            "tamanho_mb": round(int(d["format"]["size"]) / 1e6, 1),
            "bitrate_mbps": round(int(d["format"].get("bit_rate", 0)) / 1e6, 1),
            "largura": v.get("width"), "altura": v.get("height"),
            "fps": round(int(num) / int(den), 3) if int(den) else None,
            "vcodec": v.get("codec_name"), "perfil": v.get("profile"), "pix_fmt": v.get("pix_fmt"),
            "acodec": a.get("codec_name"), "a_hz": a.get("sample_rate"), "a_canais": a.get("channels"),
            "encoder": d["format"].get("tags", {}).get("encoder"),
        }
        if a:
            item.update(loudness(p))
        itens.append(item)
        print(item["arquivo"], item["largura"], item["altura"], item["fps"], item["duracao_s"], item.get("lufs_i"), flush=True)
    (SAIDA / "inventario.json").write_text(json.dumps(itens, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

"""Transcreve a narração com tempo por palavra (faster-whisper).
Uso: py ferramentas/transcrever.py <audio.wav> <pasta_saida> [arquivo_dica.txt] [modelo]
Saídas: palavras.json (palavra, início, fim) e transcricao.txt (frases com tempo).
A dica (roteiro) só ajuda o reconhecimento; o texto da tela sempre vem do roteiro aprovado.
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np
from faster_whisper import WhisperModel


def carregar(p):
    """Decodifica com ffmpeg para 16 kHz mono float32 (o PyAV 19 é incompatível com o faster-whisper 1.2.1)."""
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                       capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32)

audio, saida = Path(sys.argv[1]), Path(sys.argv[2])
dica = Path(sys.argv[3]).read_text(encoding="utf-8") if len(sys.argv) > 3 and sys.argv[3] else None
modelo = sys.argv[4] if len(sys.argv) > 4 else "small"
saida.mkdir(parents=True, exist_ok=True)

m = WhisperModel(modelo, device="cpu", compute_type="int8")
segs, info = m.transcribe(carregar(audio), language="pt", word_timestamps=True, initial_prompt=dica,
                          vad_filter=False, beam_size=5)
palavras, linhas = [], []
for s in segs:
    linhas.append(f"[{s.start:6.2f} – {s.end:6.2f}] {s.text.strip()}")
    for w in s.words:
        palavras.append({"p": w.word.strip(), "ini": round(w.start, 2), "fim": round(w.end, 2), "conf": round(w.probability, 2)})
(saida / "palavras.json").write_text(json.dumps(palavras, ensure_ascii=False, indent=1), encoding="utf-8")
(saida / "transcricao.txt").write_text("\n".join(linhas), encoding="utf-8")
print("\n".join(linhas))
print(f"\n{len(palavras)} palavras; duração {info.duration:.1f} s")

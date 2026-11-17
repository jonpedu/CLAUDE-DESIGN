"""Gera efeitos sonoros simples e livres de licença (sintetizados), em WAV 48 kHz estéreo.
Uso: py ferramentas/sfx.py <pasta_saida>
     py ferramentas/sfx.py <pasta_saida> --digitar nome="texto"@cps ...  (digitação de um texto da página)
Arquivos: whoosh_subida, whoosh_entrada (zoom para dentro), whoosh_suave, pop, pop_grave, tique.
"""
import sys, wave
from pathlib import Path
import numpy as np

SR = 48000
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(7)


def salva(nome, x, pan=0.0):
    x = x / (np.max(np.abs(x)) + 1e-9) * 0.7
    l, r = x * (1 - max(0, pan)), x * (1 + min(0, pan))
    s = (np.stack([l, r], 1) * 32767).astype(np.int16)
    with wave.open(str(out / f"{nome}.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(s.tobytes())


def env(n, a, d):  # ataque e decaimento em amostras (curva suave)
    e = np.ones(n); A = max(1, int(a * SR)); D = max(1, int(d * SR))
    e[:A] = np.sin(np.linspace(0, np.pi / 2, A)) ** 2
    e[-D:] *= np.cos(np.linspace(0, np.pi / 2, D)) ** 2
    return e


def passa_banda(ruido, f0, f1):
    """Ruído filtrado com centro que varre de f0 a f1 (filtro de 2ª ordem por amostra)."""
    n = len(ruido); y = np.zeros(n); y1 = y2 = 0.0; x1 = x2 = 0.0
    fs = np.geomspace(f0, f1, n); Q = 1.2
    for i in range(n):
        w0 = 2 * np.pi * fs[i] / SR; al = np.sin(w0) / (2 * Q); c = np.cos(w0)
        b0, b2, a0, a1, a2 = al, -al, 1 + al, -2 * c, 1 - al
        x0 = ruido[i]
        y0 = (b0 * x0 + b2 * x2 - a1 * y1 - a2 * y2) / a0
        x2, x1, y2, y1 = x1, x0, y1, y0; y[i] = y0
    return y


def whoosh(dur, f0, f1, a, d):
    n = int(dur * SR)
    return passa_banda(rng.standard_normal(n), f0, f1) * env(n, a, d)


salva("whoosh_subida", whoosh(0.55, 300, 2600, 0.30, 0.20))
salva("whoosh_entrada", whoosh(0.50, 2400, 180, 0.35, 0.12))
salva("whoosh_suave", whoosh(0.70, 400, 1400, 0.35, 0.30) * 0.6)

n = int(0.16 * SR); t = np.arange(n) / SR
f = 900 * np.exp(-t * 18) + 380
salva("pop", np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 28))
n = int(0.28 * SR); t = np.arange(n) / SR
f = 220 * np.exp(-t * 10) + 70
salva("pop_grave", (np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.25 * rng.standard_normal(n) * np.exp(-t * 60)) * np.exp(-t * 14))
n = int(0.05 * SR); t = np.arange(n) / SR
salva("tique", np.sin(2 * np.pi * 2200 * t) * np.exp(-t * 120))

# bolha: sobe de tom, curta e redonda (texto/cartão que aparece)
n = int(0.14 * SR); t = np.arange(n) / SR
f = 420 + 900 * (t / t[-1]) ** 1.5
salva("bolha", np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / t[-1]) ** 1.5)
# blob: grave e macio (elemento maior que entra ou sai)
n = int(0.22 * SR); t = np.arange(n) / SR
f = 160 + 140 * np.exp(-t * 20)
salva("blob", np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 16) * (1 - np.exp(-t * 400)))
# swish curto (marca-texto passando)
salva("swish_marca", whoosh(0.28, 1800, 5200, 0.10, 0.14) * 0.5)


def digitacao(dur, cps=30, seed=3):
    """Cliques de teclado no ritmo das letras, com leve variação de tempo e timbre."""
    r = np.random.default_rng(seed); x = np.zeros(int((dur + 0.06) * SR)); tt = 0.0
    while tt < dur:
        i = int(tt * SR); m = int(0.018 * SR); k = np.arange(m) / SR
        clique = (r.standard_normal(m) * 0.5 + np.sin(2 * np.pi * r.uniform(2600, 3600) * k)) * np.exp(-k * 380)
        x[i:i + m] += clique * r.uniform(0.6, 1.0)
        tt += (1 / cps) * r.uniform(0.75, 1.3)
    return x


salva("digitacao_curta", digitacao(0.65))
salva("digitacao_longa", digitacao(0.85, seed=5))

def tecla(r, espaco=False):
    """Uma tecla: clique agudo curto + corpo grave ("thock") + ressonância média. Espaço: mais grave e cheio."""
    m = int(0.07 * SR); k = np.arange(m) / SR
    ruido = r.standard_normal(m)
    clique = np.diff(np.concatenate([[0], ruido])) * np.exp(-k * (700 if not espaco else 500)) * 0.35
    f_corpo = r.uniform(170, 240) if not espaco else r.uniform(105, 135)
    corpo = np.sin(2 * np.pi * f_corpo * k) * np.exp(-k * (55 if not espaco else 38)) * (0.55 if not espaco else 0.8)
    f_med = r.uniform(950, 1450)
    med = np.sin(2 * np.pi * f_med * k) * np.exp(-k * 140) * 0.18
    x = (clique + corpo + med) * (1 - np.exp(-k * 3000))
    return x * r.uniform(0.75, 1.0)


def digitar_texto(texto, cps, seed=11):
    """Digitação sincronizada com o efeito de máquina de escrever (TS.digita): tecla i em i/cps s."""
    r = np.random.default_rng(seed); dur = len(texto) / cps + 0.12
    L = np.zeros(int(dur * SR)); R = np.zeros_like(L)
    for i, c in enumerate(texto):
        t0 = i / cps + r.uniform(-0.006, 0.006)
        s = tecla(r, espaco=(c == " ")); a = max(0, int(t0 * SR)); b = min(len(L), a + len(s))
        p = r.uniform(-0.25, 0.25)                      # cada tecla num ponto levemente diferente do estéreo
        L[a:b] += s[:b - a] * (1 - p); R[a:b] += s[:b - a] * (1 + p)
    x = np.stack([L, R], 1)
    x = np.convolve(x[:, 0], np.ones(3) / 3, "same"), np.convolve(x[:, 1], np.ones(3) / 3, "same")  # suaviza agudos
    x = np.stack(x, 1); x = x / (np.abs(x).max() + 1e-9) * 0.6
    return (x * 32767).astype(np.int16)


def salva_estereo(nome, s16):
    with wave.open(str(out / f"{nome}.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(s16.tobytes())


# Modo digitação: py ferramentas/sfx.py <pasta> --digitar nome="texto"@cps [...]  (gera só esses e sai).
# Use o mesmo texto e a mesma velocidade (cps) do TS.digita da página, para cada tecla cair na letra certa.
if "--digitar" in sys.argv:
    for arg in sys.argv[sys.argv.index("--digitar") + 1:]:
        nome, resto = arg.split("=", 1); txt, cps = resto.rsplit("@", 1)
        salva_estereo(nome, digitar_texto(txt.strip('"'), float(cps), seed=len(txt)))
        print("ok:", nome)
    sys.exit(0)

# textos digitados do IAM (o mesmo texto e a mesma velocidade da animação)
for nome, txt, cps in [("dig_iam_fonte1", "segundo a Sociedade", 30), ("dig_iam_fonte2", "Brasileira de Cardiologia", 30),
                       ("dig_iam_sinais1", "os sinais nem sempre são", 28), ("dig_iam_sinais2", "iguais para todo mundo", 28)]:
    salva_estereo(nome, digitar_texto(txt, cps, seed=len(txt)))

# swish do marca-texto: três variações para não repetir o mesmo som
for k, (f0, f1) in enumerate([(1800, 5200), (1500, 4600), (2100, 5800)], start=1):
    salva(f"swish_marca_{k}", whoosh(0.28, f0, f1, 0.10, 0.14) * 0.5)

# variações para eventos repetidos em sequência (evita o mesmo som várias vezes): sobem de tom como uma escala
for k, base in enumerate([520, 620, 740, 880], start=1):
    n = int(0.15 * SR); t = np.arange(n) / SR
    f = base * 1.6 * np.exp(-t * 20) + base * 0.55
    salva(f"pop_{k}", np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30) * (1 - np.exp(-t * 900)))
for k, fr in enumerate([1800, 2200, 2600], start=1):
    n = int(0.05 * SR); t = np.arange(n) / SR
    salva(f"tique_{k}", (np.sin(2 * np.pi * fr * t) + 0.3 * np.sin(2 * np.pi * fr * 1.5 * t)) * np.exp(-t * 110))
print("ok:", sorted(p.name for p in out.glob("*.wav")))

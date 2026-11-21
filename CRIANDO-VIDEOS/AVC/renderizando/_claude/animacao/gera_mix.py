"""Gera mix_v1.json (tempos dos efeitos a partir de N(), igual à página completo.html)."""
import json
N = lambda o: o + (2.5 if o < 10.7 else 3.0 if o < 13.3 else 3.8 if o < 22.35 else 4.3 if o < 37.0 else 4.9 if o < 44.1 else 5.4)
TI2, Z0, TL4, LIFT, P6 = N(2.95), N(7.60) - 0.3, N(10.45), N(13.0) + 0.95, N(21.9) + 0.25
W7, P8, S8, U9, R9, F10 = N(28.4), N(36.5) + 0.2, N(40.6), N(44.0), N(48.7), N(52.75)
I11 = F10 + 3.85; DUR = round(I11 + 4.6, 2)
S = "../../../../../biblioteca/sfx/sintetizados/"
ev = [  # (som, tempo, dB)
 ("bolha", 0.08, -16), ("dig_avc_pergunta", 0.2, -14), ("pop_grave", 0.85, -10), ("whoosh_suave", 2.3, -13),
 ("dig_avc_cidente", N(0.36), -15), ("dig_avc_ascular", N(0.76), -15), ("dig_avc_erebral", N(1.34), -15), ("bolha", N(2.38), -17),
 ("whoosh_entrada", TI2, -10), ("blob", N(4.02), -18), ("pop_grave", N(6.30), -11),
 ("whoosh_entrada", Z0, -9), ("pop_1", N(7.60) + 0.15, -15), ("whoosh_suave", N(8.54) - 0.1, -13), ("pop_grave", N(9.06), -10), ("blob", N(9.06) + 0.05, -15),
 ("whoosh_subida", TL4, -10), ("pop_2", TL4 + 0.35, -15), ("bolha", N(10.96), -16), ("dig_avc_surgir", N(11.52), -15), ("pop_grave", N(12.58), -9),
 ("whoosh_subida", LIFT, -11), ("pop_1", N(13.52), -15), ("pop_2", N(14.66), -15), ("pop_3", N(16.58), -15), ("swish_marca_1", N(18.54), -16), ("pop_4", N(19.60), -15),
 ("whoosh_entrada", P6, -10), ("pop_grave", N(24.72), -9), ("swish_marca_2", N(27.22) + 0.3, -16),
 ("whoosh_suave", W7, -11), ("tique_1", W7 + 0.1, -17), ("tique_2", W7 + 0.3, -17), ("tique_3", W7 + 0.5, -17),
 ("bolha", N(31.96), -17), ("swish_marca_3", N(31.96) + 0.35, -16), ("pop_grave", N(33.02) + 0.15, -11),
 ("pop_3", N(34.52), -15), ("pop_4", N(35.64), -15),
 ("whoosh_suave", P8, -11), ("swish_marca_1", N(39.82), -16),
 ("pop_grave", S8, -8), ("whoosh_entrada", S8, -11), ("pop_2", N(41.38), -15),
 ("pop_1", N(42.48), -14), ("pop_2", N(42.48) + 0.2, -14), ("pop_3", N(42.48) + 0.4, -14),
 ("whoosh_subida", U9, -10), ("tique_1", N(46.16) + 0.15, -16), ("tique_2", N(47.86) + 0.15, -16),
 ("whoosh_subida", R9, -11), ("tique_1", R9 + 0.55, -17), ("tique_2", R9 + 0.7, -17), ("pop_3", N(48.88) + 0.3, -15), ("tique_3", N(50.68) + 0.3, -16),
 ("whoosh_subida", F10, -10), ("pop_grave", F10 + 0.6, -10), ("swish_marca_3", F10 + 1.95, -16), ("whoosh_suave", I11, -12),
]
# tique a cada hora que o ponteiro passa no relógio (setor 0 → 135°, inOut cúbico entre N(34.30) e N(36.10))
io = lambda x: 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
a, b = N(34.30), N(36.10)
for alvo in (30, 60, 90, 120):
    k = next(i / 1000 for i in range(1001) if 135 * io(i / 1000) >= alvo)
    ev.append((["tique_1", "tique_2", "tique_3", "tique_2"][alvo // 30 - 1], a + k * (b - a), -16))
plano = {
 "video": "completo_v1_video.mp4", "saida": "../../AVC v1.mp4", "dur": DUR,
 "narracao": {"arq": "narracao_editada.wav", "ini": 0, "db": 0},
 "trilha": {"arq": "../../../trilha sonora/Balanced Learning Loop (Remix) v2.mp3", "db": -12, "fade_in": 1.0, "fade_out": 1.6,
            "ate": round(I11 + 1.2, 2), "ducking": {"reducao_db": 6, "ataque_ms": 80, "soltura_ms": 900}},
 "sfx_db_extra": -5,
 "fim_audio": {"arq": "../../../elementos/Intro NTS e PETSAUDE.mp4", "em": round(I11, 2), "db": -2, "fade_in": 0.6},
 "sfx": [{"arq": S + n + ".wav", "em": round(t, 2), "db": d} for n, t, d in sorted(ev, key=lambda e: e[1])],
}
open("mix_v1.json", "w", encoding="utf-8").write(json.dumps(plano, ensure_ascii=False, indent=1))
print("dur", DUR, "eventos", len(ev))

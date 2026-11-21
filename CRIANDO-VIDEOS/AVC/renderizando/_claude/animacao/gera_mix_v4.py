"""Gera mix_v4.json (versão final). Tempos a partir de N(), iguais aos de completo_v4.html.
Devolutiva da v3: efeitos demais em sequência curta (cena do 192). Regra aplicada: um som por gesto que importa;
no máximo um efeito por ~0,7 s; whoosh só nas transições; nada de som para movimento secundário (cartão que se reorganiza,
ícone que voa, celular que cresce)."""
import json
N = lambda o: o + (-0.2 if o < 3.0 else 0.4 if o < 10.7 else 0.9 if o < 13.3 else 1.7 if o < 22.35 else 2.2 if o < 37.0 else 2.8 if o < 44.1 else 3.3)
TI2, Z0, TL4, LIFT, P6, W7 = N(2.95) + 0.3, N(7.60) - 0.3, N(10.45), N(13.0) + 0.95, N(22.4), N(28.4)
P8, S8, U9, R9, F10 = N(36.5) + 0.2, N(40.6), N(44.0), N(48.45), N(52.56) + 0.6
FA, I11 = F10 + 0.55, F10 + 4.5; DUR = round(I11 + 4.6, 2)
tp = N(33.02); td = [N(42.48), N(42.48) + 0.2, N(42.48) + 0.4]; tExp = 0.45
S = "../../../../../biblioteca/sfx/sintetizados/"
ev = [
 # C1 gancho
 ("pop_grave", 0.04, -12), ("dig_avc2_pergunta", 0.0, -15), ("whoosh_suave", tExp, -15),
 ("dig_avc2_cidente", tExp + 0.18, -16), ("dig_avc2_ascular", max(N(0.76), tExp + 0.33), -16), ("dig_avc2_erebral", N(1.34), -16),
 # C2, C3
 ("whoosh_entrada", TI2, -11), ("pop_grave", N(6.30), -12), ("whoosh_suave", Z0, -12),
 ("pop_1", Z0 + 0.75, -17), ("pop_grave", N(9.06), -11),
 # C4
 ("whoosh_subida", TL4, -11), ("dig_avc_surgir", N(11.52), -16), ("pop_grave", N(12.58), -10),
 # C5: um pop por cartão novo; reorganização sem som
 ("whoosh_subida", LIFT, -12), ("pop_1", N(13.52), -16), ("pop_2", N(14.66), -16), ("pop_3", N(16.58), -16), ("pop_4", N(19.60), -16),
 ("swish_marca_1", N(18.54) + 0.25, -17),
 # C6
 ("whoosh_entrada", P6, -11), ("pop_grave", N(24.72), -10), ("swish_marca_2", N(27.22) + 0.3, -17),
 # C7: varredura, cérebro, marca, ampulheta (aparece + voa), tiques do relógio
 ("whoosh_suave", W7, -12), ("bolha", N(29.78), -17), ("swish_marca_3", N(31.96) + 0.35, -17),
 ("pop_2", tp - 0.2, -16), ("whoosh_subida", tp + 0.55, -14),
 # C8a
 ("whoosh_suave", P8, -12), ("swish_marca_1", N(39.82), -17),
 # C8b (192): soco da entrada, SAMU, ambulância uma vez, três teclas
 ("pop_grave", S8, -9), ("pop_2", N(41.38), -17), ("whoosh_entrada", N(40.84) + 0.55, -16),
 ("tique_1", td[0], -15), ("tique_2", td[1], -15), ("tique_3", td[2], -15),
 # C9a, C9b
 ("whoosh_subida", U9, -11), ("tique_1", N(46.16) + 0.15, -17), ("tique_2", N(47.86) + 0.15, -17),
 ("whoosh_suave", R9, -12), ("pop_1", R9 + 0.85, -16), ("pop_3", N(48.88), -16), ("pop_4", N(50.68), -16),
 # C10, C11
 ("whoosh_subida", F10, -11), ("pop_grave", F10 + 0.45, -11), ("swish_marca_3", FA + 1.84, -17), ("whoosh_suave", I11, -13),
]
io = lambda x: 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
a, b = N(34.30), N(36.10)
for alvo in (30, 60, 90, 120):   # tique a cada hora que o ponteiro passa (é o próprio tempo correndo)
    k = next(i / 1000 for i in range(1001) if 135 * io(i / 1000) >= alvo)
    ev.append((["tique_1", "tique_2", "tique_3", "tique_2"][alvo // 30 - 1], a + k * (b - a), -18))
plano = {
 "video": "completo_v4_video.mp4", "saida": "../../AVC v4.mp4", "dur": DUR, "audio_kbps": 320,
 "narracao": {"arq": "narracao_v4.wav", "ini": 0, "db": 0},
 "trilha": {"arq": "../../../trilha sonora/Balanced Learning Loop (Remix) v2.mp3", "db": -11, "desde": 12.0, "fade_in": 1.0, "fade_out": 1.6,
            "ate": round(I11 + 1.2, 2), "ducking": {"reducao_db": 5, "ataque_ms": 80, "soltura_ms": 900}},
 "sfx_db_extra": -5,
 "fim_audio": {"arq": "../../../elementos/Intro NTS e PETSAUDE.mp4", "em": round(I11, 2), "db": -2, "fade_in": 0.6},
 "sfx": [{"arq": S + n + ".wav", "em": round(max(0, t), 2), "db": d} for n, t, d in sorted(ev, key=lambda e: e[1])],
}
open("mix_v4.json", "w", encoding="utf-8").write(json.dumps(plano, ensure_ascii=False, indent=1))
ts = sorted(t for _, t, _ in ev); perto = sum(1 for x, y in zip(ts, ts[1:]) if y - x < 0.3)
print("dur", DUR, "eventos", len(ev), "(v3: 85) | pares a menos de 0,3 s:", perto)

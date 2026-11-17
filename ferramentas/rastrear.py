"""Rastreia pontos do corpo num clipe estimando o movimento do quadro (escala + translação + rotação)
em relação a um quadro de referência (ORB + RANSAC). Robusto em ilustração lisa, onde fluxo de pixel escorrega.
Uso: py ferramentas/rastrear.py <clipe.mp4> <t_ref> <saida.json> nome=x,y [nome=x,y ...]
Coordenadas em pixels do clipe (1080x1920) no instante t_ref. Saída: posição de cada ponto em cada quadro do clipe.
"""
import json, subprocess, sys
import numpy as np
import cv2

clipe, t_ref, saida = sys.argv[1], float(sys.argv[2]), sys.argv[3]
pontos = {a.split("=")[0]: tuple(map(float, a.split("=")[1].split(","))) for a in sys.argv[4:]}
W, H, ESC = 540, 960, 2.0  # analisa em meia resolução

info = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                  "stream=r_frame_rate", "-of", "json", clipe], capture_output=True, text=True).stdout)
num, den = map(int, info["streams"][0]["r_frame_rate"].split("/"))
fps = num / den
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", clipe, "-vf", f"scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                     capture_output=True, check=True).stdout
quadros = np.frombuffer(raw, np.uint8).reshape(-1, H, W)
i_ref = min(int(round(t_ref * fps)), len(quadros) - 1)

orb = cv2.ORB_create(3000)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
kr, dr = orb.detectAndCompute(quadros[i_ref], None)
ref_pts = np.array([[x / ESC, y / ESC] for x, y in pontos.values()], np.float32)

res = {n: [] for n in pontos}
ok_list = []
M_prev = np.array([[1, 0, 0], [0, 1, 0]], np.float32)
for i, q in enumerate(quadros):
    k, d = orb.detectAndCompute(q, None)
    M = None
    if d is not None and dr is not None:
        m = sorted(bf.match(dr, d), key=lambda x: x.distance)[:600]
        if len(m) >= 12:
            a = np.float32([kr[x.queryIdx].pt for x in m])
            b = np.float32([k[x.trainIdx].pt for x in m])
            M, inl = cv2.estimateAffinePartial2D(a, b, method=cv2.RANSAC, ransacReprojThreshold=3.0)
            if inl is None or inl.sum() < 10:
                M = None
    ok_list.append(M is not None)
    if M is None:
        M = M_prev
    M_prev = M
    p = cv2.transform(ref_pts[None], M)[0] * ESC
    for (n, _), (x, y) in zip(pontos.items(), p):
        res[n].append([round(float(x), 1), round(float(y), 1)])

json.dump({"fps": fps, "t_ref": t_ref, "quadros": len(quadros), "pontos": res}, open(saida, "w", encoding="utf-8"))
print(f"{len(quadros)} quadros a {fps:.2f} fps; estimativas boas: {sum(ok_list)}/{len(ok_list)}")
for n in pontos:
    print(n, "início", res[n][0], "ref", res[n][i_ref], "fim", res[n][-1])

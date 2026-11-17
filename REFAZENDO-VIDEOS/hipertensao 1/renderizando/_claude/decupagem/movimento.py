"""Energia de movimento por quadro e inícios de animação (entradas de elementos)."""
import subprocess, sys, json, numpy as np
v = sys.argv[1]; W, H = 192, 108
r = subprocess.run(["ffmpeg", "-v", "error", "-i", v, "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"], capture_output=True, check=True)
f = np.frombuffer(r.stdout, np.uint8).reshape(-1, H, W).astype(np.float32)
d = np.abs(np.diff(f, axis=0)).mean(axis=(1, 2))
sm = np.convolve(d, np.ones(3) / 3, "same")
ons = []; quiet = 0
for i, x in enumerate(sm):
    if x < 0.25: quiet += 1
    elif x > 0.6 and quiet >= 6:
        ons.append(round((i + 1) / 30, 2)); quiet = 0
    elif x >= 0.25: quiet = 0
print(len(ons)); print(" ".join(map(str, ons)))
json.dump({"d": [round(float(x), 3) for x in d]}, open(sys.argv[2], "w"))

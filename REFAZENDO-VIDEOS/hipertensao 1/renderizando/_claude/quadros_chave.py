import subprocess, sys
from PIL import Image, ImageDraw
V = "video horizontal canva/Hipertensão PET SAUDE - horinzontal.mp4"; I = "Intro NTS e PETSAUDE - horizontal.mp4"
reg = Image.open("renderizando/_claude/camadas/regua_ilha.png")
def frame(p, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", p, "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
    return Image.frombytes("RGB", (1920, 1080), r.stdout).convert("RGBA")
ts = [("V", float(x)) for x in sys.argv[1].split(",")] + [("I", float(x)) for x in sys.argv[2].split(",")]
for k, (src, t) in enumerate(ts):
    im = frame(V if src == "V" else I, t); im.alpha_composite(reg)
    lim = im.copy(); d = ImageDraw.Draw(lim)
    for x in range(96, 1824, 24): d.line([(x, 96), (x + 12, 96)], fill=(255, 0, 160), width=3); d.line([(x, 984), (x + 12, 984)], fill=(255, 0, 160), width=3)
    for y in range(96, 984, 24): d.line([(96, y), (96, y + 12)], fill=(255, 0, 160), width=3); d.line([(1824, y), (1824, y + 12)], fill=(255, 0, 160), width=3)
    nome = f"{k+1:02d}_{'fech' if src == 'I' else ''}{t + (97.5 if src == 'I' else 0):06.2f}s"
    lim.convert("RGB").save(f"renderizando/_claude/quadros-chave/{nome}.png")
    print(nome)

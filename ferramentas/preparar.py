"""Confere se esta máquina está pronta para continuar os vídeos (usado pelo comando /preparar).

Uso: py ferramentas/preparar.py            (relatório completo)
     py ferramentas/preparar.py --curto    (só o que falta)

Não instala nem altera nada: só lê e imprime o que falta, com o comando para resolver.
Partes:
  1. Programas: ffmpeg/ffprobe (com libx264 e loudnorm), Python e pacotes, Node, playwright-core, Chrome.
  2. Pastas do repositório e material grande que vem do Drive (LINKS-DRIVE.md).
  3. Cada vídeo com renderizando/_claude/00-estado.md: próximo passo e arquivos que as páginas
     (.html) e mixagens (.json) citadas no estado usam e que não estão no disco. O vídeo de entrada
     de uma mixagem ("video") não é cobrado: é gerado pelo render (ferramentas/animar.mjs).
"""
import importlib.util, io, json, os, re, shutil, subprocess, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
RAIZ = Path(__file__).resolve().parents[1]
CURTO = '--curto' in sys.argv
problemas = []


def ok(msg):
    if not CURTO:
        print(f'  [ok]    {msg}')


def falta(msg, como=''):
    problemas.append(msg)
    print(f'  [FALTA] {msg}' + (f'\n          → {como}' if como else ''))


def roda(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
        return r.returncode, r.stdout + r.stderr
    except Exception as e:  # programa ausente
        return -1, str(e)


# ---------------------------------------------------------------- 1. programas
print('\n1. Programas')
if shutil.which('ffmpeg') and shutil.which('ffprobe'):
    _, saida = roda(['ffmpeg', '-hide_banner', '-version'])
    _, filtros = roda(['ffmpeg', '-hide_banner', '-filters'])
    _, cods = roda(['ffmpeg', '-hide_banner', '-encoders'])
    if 'libx264' in cods and 'loudnorm' in filtros and 'sidechaincompress' in filtros:
        ok(saida.splitlines()[0][:70])
    else:
        falta('ffmpeg sem libx264/loudnorm (build reduzido)', 'winget install Gyan.FFmpeg  (build completo)')
else:
    falta('ffmpeg/ffprobe não encontrados no PATH', 'winget install Gyan.FFmpeg  e abra um terminal novo')

ok(f'Python {sys.version.split()[0]} ({sys.executable})')
if sys.version_info < (3, 10):
    falta('Python 3.10 ou mais novo', 'winget install Python.Python.3.12')
for mod, pacote in [('PIL', 'Pillow'), ('numpy', 'numpy'), ('cv2', 'opencv-python'), ('faster_whisper', 'faster-whisper')]:
    if importlib.util.find_spec(mod):
        ok(f'pacote {pacote}')
    else:
        falta(f'pacote Python {pacote}', 'py -m pip install -r requirements.txt')

if shutil.which('node'):
    _, v = roda(['node', '-v'])
    ok(f'Node {v.strip()}')
    if not (RAIZ / 'ferramentas' / 'node_modules' / 'playwright-core').exists():
        falta('playwright-core não instalado em ferramentas/', 'cd ferramentas; npm install')
    else:
        ok('playwright-core em ferramentas/node_modules')
else:
    falta('Node não encontrado', 'winget install OpenJS.NodeJS.LTS  e abra um terminal novo')

chrome = [Path(os.environ.get(v, '')) / 'Google/Chrome/Application/chrome.exe'
          for v in ('PROGRAMFILES', 'PROGRAMFILES(X86)', 'LOCALAPPDATA')]
if any(c.exists() for c in chrome) or shutil.which('chrome') or shutil.which('google-chrome'):
    ok('Google Chrome (o Playwright usa channel: "chrome")')
else:
    falta('Google Chrome não encontrado', 'winget install Google.Chrome')

# ---------------------------------------------------------------- 2. pastas
print('\n2. Pastas e material grande')
for pasta, origem in [
    ('biblioteca/marca/fontes', 'Git'), ('biblioteca/marca/cores', 'Git'), ('biblioteca/sfx/sintetizados', 'Git'),
    ('.claude/skills/telessaude', 'Git'),
]:
    (ok if (RAIZ / pasta).exists() else lambda m: falta(m, 'a pasta veio incompleta: baixe de novo do Drive (LINKS-DRIVE.md)'))(f'{pasta} ({origem})')

trilhas = list((RAIZ / 'biblioteca/trilhas').rglob('*.mp3')) + list((RAIZ / 'biblioteca/trilhas').rglob('*.wav'))
if trilhas:
    ok(f'biblioteca/trilhas: {len(trilhas)} faixas')
else:
    falta('biblioteca/trilhas sem áudio', 'baixe de novo a pasta biblioteca/ do Drive (LINKS-DRIVE.md)')
for pasta in ['biblioteca/videos-publicados']:
    if any((RAIZ / pasta).rglob('*.mp4')) if (RAIZ / pasta).exists() else False:
        ok(pasta)
    else:
        falta(f'{pasta} vazia (só precisa para analisar referências ou reconstruir em 16:9)', 'ver LINKS-DRIVE.md')

# ---------------------------------------------------------------- 3. vídeos
print('\n3. Vídeos (renderizando/_claude/00-estado.md)')
REF = re.compile(r'''(?:src|href)\s*=\s*["']([^"'#?]+)["']|url\(\s*["']?([^"')]+)["']?\s*\)|"(?:arq|arquivo|regua|fim_video|fim_audio)"\s*:\s*"([^"]+)"''')
CIT = re.compile(r'`([^`]+\.(?:html|json))`')
MIDIA = ('.wav', '.mp3', '.m4a', '.mp4', '.mov', '.webm', '.png', '.jpg', '.jpeg', '.webp', '.svg', '.js', '.css')


def refs_faltando(arq):
    """Arquivos relativos citados numa página ou mixagem que não existem no disco."""
    txt = arq.read_text(encoding='utf-8', errors='replace')
    faltam = []
    for m in REF.finditer(txt):
        r = next(g for g in m.groups() if g)
        if re.match(r'^(https?:|data:|file:|blob:|about:)', r) or not r.lower().endswith(MIDIA):
            continue
        if '${' in r:  # caminho montado no script: confere só a pasta fixa
            r = r.split('${')[0].rsplit('/', 1)[0] + '/'
        p = (arq.parent / r)
        if not p.exists():
            faltam.append(r)
    return sorted(set(faltam))


estados = sorted(p for p in RAIZ.rglob('renderizando/_claude/00-estado.md') if '_arquivo' not in p.parts)
for est in estados:
    video = est.parents[2]
    nome = video.relative_to(RAIZ).as_posix()
    txt = est.read_text(encoding='utf-8', errors='replace')
    passo = re.search(r'\*\*Próximo passo[^*]*\*\*:?\s*(.*)', txt)
    passo = passo.group(1).strip() if passo else '(sem linha "Próximo passo")'
    print(f'\n  ▸ {nome}\n    próximo passo: {passo[:220]}')
    cl = est.parent
    citados = []
    for c in CIT.findall(txt):
        for base in (cl, cl / 'animacao', cl / 'render', video):
            p = base / c
            if p.exists() and p.suffix in ('.html', '.json') and p not in citados:
                citados.append(p)
                break
    faltas = {}
    for p in citados:
        f = refs_faltando(p)
        if f:
            faltas[p.relative_to(cl).as_posix()] = f
    if faltas:
        n = sum(len(v) for v in faltas.values())
        falta(f'{nome}: {n} arquivo(s) de mídia citados pelas páginas/mixagens do estado não estão no disco',
              'baixe de novo a pasta do vídeo do Drive (LINKS-DRIVE.md); se o item é da biblioteca, copie com ferramentas/da_biblioteca.py')
        for pg, lst in faltas.items():
            print(f'          {pg}: ' + ', '.join(lst[:6]) + (' …' if len(lst) > 6 else ''))
    elif citados:
        ok(f'mídia das páginas/mixagens citadas no estado presente ({len(citados)} arquivo(s))')

# ---------------------------------------------------------------- resumo
print('\n' + ('Tudo pronto.' if not problemas else f'{len(problemas)} pendência(s). Resolva as de "Programas" antes de editar; '
                                                     'as de vídeo só importam para o vídeo que for continuar.'))

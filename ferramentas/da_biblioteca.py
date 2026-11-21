"""Biblioteca geral (biblioteca/): procurar itens e copiar para a pasta de um vídeo.

A biblioteca é a fonte de onde todos os vídeos bebem. Um vídeo nunca usa o arquivo direto de lá
(exceto efeitos sonoros e fontes, lidos pelo motor): copia para a pasta dele. A biblioteca nunca
é alterada por esta ferramenta.

Uso:
  py ferramentas/da_biblioteca.py --listar [termo]          lista os itens (filtra pelo termo, sem acento/maiúscula)
  py ferramentas/da_biblioteca.py --inventario              regrava biblioteca/INVENTARIO.md
  py ferramentas/da_biblioteca.py "<item ou termo>" "<pasta do vídeo>" [--para elementos|"trilha sonora"]
      Copia o item (arquivo ou pasta) para a pasta do vídeo. Destino padrão: trilhas → "trilha sonora/",
      o resto → "elementos/". Não substitui arquivo que já existe. Se o termo achar mais de um item, lista e para.

Exemplos:
  py ferramentas/da_biblioteca.py "Intro Telessaude.mp4" "CRIANDO-VIDEOS/SERVIÇOS NTS/TELECONSULTORIA"
  py ferramentas/da_biblioteca.py "regua - tele-sted" "CRIANDO-VIDEOS/DENGUE"
  py ferramentas/da_biblioteca.py "elementos/mapas/brazil.svg" "CRIANDO-VIDEOS/DENGUE"
"""
import shutil, sys, unicodedata
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
RAIZ = Path(__file__).resolve().parents[1]
BIB = RAIZ / 'biblioteca'
IGNORAR = {'README.md', 'INVENTARIO.md', 'desktop.ini', 'Thumbs.db'}


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    return ''.join(c for c in s if not unicodedata.combining(c))


def itens():
    return sorted(p for p in BIB.rglob('*') if p.is_file() and p.name not in IGNORAR)


def tam(n):
    for u in ('B', 'KB', 'MB', 'GB'):
        if n < 1024:
            return f'{n:.0f} {u}'
        n /= 1024
    return f'{n:.1f} TB'


def procurar(termo):
    t = norm(termo.replace('\\', '/'))
    exato = BIB / termo
    if exato.exists():
        return [exato]
    achados = [p for p in itens() if t in norm(p.relative_to(BIB).as_posix())]
    pastas = {p for p in BIB.rglob('*') if p.is_dir() and norm(p.relative_to(BIB).as_posix()).endswith(t)}
    return sorted(pastas) or achados


def listar(termo=''):
    for p in itens():
        rel = p.relative_to(BIB).as_posix()
        if norm(termo) in norm(rel):
            print(f'{tam(p.stat().st_size):>8}  {rel}')


def inventario():
    linhas = [f'# Inventário da biblioteca\n', f'Gerado em {date.today():%d/%m/%Y} por `py ferramentas/da_biblioteca.py --inventario`. '
              'Não edite à mão: o catálogo comentado é o `README.md`.\n']
    grupo = None
    for p in itens():
        rel = p.relative_to(BIB)
        g = '/'.join(rel.parts[:2]) if len(rel.parts) > 2 else rel.parts[0]
        if g != grupo:
            grupo = g
            linhas.append(f'\n## {g}\n')
        linhas.append(f'- `{rel.as_posix()}` ({tam(p.stat().st_size)})')
    (BIB / 'INVENTARIO.md').write_text('\n'.join(linhas) + '\n', encoding='utf-8')
    print('ok:', BIB / 'INVENTARIO.md', f'({len(itens())} arquivos)')


def copiar(termo, video, para=None):
    video = Path(video)
    if not video.is_absolute():
        video = RAIZ / video
    if not video.is_dir():
        sys.exit(f'Pasta do vídeo não existe: {video}\nCrie com: py ferramentas/novo_video.py "<pasta>" <TEMA>')
    achados = procurar(termo)
    if not achados:
        sys.exit(f'Nada na biblioteca com "{termo}". Veja: py ferramentas/da_biblioteca.py --listar')
    if len(achados) > 1:
        print(f'"{termo}" achou {len(achados)} itens; seja mais específico (use o caminho):')
        for p in achados[:40]:
            print('  ', p.relative_to(BIB).as_posix())
        sys.exit(1)
    origem = achados[0]
    rel = origem.relative_to(BIB)
    destino_pasta = video / (para or ('trilha sonora' if rel.parts[0] == 'trilhas' else 'elementos'))
    destino_pasta.mkdir(parents=True, exist_ok=True)
    arquivos = [origem] if origem.is_file() else [p for p in origem.rglob('*') if p.is_file()]
    novos = pulados = 0
    for a in arquivos:
        d = destino_pasta / (a.name if origem.is_file() else Path(origem.name) / a.relative_to(origem))
        if d.exists():
            pulados += 1
            continue
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(a, d)
        novos += 1
        print('copiado:', rel.as_posix() if origem.is_file() else (rel / a.relative_to(origem)).as_posix(),
              '->', (d.relative_to(RAIZ) if d.is_relative_to(RAIZ) else d).as_posix())
    print(f'{novos} copiado(s), {pulados} já existia(m) no vídeo (não substituídos).')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] in ('-h', '--help'):
        sys.exit(__doc__)
    if a[0] == '--listar':
        listar(a[1] if len(a) > 1 else '')
    elif a[0] == '--inventario':
        inventario()
    else:
        para = a[a.index('--para') + 1] if '--para' in a else None
        copiar(a[0], a[1], para)

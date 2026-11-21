"""Gera telediagnostico_v3.html a partir de telediagnostico_v3.src.html, embutindo os SVGs dos logos (UFG, UFMG)
para poderem ser animados parte por parte. Uso: py monta_v3.py [versão, padrão v3]."""
import re, sys
from pathlib import Path

AQUI = Path(__file__).parent
EL = AQUI.parents[2] / 'elementos'


def limpa(svg):
    svg = re.sub(r'<\?xml.*?\?>|<!DOCTYPE.*?>|<!--.*?-->', '', svg, flags=re.S)
    svg = re.sub(r'<metadata.*?</metadata>|<sodipodi:namedview.*?/>|<sodipodi:namedview.*?</sodipodi:namedview>', '', svg, flags=re.S)
    return svg.strip()


V = sys.argv[1] if len(sys.argv) > 1 else 'v3'
src = (AQUI / f'telediagnostico_{V}.src.html').read_text(encoding='utf-8')
src = src.replace('{{UFG}}', limpa((EL / 'UFG_logo.svg').read_text(encoding='utf-8')))
src = src.replace('{{UFMG}}', limpa((EL / 'ufmg-logo.svg').read_text(encoding='utf-8')))
(AQUI / f'telediagnostico_{V}.html').write_text(src, encoding='utf-8')
print('ok')

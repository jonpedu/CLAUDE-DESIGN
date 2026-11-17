"""Converte roteiros .md (formato do projeto) em HTML leve e formatado, para abrir no celular.
Uso: py ferramentas/roteiro_html.py <arquivo.md> [outro.md ...]
Gera <arquivo>.html ao lado de cada .md. Entende: títulos (#, ##), parágrafos (quebra de linha simples vira <br>),
**negrito**, *itálico*, `código`, `[texto: …]` (vira pílula), listas (- e 1.), citações (>), tabelas (|) e
as cenas "**[cena: NN] Título**" (viram cartões).
"""
import html
import re
import sys
from pathlib import Path

CSS = """
:root{--azul:#365DCC;--forte:#1C306A;--verde:#19756F;--txt:#101828;--txt2:#475467;--fundo:#F8F9FC;--borda:#E4E7EC;--aviso:#FFF7E0;--aviso-b:#F2C94C}
*{box-sizing:border-box}
html{color-scheme:light}
body{margin:0;background:var(--fundo);color:var(--txt);font:16px/1.6 Poppins,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-text-size-adjust:100%}
header{background:linear-gradient(135deg,var(--forte),var(--azul));color:#fff;padding:28px 16px 24px}
header .serie{font-size:13px;letter-spacing:.06em;text-transform:uppercase;opacity:.8;margin:0 0 4px}
header h1{font-size:30px;line-height:1.15;margin:0;font-weight:700}
main{max-width:760px;margin:0 auto;padding:16px 16px 48px}
.meta{font-size:14px;color:var(--txt2);margin:4px 0 16px}
h2{font-size:19px;color:var(--forte);margin:32px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--azul)}
p{margin:0 0 12px}
blockquote{margin:0 0 16px;padding:12px 16px;background:var(--aviso);border-left:4px solid var(--aviso-b);border-radius:8px}
blockquote p{margin:0 0 6px}
.narracao{background:#fff;border:1px solid var(--borda);border-left:4px solid var(--azul);border-radius:10px;padding:14px 16px;font-size:16px}
.cena{background:#fff;border:1px solid var(--borda);border-radius:12px;padding:14px 16px 6px;margin:0 0 14px;box-shadow:0 1px 2px rgba(16,24,40,.05)}
.cena-tit{display:flex;align-items:center;gap:10px;margin:0 0 10px;font-weight:600;color:var(--forte);font-size:17px;line-height:1.3}
.num{flex:none;background:var(--azul);color:#fff;border-radius:8px;font-size:13px;font-weight:700;padding:3px 8px;letter-spacing:.03em}
.rot{font-weight:600;color:var(--verde)}
.pill{display:inline-block;background:#EAF0FF;color:var(--forte);border:1px solid #C9D6F7;border-radius:5px;padding:1px 8px;margin:2px 1px;font-size:14px;font-weight:600;white-space:normal}
code{background:#EEF1F6;border-radius:4px;padding:1px 5px;font-size:.9em}
ul,ol{margin:0 0 12px;padding-left:22px}
li{margin:0 0 4px}
.tab{overflow-x:auto;margin:0 0 16px}
table{border-collapse:collapse;width:100%;font-size:14px;background:#fff;border-radius:10px;overflow:hidden;border:1px solid var(--borda)}
th{background:var(--forte);color:#fff;text-align:left;font-weight:600;padding:8px 10px}
td{padding:8px 10px;border-top:1px solid var(--borda);vertical-align:top}
tr:nth-child(even) td{background:#F8F9FC}
@media (max-width:560px){
 header h1{font-size:25px}
 table,thead,tbody,tr,th,td{display:block}
 thead{display:none}
 tr{border-top:1px solid var(--borda);padding:6px 0}
 td{border:0;padding:4px 10px}
 td:before{content:attr(data-col);display:block;font-size:12px;font-weight:600;color:var(--txt2);text-transform:uppercase;letter-spacing:.04em}
 tr:nth-child(even) td{background:none}
}
footer{max-width:760px;margin:0 auto;padding:0 16px 32px;color:var(--txt2);font-size:13px}
"""

ROTULOS = ("Narração:", "Tela:", "Animação:", "Visual:", "Cuidado visual:", "Sugestão visual")


def inline(t: str) -> str:
    t = html.escape(t, quote=False)

    def cod(m):
        c = m.group(1)
        if c.startswith("[texto:") and c.endswith("]"):
            return f'<span class="pill">{c[7:-1].strip()}</span>'
        return f"<code>{c}</code>"

    t = re.sub(r"`([^`]+)`", cod, t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    for r in ROTULOS:
        if t.startswith(r):
            t = f'<span class="rot">{r}</span>{t[len(r):]}'
    return t


def tabela(linhas):
    cel = lambda l: [c.strip() for c in l.strip().strip("|").split("|")]
    cab = cel(linhas[0])
    out = ['<div class="tab"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in cab) + "</tr></thead><tbody>"]
    for l in linhas[2:]:
        out.append("<tr>" + "".join(f'<td data-col="{html.escape(cab[i] if i < len(cab) else "")}">{inline(c)}</td>' for i, c in enumerate(cel(l))) + "</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def bloco(linhas):
    """Parágrafo que pode conter listas no meio."""
    out, par, lista, tipo = [], [], [], None

    def fecha_par():
        if par:
            out.append("<p>" + "<br>".join(inline(x) for x in par) + "</p>")
            par.clear()

    def fecha_lista():
        nonlocal tipo
        if lista:
            out.append(f"<{tipo}>" + "".join(f"<li>{inline(x)}</li>" for x in lista) + f"</{tipo}>")
            lista.clear()
        tipo = None

    for l in linhas:
        m_ul = re.match(r"^\s*-\s+(.*)", l)
        m_ol = re.match(r"^\s*\d+\.\s+(.*)", l)
        if m_ul or m_ol:
            fecha_par()
            t = "ul" if m_ul else "ol"
            if tipo and tipo != t:
                fecha_lista()
            tipo = t
            lista.append((m_ul or m_ol).group(1))
        else:
            fecha_lista()
            par.append(l)
    fecha_par()
    fecha_lista()
    return "\n".join(out)


def converter(md: str):
    linhas = md.splitlines()
    titulo, corpo, i = "Roteiro", [], 0
    blocos, atual = [], []
    for l in linhas:
        if l.strip() == "":
            if atual:
                blocos.append(atual)
                atual = []
        else:
            atual.append(l)
    if atual:
        blocos.append(atual)

    secao = ""
    cena_aberta = False
    primeiro_meta = True
    for b in blocos:
        p = b[0]
        if p.startswith("# "):
            titulo = p[2:].strip()
            continue
        if p.startswith("## "):
            if cena_aberta:
                corpo.append("</section>")
                cena_aberta = False
            secao = p[3:].strip()
            corpo.append(f"<h2>{inline(secao)}</h2>")
            rest = b[1:]
            if rest:
                corpo.append(bloco(rest))
            continue
        if p.startswith(">"):
            corpo.append("<blockquote>" + bloco([re.sub(r"^>\s?", "", x) for x in b]) + "</blockquote>")
            continue
        if p.startswith("|"):
            corpo.append(tabela(b))
            continue
        m = re.match(r"^\*\*\[cena:\s*(\d+)\]\s*(.*?)\*\*\s*(.*)$", p)
        if m:
            if cena_aberta:
                corpo.append("</section>")
            num, tit, extra = m.groups()
            extra = f' <em style="font-weight:400;color:var(--txt2);font-size:14px">{inline(extra.strip("* "))}</em>' if extra.strip() else ""
            corpo.append(f'<section class="cena"><div class="cena-tit"><span class="num">CENA {num}</span><span>{inline(tit)}{extra}</span></div>')
            cena_aberta = True
            if b[1:]:
                corpo.append(bloco(b[1:]))
            continue
        if primeiro_meta and not secao:
            corpo.append('<div class="meta">' + "<br>".join(inline(x) for x in b) + "</div>")
            primeiro_meta = False
            continue
        if secao.startswith("Narração completa"):
            corpo.append('<div class="narracao">' + bloco(b) + "</div>")
            continue
        corpo.append(bloco(b))
    if cena_aberta:
        corpo.append("</section>")

    t = html.escape(titulo)
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Roteiro: {t}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body><header><p class="serie">Telessaúde Maranhão · Roteiro</p><h1>{t}</h1></header>
<main>
{chr(10).join(corpo)}
</main>
<footer>Telessaúde Maranhão (NTS-UFMA) · roteiro para validação</footer>
</body></html>
"""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for a in sys.argv[1:]:
        src = Path(a)
        dst = src.with_suffix(".html")
        dst.write_text(converter(src.read_text(encoding="utf-8")), encoding="utf-8")
        print("gerado:", dst)

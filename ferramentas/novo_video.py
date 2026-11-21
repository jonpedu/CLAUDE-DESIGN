"""Cria a estrutura de pastas de um vídeo novo e o arquivo de estado.
Uso: py ferramentas/novo_video.py "<pasta do vídeo>" ["<TEMA>"]
Ex.:  py ferramentas/novo_video.py "CRIANDO-VIDEOS/DENGUE" DENGUE
Não apaga nem renomeia nada: só cria o que faltar (pastas de entrada que já existam com outro nome continuam valendo).
"""
import sys
from datetime import date
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit(__doc__)
raiz = Path(sys.argv[1])
tema = sys.argv[2] if len(sys.argv) > 2 else raiz.name

ENTRADA = ["audios", "roteiro", "elementos", "trilha sonora"]
TRABALHO = ["transcricao", "decupagem", "camadas", "animacao", "quadros", "versoes-anteriores"]

criadas = []
for p in [raiz / d for d in ENTRADA] + [raiz / "renderizando" / "_claude" / d for d in TRABALHO]:
    if not p.exists():
        p.mkdir(parents=True)
        criadas.append(p)

estado = raiz / "renderizando" / "_claude" / "00-estado.md"
if not estado.exists():
    estado.write_text(f"""# {tema}: estado

Criado em {date.today():%d/%m/%Y}. Atualize a cada entrega; o histórico detalhado fica em `{tema} - estudo da edição.md`.

- **Formato e tipo:** (9:16 / 16:9; teleorientação, campanha, institucional, registro)
- **Versão atual:** nenhuma
- **Final aprovado:** nenhum
- **Próximo passo:** conferir o pacote

## Pacote (conferência)

- [ ] Narração em `audios/`
- [ ] Roteiro final (e original / parecer, se houver)
- [ ] Elementos em `elementos/` (SVG quando houver)
- [ ] Régua de marca do parceiro certo
- [ ] Fechamento (logo animado + som, assinaturas)
- [ ] Trilha em `trilha sonora/`
- [ ] Itens obrigatórios confirmados pelo usuário

## Decisões deste vídeo

""", encoding="utf-8")
    criadas.append(estado)

for p in criadas:
    print("criado:", p)
if not criadas:
    print("nada a criar: a estrutura já existe")
print("Próximo: veja o que já existe na biblioteca (py ferramentas/da_biblioteca.py --listar) e copie para o vídeo o que servir;
"
      "peça ao usuário só o que faltar (régua e fechamento: confirme a parceria).")

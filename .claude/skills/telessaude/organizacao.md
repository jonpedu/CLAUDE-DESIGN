# Organização de pastas por vídeo

Espelha a organização que o usuário já usa no Google Drive (Compartilhados comigo › TELEORIENTAÇÃO › PET SAUDE). Todo vídeo do Telessaúde segue esta estrutura, local ou no Drive. Não renomeie nem mova o que o usuário organizou; crie só o que faltar.

## Árvore

```
<SÉRIE>/                              ex.: PET SAUDE
  0. Videos Horizontais/              versões 16:9, com a mesma estrutura por tema
  <TEMA>/                             ex.: DENGUE, DIABETES, HIPERTENSÃO 01
    PARTE 1/                          um vídeo = uma parte (tema curto pode ter só PARTE 1)
      audios/                         narração do AI Studio (.wav), uma faixa ou por trecho
      roteiro/                        roteiro final, roteiro original, parecer técnico
      elementos/                      elementos visuais entregues pelo usuário (personagens, ícones, cenas, imagens)
      trilha sonora/                  trilhas candidatas
      renderizando/                   tudo o que entra na finalização + o vídeo final
    PARTE 2/                          mesma estrutura
  <documentos da série>               ex.: petsaudeorienta.pdf, roteiros da série
```

Observado no Drive (DENGUE › PARTE 1): o roteiro e o **parecer técnico** (validação da SEMUS) ficam soltos na pasta da parte, em PDF. Leia os dois antes de editar: o parecer pode pedir correções no texto da tela.

## O que vai em `renderizando/`

Antes, o vídeo-base era montado no Canva e finalizado no Premiere Pro. Agora o Claude faz as duas etapas (`producao.md`); a pasta continua guardando o que entra na finalização e o vídeo final. Exemplo real do fluxo antigo (DENGUE parte 1):

| Arquivo | Papel | Quem fornece |
| --- | --- | --- |
| `base DENGUE parte 1.mp4` | vídeo-base (antes exportado do Canva; agora montado pelo Claude) | Claude |
| `tele-sted-sao luis-….png` | régua de marca da série | usuário |
| `Regulate - Dyalla.mp3`, `Vital Signs.mp3`, `The Briefing.mp3`, `Balanced Learning….mp3` | trilhas candidatas | usuário |
| `SOM DE FLASH PARA….mp3` | efeito sonoro | usuário |
| `CAPA.png` | capa do vídeo; também vira o **primeiro quadro** do vídeo final (miniatura do WhatsApp) | Claude propõe em toda entrega (quadro do vídeo com a régua ou capa composta); o usuário decide (ver `formatos/vertical.md`, Capa) |
| `Dengue parte 1.prproj` | projeto do Premiere | usuário — **não abrir nem alterar** |
| `DENGUE parte 1.mp4` | vídeo final | saída da finalização |

## Onde o Claude escreve

- **Saídas finais** em `renderizando/`, com o nome no padrão do usuário: `<TEMA> parte <N>.mp4` (ex.: `DENGUE parte 1.mp4`). Se já existir um arquivo com esse nome, **não sobrescrever**: perguntar ou salvar como `<TEMA> parte <N> - v2.mp4`.
- **`renderizando/` guarda só a versão final em qualidade máxima e aprovada** (e a capa dela), ou o que o usuário pedir para mover (regra de 16/11/2026). **Todo vídeo de teste, prévia ou versão em avaliação fica em `renderizando/_claude/`** (as versões numeradas em `_claude/versoes-anteriores/`, ex. `AVC v2.mp4`), porque o usuário assiste por ali, pelo chat. Não apagar esses arquivos sem pedido explícito; quando ele pedir para "limpar", mover para `_claude/` em vez de apagar, salvo se disser que é para apagar. **Vale também para as reconstruções horizontais** (devolutiva da Hipertensão parte 2, 15/11/2026: as v1–v7 foram para `renderizando/` por engano e o usuário pediu para tirar). Ao entregar uma versão em avaliação, mande o arquivo pelo chat a partir de `_claude/versoes-anteriores/`; em `renderizando/` só entra o final que ele aprovou.
- **Arquivos de trabalho** (quadros-chave para aprovação, cenas intermediárias, máscara de área segura, plano cronometrado, `.srt`) em `renderizando/_claude/`. Assim o usuário encontra o que é dele sem misturar.
- **Estado do vídeo** em `renderizando/_claude/00-estado.md`: versão atual, final aprovado, próximo passo e decisões só deste vídeo. Atualize a cada entrega; o `CLAUDE.md` da raiz guarda só um índice curto. Vídeo novo: `py ferramentas/novo_video.py "<pasta>" <TEMA>` cria as pastas e esse arquivo.
- Nada é gravado em `audios/`, `roteiro/`, `elementos/` ou `trilha sonora/`: são pastas de entrada.

## Conferência do pacote (primeiro passo de todo vídeo)

Antes de qualquer edição, liste o que existe e aponte o que falta. Os nomes das pastas variam (ex.: `audio de narração/`, `elementos/para remover fundo/`, roteiro solto em PDF): aceite como vieram, sem renomear.

- [ ] Narração em `audios/`
- [ ] Roteiro final (e original / parecer, se houver)
- [ ] Elementos para montar as cenas em `elementos/` (personagens, ícones, cenas geradas, imagens)
- [ ] Fontes da marca disponíveis (`referencias/fontes/`)
- [ ] Régua de marca do parceiro certo (PNG) em `renderizando/` ou `elementos/` — **muda por parceria; se faltar, pedir antes de montar** (nunca copiar a de outro vídeo)
- [ ] Trilha escolhida (ou candidatas) e efeitos sonoros
- [ ] Logo animado / som de logo do fechamento, se o vídeo-base não os tiver

Antes da conferência, **peça ao usuário a lista completa de assets do vídeo**, cena a cena (regra de 20/11/2026 em `SKILL.md`); o que faltar, pesquise e sugira (com link e licença) para baixar em `elementos/` após o ok dele.

Faltando um elemento de marca, **pergunte**: não crie um substituto. Mesmo com tudo presente, **mostre ao usuário o arquivo escolhido para cada item obrigatório e espere a confirmação** antes de montar (regra em `SKILL.md`).

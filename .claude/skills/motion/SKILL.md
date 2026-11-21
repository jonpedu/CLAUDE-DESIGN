---
name: motion
description: Use ao planejar, animar ou revisar qualquer vídeo de motion design (vertical, horizontal, quadrado; institucional, explicativo, produto, redes sociais). Base geral de princípios, efeitos nomeados, transições, som, formatos e pipeline local. Sub-skills de marca (ex. telessaude) somam regras específicas por cima desta.
---

# Motion — skill geral

Esta é a base de tudo que é animado nesta pasta. As sub-skills de marca, como `telessaude`, só acrescentam regras de marca, formato e conteúdo. O que está aqui vale sempre, salvo quando a sub-skill disser outra coisa.

## Arquivos desta skill (leia só o que a tarefa pedir)

| Arquivo | Quando ler |
| --- | --- |
| `principios.md` | Antes de animar qualquer coisa: 12 princípios da animação aplicados a vídeo, tempos em frames, curvas de easing |
| `efeitos.md` | Ao escolher ou executar um efeito: catálogo de efeitos com nome, duração e receita (use os nomes nas conversas) |
| `metodo-referencia.md` | Quando o usuário mandar um vídeo, PDF ou print de referência: como extrair o estilo sem copiar o conteúdo e como montar o plano cronometrado |
| `takes.md` | Quando o vídeo usa clipes gerados por IA (AI Studio, Flow, Veo): decupagem em trechos, reuso, corte entre takes e sincronia de boca e gestos com a narração |
| `formatos.md` | Ao definir proporção, resolução, áreas seguras e duração por plataforma |
| `som.md` | Ao montar trilha, efeitos sonoros e mixagem |
| `tecnico.md` | Ao renderizar: pipeline local (ffmpeg, Python, HTML + Playwright), organização por cena, padrões de exportação |
| `estilos/*.md` | Quando o usuário pedir um estilo por nome (ex. "editorial pastel 3D"): presets de estilo extraídos de referências |
| `fontes.md` | Para saber de onde veio cada ideia (cursos, PDFs, perfis) |

## Regras de ouro

1. **Direção, não pedido genérico.** Antes de animar, saiba: público, plataforma, duração, referência de estilo e o que aparece em cada cena. Se faltar algo essencial, pergunte uma vez, em lista curta.
2. **A narração manda no tempo.** Cada elemento entra junto da palavra que ele ilustra (no máximo 4 frames depois), nunca antes de ela ser dita.
3. **Um foco por vez.** Em cada momento, o olho deve saber para onde ir. O resto fica parado, menor ou mais apagado.
4. **Nada em velocidade constante.** Toda entrada desacelera; toda saída acelera; todo deslocamento faz as duas coisas.
5. **Objetos fazem a transição.** Prefira um cartão que sobe e cobre a cena, ou uma forma que vira a próxima cena, a um efeito de transição solto.
6. **Nada congela.** Em pausas longas, mantenha uma flutuação leve (1–2% de escala ou 4–8 px de deslocamento em 2–4 s).
7. **Texto curto e exato.** Até 6–8 palavras por cartão; o texto da tela nunca contradiz a fala.
8. **Áreas seguras sempre.** Texto, logo e rosto ficam dentro da área segura do formato (`formatos.md`).
9. **Final limpo.** Os últimos 0,5–0,7 s ficam assentados: texto legível, sem blur de transição, sem corte no meio de um movimento.
10. **Prova antes do render.** Mostre quadros-chave em tamanho real antes do vídeo completo; um render completo por pedido.
11. **Tipografia com intenção: liberdade criativa consciente.** Não é obrigatório fugir das fontes comuns, mas a escolha deve ser analisada: qual fonte serve melhor ao tema, ao tom e à leitura no celular. Se a marca tiver um padrão, ele tem prioridade, mas não é obrigatório: uma fonte diferente pode entrar, inclusive no lugar da base, e o vídeo pode usar quantas famílias precisar, desde que haja um motivo claro (tema de campanha, tom do vídeo, hierarquia) e o usuário aprove. O Claude tem autonomia para **pesquisar e propor fontes** que combinem com o tema e o estilo (Google Fonts, Fontshare e outras com licença livre para uso comercial, como a SIL OFL). Ao propor, diga o nome, a fonte de onde vem, a licença e onde ela entra no vídeo; com o OK do usuário, baixe para `biblioteca/marca/fontes/<Família>/` junto do arquivo de licença e registre na tabela de fontes da sub-skill. Use sempre o arquivo local no render, nunca um link da web. A sub-skill de marca define as fontes-base preferidas; sair delas é possível, com motivo e aprovação.
12. **Vetor (SVG) sempre que houver** (decisão do usuário, 16/11/2026). SVG é texto: dá para animar cada parte (braço, coração, traço que se desenha), recolorir para a paleta e ampliar sem perder nitidez. Ordem de preferência para ícones, órgãos, setas e grafismos flat:
    1. **SVG entregue pelo usuário** em `elementos/` (inclusive elementos baixados do Canva em SVG);
    2. **SVG desenhado pelo Claude em código**, quando a forma for simples (setas, gráficos, ECG, formas geométricas, ícones de linha);
    3. **SVG de bibliotecas abertas** (ex.: Phosphor, Lucide, Iconify, ilustrações com licença livre), buscado pelo Claude e proposto com nome, origem e licença;
    4. PNG/JPG recortado (`recortar.py`) quando só houver imagem.
    **Não converter PNG/JPG em SVG** (vtracer, potrace e afins): o resultado sai cheio de defeitos. Personagens que falam e gesticulam continuam em vídeo (Flow).

## Fluxo de trabalho padrão

1. **Briefing:** objetivo, público, plataforma, formato, duração, identidade visual, referência de estilo.
2. **Roteiro em batidas:** divida a narração em batidas com tempos reais (meça o áudio). Arco padrão: gancho → contexto → conteúdo/prova → ação → mensagem final.
3. **Plano cronometrado:** para cada batida, registre o tempo, o que está na tela, a composição, o efeito (nome do `efeitos.md`), o texto exato, a transição de saída e o som. Use a tabela modelo de `metodo-referencia.md`.
4. **Quadros-chave:** renderize 4 a 6 quadros estáticos em tamanho real (gancho, um cartão, um momento de prova, CTA, final) e peça aprovação.
5. **Animação e render:** renderize por cena, una as cenas e mixe o som (`tecnico.md`, `som.md`).
6. **Revisão:** o usuário aponta ajustes por tempo ("0:23 trocar ícone"). Refaça só as cenas afetadas.

## Checagem final (todo vídeo)

- [ ] Nenhum trecho com velocidade linear ou objeto parado por mais de 2 s sem flutuação
- [ ] No máximo 2 elementos novos entrando ao mesmo tempo, além da legenda
- [ ] Cada texto fica na tela pelo menos 0,5 s + 0,3 s por palavra (mínimo 1,5 s)
- [ ] Tudo o que importa está dentro da área segura; conferido com a máscara sobreposta
- [ ] Som sincronizado com o impacto visual, sem efeito sonoro encobrindo a voz
- [ ] Final assentado e legível; o vídeo assistido inteiro no celular, com e sem som

## Sub-skills de projeto

- `telessaude`: todos os vídeos do Telessaúde Maranhão (marca, áreas seguras, cuidados com conteúdo de saúde). Cada tipo de vídeo tem seu arquivo em `telessaude/tipos/` (teleorientação, campanha, institucional, registro de ação).

Para outro cliente ou marca, copie a pasta `telessaude`, troque nome e descrição, e mantenha só o que é específico: identidade visual, formatos e um arquivo por tipo de vídeo em `tipos/` (estrutura de tempo, regras de conteúdo, efeitos preferidos). Tudo que for geral fica aqui.

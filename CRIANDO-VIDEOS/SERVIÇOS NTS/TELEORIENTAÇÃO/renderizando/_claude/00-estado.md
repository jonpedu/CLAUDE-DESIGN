# TELEORIENTAÇÃO: estado

Criado em 17/11/2026. Atualize a cada entrega; o histórico detalhado fica em `TELEORIENTAÇÃO - estudo da edição.md`.

- **Formato e tipo:** institucional; vertical (9:16) primeiro, depois horizontal (16:9)
- **Versão atual:** **final v3 entregue (20/11/2026, 20h)**: `renderizando/TELEORIENTAÇÃO v3.mp4` (1080×1920, 30 fps, −14 LUFS, 24,85 s; QUALIDADE=max; capa no quadro 0) e `renderizando/CAPA TELEORIENTAÇÃO v3.png` (quadro de 19,0 s). Página `animacao/teleorientacao_v3.html`, mix final `animacao/mix_final_v3.json` (prévia: `mix_v3.json`, `versoes-anteriores/Teleorientacao_previa_v3.mp4`). v3 = sem recorte: pessoas = quadros JPG dos clipes originais (`camadas/quadros_orig/`), em multiplicar sobre fundo claro; Maranhão em azul claro e mapa apagado na faixa das pessoas; fecho sem painel azul (cartão azul + pessoas). Clipes como `<video>` travaram o render (busca intermitente) e saíram pretos: por isso, quadros JPG.
- **Final aprovado:** nenhum ainda (a v3 aguarda o ok do usuário).
- **Próximo passo:** (1) ok do usuário na v3 (ou ajustes por cena com o bloco de avaliação); (2) versão 16:9: pedir a intro horizontal `Intro Telessaude` em 16:9 e recompor (`telessaude/formatos/horizontal.md`). Piloto da série: o visual dele (etiquetas, notificação como fio condutor, pessoas com o pé na régua) é a base dos outros serviços. Linha de produção em `../../01-linha-de-producao.md`.
- **Anterior:** prévia v2 (540×960, com som) em `versoes-anteriores/Teleorientacao_previa_v2.mp4`; página `animacao/teleorientacao_v2.html`, mix `animacao/mix_v2.json`; quadros em `quadros/v2/`.
- **Trilha (escolha do Claude, "me surpreenda"):** `biblioteca-trilhas/animado/joyful-marimba-universfield.mp3`, combinada com uma notificação de marimba sintetizada (`biblioteca-sfx/sintetizados/notificacao_marimba.wav`) em 0,88 s e 18,16 s: o toque do celular "abre" a música.
- **Decisões de layout (v2):** fio condutor = a notificação (chega → vira título → cabeçalho → cartão do fecho); mapa do Brasil como marca d'água contínua; pessoas grandes com o pé na régua; tela toda ocupada (WhatsApp).

## Pacote (conferência)

- [x] Narração `audios/áudio teleorientação.wav` (20,4 s)
- [x] Roteiro final (v2 aprovado pela Amanda, 20/11/2026)
- [x] Elementos: 3 clipes do Flow (idosa, agricultor, estudante), `brazil.svg`, capas das teleorientações
- [x] Régua `regua - tele-sted-sus-govbr.svg`
- [x] Fechamento `Intro Telessaude.mp4` (vertical; o horizontal ainda falta)
- [x] Trilha `joyful-marimba-universfield.mp3`
- [x] Itens obrigatórios confirmados pelo usuário (20/11/2026)

## Decisões deste vídeo

- 20/11/2026: capas de 20 teleorientações baixadas do YouTube em `elementos/capas-youtube/`, com os links em `fontes.md`; prévia em `elementos/_folha-capas.jpg`. Todas em 1080×1920, menos a meningite (720×1280). AVC e Infarto ainda não estão publicados: tirar quadros dos finais locais. Falta escolher quais capas entram na cena 03.
- 20/11/2026: o usuário entregou os finais e as capas oficiais em `TELEORIENTAÇÃO capas e versoes finais/`. Proposta para a cena 03: trechos animados de 1,6 s, sem áudio, passando na tela do celular, 2 por palavra-chave (bem-estar: dengue e obesidade infantil; cuidados em saúde: retinopatia e hipertensão; prevenção de doenças: AVC e hanseníase). Trechos em `animacao/trechos/`, prévia em `animacao/previa-cena03-trechos.gif`. Aguardando o ok do usuário.
- 20/11/2026: prompts do Flow da cena 02 entregues em `roteiro/prompts-flow.md` (clipes A, B e C, mais o D opcional; uma pessoa por clipe, fundo branco, composição feita na edição). Aguardando os clipes.
- 20/11/2026, pacote recebido: narração `audios/áudio teleorientação.wav` (20,4 s, 24 kHz; transcrição em `transcricao/`, bate com o roteiro; cena 02 = 5,6–8,5 s), 3 clipes do Flow **em 16:9** (idosa, agricultor, estudante; 3,9 s, fundo branco, corpo inteiro: servem para os dois formatos depois do recorte), `brazil.svg` (estados com id, `BR-MA`), régua `regua - tele-sted-sus-govbr.svg` (1080×160), fechamento `Intro Telessaude.mp4` (vertical, 4,4 s, com som). Proposta: na cena 02, o mapa do Brasil aproxima no Maranhão (azul) e as 3 pessoas entram na frente.
- (Resolvido em 20/11/2026: itens confirmados e trilha escolhida, ver acima.) Antes: o usuário confirmar os itens obrigatórios e escolher a trilha. Candidatas agora no banco geral `biblioteca-trilhas/` (20/11/2026); sugestão: corporativo/`corporate-maksymmalko.mp3` (série toda) ou tecnologia/`technology-background-atlasaudio-631954.mp3`. Fechamento horizontal: pedir quando chegar a versão 16:9.
- (Resolvido em 20/11/2026: régua e fechamento só do NTS; trilha da v3.) Pendente só o fechamento horizontal.


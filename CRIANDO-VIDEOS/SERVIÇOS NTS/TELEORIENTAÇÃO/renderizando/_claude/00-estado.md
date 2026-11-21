# TELEORIENTAÇÃO: estado

Criado em 17/11/2026. Atualize a cada entrega; o histórico detalhado fica em `TELEORIENTAÇÃO - estudo da edição.md`.

- **Formato e tipo:** institucional; vertical (9:16) primeiro, depois horizontal (16:9)
- **Versão atual (20/11/2026, 19:50):** prévia v3 em `versoes-anteriores/Teleorientacao_previa_v3.mp4` (página `animacao/teleorientacao_v3.html`, mix `mix_v3.json`). v3 = sem recorte: pessoas = quadros JPG dos clipes originais (`camadas/quadros_orig/`), em multiplicar sobre fundo claro; Maranhão em azul claro e mapa apagado na faixa das pessoas; fecho sem painel azul (cartão azul + pessoas). Clipes como `<video>` travaram o render (busca intermitente) e saíram pretos: por isso, quadros JPG. Aguardando aprovação para o render final.
- **Anterior:** prévia v2 (540×960, com som) em `versoes-anteriores/Teleorientacao_previa_v2.mp4`; página `animacao/teleorientacao_v2.html`, mix `animacao/mix_v2.json`; quadros em `quadros/v2/`. Aguardando aprovação dos quadros-chave e da prévia antes do render final em 1080×1920.
- **Trilha (escolha do Claude, "me surpreenda"):** `biblioteca-trilhas/animado/joyful-marimba-universfield.mp3`, combinada com uma notificação de marimba sintetizada (`biblioteca-sfx/sintetizados/notificacao_marimba.wav`) em 0,88 s e 18,16 s: o toque do celular "abre" a música.
- **Decisões de layout (v2):** fio condutor = a notificação (chega → vira título → cabeçalho → cartão do fecho); mapa do Brasil como marca d'água contínua; pessoas grandes com o pé na régua; tela toda ocupada (WhatsApp).
- **Final aprovado:** nenhum ainda. **Final v3 entregue (20/11/2026, 20h):** `renderizando/TELEORIENTAÇÃO v3.mp4` (1080×1920, 30 fps, −14 LUFS, 24,85 s; QUALIDADE=max; capa no quadro 0) e `renderizando/CAPA TELEORIENTAÇÃO v3.png` (quadro de 19,0 s). Mix em `animacao/mix_final_v3.json`. Próximo: ok do usuário; depois a versão 16:9 (falta a intro horizontal).
- **Próximo passo:** roteiro v2 aprovado pela Amanda (20/11/2026). **Piloto da série.** Etapa atual: assets (capas das teleorientações publicadas para a cena 03, depois narração, cenas do Flow, régua, fechamento e trilha). Checklist da série em `../../../00-checklist.md`

## Pacote (conferência)

- [ ] Narração em `audios/`
- [ ] Roteiro final (e original / parecer, se houver)
- [ ] Elementos em `elementos/` (SVG quando houver)
- [ ] Régua de marca do parceiro certo
- [ ] Fechamento (logo animado + som, assinaturas)
- [ ] Trilha em `trilha sonora/`
- [ ] Itens obrigatórios confirmados pelo usuário

## Decisões deste vídeo

- 20/11/2026: capas de 20 teleorientações baixadas do YouTube em `elementos/capas-youtube/`, com os links em `fontes.md`; prévia em `elementos/_folha-capas.jpg`. Todas em 1080×1920, menos a meningite (720×1280). AVC e Infarto ainda não estão publicados: tirar quadros dos finais locais. Falta escolher quais capas entram na cena 03.
- 20/11/2026: o usuário entregou os finais e as capas oficiais em `TELEORIENTAÇÃO capas e versoes finais/`. Proposta para a cena 03: trechos animados de 1,6 s, sem áudio, passando na tela do celular, 2 por palavra-chave (bem-estar: dengue e obesidade infantil; cuidados em saúde: retinopatia e hipertensão; prevenção de doenças: AVC e hanseníase). Trechos em `animacao/trechos/`, prévia em `animacao/previa-cena03-trechos.gif`. Aguardando o ok do usuário.
- 20/11/2026: prompts do Flow da cena 02 entregues em `roteiro/prompts-flow.md` (clipes A, B e C, mais o D opcional; uma pessoa por clipe, fundo branco, composição feita na edição). Aguardando os clipes.
- 20/11/2026, pacote recebido: narração `audios/áudio teleorientação.wav` (20,4 s, 24 kHz; transcrição em `transcricao/`, bate com o roteiro; cena 02 = 5,6–8,5 s), 3 clipes do Flow **em 16:9** (idosa, agricultor, estudante; 3,9 s, fundo branco, corpo inteiro: servem para os dois formatos depois do recorte), `brazil.svg` (estados com id, `BR-MA`), régua `regua - tele-sted-sus-govbr.svg` (1080×160), fechamento `Intro Telessaude.mp4` (vertical, 4,4 s, com som). Proposta: na cena 02, o mapa do Brasil aproxima no Maranhão (azul) e as 3 pessoas entram na frente.
- Pendente: o usuário confirmar os itens obrigatórios e escolher a trilha. Candidatas agora no banco geral `biblioteca-trilhas/` (20/11/2026); sugestão: corporativo/`corporate-maksymmalko.mp3` (série toda) ou tecnologia/`technology-background-atlasaudio-631954.mp3`. Fechamento horizontal: pedir quando chegar a versão 16:9.
- Assets pendentes: trilha, régua e fechamento (só NTS ou NTS + PET-Saúde?), trilha da série.


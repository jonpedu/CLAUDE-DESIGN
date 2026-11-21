# Linha de produção: Serviços do NTS

**Atualizado em 20/11/2026.** Um quadro por vídeo, da validação do roteiro até a publicação. Atualize a cada etapa concluída (o Claude atualiza junto com o `00-estado.md` do vídeo). **Este `.md` é a fonte; a versão para o usuário e a equipe é a página online** (https://claude.ai/artifact/BbL1Wd6C1BdcENfFEbBwEL, arquivo `linha-de-producao-online.html`): a cada mudança aqui, passe para a página e republique. Não há outra versão HTML (decidido em 20/11/2026). Histórico das validações: `00-checklist.md` e documento "Vídeos novos a produzir".

> **Em produção:** Teleorientação (piloto) e Telediagnóstico. **Pode começar depois:** Teleconsultoria (roteiro com ok completo). A Teleconsulta está aprovada só para o vídeo Diferença entre os Serviços.

## Situação de cada roteiro

| Vídeo | Duração | Roteiro | Quem valida | Situação |
| --- | --- | --- | --- | --- |
| Teleconsulta | ~30 s | v2 | Amanda | 🟣 **Aprovado só para a Diferença entre os Serviços** ("esse roteiro aqui tá ok"). O vídeo individual **não está aprovado**: o serviço ainda não é oferecido pelo NTS (proposta de implementação) e há perguntas abertas (quais profissionais, onde fica o paciente, chamada de acesso) |
| Teleorientação | ~25 s | v2 | Amanda | ✅ **Aprovado** (miniaturas aprovadas; "nenhuma outra consideração") |
| Telediagnóstico | ~45 s | v2 | Amanda | ✅ **Aprovado** ("achei ótimo"; frase da espirometria aprovada em 20/11) |
| Teleconsultoria | ~30 s | v2 | Amanda | ✅ **Aprovado** (ok da Amanda na v2, 20/11/2026) |
| Teleducação | ~28 s | v2 | Amanda | ⏳ **Falta o ok da v2** (público e matriciamento foram reescritos com base no retorno dela) |
| Teleinterconsulta | ~58 s | v2 | Gyovanna | ⏳ **Aguardando a Gyovanna** (fluxo do NTS: começa com uma teleconsultoria; Genésio Rego retirado a pedido da Amanda) |
| Telerregulação | ~33 s | v2 | Gyovanna | ⏳ **Aguardando a Gyovanna** (tipo de regulação que o NTS oferece) |
| Diferença entre os Serviços | ~60 s | v2 | Gyovanna | ⏳ **Aguardando a Gyovanna** |

Perguntas opcionais que ficaram sem resposta nos roteiros aprovados (canal da teleconsultoria, chamada para solicitar) **não mudam o texto**: o roteiro segue como está.

## Ordem sugerida de produção

1. **Teleorientação** (**piloto da série**, decidido em 20/11/2026): curta, é o serviço mais conhecido do NTS e define o visual que os outros vão repetir (etiquetas, ganchos, transições, régua e fechamento). Precisa das capas das teleorientações publicadas.
2. **Telediagnóstico**: mais longa; precisa dos ícones dos exames e do mapa do Maranhão (logos UFG/UFMG, se quiser).
3. **Teleconsultoria**.
4. **Teleconsulta**: o NTS **ainda não oferece** (há uma proposta de implementação). O texto está aprovado só para entrar no vídeo Diferença entre os Serviços; o vídeo individual não está aprovado (decidido em 20/11/2026).
5. Teleducação, teleinterconsulta, telerregulação e Diferença entre os Serviços, conforme chegarem os oks.

Formato: **vertical (9:16) primeiro**, depois a versão horizontal (16:9) de cada um.

## Quadro de produção

Legenda: ✅ feito · ⏳ em andamento ou aguardando · 🟣 aprovado só para a Diferença entre os Serviços · — ainda não começou

| Vídeo | Roteiro ok | Assets pedidos | Narração | Cenas Flow | Pacote confirmado | Quadros-chave | Render 9:16 | Final 9:16 | 16:9 | Publicado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Teleconsulta | 🟣 | — | — | — | — | — | — | — | — | — |
| Teleorientação | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⏳ | — | — |
| Telediagnóstico | ✅ | ✅ | ✅ | ✅ (sem Flow) | ✅ | — | — | — | — | — |
| Teleconsultoria | ✅ | — | — | — | — | — | — | — | — | — |
| Teleducação | ⏳ | — | — | — | — | — | — | — | — | — |
| Teleinterconsulta | ⏳ | — | — | — | — | — | — | — | — | — |
| Telerregulação | ⏳ | — | — | — | — | — | — | — | — | — |
| Diferença entre os Serviços | ⏳ | — | — | — | — | — | — | — | — | — |

## O que cada etapa quer dizer

1. **Roteiro ok:** validação da equipe (Amanda ou Gyovanna). Texto na tela e narração só mudam com novo ok.
2. **Assets pedidos:** o Claude lista, cena a cena, tudo o que o vídeo precisa e pede ao usuário; o que faltar, pesquisa e sugere com link e licença, para baixar em `elementos/` depois do ok (regra de 20/11/2026).
3. **Narração:** gravada no Google AI Studio com o texto da seção "Narração completa" do roteiro; `.wav` em `audios/`.
4. **Cenas Flow:** personagens e cenas do Google Flow (motion design + flat design, fundo claro e liso, 9:16), em `elementos/`.
5. **Pacote confirmado:** régua, fechamento (logo animado e som), trilha e narração confirmados pelo usuário, arquivo por arquivo.
6. **Quadros-chave:** 4 a 6 quadros em tamanho real, com a máscara da área segura, aprovados pelo usuário.
7. **Render 9:16:** primeira versão completa, para avaliação, em `renderizando/_claude/`; ajustes por cena.
8. **Final 9:16:** versão aprovada em `renderizando/`, com a capa.
9. **16:9:** versão horizontal recomposta (não recortada).
10. **Publicado:** Instagram (Reels), YouTube (Shorts e vídeo 16:9).

## Itens comuns da série (pedir uma vez, no piloto)

- Régua de marca: `regua - tele-sted-sus-govbr.svg` (Telessaúde, STED/UFMA, SUS Digital, Ministério da Saúde/Governo Federal), confirmada no piloto (20/11/2026).
- Fechamento: `Intro Telessaude.mp4` (vertical, 4,4 s, com som), confirmado no piloto. Falta a versão horizontal.
- Trilha: escolhida por vídeo, conforme o clima, no banco `biblioteca-trilhas/`.
- Personagens recorrentes: enfermeira da UBS, médico (especialista a distância), paciente, agente comunitário de saúde, estudante.

## Narração no Google AI Studio (configuração da série)

Usada no piloto (Teleorientação, 20/11/2026). Repita igual em todos os vídeos da série, para a voz ficar a mesma.

- **Onde:** Google AI Studio → Playground → geração de fala (`aistudio.google.com/generate-speech`).
- **Modelo:** Gemini 3.1 Flash TTS Preview (`gemini-3.1-flash-tts-preview`).
- **Voz:** **Sulafat** (Speaker 1; "Warm, Middle pitch"), com o rótulo de locutor `Narrador`.
- **Scene** (igual em todos os vídeos):
  > Scene: Estúdio profissional de gravação com acústica limpa e isolamento total, clima acolhedor, informativo e dinâmico voltado para comunicação pública em saúde.
- **Sample Context** (muda só a primeira frase: duração e serviço). Texto do piloto:
  > Sample Context: Vídeo institucional curto (cerca de 25 segundos) do Telessaúde Maranhão explicando ao cidadão o conceito de teleorientação por meio de exemplos cotidianos no celular. Director's Notes: Voz de locutor profissional, clara e com excelente projeção. NÃO sussurrar e não usar voz soprosa (sem excesso de ar). A entrega deve ser firme, nítida e contínua, com ritmo ágil e natural. Manter leitura limpa e neutra em português brasileiro, sem sotaques carregados, arrastados ou caricatos.
- **Text:** o usuário gera com o **Gem dele no Gemini** (narração aprovada + marcações de entrega); o Claude não prepara esse texto. Começa com `[speaker: Narrador]`, com marcações antes das frases (`[clear]`, `[projecting]`, `[warm]`, `[informative]`, `[professional]`) e `[no pause]` entre elas. Texto do piloto:
  > [speaker: Narrador]
  > [clear] [projecting] [warm] Recebeu uma dica de saúde pelo celular? [no pause] [informative] Isso pode ser teleorientação. [no pause] [clear] É uma ação de conscientização feita para o cidadão. [no pause] [professional] Ela leva informações e orientações em saúde sobre bem-estar, cuidados em saúde e prevenção de doenças. [no pause] [warm] [projecting] Teleorientação: informação em saúde para você.
- **Saída:** baixar o `.wav` e salvar em `audios/` do vídeo.

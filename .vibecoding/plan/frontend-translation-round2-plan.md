# Objetivo
Planejar a próxima rodada de traduções visíveis do frontend do OneManCompany para pt-BR, cobrindo apenas a interface do usuário em [`frontend/index.html`](frontend/index.html:1), [`frontend/app.js`](frontend/app.js:1), [`frontend/office.js`](frontend/office.js:1), [`frontend/conversation.js`](frontend/conversation.js:1) e [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:1).

# Contexto
A base de i18n já foi centralizada em [`frontend/i18n/en.json`](frontend/i18n/en.json:1) e [`frontend/i18n/pt-BR.json`](frontend/i18n/pt-BR.json:1), com `window.OMC_I18N` mantido como contrato de consumo. A maior parte da UI já foi traduzida e commitada. O restante em inglês parece pequeno, espalhado e concentrado em hardcodes, fallbacks, títulos, tooltips, placeholders e labels auxiliares.

# Decisões aplicadas
- A tradução continua client-side.
- Não reintroduzir [`frontend/i18n.js`](frontend/i18n.js:1).
- Manter `window.OMC_I18N` como API pública.
- Usar paridade 1-pra-1 entre [`frontend/i18n/en.json`](frontend/i18n/en.json:1) e [`frontend/i18n/pt-BR.json`](frontend/i18n/pt-BR.json:1) quando novas chaves forem criadas.
- Preservar emojis, siglas, nomes próprios e termos técnicos intencionais.
- Traduzir apenas texto visível ao usuário; não tratar rotas, IDs, logs ou payloads internos como conteúdo de UI.

# Estratégia
1. Fazer uma varredura final orientada por superfície de UI, priorizando os arquivos já identificados como mais prováveis de conter texto visível remanescente.
2. Classificar cada string remanescente em duas categorias: traduzível e intencional/técnica.
3. Traduzir primeiro os itens de maior impacto visual: títulos, botões, placeholders, tooltips, empty states e mensagens de ação.
4. Quando uma string traduzível não tiver chave existente, adicionar a chave em [`frontend/i18n/en.json`](frontend/i18n/en.json:1) e [`frontend/i18n/pt-BR.json`](frontend/i18n/pt-BR.json:1) mantendo o formato atual.
5. Consolidar as mudanças em commits pequenos, cada um cobrindo um grupo coerente de telas ou componentes.

# Etapas
1. Revisar [`frontend/index.html`](frontend/index.html:1) para localizar textos estáticos visíveis, `aria-label`, `title`, placeholders e títulos de modal.
2. Revisar [`frontend/app.js`](frontend/app.js:1) para localizar fallbacks de `t()`, textos de botão, mensagens de estado vazio, tooltips e comandos slash.
3. Revisar [`frontend/office.js`](frontend/office.js:1) para localizar labels auxiliares e mensagens de painel ainda em inglês.
4. Revisar [`frontend/conversation.js`](frontend/conversation.js:1) e [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:1) para localizar mensagens de conversa, welcome text, cards de finalização e textos de apoio.
5. Separar o que deve ser traduzido do que deve permanecer técnico ou intencional.
6. Atualizar os JSONs de i18n apenas quando surgirem novas chaves necessárias.
7. Validar paridade básica entre os JSONs e revisar visualmente os pontos alterados.

# Ordem sugerida de commits
1. Commit 1: textos mais visíveis do chrome principal em [`frontend/index.html`](frontend/index.html:1) e [`frontend/app.js`](frontend/app.js:1).
2. Commit 2: textos auxiliares de interação em [`frontend/conversation.js`](frontend/conversation.js:1) e [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:1).
3. Commit 3: ajustes finais em [`frontend/office.js`](frontend/office.js:1) e quaisquer fallbacks restantes de baixa exposição.

# Riscos
- Traduzir texto técnico ou intencional pode degradar a clareza de logs e fluxos internos.
- Alterar fallback sem criar chave correspondente pode gerar inconsistência entre idiomas.
- Misturar muitos arquivos num único commit pode dificultar revisão e rollback.
- Strings geradas dinamicamente podem parecer hardcoded, mas na prática já vir de dados de domínio.

# Observações
- A próxima rodada deve ser conservadora e orientada a impacto visual.
- Priorizar consistência com o padrão atual de 1-pra-1 e com o vocabulário já aprovado no frontend.
- Após essa rodada, o restante em inglês esperado deve ficar restrito a termos técnicos intencionais ou dados de domínio.
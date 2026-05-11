# Objetivo
Definir a próxima rodada incremental de traduções client-side da UI do OneManCompany, com mudança mínima, sem traduzir emojis nem símbolos, mantendo a fonte de verdade em [`.vibecoding/`](.vibecoding/) e evitando novo crescimento de escopo.

# Contexto
A base de i18n client-side já está estabelecida em [`frontend/i18n.js`](frontend/i18n.js:1). O seletor de idioma já existe, a preferência em `localStorage` foi validada e a tradução do topo/console já foi concluída. O foco agora é mapear os próximos pontos visíveis de chrome/UI, começando pelos labels e controles já identificados, com atenção para evitar novos blocos grandes.

# Decisões aplicadas
- A tradução continua **client-side** e sem depender de API key para o fluxo principal.
- [`frontend/i18n.js`](frontend/i18n.js:1) permanece como base da infraestrutura de i18n desta fase.
- A preferência de idioma continua persistida em `localStorage` e restaurada no carregamento.
- A cobertura permanece focada em chrome/UI visível, com fallback seguro para o idioma original quando faltar chave.
- Não traduzir emojis nem símbolos; apenas texto natural de labels, títulos, placeholders e controles.
- A seção de API settings e áreas correlatas serão tratadas como frentes incrementais, sem tentativa de cobertura ampla em uma única passagem.
- **Regra operacional:** avançar com **uma label/controle por vez** e **uma microtarefa por vez**; não expandir o escopo no meio da execução.

# Estratégia
Seguir a trilha já validada e manter a implementação em incrementos muito pequenos:
1. estabilizar as labels/controles já traduzidos;
2. mapear os próximos alvos imediatos de UI visível no `frontend/index.html` e `frontend/app.js`;
3. priorizar a seção de API settings e controles adjacentes em passos mínimos;
4. revisar impacto visual e consistência apenas no elemento alvo da vez;
5. registrar qualquer nova lacuna no plano antes de ampliar cobertura.

# Etapas
1. Considerar concluído o núcleo de i18n em [`frontend/i18n.js`](frontend/i18n.js:1), incluindo seletor, persistência e aplicação inicial.
2. Tratar o topo e o console como cobertura já concluída, sem reabrir esse escopo.
3. Listar os próximos pontos visíveis de tradução por bloco pequeno, começando por labels, botões, tooltips e placeholders já expostos na UI.
4. Avançar a seção de API settings e controles adjacentes em microtarefas pequenas, uma label/controle por vez, validando o texto após cada ajuste.
5. Mapear apenas o próximo alvo imediato quando a label atual estiver estável.
6. Evitar abrir novos blocos de tradução até que a seção atual esteja consistente.
7. Se surgir um novo agrupamento de textos, registrar primeiro no contexto em [`.vibecoding/`](.vibecoding/) antes de executar a próxima rodada.

# Riscos
- O escopo da API settings pode crescer rapidamente e reintroduzir o ciclo de “traduzir tudo de uma vez”.
- Cobertura parcial de labels pode deixar estados mistos de idioma se a próxima microtarefa não for aplicada no mesmo bloco visual.
- Textos dinâmicos, placeholders e tooltips podem exigir chaves adicionais fora da label principal.
- Símbolos, emojis e atalhos visuais não devem entrar no fluxo de tradução.
- Duplicação de lógica entre arquivos de frontend pode confundir a fonte de verdade se o plano voltar a misturar prioridades.

# Observações
- O plano deve permanecer como guia de execução incremental, não como inventário completo de tradução.
- Arquivos de referência principal nesta fase: [`frontend/i18n.js`](frontend/i18n.js:1), [`frontend/app.js`](frontend/app.js:1), [`frontend/index.html`](frontend/index.html:1) e [`frontend/style.css`](frontend/style.css:1).
- A próxima execução deve respeitar a regra de menor mudança possível, parar assim que o bloco atual estiver traduzido e consistente, e não incluir símbolos/emoji no escopo.
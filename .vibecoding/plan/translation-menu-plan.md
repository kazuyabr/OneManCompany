# Objetivo
Consolidar a continuidade das traduções client-side da UI do OneManCompany com mudança mínima, mantendo a fonte de verdade em [`.vibecoding/`](.vibecoding/) e evitando novo crescimento de escopo.

# Contexto
A base de i18n client-side já está estabelecida em [`frontend/i18n.js`](frontend/i18n.js:1). O seletor de idioma já existe, a preferência em `localStorage` foi validada e a tradução do topo/console já foi concluída. O próximo trecho em andamento é a seção de API settings, que deve avançar apenas por microtarefas pequenas para evitar loops de escopo.

# Decisões aplicadas
- A tradução continua **client-side** e sem depender de API key para o fluxo principal.
- [`frontend/i18n.js`](frontend/i18n.js:1) é a base da infraestrutura de i18n desta fase.
- A preferência de idioma deve continuar persistida em `localStorage` e restaurada no carregamento.
- A cobertura deve permanecer focada em chrome/UI visível, com fallback seguro para o idioma original quando faltar chave.
- A seção de API settings será tratada como área incremental, sem tentativa de cobertura ampla em uma única passagem.
- **Regra operacional:** avançar com **uma label por vez** e **uma microtarefa por vez**; não expandir o escopo no meio da execução.

# Estratégia
Seguir a trilha já validada e manter a implementação em incrementos muito pequenos:
1. estabilizar as labels/controles já traduzidos;
2. concluir a seção de API settings em passos mínimos;
3. revisar impacto visual e consistência apenas no elemento alvo da vez;
4. registrar qualquer nova lacuna no plano antes de ampliar cobertura.

# Etapas
1. Considerar concluído o núcleo de i18n em [`frontend/i18n.js`](frontend/i18n.js:1), incluindo seletor, persistência e aplicação inicial.
2. Tratar o topo e o console como cobertura já concluída, sem reabrir esse escopo.
3. Avançar a seção de API settings em microtarefas pequenas, uma label/controle por vez, validando o texto após cada ajuste.
4. Mapear apenas os próximos alvos imediatos da API settings quando a label atual estiver estável.
5. Evitar abrir novos blocos de tradução até que a seção atual esteja consistente.
6. Se surgir um novo agrupamento de textos, registrar primeiro no contexto em [`.vibecoding/`](.vibecoding/) antes de executar a próxima rodada.

# Riscos
- O escopo da API settings pode crescer rapidamente e reintroduzir o ciclo de “traduzir tudo de uma vez”.
- Cobertura parcial de labels pode deixar estados mistos de idioma se a próxima microtarefa não for aplicada no mesmo bloco visual.
- Textos dinâmicos, placeholders e tooltips podem exigir chaves adicionais fora da label principal.
- Duplicação de lógica entre arquivos de frontend pode confundir a fonte de verdade se o plano voltar a misturar prioridades.

# Observações
- O plano deve permanecer como guia de execução incremental, não como inventário completo de tradução.
- Arquivos de referência principal nesta fase: [`frontend/i18n.js`](frontend/i18n.js:1), [`frontend/app.js`](frontend/app.js:1), [`frontend/index.html`](frontend/index.html:1) e [`frontend/style.css`](frontend/style.css:1).
- A próxima execução deve respeitar a regra de menor mudança possível e parar assim que a label atual estiver traduzida e consistente.
# Objetivo
Migrar a camada de traduções client-side do OneManCompany de [`frontend/i18n.js`](frontend/i18n.js:1) para [`frontend/i18n/`](frontend/i18n/), com um arquivo JSON por idioma e um loader central em JavaScript, sem alterar o comportamento atual da UI.

# Contexto
A aplicação já usa i18n no cliente, com preferência persistida em `localStorage`, aplicação automática no carregamento e consumo por [`frontend/app.js`](frontend/app.js:134), [`frontend/index.html`](frontend/index.html:753) e [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:28). O painel do CEO e os rótulos visíveis já foram estabilizados; a migração agora precisa preservar a separação correta entre idiomas e reduzir acoplamento.

# Decisões aplicadas
- A tradução continua **client-side**.
- A fonte de verdade permanece em [`frontend/i18n.js`](frontend/i18n.js:1) até a migração ser concluída.
- A nova estrutura será [`frontend/i18n/`](frontend/i18n/) com, no mínimo:
  - [`frontend/i18n/en.json`](frontend/i18n/en.json:1)
  - [`frontend/i18n/pt-BR.json`](frontend/i18n/pt-BR.json:1)
  - um loader central em JavaScript, por exemplo [`frontend/i18n-loader.js`](frontend/i18n-loader.js:1)
- O formato dos JSONs será **plano**: chaves string → valores string.
- O loader central deve manter a API pública atual consumida por [`frontend/app.js`](frontend/app.js:134) e [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:28):
  - `getLanguage()`
  - `setLanguage(lang)`
  - `getLanguages()`
  - `t(key, fallback = '', vars = {})`
  - `format(template, vars = {})`
  - `applyTo(root = document)`
  - `STORAGE_KEY`
  - `DEFAULT_LANGUAGE`
- O loader deve persistir a seleção em `localStorage` e validar idioma suportado antes de aplicar.
- O loader deve aplicar fallback seguro para `DEFAULT_LANGUAGE` e, em último caso, para o texto recebido como `fallback`.
- A aplicação de texto em DOM deve continuar cobrindo `data-i18n`, `data-i18n-title`, `placeholder` e `aria-label` quando aplicável.
- Emojis e símbolos não entram no escopo de tradução.

# Contrato dos JSONs
Cada arquivo de idioma deve seguir o mesmo contrato:

- Codificação: UTF-8
- Raiz: objeto JSON simples
- Valores: strings somente
- Interpolação: usando placeholders no formato `{name}`
- Nenhuma lógica, função ou metadado de runtime dentro dos JSONs
- As mesmas chaves devem existir em todos os idiomas suportados, mesmo quando o texto seja idêntico ou vazio por decisão explícita

Exemplo de formato:

```json
{
  "nav.products": "PRODUCTS",
  "ceo.chatWithEA": "Chat with EA",
  "meeting.roomTitle": "🏢 {name}"
}
```

# Contrato do loader central
O loader será o único ponto de orquestração de idioma no cliente.

Responsabilidades:
- carregar o JSON do idioma ativo;
- aplicar fallback para o idioma padrão quando o idioma salvo não existir;
- manter uma cache interna dos textos carregados para evitar recomputação excessiva;
- expor a mesma superfície pública usada hoje por [`frontend/app.js`](frontend/app.js:134);
- preservar o comportamento atual de `window.OMC_I18N` para não quebrar a UI existente.

Comportamento esperado:
- `getLanguage()` retorna o idioma efetivo atual;
- `setLanguage(lang)` normaliza para um idioma suportado, persiste a escolha e retorna o idioma efetivo;
- `t()` resolve a chave no idioma atual, depois no idioma padrão, depois no fallback fornecido;
- `applyTo()` atualiza textos estáticos do DOM sem tocar em nós com conteúdo composto;
- falhas de carregamento não devem bloquear renderização nem quebrar o boot.

# Estratégia
1. Extrair o conteúdo atual de [`frontend/i18n.js`](frontend/i18n.js:1) para JSONs por idioma, preservando as chaves existentes.
2. Introduzir o loader central com cache, fallback e API compatível.
3. Atualizar [`frontend/index.html`](frontend/index.html:752) para carregar o loader novo antes de [`frontend/app.js`](frontend/app.js:1).
4. Atualizar [`frontend/app.js`](frontend/app.js:134) apenas para continuar consumindo `window.OMC_I18N` sem depender do formato antigo interno.
5. Ajustar [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:28) somente se algum refresh de texto localizado precisar ser acionado por contrato novo.
6. Desativar o arquivo monolítico antigo apenas quando a nova estrutura estiver estável e validada.

# Etapas
1. Definir os arquivos finais da nova estrutura e o contrato JSON exato.
2. Mapear todas as chaves existentes para garantir paridade entre idiomas.
3. Implementar o loader central com fallback, persistência e interpolação.
4. Atualizar os pontos de boot em [`frontend/index.html`](frontend/index.html:752) e [`frontend/app.js`](frontend/app.js:134).
5. Validar o refresh de textos em [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:28) e em rotas do chrome localizadas.
6. Remover a dependência direta da constante `TRANSLATIONS` apenas após a migração estar estável.

# Riscos
- Falha no carregamento assíncrono pode deixar textos vazios se o fallback não for robusto.
- Alterar a ordem de boot em [`frontend/index.html`](frontend/index.html:752) pode quebrar a inicialização do app.
- Se `app.js` assumir que as traduções já estão carregadas de forma síncrona, a migração pode introduzir race conditions.
- Se os JSONs não mantiverem paridade de chaves, a UI pode ficar inconsistente entre idiomas.
- Uma migração parcial pode gerar divergência entre o estado do seletor de idioma e o texto renderizado.

# Observações
- O escopo permanece incremental e conservador.
- O carregador novo deve preservar a compatibilidade observada em [`frontend/app.js`](frontend/app.js:134), [`frontend/index.html`](frontend/index.html:145) e [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:28).
- Emojis, símbolos e marcadores visuais permanecem intactos.
- A migração deve priorizar estabilidade da UI sobre limpeza imediata do arquivo antigo.
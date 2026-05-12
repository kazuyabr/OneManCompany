# Objetivo
Migrar a camada de traduções client-side do OneManCompany de um único arquivo JavaScript para uma pasta dedicada [`.i18n`](frontend/i18n/:1), com um arquivo JSON por idioma e um carregador central em JavaScript, preservando o comportamento atual e a separação correta entre idiomas.

# Contexto
A UI já usa i18n client-side, com preferência persistida em `localStorage`, aplicação inicial no carregamento e cobertura visível do painel do CEO já estabilizada em [`frontend/index.html`](frontend/index.html:84), [`frontend/app.js`](frontend/app.js:134) e [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:24). O próximo passo é organizar as traduções por idioma para facilitar replicação e manutenção, sem quebrar o fluxo atual.

# Decisões aplicadas
- A tradução continua **client-side**.
- As traduções sairão de [`frontend/i18n.js`](frontend/i18n.js:1) e passarão para arquivos JSON por idioma.
- A pasta dedicada será [`frontend/i18n/`](frontend/i18n/), com arquivos como [`frontend/i18n/en.json`](frontend/i18n/en.json:1) e [`frontend/i18n/pt-BR.json`](frontend/i18n/pt-BR.json:1).
- O carregador central permanecerá em JavaScript e será responsável por:
  - carregar o JSON do idioma atual;
  - manter fallback seguro para o idioma padrão;
  - expor `t()`, `setLanguage()`, `getLanguage()` e `applyTo()`;
  - preservar a aplicação automática em elementos com `data-i18n`, `data-i18n-title` e placeholders.
- A preferência de idioma continua persistida em `localStorage`.
- Emojis e símbolos continuam fora do escopo de tradução.
- O contrato textual entre idiomas deve permanecer separado: inglês em `en.json`, português em `pt-BR.json`.

# Estratégia
1. Extrair as traduções atuais para arquivos JSON por idioma, mantendo as chaves existentes.
2. Criar um loader central pequeno para buscar o JSON do idioma escolhido e aplicar fallback ao padrão.
3. Ajustar [`frontend/app.js`](frontend/app.js:134) para inicializar o novo loader sem alterar o fluxo de UI.
4. Ajustar [`frontend/index.html`](frontend/index.html:84) e [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:24) apenas se houver necessidade de leitura adicional do loader ou refresh de textos localizados.
5. Manter a migração incremental: primeiro arquitetura de carregamento, depois organização dos dados, depois limpeza do arquivo antigo.

# Etapas
1. Definir o formato dos JSONs por idioma, incluindo estrutura plana de chave/valor e codificação UTF-8.
2. Criar a pasta [`frontend/i18n/`](frontend/i18n/) e os arquivos [`frontend/i18n/en.json`](frontend/i18n/en.json:1) e [`frontend/i18n/pt-BR.json`](frontend/i18n/pt-BR.json:1).
3. Implementar um loader central em JavaScript para:
   - descobrir o idioma atual;
   - carregar o JSON correspondente;
   - manter fallback em inglês ou no idioma padrão;
   - sinalizar erro de carga sem quebrar a UI.
4. Atualizar [`frontend/app.js`](frontend/app.js:134) para usar o novo loader ao inicializar e ao trocar idioma.
5. Validar que os elementos do CEO, do topo e dos painéis ainda recebem textos corretos após a troca de idioma.
6. Remover ou desativar a dependência direta do objeto grande `TRANSLATIONS` em [`frontend/i18n.js`](frontend/i18n.js:1) somente quando a nova estrutura estiver estável.
7. Registrar qualquer ajuste adicional no contexto antes de ampliar a migração para outras áreas.

# Riscos
- Falta de fallback pode deixar a UI com textos vazios durante falhas de leitura dos JSONs.
- Migrar tudo de uma vez pode introduzir regressões de idioma ou de encoding.
- Se o carregador central não respeitar o estado do `localStorage`, a troca de idioma pode ficar inconsistente.
- Arquivos JSON muito grandes ainda podem concentrar manutenção, então a divisão por idioma precisa ser mantida limpa.
- Mudanças no carregamento assíncrono podem exigir um pequeno refresh após a troca de idioma para atualizar textos já renderizados.

# Observações
- O escopo atual é organizacional: separar traduções por idioma, sem mudar o conteúdo textual além do necessário para manter a separação correta.
- O carregador central deve preservar a API atual usada por [`frontend/app.js`](frontend/app.js:134) e pelos componentes que já chamam `window.OMC_I18N`.
- A migração deve manter a compatibilidade com a cobertura já feita no painel do CEO.
- Símbolos, emojis e marcadores visuais permanecem intactos.
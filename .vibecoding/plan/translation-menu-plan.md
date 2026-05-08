# Objetivo
Adicionar um menu de tradução na interface do OneManCompany com mudança mínima no código existente, permitindo alternar o idioma da UI sem exigir API key quando possível.

# Contexto
O projeto já possui uma frontend grande em [`frontend/index.html`](frontend/index.html:1) e [`frontend/app.js`](frontend/app.js:1), com bastante texto renderizado no HTML e em trechos dinâmicos via JavaScript. A demanda prioriza baixo impacto arquitetural e deve preservar o comportamento atual do app.

# Decisões aplicadas
- Preferir uma solução **client-side** para evitar alterar backend, rotas ou persistência de dados do servidor.
- Não depender de API key como requisito básico.
- Tratar a tradução como uma camada de apresentação, com fallback seguro para o idioma original.
- Persistir a preferência de idioma no navegador para manter a escolha após reload.

# Estratégia
Implementar um seletor de idioma no cabeçalho da UI e introduzir uma camada de tradução no frontend que opere sobre o conteúdo textual visível da página.

Abordagem recomendada:
1. **Camada base sem API key**: usar traduções locais para o texto da própria interface, cobrindo menus, botões, labels e títulos principais.
2. **Atualização DOM controlada**: marcar nós relevantes com chaves de tradução para trocar texto sem reescrever a tela inteira.
3. **Fallback opcional**: se houver suporte nativo no navegador para tradução de conteúdo, aproveitar como melhoria opcional; caso contrário, manter o fallback local.
4. **Conteúdo dinâmico**: limitar inicialmente a tradução aos elementos de chrome/UI e aos textos gerados pelo próprio app; deixar conteúdo complexo, logs e mensagens de sistema no idioma original até segunda fase.

# Etapas
1. Mapear os textos fixos e os blocos de UI com maior visibilidade em [`frontend/index.html`](frontend/index.html:1).
2. Criar uma tabela simples de traduções por idioma em [`frontend/app.js`](frontend/app.js:1), com chaves estáveis para labels e botões.
3. Inserir um menu de idioma no header atual da aplicação, reutilizando o padrão visual existente.
4. Aplicar a tradução no carregamento inicial e quando o usuário trocar o idioma.
5. Persistir o idioma selecionado em `localStorage` e restaurar na inicialização.
6. Adicionar fallback para idioma padrão caso uma chave esteja ausente.
7. Ajustar textos dinâmicos e áreas mais críticas apenas se necessário para manter consistência visual.

# Riscos
- Uma tradução puramente automática do HTML inteiro pode quebrar seletores, estados e conteúdo dinâmico.
- Conteúdo renderizado depois do carregamento pode não ser traduzido se não houver um mecanismo de reaplicação.
- Tradução externa sem API key pode depender de recurso de navegador ou de serviço de terceiros e pode ser instável.
- Textos dentro de atributos, placeholders e tooltips exigem cobertura explícita.

# Observações
- A solução recomendada prioriza **baixo acoplamento** e **baixo risco**.
- Se o objetivo evoluir para tradução completa automática de toda a página, isso deve virar uma fase separada com impacto maior.
- Arquivos mais prováveis de alteração: [`frontend/index.html`](frontend/index.html:1), [`frontend/app.js`](frontend/app.js:1), e possivelmente [`frontend/style.css`](frontend/style.css:1) para o seletor de idioma.
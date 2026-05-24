# Domain Mode

- Active domain: frontend translation cleanup for pt-BR.
- Current state:
  - [`frontend/conversation.js`](frontend/conversation.js:1) done.
  - [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:1) done.
  - [`frontend/i18n/en.json`](frontend/i18n/en.json:1) and [`frontend/i18n/pt-BR.json`](frontend/i18n/pt-BR.json:1) synced and validated.
  - [`frontend/task-tree-g6.js`](frontend/task-tree-g6.js:1) updated with translated labels/fallbacks.
  - [`frontend/index.html`](frontend/index.html:1) still has visible English text pending.
- Translation rules:
  - translate only user-visible text
  - preserve emojis, siglas, proper nouns, and intentional technical terms
  - keep `window.OMC_I18N` as the public contract
  - keep client-side i18n isolated in the JSON files
- Remaining work focuses on finishing visible strings in [`frontend/index.html`](frontend/index.html:1) and then rechecking for any residual hardcoded UI text.

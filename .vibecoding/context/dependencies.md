# Dependencies

- Frontend i18n source of truth:
  - [`frontend/i18n/en.json`](frontend/i18n/en.json:1)
  - [`frontend/i18n/pt-BR.json`](frontend/i18n/pt-BR.json:1)
- Public runtime contract: `window.OMC_I18N` from [`frontend/i18n-loader.js`](frontend/i18n-loader.js:1)
- UI surfaces already translated or in scope:
  - [`frontend/conversation.js`](frontend/conversation.js:1)
  - [`frontend/ceo-terminal.js`](frontend/ceo-terminal.js:1)
  - [`frontend/task-tree-g6.js`](frontend/task-tree-g6.js:1)
  - [`frontend/index.html`](frontend/index.html:1)
- Higher-level chrome/interaction surfaces may still depend on fallback text in:
  - [`frontend/app.js`](frontend/app.js:1)
  - [`frontend/office.js`](frontend/office.js:1)
- Do not reintroduce [`frontend/i18n.js`](frontend/i18n.js:1).
- Preserve parity 1:1 between `en.json` and `pt-BR.json` for any new keys.

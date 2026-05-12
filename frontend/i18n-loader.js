(() => {
  const STORAGE_KEY = 'omc-ui-language';
  const DEFAULT_LANGUAGE = 'pt-BR';
  const LANGUAGES = [
    { code: 'en', label: 'English' },
    { code: 'pt-BR', label: 'Português (Brasil)' },
  ];
  const LANGUAGE_CODES = new Set(LANGUAGES.map((lang) => lang.code));
  const TRANSLATION_CACHE = new Map();

  function normalizeLanguage(lang) {
    return LANGUAGE_CODES.has(lang) ? lang : DEFAULT_LANGUAGE;
  }

  function safeReadStorage() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch {
      return null;
    }
  }

  function safeWriteStorage(lang) {
    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch {
      // Ignore storage failures; keep runtime behavior intact.
    }
  }

  function format(template, vars = {}) {
    return String(template).replace(/\{(\w+)\}/g, (_, key) => (
      vars[key] == null ? `{${key}}` : String(vars[key])
    ));
  }

  function loadLanguage(lang) {
    const normalized = normalizeLanguage(lang);
    if (TRANSLATION_CACHE.has(normalized)) return TRANSLATION_CACHE.get(normalized);

    let translations = {};
    try {
      const xhr = new XMLHttpRequest();
      xhr.open('GET', `i18n/${normalized}.json`, false);
      xhr.send(null);
      const ok = (xhr.status >= 200 && xhr.status < 300) || xhr.status === 0;
      if (ok && xhr.responseText) {
        const parsed = JSON.parse(xhr.responseText);
        if (parsed && typeof parsed === 'object' && !Array.isArray(parsed)) {
          translations = parsed;
        }
      }
    } catch {
      translations = {};
    }

    TRANSLATION_CACHE.set(normalized, translations);
    return translations;
  }

  function getStoredLanguage() {
    const saved = safeReadStorage();
    return normalizeLanguage(saved);
  }

  let currentLanguage = getStoredLanguage();
  loadLanguage(DEFAULT_LANGUAGE);
  loadLanguage(currentLanguage);

  function getLanguage() {
    return currentLanguage;
  }

  function setLanguage(lang) {
    currentLanguage = normalizeLanguage(lang);
    safeWriteStorage(currentLanguage);
    loadLanguage(currentLanguage);
    return currentLanguage;
  }

  function getLanguages() {
    return LANGUAGES.slice();
  }

  function resolveTemplate(key, fallback = '') {
    const active = TRANSLATION_CACHE.get(currentLanguage) || loadLanguage(currentLanguage);
    const defaultTranslations = TRANSLATION_CACHE.get(DEFAULT_LANGUAGE) || loadLanguage(DEFAULT_LANGUAGE);
    return active[key] ?? defaultTranslations[key] ?? fallback;
  }

  function t(key, fallback = '', vars = {}) {
    return format(resolveTemplate(key, fallback), vars);
  }

  function applyTo(root = document) {
    if (!root || typeof root.querySelectorAll !== 'function') return;

    root.querySelectorAll('[data-i18n]').forEach((node) => {
      const key = node.getAttribute('data-i18n');
      if (!key) return;
      if (key.startsWith('status.')) return;
      if (node.childElementCount > 0) return;

      const value = t(key, node.textContent || '');
      if ('placeholder' in node) {
        node.placeholder = value;
      } else {
        node.textContent = value;
      }
    });

    root.querySelectorAll('[data-i18n-title]').forEach((node) => {
      const key = node.getAttribute('data-i18n-title');
      if (!key) return;

      const value = t(key, node.getAttribute('title') || '');
      node.title = value;
      if (node.getAttribute('aria-label') != null) node.setAttribute('aria-label', value);
    });

    if (typeof document !== 'undefined' && document.documentElement) {
      document.documentElement.lang = currentLanguage;
    }
  }

  if (typeof document !== 'undefined') {
    applyTo(document);
  }

  window.OMC_I18N = {
    STORAGE_KEY,
    DEFAULT_LANGUAGE,
    getLanguage,
    setLanguage,
    t,
    format,
    getLanguages,
    applyTo,
  };
})();

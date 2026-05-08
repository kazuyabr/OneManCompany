(() => {
  const STORAGE_KEY = 'omc-ui-language';
  const DEFAULT_LANGUAGE = 'en';

  const LANGUAGES = [
    { code: 'en', label: 'English' },
    { code: 'pt-BR', label: 'Português (Brasil)' },
  ];

  const TRANSLATIONS = {
    en: {
      'nav.products': 'PRODUCTS',
      'nav.activity': 'ACTIVITY LOG',
      'nav.teamRoster': 'TEAM ROSTER',
      'nav.ceoConsole': 'CEO CONSOLE',
      'toolbar.settings': 'Settings',
      'settings.title': '⚙ SETTINGS',
      'settings.languageLabel': 'Language',
      'settings.textSize': 'Text Size',
      'settings.apiConnections': '🔑 API Connections',
      'settings.systemCrons': '⏰ System Crons',
      'settings.display': '👁 Display',
    },
    'pt-BR': {
      'nav.products': 'PRODUTOS',
      'nav.activity': 'LOG DE ATIVIDADE',
      'nav.teamRoster': 'EQUIPE',
      'nav.ceoConsole': 'PAINEL DO CEO',
      'toolbar.settings': 'Configurações',
      'settings.title': '⚙ CONFIGURAÇÕES',
      'settings.languageLabel': 'Idioma',
      'settings.textSize': 'Tamanho do texto',
      'settings.apiConnections': '🔑 Conexões de API',
      'settings.systemCrons': '⏰ Tarefas agendadas',
      'settings.display': '👁 Exibição',
    },
  };

  function getLanguage() {
    const saved = localStorage.getItem(STORAGE_KEY);
    return TRANSLATIONS[saved] ? saved : DEFAULT_LANGUAGE;
  }

  function setLanguage(lang) {
    const next = TRANSLATIONS[lang] ? lang : DEFAULT_LANGUAGE;
    localStorage.setItem(STORAGE_KEY, next);
    return next;
  }

  function t(key, fallback = '') {
    const lang = getLanguage();
    return TRANSLATIONS[lang]?.[key] || TRANSLATIONS[DEFAULT_LANGUAGE]?.[key] || fallback;
  }

  function getLanguages() {
    return LANGUAGES.slice();
  }

  function applyTo(root = document) {
    root.querySelectorAll('[data-i18n]').forEach((node) => {
      const key = node.getAttribute('data-i18n');
      const value = t(key, node.textContent || '');
      if ('placeholder' in node) {
        node.placeholder = value;
      } else {
        node.textContent = value;
      }
    });
    document.documentElement.lang = getLanguage();
  }

  window.OMC_I18N = {
    STORAGE_KEY,
    DEFAULT_LANGUAGE,
    getLanguage,
    setLanguage,
    t,
    getLanguages,
    applyTo,
  };
})();

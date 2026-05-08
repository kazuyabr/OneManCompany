(() => {
  const STORAGE_KEY = 'omc-ui-language';
  const DEFAULT_LANGUAGE = 'pt-BR';

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
      'toolbar.newProduct': 'New Product',
      'toolbar.importProduct': 'Import Product',
      'toolbar.exEmployeeWall': 'Ex-Employee Wall',
      'toolbar.companyCulture': 'Company Culture',
      'toolbar.companyDirection': 'Company Direction',
      'toolbar.dashboard': 'Dashboard',
      'toolbar.announcements': 'Announcements',
      'toolbar.doNotDisturb': 'Do Not Disturb',
      'toolbar.backgroundTasks': 'Background Tasks',
      'toolbar.exportScreenshot': 'Export SVG Screenshot',
      'toolbar.stopAllTasks': 'Stop All Tasks',
      'toolbar.forceReload': 'Force reload all data from disk',
      'settings.title': '⚙ SETTINGS',
      'settings.languageLabel': 'Language',
      'settings.textSize': 'Text Size',
      'settings.apiConnections': '🔑 API Connections',
      'settings.systemCrons': '⏰ System Crons',
      'settings.display': '👁 Display',
      'ceo.chat': '💬 Chat',
      'ceo.projects': 'Projects',
      'ceo.oneOnOne': '1-on-1',
      'ceo.linkTaskToProduct': 'Link task to product',
      'ceo.noProduct': 'No Product',
      'status.employeeCount': '👥 {count}',
      'status.toolCount': '🔧 {count}',
      'status.roomCount': '🏢 {free}/{total}',
      'announcements.title': '🔔 Announcements',
      'announcements.loading': 'Loading...',
      'meeting.roomTitle': '🏢 {name}',
      'meeting.minutesTitle': '📒 Meeting Minutes: {name}',
      'meeting.oneononeTitle': '🎓 1-on-1 Meeting',
      'meeting.available': 'Available',
      'meeting.inMeeting': 'In Meeting',
      'meeting.capacity': '{count} people',
      'meeting.participants': 'Participants',
      'meeting.noParticipants': 'No participants',
      'meeting.liveLog': 'Live Meeting Log',
      'meeting.loading': 'Loading...',
      'meeting.loadingMinutes': 'Loading minutes...',
      'meeting.noLogs': 'No meeting logs',
      'meeting.noArchivedMeetings': 'No archived meetings',
      'meeting.failedLoadChat': 'Failed to load chat',
      'meeting.failedLoadMinutes': 'Failed to load minutes',
      'meeting.notFound': 'Not found',
      'meeting.backToList': 'Back to list',
      'meeting.summary': 'Summary',
      'meeting.noData': 'No data',
      'meeting.selectEmployee': 'Select Employee',
      'meeting.selectEmployeePlaceholder': '-- Select Employee --',
      'workflow.selectPrompt': '← Select a workflow to view',
      'employee.detailsTitle': 'Employee Details',
      'interview.title': '🎤 Interview',
      'toolList.title': '🛠 TOOL LIST',
      'product.detailTitle': 'Product Detail',
      'traceViewer.title': 'TRACE VIEWER',
      'companyDirection.placeholder': 'e.g. We focus on AI-driven creative tools for indie creators...',
      'companyCulture.placeholder': 'Add a new culture entry...',
      'createProduct.namePlaceholder': 'e.g. OneManCompany官网',
      'createProduct.objectivePlaceholder': 'Product goal / objective',
      'ceo.messagePlaceholder': '$ Type message, / for commands (Enter to send)',
      'meeting.messagePlaceholder': 'Type a message...',
      'onboarding.toggle': '▼',
      'candidate.selectedCount': '0 selected',
      'talentPool.sourceBadge': '',
      'common.approve': 'Approve',
      'common.reject': 'Reject',
      'common.close': '✕',
      'common.notification': 'Notification',
      'banner.codeUpdated': '🔄 Code updated',
      'banner.apply': 'Apply',
      'banner.waiting': 'Waiting...',
      'banner.reconnecting': '🔄 Reconnecting...',
    },
    'pt-BR': {
      'nav.products': 'PRODUTOS',
      'nav.activity': 'LOG DE ATIVIDADE',
      'nav.teamRoster': 'EQUIPE',
      'nav.ceoConsole': 'PAINEL DO CEO',
      'toolbar.settings': 'Configurações',
      'toolbar.newProduct': 'Novo Produto',
      'toolbar.importProduct': 'Importar Produto',
      'toolbar.exEmployeeWall': 'Mural de Ex-funcionários',
      'toolbar.companyCulture': 'Cultura da Empresa',
      'toolbar.companyDirection': 'Direção da Empresa',
      'toolbar.dashboard': 'Painel',
      'toolbar.announcements': 'Anúncios',
      'toolbar.doNotDisturb': 'Não Perturbe',
      'toolbar.backgroundTasks': 'Tarefas em Segundo Plano',
      'toolbar.exportScreenshot': 'Exportar captura SVG',
      'toolbar.stopAllTasks': 'Parar todas as tarefas',
      'toolbar.forceReload': 'Recarregar todos os dados do disco',
      'settings.title': '⚙ CONFIGURAÇÕES',
      'settings.languageLabel': 'Idioma',
      'settings.textSize': 'Tamanho do texto',
      'settings.apiConnections': '🔑 Conexões de API',
      'settings.systemCrons': '⏰ Tarefas agendadas',
      'settings.display': '👁 Exibição',
      'ceo.chat': '💬 Chat',
      'ceo.projects': 'Projetos',
      'ceo.oneOnOne': '1-a-1',
      'ceo.linkTaskToProduct': 'Vincular tarefa ao produto',
      'ceo.noProduct': 'Sem produto',
      'status.employeeCount': '👥 {count}',
      'status.toolCount': '🔧 {count}',
      'status.roomCount': '🏢 {free}/{total}',
      'announcements.title': '🔔 Anúncios',
      'announcements.loading': 'Carregando...',
      'meeting.roomTitle': '🏢 {name}',
      'meeting.minutesTitle': '📒 Atas da reunião: {name}',
      'meeting.oneononeTitle': '🎓 Reunião 1-a-1',
      'meeting.available': 'Disponível',
      'meeting.inMeeting': 'Em reunião',
      'meeting.capacity': '{count} pessoas',
      'meeting.participants': 'Participantes',
      'meeting.noParticipants': 'Nenhum participante',
      'meeting.liveLog': 'Registro ao vivo da reunião',
      'meeting.loading': 'Carregando...',
      'meeting.loadingMinutes': 'Carregando atas...',
      'meeting.noLogs': 'Sem registros da reunião',
      'meeting.noArchivedMeetings': 'Sem reuniões arquivadas',
      'meeting.failedLoadChat': 'Falha ao carregar o chat',
      'meeting.failedLoadMinutes': 'Falha ao carregar as atas',
      'meeting.notFound': 'Não encontrado',
      'meeting.backToList': 'Voltar para a lista',
      'meeting.summary': 'Resumo',
      'meeting.noData': 'Sem dados',
      'meeting.selectEmployee': 'Selecionar funcionário',
      'meeting.selectEmployeePlaceholder': '-- Selecione um funcionário --',
      'workflow.selectPrompt': '← Selecione um workflow para ver',
      'employee.detailsTitle': 'Detalhes do funcionário',
      'interview.title': '🎤 Entrevista',
      'toolList.title': '🛠 LISTA DE FERRAMENTAS',
      'product.detailTitle': 'Detalhe do produto',
      'traceViewer.title': 'VISUALIZADOR DE TRACE',
      'companyDirection.placeholder': 'ex.: Focamos em ferramentas criativas com IA para criadores independentes...',
      'companyCulture.placeholder': 'Adicione uma nova entrada de cultura...',
      'createProduct.namePlaceholder': 'ex.: OneManCompany官网',
      'createProduct.objectivePlaceholder': 'Objetivo do produto',
      'ceo.messagePlaceholder': '$ Digite uma mensagem, / para comandos (Enter para enviar)',
      'meeting.messagePlaceholder': 'Digite uma mensagem...',
      'onboarding.toggle': '▼',
      'candidate.selectedCount': '0 selecionados',
      'talentPool.sourceBadge': '',
      'common.approve': 'Aprovar',
      'common.reject': 'Rejeitar',
      'common.close': '✕',
      'common.notification': 'Notificação',
      'banner.codeUpdated': '🔄 Código atualizado',
      'banner.apply': 'Aplicar',
      'banner.waiting': 'Aguardando...',
      'banner.reconnecting': '🔄 Reconectando...',
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

  function format(template, vars = {}) {
    return String(template).replace(/\{(\w+)\}/g, (_, key) => (vars[key] == null ? `{${key}}` : String(vars[key])));
  }

  function t(key, fallback = '', vars = {}) {
    const lang = getLanguage();
    const template = TRANSLATIONS[lang]?.[key] || TRANSLATIONS[DEFAULT_LANGUAGE]?.[key] || fallback;
    return format(template, vars);
  }

  function getLanguages() {
    return LANGUAGES.slice();
  }

  function applyTo(root = document) {
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
    document.documentElement.lang = getLanguage();
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

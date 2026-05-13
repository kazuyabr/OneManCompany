from pathlib import Path

# Patch frontend/app.js with a few remaining visible strings.
app = Path('frontend/app.js')
s = app.read_text(encoding='utf-8')
repls = [
    ('        <span style="font-size:6px;color:var(--pixel-yellow);min-width:55px;">Agent Family</span>', '        <span style="font-size:6px;color:var(--pixel-yellow);min-width:55px;">${window.OMC_I18N?.t(\'employee.agentFamily\', \'Família do agente\') || \'Família do agente\'}</span>'),
    ('        <span style="font-size:6px;color:var(--pixel-yellow);min-width:55px;">Model</span>', '        <span style="font-size:6px;color:var(--pixel-yellow);min-width:55px;">${window.OMC_I18N?.t(\'employee.llmModelLabel\', \'Modelo LLM\') || \'Modelo LLM\'}</span>'),
    ('        <span style="font-size:6px;color:var(--pixel-yellow);min-width:55px;">Status</span>', '        <span style="font-size:6px;color:var(--pixel-yellow);min-width:55px;">${window.OMC_I18N?.t(\'settings.status\', \'Status\') || \'Status\'}</span>'),
    ('      ${sessions.length > 0 ? `<div style="font-size:5px;color:var(--text-dim);margin-top:2px;">${sessions.length} session(s)</div>` : \'' , '      ${sessions.length > 0 ? `<div style="font-size:5px;color:var(--text-dim);margin-top:2px;">${sessions.length} ${window.OMC_I18N?.t(\'common.sessions\', \'sessão(ões)\') || \'sessão(ões)\'}</div>` : \''),
    ("saveBtn.textContent = 'Save';", "saveBtn.textContent = window.OMC_I18N?.t('common.save', 'Salvar') || 'Salvar';"),
    ("keyStatus.textContent = data.api_key_set ? 'Authenticated' : 'No key';", "keyStatus.textContent = data.api_key_set ? window.OMC_I18N?.t('settings.connected', 'Conectado') || 'Conectado' : window.OMC_I18N?.t('settings.noKey', 'Sem chave') || 'Sem chave';"),
    ("keyInput.placeholder = data.api_key_set ? 'API Key set (update to change)' : 'Enter API Key...';", "keyInput.placeholder = data.api_key_set ? window.OMC_I18N?.t('settings.saved', 'Salvo') || 'Salvo' : window.OMC_I18N?.t('settings.apiKeyPlaceholder', '(nenhuma)') || '(nenhuma)';"),
    ("statusEl.textContent = `Sessions (${sessions.length}): ${labels}`;", "statusEl.textContent = `${window.OMC_I18N?.t('common.sessions', 'Sessões') || 'Sessões'} (${sessions.length}): ${labels}`;"),
    ("statusEl.textContent = t('settings.enterValue', 'On-demand (no active sessions)');", "statusEl.textContent = t('settings.enterValue', 'Sob demanda (sem sessões ativas)');"),
    ("keyStatus.textContent = t('settings.ok', 'Ready');", "keyStatus.textContent = t('settings.ok', 'Pronto');"),
    ("select.innerHTML = '<option value="">-- Use default model --</option>';", "select.innerHTML = `<option value=\"\">${window.OMC_I18N?.t('settings.selectModel', 'Usar modelo padrão') || 'Usar modelo padrão'}</option>`;"),
    ("statusEl.textContent = t('settings.errorLoading', 'Status unknown');", "statusEl.textContent = t('settings.errorLoading', 'Status desconhecido');"),
    ("<option value=\"\">${window.OMC_I18N?.t('common.loadFailed', 'Falha ao carregar') || 'Falha ao carregar'}</option>", "<option value=\"\">${window.OMC_I18N?.t('common.loadFailed', 'Falha ao carregar') || 'Falha ao carregar'}</option>"),
]
for old, new in repls:
    s = s.replace(old, new)
app.write_text(s, encoding='utf-8')

# Patch frontend/office.js for remaining visible English defaults.
office = Path('frontend/office.js')
s = office.read_text(encoding='utf-8')
repls = [
    ("const fullLabel = roomData.name || window.OMC_I18N?.t('office.meetingLabel', 'Reunião') || 'Reunião';", "const fullLabel = roomData.name || window.OMC_I18N?.t('office.meetingLabel', 'Reunião') || 'Reunião';"),
    ("ctx.fillText(`\u{1F4CB} ${window.OMC_I18N?.t('office.bulletinBoardLabel', 'Regras') || 'Regras'}`, bx + TILE * 1.5, by + TILE + 4);", "ctx.fillText(`\u{1F4CB} ${window.OMC_I18N?.t('office.bulletinBoardLabel', 'Regras') || 'Regras'}`, bx + TILE * 1.5, by + TILE + 4);")
]
for old, new in repls:
    s = s.replace(old, new)
office.write_text(s, encoding='utf-8')

# Patch frontend/index.html for a handful of remaining visible English labels.
html = Path('frontend/index.html')
s = html.read_text(encoding='utf-8')
s = s.replace('<aside id="roster-panel" aria-label="Team Roster" data-i18n-aria-label="nav.teamRoster">', '<aside id="roster-panel" aria-label="Equipe" data-i18n-aria-label="nav.teamRoster">')
s = s.replace('<textarea id="workflow-content" class="workflow-textarea hidden" rows="20" aria-label="Workflow content" data-i18n-aria-label="workflow.contentLabel"></textarea>', '<textarea id="workflow-content" class="workflow-textarea hidden" rows="20" aria-label="Conteúdo do workflow" data-i18n-aria-label="workflow.contentLabel"></textarea>')
html.write_text(s, encoding='utf-8')
print('patched frontend i18n round 3')

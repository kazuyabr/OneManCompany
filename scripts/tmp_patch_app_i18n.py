from pathlib import Path

p = Path('frontend/app.js')
s = p.read_text(encoding='utf-8')
replacements = [
    ("        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">Agent Family</span>", "        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">${window.OMC_I18N?.t('employee.agentFamily', 'Família do agente') || 'Família do agente'}</span>"),
    ("        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">Model</span>", "        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">${window.OMC_I18N?.t('employee.llmModelLabel', 'Modelo LLM') || 'Modelo LLM'}</span>"),
    ("        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">Status</span>", "        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">${window.OMC_I18N?.t('settings.status', 'Status') || 'Status'}</span>"),
    ("        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:45px;\">${window.OMC_I18N?.t('employee.providerLabel', 'Fornecedor') || 'Fornecedor'}</span>", "        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:45px;\">${window.OMC_I18N?.t('employee.providerLabel', 'Fornecedor') || 'Fornecedor'}</span>"),
    ("        <button id=\"emp-model-save-btn\" class=\"pixel-btn small\" disabled>${window.OMC_I18N?.t('common.save', 'Salvar') || 'Salvar'}</button>", "        <button id=\"emp-model-save-btn\" class=\"pixel-btn small\" disabled>${window.OMC_I18N?.t('common.save', 'Salvar') || 'Salvar'}</button>"),
    ("        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">${window.OMC_I18N?.t('employee.agentFamily', 'Família do agente') || 'Família do agente'}</span>", "        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">${window.OMC_I18N?.t('employee.agentFamily', 'Família do agente') || 'Família do agente'}</span>"),
    ("        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">${window.OMC_I18N?.t('employee.llmModelLabel', 'Modelo LLM') || 'Modelo LLM'}</span>", "        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">${window.OMC_I18N?.t('employee.llmModelLabel', 'Modelo LLM') || 'Modelo LLM'}</span>"),
    ("        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">${window.OMC_I18N?.t('settings.status', 'Status') || 'Status'}</span>", "        <span style=\"font-size:6px;color:var(--pixel-yellow);min-width:55px;\">${window.OMC_I18N?.t('settings.status', 'Status') || 'Status'}</span>"),
    ("      ${sessions.length > 0 ? `<div style=\"font-size:5px;color:var(--text-dim);margin-top:2px;\">${sessions.length} session(s)</div>` : ''}", "      ${sessions.length > 0 ? `<div style=\"font-size:5px;color:var(--text-dim);margin-top:2px;\">${sessions.length} ${window.OMC_I18N?.t('common.sessions', 'sessão(ões)') || 'sessão(ões)'}</div>` : ''}"),
    ("      saveBtn.textContent = 'Save';", "      saveBtn.textContent = window.OMC_I18N?.t('common.save', 'Salvar') || 'Salvar';"),
]
for old, new in replacements:
    s = s.replace(old, new)
p.write_text(s, encoding='utf-8')
print('patched')

from __future__ import annotations

import json
from pathlib import Path

BASE = Path('d:/Workspace/OneManCompany')


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8-sig'))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def update_json(path: Path, updates: dict[str, str]) -> None:
    data = load_json(path)
    changed = False
    for key, value in updates.items():
        if data.get(key) != value:
            data[key] = value
            changed = True
    if changed:
        save_json(path, data)
        print(f'[ok] {path}')
    else:
        print(f'[noop] {path}')


def replace_all(text: str, replacements: list[tuple[str, str]]) -> str:
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def update_text(path: Path, replacements: list[tuple[str, str]]) -> None:
    original = path.read_text(encoding='utf-8-sig')
    updated = replace_all(original, replacements)
    if updated != original:
        path.write_text(updated, encoding='utf-8')
        print(f'[ok] {path}')
    else:
        print(f'[noop] {path}')


en_updates = {
    'common.tasks': 'tasks',
    'employee.noWorkPrinciplesLabel': 'No work principles yet',
    'employee.noOneOnOneNotesLabel': 'No 1-on-1 notes yet',
    'employee.noLogsLabel': 'No logs',
    'employee.noWorkHistoryLabel': 'No work history',
    'employee.noScheduledJobsLabel': 'No scheduled jobs',
    'employee.scheduledJobsLabel': 'Scheduled Jobs',
    'employee.stopAllLabel': 'Stop All',
    'employee.projectHistoryLabel': 'Project History',
    'exEmployees.title': 'Ex-Employee Wall',
    'exEmployees.empty': 'No ex-employees',
    'exEmployees.loadFailed': 'Load failed',
    'exEmployees.rehireButton': '🔄 Rehire',
    'exEmployees.rehireConfirm': 'Confirm rehire {name}{nickname}? Will restart from Lv.1.',
    'exEmployees.rehireFailed': 'Rehire failed',
    'companyCulture.title': 'Company Culture',
    'companyCulture.empty': 'No culture entries yet. CEO can add above.',
    'companyCulture.failed': 'Failed to load culture.',
    'companyCulture.added': 'Company culture added',
    'companyCulture.removed': 'Company culture removed',
    'companyDirection.title': 'Company Direction',
    'companyDirection.saveFailed': 'Save failed',
    'companyDirection.updated': 'Company direction updated',
    'companyDirection.draftFirst': 'Please write a draft direction first.',
    'companyDirection.sending': '⏳ Sending...',
    'companyDirection.enrichFailed': 'Enrich failed',
    'companyDirection.taskSent': 'Direction polish task sent to EA',
    'companyDirection.enrichButton': '✨ Polish / Enrich',
    'office.companyRulesTooltip': 'Company Rules\nClick to view and edit workflows',
    'office.projectWallTooltip': 'Project Wall\nClick to view project history',
    'office.ceoTooltip': 'CEO (You)\nRole: Chief Executive\nInput tasks below',
    'office.employeeTooltipSkills': 'Skills:',
    'office.employeeTooltipPerformance': 'Performance:',
    'office.employeeTooltipNeedsSetup': '🔑 Needs API setup',
    'office.employeeTooltipApiOffline': '🔴 API offline',
    'office.employeeTooltipInMeeting': '📖 In 1-on-1 meeting...',
    'office.employeeTooltipClickDetails': '(Click for details)',
    'office.roomTooltipCapacity': 'Capacity:',
    'office.roomTooltipStatus': 'Status:',
    'office.roomStatusInUse': '🔴 In Use',
    'office.roomStatusAvailable': '🟢 Available',
    'office.roomTooltipParticipants': 'Participants:',
    'office.roomInUseBadge': 'IN USE',
    'office.bulletinBoardLabel': 'Rules',
    'office.projectWallLabel': 'Projects',
    'office.executiveLabel': 'Executive',
    'banner.applying': 'Applying...',
    'banner.waitingTasks': 'Waiting for tasks...',
}

pt_updates = {
    'common.tasks': 'tarefas',
    'employee.noWorkPrinciplesLabel': 'Nenhum princípio de trabalho ainda',
    'employee.noOneOnOneNotesLabel': 'Nenhuma nota de 1-pra-1 ainda',
    'employee.noLogsLabel': 'Sem logs',
    'employee.noWorkHistoryLabel': 'Sem histórico de trabalho',
    'employee.noScheduledJobsLabel': 'Nenhuma tarefa agendada',
    'employee.scheduledJobsLabel': 'Tarefas agendadas',
    'employee.stopAllLabel': 'Parar tudo',
    'employee.projectHistoryLabel': 'Histórico de projetos',
    'exEmployees.title': 'Mural de Ex-funcionários',
    'exEmployees.empty': 'Nenhum ex-funcionário',
    'exEmployees.loadFailed': 'Falha ao carregar',
    'exEmployees.rehireButton': '🔄 Recontratar',
    'exEmployees.rehireConfirm': 'Confirmar recontratação de {name}{nickname}? Isso vai reiniciar a partir do Lv.1.',
    'exEmployees.rehireFailed': 'Falha na recontratação',
    'companyCulture.title': 'Cultura da Empresa',
    'companyCulture.empty': 'Ainda não há entradas de cultura. O CEO pode adicionar acima.',
    'companyCulture.failed': 'Falha ao carregar a cultura.',
    'companyCulture.added': 'Cultura da empresa adicionada',
    'companyCulture.removed': 'Cultura da empresa removida',
    'companyDirection.title': 'Direção da Empresa',
    'companyDirection.saveFailed': 'Falha ao salvar',
    'companyDirection.updated': 'Direção da empresa atualizada',
    'companyDirection.draftFirst': 'Escreva primeiro um rascunho da direção.',
    'companyDirection.sending': '⏳ Enviando...',
    'companyDirection.enrichFailed': 'Falha ao enriquecer',
    'companyDirection.taskSent': 'Tarefa de polimento da direção enviada para EA',
    'companyDirection.enrichButton': '✨ Polir / enriquecer',
    'office.companyRulesTooltip': 'Regras da empresa\nClique para ver e editar workflows',
    'office.projectWallTooltip': 'Mural de projetos\nClique para ver o histórico de projetos',
    'office.ceoTooltip': 'CEO (Você)\nFunção: Chief Executive\nInsira tarefas abaixo',
    'office.employeeTooltipSkills': 'Habilidades:',
    'office.employeeTooltipPerformance': 'Desempenho:',
    'office.employeeTooltipNeedsSetup': '🔑 Precisa de configuração de API',
    'office.employeeTooltipApiOffline': '🔴 API offline',
    'office.employeeTooltipInMeeting': '📖 Em reunião 1-pra-1...',
    'office.employeeTooltipClickDetails': '(Clique para detalhes)',
    'office.roomTooltipCapacity': 'Capacidade:',
    'office.roomTooltipStatus': 'Status:',
    'office.roomStatusInUse': '🔴 Em uso',
    'office.roomStatusAvailable': '🟢 Disponível',
    'office.roomTooltipParticipants': 'Participantes:',
    'office.roomInUseBadge': 'EM USO',
    'office.bulletinBoardLabel': 'Regras',
    'office.projectWallLabel': 'Projetos',
    'office.executiveLabel': 'Executivo',
    'banner.applying': 'Aplicando...',
    'banner.waitingTasks': 'Aguardando tarefas...',
}

update_json(BASE / 'frontend/i18n/en.json', en_updates)
update_json(BASE / 'frontend/i18n/pt-BR.json', pt_updates)

update_text(BASE / 'frontend/index.html', [
    ('<h3 class="pixel-title">&#128220; Mural de ex-funcionários</h3>', '<h3 class="pixel-title" data-i18n="exEmployees.title">&#128220; Ex-Employee Wall</h3>'),
    ('<h3 class="pixel-title">&#127988; Cultura da Empresa</h3>', '<h3 class="pixel-title" data-i18n="companyCulture.title">&#127988; Company Culture</h3>'),
    ('<button id="company-culture-add-btn" class="pixel-btn">&#10010; Add</button>', '<button id="company-culture-add-btn" class="pixel-btn" data-i18n="common.add">&#10010; Add</button>'),
    ('<h3 class="pixel-title" data-i18n="toolbar.companyDirection">&#127919; Company Direction</h3>', '<h3 class="pixel-title" data-i18n="companyDirection.title">&#127919; Company Direction</h3>'),
    ('<button id="company-direction-enrich-btn" class="pixel-btn secondary" onclick="app.enrichCompanyDirection()">&#10024; Polir / enriquecer</button>', '<button id="company-direction-enrich-btn" class="pixel-btn secondary" onclick="app.enrichCompanyDirection()" data-i18n="companyDirection.enrichButton">&#10024; Polish / Enrich</button>'),
])

update_text(BASE / 'frontend/app.js', [
    ("      btn.textContent = window.OMC_I18N?.t('banner.applying', 'Applying...') || 'Applying...';", "      btn.textContent = window.OMC_I18N?.t('banner.applying', 'Applying...') || 'Applying...';"),
    ("            btn.textContent = window.OMC_I18N?.t('banner.waitingTasks', 'Waiting for tasks...') || 'Waiting for tasks...';", "            btn.textContent = window.OMC_I18N?.t('banner.waitingTasks', 'Waiting for tasks...') || 'Waiting for tasks...';"),
    ("        listEl.innerHTML = `<div style=\"color:var(--pixel-red);font-size:7px;\">${t('exEmployees.loadFailed', 'Load failed')}: ${this._escHtml(err.message)}</div>`;", "        listEl.innerHTML = `<div style=\"color:var(--pixel-red);font-size:7px;\">${t('exEmployees.loadFailed', 'Load failed')}: ${this._escHtml(err.message)}</div>`;"),
    ("        <button class=\"pixel-btn small rehire-btn\" data-id=\"${emp.id}\">${t('exEmployees.rehireButton', '🔄 Rehire')}</button>", "        <button class=\"pixel-btn small rehire-btn\" data-id=\"${emp.id}\">${t('exEmployees.rehireButton', '🔄 Rehire')}</button>"),
    ("    if (!confirm(t('exEmployees.rehireConfirm', 'Confirm rehire {name}{nickname}? Will restart from Lv.1.', { name: emp.name, nickname: emp.nickname ? `(${emp.nickname})` : '' }))) return;", "    if (!confirm(t('exEmployees.rehireConfirm', 'Confirm rehire {name}{nickname}? Will restart from Lv.1.', { name: emp.name, nickname: emp.nickname ? `(${emp.nickname})` : '' }))) return;"),
    ("          this.logEntry('SYSTEM', `${t('exEmployees.rehireFailed', 'Rehire failed')}: ${data.error}`, 'system');", "          this.logEntry('SYSTEM', `${t('exEmployees.rehireFailed', 'Rehire failed')}: ${data.error}`, 'system');"),
    ("        if (data.error) {\n          this.logEntry('SYSTEM', `${t('common.add', 'Add')} failed: ${data.error}`, 'system');\n        } else {\n          this.logEntry('CEO', `${t('companyCulture.added', 'Company culture added')}: ${content.slice(0, 40)}`, 'ceo');", "        if (data.error) {\n          this.logEntry('SYSTEM', `${t('common.add', 'Add')} failed: ${data.error}`, 'system');\n        } else {\n          this.logEntry('CEO', `${t('companyCulture.added', 'Company culture added')}: ${content.slice(0, 40)}`, 'ceo');"),
    ("          this.logEntry('CEO', `${t('companyCulture.removed', 'Company culture removed')}: ${data.removed?.content?.slice(0, 40) || ''}`, 'ceo');", "          this.logEntry('CEO', `${t('companyCulture.removed', 'Company culture removed')}: ${data.removed?.content?.slice(0, 40) || ''}`, 'ceo');"),
    ("          this.logEntry('SYSTEM', `${t('companyDirection.saveFailed', 'Save failed')}: ${data.error}`, 'system');", "          this.logEntry('SYSTEM', `${t('companyDirection.saveFailed', 'Save failed')}: ${data.error}`, 'system');"),
    ("          this.logEntry('CEO', t('companyDirection.updated', 'Company direction updated'), 'ceo');", "          this.logEntry('CEO', t('companyDirection.updated', 'Company direction updated'), 'ceo');"),
    ("      this.logEntry('SYSTEM', t('companyDirection.draftFirst', 'Please write a draft direction first.'), 'system');", "      this.logEntry('SYSTEM', t('companyDirection.draftFirst', 'Please write a draft direction first.'), 'system');"),
    ("    btn.textContent = t('companyDirection.sending', '⏳ Sending...');", "    btn.textContent = t('companyDirection.sending', '⏳ Sending...');"),
    ("          this.logEntry('SYSTEM', `${t('companyDirection.enrichFailed', 'Enrich failed')}: ${data.error}`, 'system');", "          this.logEntry('SYSTEM', `${t('companyDirection.enrichFailed', 'Enrich failed')}: ${data.error}`, 'system');"),
    ("          this.logEntry('CEO', t('companyDirection.taskSent', 'Direction polish task sent to EA'), 'ceo');", "          this.logEntry('CEO', t('companyDirection.taskSent', 'Direction polish task sent to EA'), 'ceo');"),
    ("        btn.innerHTML = t('companyDirection.enrichButton', '&#10024; Polish / Enrich');", "        btn.innerHTML = t('companyDirection.enrichButton', '✨ Polish / Enrich');"),
])

update_text(BASE / 'frontend/office.js', [
    ("    ctx.fillText('\\u{1F4CB} Rules', bx + TILE * 1.5, by + TILE + 4);", "    ctx.fillText(`\\u{1F4CB} ${window.OMC_I18N?.t('office.bulletinBoardLabel', 'Rules') || 'Rules'}`, bx + TILE * 1.5, by + TILE + 4);") ,
    ("    ctx.fillText('\\u{1F4CA} Projects', bx + TILE * 1.5, by + TILE + 4);", "    ctx.fillText(`\\u{1F4CA} ${window.OMC_I18N?.t('office.projectWallLabel', 'Projects') || 'Projects'}`, bx + TILE * 1.5, by + TILE + 4);") ,
    ("      tooltipText = '📋 Company Rules\\nClick to view and edit workflows';", "      tooltipText = window.OMC_I18N?.t('office.companyRulesTooltip', 'Company Rules\\nClick to view and edit workflows');"),
    ("      tooltipText = '📋 Project Wall\\nClick to view project history';", "      tooltipText = window.OMC_I18N?.t('office.projectWallTooltip', 'Project Wall\\nClick to view project history');"),
    ("      tooltipText = 'CEO (You)\\nRole: Chief Executive\\nInput tasks below';", "      tooltipText = window.OMC_I18N?.t('office.ceoTooltip', 'CEO (You)\\nRole: Chief Executive\\nInput tasks below');"),
    ("        tooltipText = `${emp.name}${nn}\\n${title}\\nSkills: ${(emp.skills || []).join(', ')}\\nPerformance: ${latestScore}`;", "        tooltipText = `${emp.name}${nn}\\n${title}\\n${window.OMC_I18N?.t('office.employeeTooltipSkills', 'Skills:')} ${(emp.skills || []).join(', ')}\\n${window.OMC_I18N?.t('office.employeeTooltipPerformance', 'Performance:')} ${latestScore}`;"),
    ("        if (emp.needs_setup) tooltipText += '\\n🔑 Needs API setup';", "        if (emp.needs_setup) tooltipText += `\\n${window.OMC_I18N?.t('office.employeeTooltipNeedsSetup', '🔑 Needs API setup')}`;"),
    ("        else if (emp.api_online === false) tooltipText += '\\n🔴 API offline';", "        else if (emp.api_online === false) tooltipText += `\\n${window.OMC_I18N?.t('office.employeeTooltipApiOffline', '🔴 API offline')}`;"),
    ("        if (emp.is_listening) tooltipText += '\\n📖 In 1-on-1 meeting...';", "        if (emp.is_listening) tooltipText += `\\n${window.OMC_I18N?.t('office.employeeTooltipInMeeting', '📖 In 1-on-1 meeting...')}`;"),
    ("        tooltipText += '\\n\\n(Click for details)';", "        tooltipText += `\\n\\n${window.OMC_I18N?.t('office.employeeTooltipClickDetails', '(Click for details)')}`;"),
    ("        const status = room.is_booked ? '🔴 In Use' : '🟢 Available';", "        const status = room.is_booked ? window.OMC_I18N?.t('office.roomStatusInUse', '🔴 In Use') : window.OMC_I18N?.t('office.roomStatusAvailable', '🟢 Available');"),
    ("        tooltipText = `🏢 ${room.name}\\n${room.description}\\nCapacity: ${room.capacity}\\nStatus: ${status}`;", "        tooltipText = `🏢 ${room.name}\\n${room.description}\\n${window.OMC_I18N?.t('office.roomTooltipCapacity', 'Capacity:')} ${room.capacity}\\n${window.OMC_I18N?.t('office.roomTooltipStatus', 'Status:')} ${status}`;"),
    ("          tooltipText += `\\nParticipants: ${room.participants.join(', ')}`;", "          tooltipText += `\\n${window.OMC_I18N?.t('office.roomTooltipParticipants', 'Participants:')} ${room.participants.join(', ')}`;"),
    ("      this._rect(px + TILE - 4, py - 6, 10, 10, statusColor);", "      this._rect(px + TILE - 4, py - 6, 10, 10, statusColor);") ,
    ("      ctx.fillText('IN USE', px + TILE, ly + 8 + lines.length * lineH);", "      ctx.fillText(window.OMC_I18N?.t('office.roomInUseBadge', 'IN USE'), px + TILE, ly + 8 + lines.length * lineH);") ,
])

print('[done]')

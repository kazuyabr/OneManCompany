from __future__ import annotations

import json
from pathlib import Path

ROOT = Path('d:/Workspace/OneManCompany')


def patch_json(path: Path, updates: dict[str, str]) -> None:
    data = json.loads(path.read_text(encoding='utf-8'))
    data.update(updates)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def replace(text: str, old: str, new: str) -> tuple[str, bool]:
    if old in text:
        return text.replace(old, new), True
    return text, False


patch_json(ROOT / 'frontend/i18n/en.json', {
    'candidate.selectHint': '0 selected — click cards to select',
    'candidate.remoteInterviewOnly': 'For security reasons, only remote (self-hosted) employees support interview',
    'candidate.invalidCvJson': 'Invalid JSON in CV field.',
    'candidate.recruiting': 'RECRUITING...',
    'common.sessions': 'sessions',
    'common.showMore': 'Show more',
    'common.showLess': 'Show less',
    'common.details': 'Details',
    'common.export': 'Export',
    'common.reopen': 'Reopen',
    'common.login': 'Login',
    'common.hiring': 'Hiring...',
    'common.submitting': 'Submitting...',
    'common.stopping': 'Stopping...',
    'common.confirm': 'Confirm',
    'common.autoConfirmIn': 'Auto-confirm in {seconds}s',
    'common.hire': 'Hire',
    'meeting.sessionStarted': '{type} meeting started in {room}. Participants: {participants}',
    'meeting.allHandsModeInstruction': 'All-Hands mode: Send your address. Employees will absorb silently.',
    'meeting.discussionModeInstruction': 'Discussion mode: Send a message to start discussion. Employees will compete to respond.',
    'oauth.openLoginPage': 'Click here to open login page',
    'oauth.authorizing': 'Authorizing... login will complete automatically.',
    'product.startPlanning': 'Start Planning',
    'product.activate': 'Activate Product',
    'product.versionHistory': 'Version History',
    'product.releaseVersion': '+ Release Version',
    'product.newIssue': '+ New Issue',
    'product.reviews': 'Reviews',
    'product.createReview': '+ Create Review',
    'product.reviewCreated': 'Review created',
    'product.noReviewsYet': 'No reviews yet.',
    'product.noSprintsYet': 'No sprints yet. Click "+ New Sprint" to plan your first sprint.',
    'product.selectIssuesForRelease': 'Select issues to include in release ({count} done):',
    'product.bumpLabel': 'Bump:',
    'product.noSprint': 'No Sprint',
    'product.sprintLabel': 'Sprint: ',
    'product.assigneeLabel': 'Assignee: ',
    'product.linksTitle': 'Links',
    'product.noLinks': 'No links',
    'product.removeLink': 'Remove link',
    'product.add': 'Add',
    'product.sprints': 'Sprints',
    'product.edit': 'Edit',
    'product.start': 'Start',
    'product.close': 'Close',
    'product.releases': 'Releases',
    'product.milestonedIssues': 'Milestoned Issues',
    'product.issuesResolved': '{count} issues resolved',
    'product.suggestedCapacity': '(suggested: {capacity} pts)',
    'product.owner': 'Product owner',
    'product.detail': 'Product detail',
    'traceViewer.loading': 'Loading trace...',
})

patch_json(ROOT / 'frontend/i18n/pt-BR.json', {
    'candidate.selectHint': '0 selecionados — clique nos cards para selecionar',
    'candidate.remoteInterviewOnly': 'Por segurança, apenas funcionários remotos (self-hosted) suportam entrevista',
    'candidate.invalidCvJson': 'JSON inválido no campo de CV.',
    'candidate.recruiting': 'RECRUTANDO...',
    'common.sessions': 'sessões',
    'common.showMore': 'Mostrar mais',
    'common.showLess': 'Mostrar menos',
    'common.details': 'Detalhes',
    'common.export': 'Exportar',
    'common.reopen': 'Reabrir',
    'common.login': 'Entrar',
    'common.hiring': 'Contratando...',
    'common.submitting': 'Enviando...',
    'common.stopping': 'Parando...',
    'common.confirm': 'Confirmar',
    'common.autoConfirmIn': 'Auto-confirmar em {seconds}s',
    'common.hire': 'Contratar',
    'meeting.sessionStarted': 'Reunião {type} iniciada em {room}. Participantes: {participants}',
    'meeting.allHandsModeInstruction': 'Modo All-Hands: envie seu pronunciamento. Os funcionários vão absorver em silêncio.',
    'meeting.discussionModeInstruction': 'Modo de discussão: envie uma mensagem para iniciar a conversa. Os funcionários vão competir para responder.',
    'oauth.openLoginPage': 'Clique aqui para abrir a página de login',
    'oauth.authorizing': 'Autorizando... o login será concluído automaticamente.',
    'product.startPlanning': 'Iniciar planejamento',
    'product.activate': 'Ativar produto',
    'product.versionHistory': 'Histórico de versões',
    'product.releaseVersion': '+ Liberar versão',
    'product.newIssue': '+ Nova issue',
    'product.reviews': 'Revisões',
    'product.createReview': '+ Criar revisão',
    'product.reviewCreated': 'Revisão criada',
    'product.noReviewsYet': 'Ainda não há revisões.',
    'product.noSprintsYet': 'Ainda não há sprints. Clique em "+ New Sprint" para planejar a primeira sprint.',
    'product.selectIssuesForRelease': 'Selecione as issues para incluir no release ({count} concluídas):',
    'product.bumpLabel': 'Impulsionar:',
    'product.noSprint': 'Sem sprint',
    'product.sprintLabel': 'Sprint: ',
    'product.assigneeLabel': 'Responsável: ',
    'product.linksTitle': 'Links',
    'product.noLinks': 'Sem links',
    'product.removeLink': 'Remover link',
    'product.add': 'Adicionar',
    'product.sprints': 'Sprints',
    'product.edit': 'Editar',
    'product.start': 'Iniciar',
    'product.close': 'Fechar',
    'product.releases': 'Releases',
    'product.milestonedIssues': 'Issues com milestone',
    'product.issuesResolved': '{count} issues resolvidas',
    'product.suggestedCapacity': '(sugerido: {capacity} pts)',
    'product.owner': 'Dono do produto',
    'product.detail': 'Detalhe do produto',
    'traceViewer.loading': 'Carregando trace...',
})

app = ROOT / 'frontend/app.js'
text = app.read_text(encoding='utf-8')
repls = [
    ("    const typeLabel = meetingType === 'all_hands' ? 'All-Hands' : 'Discussion';", "    const typeLabel = meetingType === 'all_hands'\n      ? window.OMC_I18N?.t('meeting.type.allHands', 'All-Hands') || 'All-Hands'\n      : window.OMC_I18N?.t('meeting.type.discussion', 'Discussion') || 'Discussion';"),
    ("    this._addOneononeSystemMsg(`${typeLabel} meeting started in ${res.room_name}. Participants: ${participantNames}`);", "    this._addOneononeSystemMsg(window.OMC_I18N?.t('meeting.sessionStarted', '{type} meeting started in {room}. Participants: {participants}', { type: typeLabel, room: res.room_name, participants: participantNames }) || `${typeLabel} meeting started in ${res.room_name}. Participants: ${participantNames}`);"),
    ("      this._addOneononeSystemMsg('All-Hands mode: Send your address. Employees will absorb silently.');", "      this._addOneononeSystemMsg(window.OMC_I18N?.t('meeting.allHandsModeInstruction', 'All-Hands mode: Send your address. Employees will absorb silently.') || 'All-Hands mode: Send your address. Employees will absorb silently.');"),
    ("      this._addOneononeSystemMsg('Discussion mode: Send a message to start discussion. Employees will compete to respond.');", "      this._addOneononeSystemMsg(window.OMC_I18N?.t('meeting.discussionModeInstruction', 'Discussion mode: Send a message to start discussion. Employees will compete to respond.') || 'Discussion mode: Send a message to start discussion. Employees will compete to respond.');"),
    ("      talentPoolBtn.textContent = '📋 Talent Pool';", "      talentPoolBtn.textContent = window.OMC_I18N?.t('talentPool.title', '💼 Talent Pool') || '💼 Talent Pool';"),
    ("    metaEl.textContent = 'loading...';", "    metaEl.textContent = window.OMC_I18N?.t('common.loading', 'Loading...') || 'Loading...';"),
    ("        this.logEntry('SYSTEM', 'Invalid JSON in CV field.', 'system');", "        this.logEntry('SYSTEM', window.OMC_I18N?.t('candidate.invalidCvJson', 'Invalid JSON in CV field.') || 'Invalid JSON in CV field.', 'system');"),
    ("      btn.textContent = 'Hiring...';", "      btn.textContent = window.OMC_I18N?.t('common.hiring', 'Hiring...') || 'Hiring...';"),
    ("      .finally(() => { btn.disabled = false; btn.textContent = 'Login'; });", "      .finally(() => { btn.disabled = false; btn.textContent = window.OMC_I18N?.t('common.login', 'Login') || 'Login'; });"),
    ("        detailBtn.textContent = '📋 Details';", "        detailBtn.textContent = window.OMC_I18N?.t('common.details', 'Details') || 'Details';"),
    ("      newInterviewBtn.title = 'For security reasons, only remote (self-hosted) employees support interview';", "      newInterviewBtn.title = window.OMC_I18N?.t('candidate.remoteInterviewOnly', 'For security reasons, only remote (self-hosted) employees support interview') || 'For security reasons, only remote (self-hosted) employees support interview';"),
    ("      newSelectBtn.textContent = nowSelected ? '✗ Deselect' : '✔ Select';", "      newSelectBtn.textContent = nowSelected ? '✗ Deselect' : window.OMC_I18N?.t('candidate.select', '✔ Select') || '✔ Select';"),
    ("      countEl.textContent = `${count} selected`;", "      countEl.textContent = window.OMC_I18N?.t('candidate.batchSelected', '{count} selected', { count }) || `${count} selected`;"),
    ("      btn.textContent = `RECRUIT PARTY (${count})`;", "      btn.textContent = window.OMC_I18N?.t('candidate.batchRecruit', 'RECRUIT PARTY ({count})', { count }) || `RECRUIT PARTY (${count})`;"),
    ("      countEl.textContent = '0 selected — click cards to select';", "      countEl.textContent = window.OMC_I18N?.t('candidate.selectHint', '0 selected — click cards to select') || '0 selected — click cards to select';"),
    ("      btn.textContent = 'RECRUIT PARTY (0)';", "      btn.textContent = window.OMC_I18N?.t('candidate.batchRecruit', 'RECRUIT PARTY ({count})', { count: 0 }) || 'RECRUIT PARTY (0)';"),
    ("    btn.textContent = 'RECRUITING...';", "    btn.textContent = window.OMC_I18N?.t('candidate.recruiting', 'RECRUITING...') || 'RECRUITING...';"),
    ("    document.querySelectorAll('.pixel-btn.hire').forEach(b => { b.disabled = true; b.textContent = 'Hiring...'; });", "    document.querySelectorAll('.pixel-btn.hire').forEach(b => { b.disabled = true; b.textContent = window.OMC_I18N?.t('common.hiring', 'Hiring...') || 'Hiring...'; });"),
    ("          document.querySelectorAll('.pixel-btn.hire').forEach(b => { b.disabled = false; b.textContent = 'Hire'; });", "          document.querySelectorAll('.pixel-btn.hire').forEach(b => { b.disabled = false; b.textContent = window.OMC_I18N?.t('common.hire', 'Hire') || 'Hire'; });"),
    ("      cancelBtn.textContent = 'Cancel';", "      cancelBtn.textContent = window.OMC_I18N?.t('common.cancel', 'Cancel') || 'Cancel';"),
    ("      statusText.textContent = 'In Meeting';", "      statusText.textContent = window.OMC_I18N?.t('meeting.inMeeting', 'In Meeting') || 'In Meeting';"),
    ("      statusText.textContent = 'Available';", "      statusText.textContent = window.OMC_I18N?.t('meeting.available', 'Available') || 'Available';"),
    ("      if (resultEl) { resultEl.textContent = 'Error'; resultEl.className = 'api-test-result fail'; }", "      if (resultEl) { resultEl.textContent = window.OMC_I18N?.t('settings.errorLoading', 'Error loading') || 'Error loading'; resultEl.className = 'api-test-result fail'; }"),
    ("        if (resultEl) { resultEl.textContent = 'OK'; resultEl.className = 'api-test-result success'; }", "        if (resultEl) { resultEl.textContent = window.OMC_I18N?.t('settings.ok', 'OK') || 'OK'; resultEl.className = 'api-test-result success'; }"),
    ("        if (resultEl) { resultEl.textContent = 'FAIL'; resultEl.className = 'api-test-result fail'; }", "        if (resultEl) { resultEl.textContent = window.OMC_I18N?.t('settings.fail', 'FAIL') || 'FAIL'; resultEl.className = 'api-test-result fail'; }"),
    ("      if (resultEl) { resultEl.textContent = 'ERR'; resultEl.className = 'api-test-result fail'; }", "      if (resultEl) { resultEl.textContent = window.OMC_I18N?.t('settings.err', 'ERR') || 'ERR'; resultEl.className = 'api-test-result fail'; }"),
    ("      if (resultEl) resultEl.textContent = 'Waiting for code...';", "      if (resultEl) resultEl.textContent = window.OMC_I18N?.t('oauth.waitingForCode', 'Waiting for code...');"),
    ("      countdownEl.textContent = `Auto-confirm in ${remaining}s`;", "      countdownEl.textContent = window.OMC_I18N?.t('common.autoConfirmIn', 'Auto-confirm in {seconds}s', { seconds: remaining }) || `Auto-confirm in ${remaining}s`;"),
    ("      planBtn.textContent = 'Start Planning';", "      planBtn.textContent = window.OMC_I18N?.t('product.startPlanning', 'Start Planning') || 'Start Planning';"),
    ("      activateBtn.textContent = 'Activate Product';", "      activateBtn.textContent = window.OMC_I18N?.t('product.activate', 'Activate Product') || 'Activate Product';"),
    ("    exportBtn.textContent = 'Export';", "    exportBtn.textContent = window.OMC_I18N?.t('common.export', 'Export') || 'Export';"),
    ("    objLabel.textContent = 'Objective';", "    objLabel.textContent = window.OMC_I18N?.t('createProduct.objectiveLabel', 'Objective') || 'Objective';"),
    ("    ownerLabel.textContent = 'Owner';", "    ownerLabel.textContent = window.OMC_I18N?.t('createProduct.ownerLabel', 'Owner') || 'Owner';"),
    ("    krLabel.textContent = 'Key Results';", "    krLabel.textContent = window.OMC_I18N?.t('createProduct.keyResultsLabel', 'Key Results') || 'Key Results';"),
    ("    verLabel.textContent = 'Version History';", "    verLabel.textContent = window.OMC_I18N?.t('product.versionHistory', 'Version History') || 'Version History';"),
    ("    addKrBtn.textContent = '+ Add KR';", "    addKrBtn.textContent = window.OMC_I18N?.t('createProduct.addKr', '+ Add KR') || '+ Add KR';"),
    ("    releaseBtn.textContent = '+ Release Version';", "    releaseBtn.textContent = window.OMC_I18N?.t('product.releaseVersion', '+ Release Version') || '+ Release Version';"),
    ("    newBtn.textContent = '+ New Issue';", "    newBtn.textContent = window.OMC_I18N?.t('product.newIssue', '+ New Issue') || '+ New Issue';"),
    ("    actionBtn.textContent = 'Reopen';", "    actionBtn.textContent = window.OMC_I18N?.t('common.reopen', 'Reopen') || 'Reopen';"),
    ("      actionBtn.textContent = 'Close';", "      actionBtn.textContent = window.OMC_I18N?.t('common.closeText', 'Close') || 'Close';"),
    ("    sprintRow.textContent = 'Sprint: ';", "    sprintRow.textContent = window.OMC_I18N?.t('product.sprintLabel', 'Sprint: ') || 'Sprint: ';"),
    ("    sprintSel.innerHTML = '<option value="">No Sprint</option>';", "    sprintSel.innerHTML = `<option value=\"\">${window.OMC_I18N?.t('product.noSprint', 'No Sprint') || 'No Sprint'}</option>`;"),
    ("    assignRow.textContent = 'Assignee: ';", "    assignRow.textContent = window.OMC_I18N?.t('product.assigneeLabel', 'Assignee: ') || 'Assignee: ';"),
    ("    title.textContent = 'Links';", "    title.textContent = window.OMC_I18N?.t('product.linksTitle', 'Links') || 'Links';"),
    ("      empty.textContent = 'No links';", "      empty.textContent = window.OMC_I18N?.t('product.noLinks', 'No links') || 'No links';"),
    ("        removeBtn.title = 'Remove link';", "        removeBtn.title = window.OMC_I18N?.t('product.removeLink', 'Remove link') || 'Remove link';"),
    ("    saveBtn.textContent = 'Add';", "    saveBtn.textContent = window.OMC_I18N?.t('product.add', 'Add') || 'Add';"),
    ("          h.textContent = 'Sprints';", "          h.textContent = window.OMC_I18N?.t('product.sprints', 'Sprints') || 'Sprints';"),
    ("          newBtn.textContent = '+ New Sprint';", "          newBtn.textContent = window.OMC_I18N?.t('product.newSprint', '+ New Sprint') || '+ New Sprint';"),
    ("            empty.textContent = 'No sprints yet. Click \"+ New Sprint\" to plan your first sprint.';", "            empty.textContent = window.OMC_I18N?.t('product.noSprintsYet', 'No sprints yet. Click \"+ New Sprint\" to plan your first sprint.') || 'No sprints yet. Click \"+ New Sprint\" to plan your first sprint.';"),
    ("              editBtn.textContent = 'Edit';", "              editBtn.textContent = window.OMC_I18N?.t('product.edit', 'Edit') || 'Edit';"),
    ("              startBtn.textContent = 'Start';", "              startBtn.textContent = window.OMC_I18N?.t('product.start', 'Start') || 'Start';"),
    ("              closeBtn.textContent = 'Close';", "              closeBtn.textContent = window.OMC_I18N?.t('common.closeText', 'Close') || 'Close';"),
    ("          h.textContent = 'Releases';", "          h.textContent = window.OMC_I18N?.t('product.releases', 'Releases') || 'Releases';"),
    ("          count.textContent = `${v.resolved_count} issues resolved`;", "          count.textContent = window.OMC_I18N?.t('product.issuesResolved', '{count} issues resolved', { count: v.resolved_count }) || `${v.resolved_count} issues resolved`;"),
    ("          h.textContent = 'Milestoned Issues';", "          h.textContent = window.OMC_I18N?.t('product.milestonedIssues', 'Milestoned Issues') || 'Milestoned Issues';"),
    ("          hint.textContent = `(suggested: ${d.suggested_capacity} pts)`;", "          hint.textContent = window.OMC_I18N?.t('product.suggestedCapacity', '(suggested: {capacity} pts)', { capacity: d.suggested_capacity }) || `(suggested: ${d.suggested_capacity} pts)`;"),
    ("    createBtn.textContent = '+ Create Review';", "    createBtn.textContent = window.OMC_I18N?.t('product.createReview', '+ Create Review') || '+ Create Review';"),
    ("        this._showToast('Review created', 'success');", "        this._showToast(window.OMC_I18N?.t('product.reviewCreated', 'Review created') || 'Review created', 'success');"),
    ("      emptyMsg.textContent = 'No reviews yet.';", "      emptyMsg.textContent = window.OMC_I18N?.t('product.noReviewsYet', 'No reviews yet.') || 'No reviews yet.';"),
    ("        label.textContent = `Select issues to include in release (${doneIssues.length} done):`;", "        label.textContent = window.OMC_I18N?.t('product.selectIssuesForRelease', 'Select issues to include in release ({count} done):', { count: doneIssues.length }) || `Select issues to include in release (${doneIssues.length} done):`;"),
    ("        bumpLabel.textContent = 'Bump:';", "        bumpLabel.textContent = window.OMC_I18N?.t('product.bumpLabel', 'Bump:') || 'Bump:';"),
    ("        releaseBtn.textContent = 'Release';", "        releaseBtn.textContent = window.OMC_I18N?.t('product.releaseVersion', '+ Release Version') || 'Release';"),
    ("            ownerEl.title = 'Product owner';", "            ownerEl.title = window.OMC_I18N?.t('product.owner', 'Product owner') || 'Product owner';"),
    ("          detailBtn.textContent = '📋 Details';", "          detailBtn.textContent = window.OMC_I18N?.t('common.details', 'Details') || 'Details';"),
    ("          detailBtn.title = 'Product detail';", "          detailBtn.title = window.OMC_I18N?.t('product.detail', 'Product detail') || 'Product detail';"),
    ("        if (!confirm('Stop this background task?')) return;", "        if (!confirm(window.OMC_I18N?.t('common.confirm', 'Confirm') || 'Confirm')) return;"),
    ("        stopBtn.textContent = 'STOPPING...';", "        stopBtn.textContent = window.OMC_I18N?.t('common.stopping', 'Stopping...') || 'Stopping...';"),
    ("      if (btn) { btn.disabled = true; btn.textContent = '⏳ Submitting...'; }", "      if (btn) { btn.disabled = true; btn.textContent = window.OMC_I18N?.t('common.submitting', 'Submitting...') || 'Submitting...'; }"),
    ("          if (btn) { btn.disabled = false; btn.textContent = '▶ Continue Current Iteration'; }", "          if (btn) { btn.disabled = false; btn.textContent = window.OMC_I18N?.t('common.continueCurrentIteration', '▶ Continue Current Iteration') || '▶ Continue Current Iteration'; }"),
    ("        if (btn) { btn.disabled = false; btn.textContent = '▶ Continue Current Iteration'; }", "        if (btn) { btn.disabled = false; btn.textContent = window.OMC_I18N?.t('common.continueCurrentIteration', '▶ Continue Current Iteration') || '▶ Continue Current Iteration'; }"),
    ("        this.logEntry('CEO', `Continue failed: ${data.error}`, 'error');", "        this.logEntry('CEO', `${window.OMC_I18N?.t('common.errorLoading', 'Error loading') || 'Error loading'}: ${data.error}`, 'error');"),
    ("        this.logEntry('CEO', `Continue failed: ${err.message}`, 'error');", "        this.logEntry('CEO', `${window.OMC_I18N?.t('common.errorLoading', 'Error loading') || 'Error loading'}: ${err.message}`, 'error');"),
    ("      if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = '⏳ Submitting...'; }", "      if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = window.OMC_I18N?.t('common.submitting', 'Submitting...') || 'Submitting...'; }"),
    ("          if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Send'; }", "          if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = window.OMC_I18N?.t('common.send', 'Send') || 'Send'; }"),
    ("        if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Send'; }", "        if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = window.OMC_I18N?.t('common.send', 'Send') || 'Send'; }"),
]
for old, new in repls:
    text, _ = replace(text, old, new)
app.write_text(text, encoding='utf-8')

html_path = ROOT / 'frontend/index.html'
html = html_path.read_text(encoding='utf-8')
html, _ = replace(html, '<aside id="roster-panel" aria-label="Team Roster" data-i18n-aria-label="nav.teamRoster">', '<aside id="roster-panel" aria-label="Equipe" data-i18n-aria-label="nav.teamRoster">')
html, _ = replace(html, '<textarea id="workflow-content" class="workflow-textarea hidden" rows="20" aria-label="Workflow content" data-i18n-aria-label="workflow.contentLabel"></textarea>', '<textarea id="workflow-content" class="workflow-textarea hidden" rows="20" aria-label="Conteúdo do workflow" data-i18n-aria-label="workflow.contentLabel"></textarea>')
html, _ = replace(html, '<option value="all_hands" data-i18n="meeting.type.allHands">All-Hands (fala do CEO)</option>', '<option value="all_hands" data-i18n="meeting.type.allHands">Reunião geral (fala do CEO)</option>')
html_path.write_text(html, encoding='utf-8')

terminal_path = ROOT / 'frontend/ceo-terminal.js'
terminal = terminal_path.read_text(encoding='utf-8')
terminal, _ = replace(terminal, "          + `<span class=\"ceo-msg-text ceo-msg-full\" style=\"display:none\">${this._esc(full)}</span>`\n          + `<span class=\"ceo-msg-toggle\" onclick=\"this.parentElement.querySelector('.ceo-msg-collapsed').style.display=this.parentElement.querySelector('.ceo-msg-collapsed').style.display==='none'?'':'none';this.parentElement.querySelector('.ceo-msg-full').style.display=this.parentElement.querySelector('.ceo-msg-full').style.display==='none'?'':'none';this.textContent=this.textContent==='▼ Show more'?'▲ Show less':'▼ Show more'\">▼ Show more</span>`;", "          + `<span class=\"ceo-msg-text ceo-msg-full\" style=\"display:none\">${this._esc(full)}</span>`\n          + `<span class=\"ceo-msg-toggle\" onclick=\"this.parentElement.querySelector('.ceo-msg-collapsed').style.display=this.parentElement.querySelector('.ceo-msg-collapsed').style.display==='none'?'':'none';this.parentElement.querySelector('.ceo-msg-full').style.display=this.parentElement.querySelector('.ceo-msg-full').style.display==='none'?'':'none';this.textContent=this.textContent===window.OMC_I18N?.t('common.showMore', 'Show more')?'▲ '+window.OMC_I18N?.t('common.showLess', 'Show less'):window.OMC_I18N?.t('common.showMore', 'Show more')\">${window.OMC_I18N?.t('common.showMore', 'Show more')}</span>`;")
terminal_path.write_text(terminal, encoding='utf-8')

print('patched frontend round 3')

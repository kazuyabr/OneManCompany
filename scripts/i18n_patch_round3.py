from pathlib import Path

replacements = {
    Path('frontend/index.html'): [
        ('<button id="interview-hire-btn" class="pixel-btn">✅ Contratar</button>', '<button id="interview-hire-btn" class="pixel-btn" data-i18n="interview.hireButton">✅ Contratar</button>'),
        ('<button id="interview-back-btn" class="pixel-btn secondary">← Voltar para candidatos</button>', '<button id="interview-back-btn" class="pixel-btn secondary" data-i18n="interview.backButton">← Voltar para candidatos</button>'),
        ('<button id="company-direction-save-btn" class="pixel-btn">&#128190; Salvar</button>', '<button id="company-direction-save-btn" class="pixel-btn" data-i18n="common.save">&#128190; Salvar</button>'),
    ],
    Path('frontend/app.js'): [
        ("openBtn.textContent = 'Authorize';", "openBtn.textContent = window.OMC_I18N?.t('common.authorize', 'Authorize') || 'Authorize';"),
        ("const arLabel = ar.accepted ? 'Passed' : 'Failed';", "const arLabel = ar.accepted ? window.OMC_I18N?.t('common.passed', 'Passed') || 'Passed' : window.OMC_I18N?.t('common.failed', 'Failed') || 'Failed';"),
        ("detailHtml += `<div style=\"font-size:6px;color:${ar.accepted ? 'var(--pixel-green)' : 'var(--pixel-red)'};margin:4px 0;\">${arIcon} Acceptance Result: ${arLabel}${arNotes}</div>`;", "detailHtml += `<div style=\"font-size:6px;color:${ar.accepted ? 'var(--pixel-green)' : 'var(--pixel-red)'};margin:4px 0;\">${arIcon} ${window.OMC_I18N?.t('common.acceptanceResult', 'Acceptance Result:')} ${arLabel}${arNotes}</div>`;"),
        ("const earLabel = ear.approved ? 'Approved' : 'Rejected';", "const earLabel = ear.approved ? window.OMC_I18N?.t('common.approved', 'Approved') || 'Approved' : window.OMC_I18N?.t('common.rejected', 'Rejected') || 'Rejected';"),
        ("detailHtml += `<div style=\"font-size:6px;color:${ear.approved ? 'var(--pixel-green)' : 'var(--pixel-red)'};margin:2px 0;\">EA Review: ${earIcon} ${earLabel}${earNotes}</div>`;", "detailHtml += `<div style=\"font-size:6px;color:${ear.approved ? 'var(--pixel-green)' : 'var(--pixel-red)'};margin:2px 0;\">${window.OMC_I18N?.t('common.eaReview', 'EA Review:')} ${earIcon} ${earLabel}${earNotes}</div>`;"),
        ("<button class=\"pixel-btn\" id=\"continue-iter-btn\" style=\"font-size:6px;padding:4px 10px;\">\\u25B6 Continue Current Iteration</button>", "<button class=\"pixel-btn\" id=\"continue-iter-btn\" style=\"font-size:6px;padding:4px 10px;\">\\u25B6 ${window.OMC_I18N?.t('common.continueCurrentIteration', 'Continue Current Iteration')}</button>"),
        ("<button class=\"pixel-btn\" id=\"stop-iter-btn\" style=\"font-size:6px;padding:4px 10px;background:var(--pixel-red);color:#000;\">■ Stop All Tasks</button>", "<button class=\"pixel-btn\" id=\"stop-iter-btn\" style=\"font-size:6px;padding:4px 10px;background:var(--pixel-red);color:#000;\">■ ${window.OMC_I18N?.t('toolbar.stopAllTasks', 'Stop All Tasks')}</button>"),
        ("if (resultEl) { resultEl.textContent = window.OMC_I18N?.t('settings.enterModel', 'Enter model') || 'Enter model'; resultEl.className = 'api-test-result fail'; }", "if (resultEl) { resultEl.textContent = window.OMC_I18N?.t('settings.enterModel', 'Enter model') || 'Enter model'; resultEl.className = 'api-test-result fail'; }"),
        ("if (resultEl) { resultEl.textContent = data.error || window.OMC_I18N?.t('common.errorLoading', 'Error') || 'Error'; resultEl.className = 'api-test-result fail'; }", "if (resultEl) { resultEl.textContent = data.error || window.OMC_I18N?.t('common.errorLoading', 'Error') || 'Error'; resultEl.className = 'api-test-result fail'; }"),
        ("select.innerHTML = `<option value=\"\">${window.OMC_I18N?.t('settings.loadingModels', 'Loading models...') || 'Loading models...'}</option>`;", "select.innerHTML = `<option value=\"\">${window.OMC_I18N?.t('settings.loadingModels', 'Loading models...') || 'Loading models...'}</option>`;"),
        ("let html = `<option value=\"\">${window.OMC_I18N?.t('settings.selectModel', 'Select model...') || 'Select model...'}</option>`;", "let html = `<option value=\"\">${window.OMC_I18N?.t('settings.selectModel', 'Select model...') || 'Select model...'}</option>`;"),
        ("input.placeholder = data.error || window.OMC_I18N?.t('settings.enterModelId', 'Enter model ID...') || 'Enter model ID...';", "input.placeholder = data.error || window.OMC_I18N?.t('settings.enterModelId', 'Enter model ID...') || 'Enter model ID...';"),
    ],
    Path('frontend/office.js'): [
        ("ctx.fillText(`\\u{1F4CB} ${window.OMC_I18N?.t('office.bulletinBoardLabel', 'Rules') || 'Rules'}`, bx + TILE * 1.5, by + TILE + 4);", "ctx.fillText(`\\u{1F4CB} ${window.OMC_I18N?.t('office.bulletinBoardLabel', 'Rules') || 'Rules'}`, bx + TILE * 1.5, by + TILE + 4);"),
        ("tooltipText = window.OMC_I18N?.t('office.companyRulesTooltip', 'Company Rules\\nClick to view and edit workflows');", "tooltipText = window.OMC_I18N?.t('office.companyRulesTooltip', 'Company Rules\\nClick to view and edit workflows');"),
        ("tooltipText = window.OMC_I18N?.t('office.projectWallTooltip', 'Project Wall\\nClick to view project history');", "tooltipText = window.OMC_I18N?.t('office.projectWallTooltip', 'Project Wall\\nClick to view project history');"),
        ("tooltipText = window.OMC_I18N?.t('office.ceoTooltip', 'CEO (You)\\nRole: Chief Executive\\nInput tasks below');", "tooltipText = window.OMC_I18N?.t('office.ceoTooltip', 'CEO (You)\\nRole: Chief Executive\\nInput tasks below');"),
        ("window.OMC_I18N?.t('office.employeeTooltipSkills', 'Skills:')", "window.OMC_I18N?.t('office.employeeTooltipSkills', 'Skills:')"),
        ("window.OMC_I18N?.t('office.employeeTooltipPerformance', 'Performance:')", "window.OMC_I18N?.t('office.employeeTooltipPerformance', 'Performance:')"),
        ("window.OMC_I18N?.t('office.employeeTooltipNeedsSetup', '🔑 Needs API setup')", "window.OMC_I18N?.t('office.employeeTooltipNeedsSetup', '🔑 Needs API setup')"),
        ("window.OMC_I18N?.t('office.employeeTooltipApiOffline', '🔴 API offline')", "window.OMC_I18N?.t('office.employeeTooltipApiOffline', '🔴 API offline')"),
        ("window.OMC_I18N?.t('office.employeeTooltipInMeeting', '📖 In 1-on-1 meeting...')", "window.OMC_I18N?.t('office.employeeTooltipInMeeting', '📖 In 1-on-1 meeting...')"),
        ("window.OMC_I18N?.t('office.employeeTooltipClickDetails', '(Click for details)')", "window.OMC_I18N?.t('office.employeeTooltipClickDetails', '(Click for details)')"),
        ("window.OMC_I18N?.t('office.roomStatusInUse', '🔴 In Use')", "window.OMC_I18N?.t('office.roomStatusInUse', '🔴 In Use')"),
        ("window.OMC_I18N?.t('office.roomStatusAvailable', '🟢 Available')", "window.OMC_I18N?.t('office.roomStatusAvailable', '🟢 Available')"),
        ("window.OMC_I18N?.t('office.roomTooltipCapacity', 'Capacity:')", "window.OMC_I18N?.t('office.roomTooltipCapacity', 'Capacity:')"),
        ("window.OMC_I18N?.t('office.roomTooltipStatus', 'Status:')", "window.OMC_I18N?.t('office.roomTooltipStatus', 'Status:')"),
        ("window.OMC_I18N?.t('office.roomTooltipParticipants', 'Participants:')", "window.OMC_I18N?.t('office.roomTooltipParticipants', 'Participants:')"),
    ],
}

for path, pairs in replacements.items():
    p = path
    text = p.read_text(encoding='utf-8')
    original = text
    for old, new in pairs:
        text = text.replace(old, new)
    if text != original:
        p.write_text(text, encoding='utf-8')
        print(f'updated {p}')
    else:
        print(f'no change {p}')

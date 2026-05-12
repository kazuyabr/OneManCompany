from pathlib import Path
import json

en = json.loads(Path('frontend/i18n/en.json').read_text(encoding='utf-8'))
pt = json.loads(Path('frontend/i18n/pt-BR.json').read_text(encoding='utf-8'))
missing_in_pt = [k for k in en if k not in pt]
missing_in_en = [k for k in pt if k not in en]
report = [
    f'en={len(en)}',
    f'pt={len(pt)}',
    f'missing_in_pt={len(missing_in_pt)}',
    f'missing_in_en={len(missing_in_en)}',
    '',
    '[missing_in_pt]',
    *missing_in_pt,
    '',
    '[missing_in_en]',
    *missing_in_en,
]
Path('.tmp_i18n_compare_report.txt').write_text('\n'.join(report) + '\n', encoding='utf-8')
print('ok')

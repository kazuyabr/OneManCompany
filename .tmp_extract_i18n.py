from pathlib import Path
import json
import re

src = Path('frontend/i18n.js').read_text(encoding='utf-8').splitlines()
blocks = {}
current = None
key_re = re.compile(r"^\s*'((?:\\'|[^'])+)':\s*'((?:\\'|[^'])*)',?\s*$")
for line in src:
    stripped = line.strip()
    if stripped == 'en: {':
        current = 'en'
        blocks[current] = {}
        continue
    if stripped == "'pt-BR': {":
        current = 'pt-BR'
        blocks[current] = {}
        continue
    if current and stripped == '},':
        current = None
        continue
    if not current:
        continue
    m = key_re.match(line)
    if not m:
        continue
    key = m.group(1).replace("\\'", "'")
    val = m.group(2).replace("\\'", "'")
    blocks[current][key] = val
out = Path('frontend/i18n')
out.mkdir(parents=True, exist_ok=True)
for lang, obj in blocks.items():
    Path(out / f'{lang}.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print({k: len(v) for k, v in blocks.items()})

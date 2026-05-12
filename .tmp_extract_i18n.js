const fs = require('fs');
const path = require('path');

const src = fs.readFileSync(path.join('frontend', 'i18n.js'), 'utf8');
const marker = 'const TRANSLATIONS = {';
const start = src.indexOf(marker);
if (start === -1) throw new Error('TRANSLATIONS marker not found');

let i = start + marker.length;
let depth = 1;
let inSingle = false;
let inDouble = false;
let inTemplate = false;
let escaped = false;
for (; i < src.length; i++) {
  const ch = src[i];
  if (escaped) {
    escaped = false;
    continue;
  }
  if (ch === '\\') {
    escaped = true;
    continue;
  }
  if (inSingle) {
    if (ch === "'") inSingle = false;
    continue;
  }
  if (inDouble) {
    if (ch === '"') inDouble = false;
    continue;
  }
  if (inTemplate) {
    if (ch === '`') inTemplate = false;
    continue;
  }
  if (ch === "'") { inSingle = true; continue; }
  if (ch === '"') { inDouble = true; continue; }
  if (ch === '`') { inTemplate = true; continue; }
  if (ch === '{') depth++;
  if (ch === '}') {
    depth--;
    if (depth === 0) {
      i++;
      break;
    }
  }
}

const objText = src.slice(start + 'const TRANSLATIONS = '.length, i);
const translations = eval('(' + objText + ')');
const outDir = path.join('frontend', 'i18n');
fs.mkdirSync(outDir, { recursive: true });
for (const [lang, data] of Object.entries(translations)) {
  fs.writeFileSync(path.join(outDir, `${lang}.json`), JSON.stringify(data, null, 2) + '\n', 'utf8');
}
console.log(Object.fromEntries(Object.entries(translations).map(([k, v]) => [k, Object.keys(v).length])));

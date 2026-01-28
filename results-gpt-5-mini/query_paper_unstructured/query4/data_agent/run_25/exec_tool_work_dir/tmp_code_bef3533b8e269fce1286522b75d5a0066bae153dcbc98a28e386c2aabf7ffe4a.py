code = """import json, re
# var_call_e3SIv64u5ksvMEFjSB2sbp7v is available in storage
path = var_call_e3SIv64u5ksvMEFjSB2sbp7v
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
papers = []
titles = []
for rec in data:
    filename = rec.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text', '')
    m = re.search(r'(19|20)\d{2}', text)
    year = m.group(0) if m else None
    domain_found = 'physical activity' in text.lower()
    papers.append({'title': title, 'year': year, 'domain_found': domain_found})
    titles.append(title)
out = {'titles': titles, 'papers': papers}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_e3SIv64u5ksvMEFjSB2sbp7v': 'file_storage/call_e3SIv64u5ksvMEFjSB2sbp7v.json'}

exec(code, env_args)

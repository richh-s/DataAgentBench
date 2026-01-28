code = """import json, re

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_records(var_call_PF945Zw0JElUWZwT5KGXqZEA)

park_keywords = re.compile(r'\b(park|playground|bluffs|skate)\b', re.I)

hits = []
for d in docs:
    text = d.get('text','')
    if '2022' not in text:
        continue
    if not re.search(r'Construction was completed', text, re.I):
        continue
    if not park_keywords.search(text):
        continue
    lines = text.splitlines()
    for idx, ln in enumerate(lines):
        if re.search(r'Construction was completed', ln, re.I) and '2022' in ln:
            start = max(0, idx-5); end = min(len(lines), idx+4)
            snippet = "\\n".join([l.strip() for l in lines[start:end]])
            hits.append({'filename': d.get('filename'), 'snippet': snippet})

print('__RESULT__:')
print(json.dumps(hits[:50]))"""

env_args = {'var_call_PF945Zw0JElUWZwT5KGXqZEA': 'file_storage/call_PF945Zw0JElUWZwT5KGXqZEA.json', 'var_call_DzrJsyGi8yVyguqqLp4vcoWd': 'file_storage/call_DzrJsyGi8yVyguqqLp4vcoWd.json', 'var_call_T91ysjF9P7VgpzVdTV1ByLnj': {'total_funding': 0, 'matched_projects': []}}

exec(code, env_args)

code = """import json, re

docs_src = var_call_uimwfzwWJBpsV8m3WbZCAK8D
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

completed_line_kw = re.compile(r'(Construction\s+was\s+completed|Construction\s+completed|Completed\s+Construction|Complete\s+Construction|Construction\s+complete(?:d)?)', re.I)

hits = []
for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue
    if completed_line_kw.search(text):
        # find first line containing completed & 2022
        for ln in text.splitlines():
            if completed_line_kw.search(ln) and '2022' in ln:
                hits.append({'filename': d.get('filename'), 'line': ln.strip()})
                break

print('__RESULT__:')
print(json.dumps({'n_docs_with_completed_2022_lines': len(hits), 'examples': hits[:10]}))"""

env_args = {'var_call_uimwfzwWJBpsV8m3WbZCAK8D': 'file_storage/call_uimwfzwWJBpsV8m3WbZCAK8D.json', 'var_call_VmLgdKiy6567QWf43xxaq9P4': 'file_storage/call_VmLgdKiy6567QWf43xxaq9P4.json', 'var_call_DTXp4U7e3Lx9LTOf7KaJJAqy': {'total_funding_completed_2022_park_projects': 0}, 'var_call_KGK8hJ71LeuUyDRwRNwhztSs': {'projects': [], 'total_funding_completed_2022_park_projects': 0, 'n_projects': 0}}

exec(code, env_args)

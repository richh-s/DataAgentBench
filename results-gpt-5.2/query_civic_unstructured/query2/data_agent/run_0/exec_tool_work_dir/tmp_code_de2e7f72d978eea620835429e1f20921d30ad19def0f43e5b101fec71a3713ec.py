code = """import json

docs_src = var_call_uimwfzwWJBpsV8m3WbZCAK8D
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

# find the doc mentioned
fn = 'malibucity_agenda_03222023-2060.txt'
doc = next((d for d in docs if d.get('filename')==fn), None)
lines = [ln.strip() for ln in doc.get('text','').splitlines()]
idxs = [i for i,ln in enumerate(lines) if 'Construction was completed November 2022' in ln]
context = []
for i in idxs:
    start = max(0,i-12)
    end = min(len(lines), i+6)
    context.append({'i': i, 'before': lines[start:i], 'line': lines[i], 'after': lines[i+1:end]})

print('__RESULT__:')
print(json.dumps({'matches': context[:2]}))"""

env_args = {'var_call_uimwfzwWJBpsV8m3WbZCAK8D': 'file_storage/call_uimwfzwWJBpsV8m3WbZCAK8D.json', 'var_call_VmLgdKiy6567QWf43xxaq9P4': 'file_storage/call_VmLgdKiy6567QWf43xxaq9P4.json', 'var_call_DTXp4U7e3Lx9LTOf7KaJJAqy': {'total_funding_completed_2022_park_projects': 0}, 'var_call_KGK8hJ71LeuUyDRwRNwhztSs': {'projects': [], 'total_funding_completed_2022_park_projects': 0, 'n_projects': 0}, 'var_call_v0H9bZ6QCs7bx9O7WF3WWgck': {'n_docs_with_completed_2022_lines': 1, 'examples': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}]}, 'var_call_VbOaPt4zXglh42XFAPSnBxFO': {'projects': [], 'total': 0, 'n_projects': 0, 'funding_rows': []}}

exec(code, env_args)

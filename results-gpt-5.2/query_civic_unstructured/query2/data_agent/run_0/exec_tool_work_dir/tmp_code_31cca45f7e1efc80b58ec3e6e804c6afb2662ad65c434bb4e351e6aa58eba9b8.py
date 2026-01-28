code = """import json, re

src = var_call_uimwfzwWJBpsV8m3WbZCAK8D
if isinstance(src, str):
    with open(src,'r',encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = src

doc = next(d for d in docs if d.get('filename')=='malibucity_agenda_03222023-2060.txt')
lines = [ln.strip() for ln in (doc.get('text','') or '').splitlines()]

completed_line_kw = re.compile(r'(Construction\s+was\s+completed|Construction\s+completed|Completed\s+Construction|Complete\s+Construction|Construction\s+complete(?:d)?)', re.I)

i = next(i for i,ln in enumerate(lines) if completed_line_kw.search(ln) and '2022' in ln)
back = []
for j in range(i-1, max(-1,i-25), -1):
    cand = lines[j]
    back.append({'j': j, 'line': cand})

print('__RESULT__:')
print(json.dumps({'i': i, 'completion_line': lines[i], 'backward_scan': back}))"""

env_args = {'var_call_uimwfzwWJBpsV8m3WbZCAK8D': 'file_storage/call_uimwfzwWJBpsV8m3WbZCAK8D.json', 'var_call_VmLgdKiy6567QWf43xxaq9P4': 'file_storage/call_VmLgdKiy6567QWf43xxaq9P4.json', 'var_call_DTXp4U7e3Lx9LTOf7KaJJAqy': {'total_funding_completed_2022_park_projects': 0}, 'var_call_KGK8hJ71LeuUyDRwRNwhztSs': {'projects': [], 'total_funding_completed_2022_park_projects': 0, 'n_projects': 0}, 'var_call_v0H9bZ6QCs7bx9O7WF3WWgck': {'n_docs_with_completed_2022_lines': 1, 'examples': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}]}, 'var_call_VbOaPt4zXglh42XFAPSnBxFO': {'projects': [], 'total': 0, 'n_projects': 0, 'funding_rows': []}, 'var_call_wF0m05kvkqrLIsIwJblP5qn1': {'matches': [{'i': 314, 'before': ['', '(cid:190) Updates:', '', '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.', '', '(cid:190) Project Schedule:', '', '(cid:131) Begin construction: Summer 2023', '(cid:131) Complete Construction: Summer 2023', '', 'Bluffs Park Shade Structure', ''], 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'after': ['', 'filed January 2023', '', 'Page 4 of 6', '']}]}, 'var_call_vL4bmyTImjqKIengu96l9ZwH': {'projects': [], 'total_funding': 0, 'n_projects': 0}}

exec(code, env_args)

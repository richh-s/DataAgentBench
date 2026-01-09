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
park_name_kw = re.compile(r'\bpark\b|\bplayground\b|\bbluffs\b|\bskate\b', re.I)

for i, ln in enumerate(lines):
    if completed_line_kw.search(ln) and '2022' in ln:
        proj=None
        for j in range(i-1, max(-1,i-80), -1):
            cand=lines[j].strip()
            if not cand:
                continue
            if cand.startswith('('):
                continue
            if re.search(r'^(Page \d+ of \d+|Agenda Item)', cand, re.I):
                continue
            if re.search(r'^(Updates:|Project Schedule:|Estimated Schedule:|Project Updates:|Project Description:|DISCUSSION|RECOMMENDED ACTION)$', cand, re.I):
                continue
            if completed_line_kw.search(cand):
                continue
            if re.search(r'[A-Za-z]', cand) and len(cand)<=120:
                proj=cand
                break
        print('__RESULT__:')
        print(json.dumps({'i': i, 'completion_line': ln, 'picked_project': proj, 'is_park': bool(proj and park_name_kw.search(proj))}))
        break"""

env_args = {'var_call_uimwfzwWJBpsV8m3WbZCAK8D': 'file_storage/call_uimwfzwWJBpsV8m3WbZCAK8D.json', 'var_call_VmLgdKiy6567QWf43xxaq9P4': 'file_storage/call_VmLgdKiy6567QWf43xxaq9P4.json', 'var_call_DTXp4U7e3Lx9LTOf7KaJJAqy': {'total_funding_completed_2022_park_projects': 0}, 'var_call_KGK8hJ71LeuUyDRwRNwhztSs': {'projects': [], 'total_funding_completed_2022_park_projects': 0, 'n_projects': 0}, 'var_call_v0H9bZ6QCs7bx9O7WF3WWgck': {'n_docs_with_completed_2022_lines': 1, 'examples': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}]}, 'var_call_VbOaPt4zXglh42XFAPSnBxFO': {'projects': [], 'total': 0, 'n_projects': 0, 'funding_rows': []}, 'var_call_wF0m05kvkqrLIsIwJblP5qn1': {'matches': [{'i': 314, 'before': ['', '(cid:190) Updates:', '', '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.', '', '(cid:190) Project Schedule:', '', '(cid:131) Begin construction: Summer 2023', '(cid:131) Complete Construction: Summer 2023', '', 'Bluffs Park Shade Structure', ''], 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'after': ['', 'filed January 2023', '', 'Page 4 of 6', '']}]}, 'var_call_vL4bmyTImjqKIengu96l9ZwH': {'projects': [], 'total_funding': 0, 'n_projects': 0}, 'var_call_ypqcARPpZc6Waqu26qObI5d2': {'i': 314, 'completion_line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'backward_scan': [{'j': 313, 'line': ''}, {'j': 312, 'line': 'Bluffs Park Shade Structure'}, {'j': 311, 'line': ''}, {'j': 310, 'line': '(cid:131) Complete Construction: Summer 2023'}, {'j': 309, 'line': '(cid:131) Begin construction: Summer 2023'}, {'j': 308, 'line': ''}, {'j': 307, 'line': '(cid:190) Project Schedule:'}, {'j': 306, 'line': ''}, {'j': 305, 'line': '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.'}, {'j': 304, 'line': ''}, {'j': 303, 'line': '(cid:190) Updates:'}, {'j': 302, 'line': ''}, {'j': 301, 'line': 'Storm Drain Trash Screens Phase Two'}, {'j': 300, 'line': ''}, {'j': 299, 'line': '(cid:131) Complete Construction: Summer 2025'}, {'j': 298, 'line': '(cid:131) Begin construction: April 2023'}, {'j': 297, 'line': ''}, {'j': 296, 'line': '(cid:190) Project Schedule:'}, {'j': 295, 'line': ''}, {'j': 294, 'line': 'Engineering, Inc.'}, {'j': 293, 'line': ''}, {'j': 292, 'line': '(cid:131) On February 27, 2023, City Council awarded the contract to GMZ'}, {'j': 291, 'line': ''}, {'j': 290, 'line': '(cid:190) Updates:'}]}, 'var_call_HEbNRoGJFWwMgojLYpNAPGzx': {'projects': [], 'total_funding': 0, 'n_projects': 0, 'details': []}}

exec(code, env_args)

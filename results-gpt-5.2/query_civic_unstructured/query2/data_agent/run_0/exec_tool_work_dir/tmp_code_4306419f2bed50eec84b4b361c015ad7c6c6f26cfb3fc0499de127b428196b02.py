code = """import json, re
import pandas as pd

# Load docs
src = var_call_uimwfzwWJBpsV8m3WbZCAK8D
if isinstance(src, str):
    with open(src,'r',encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = src

fund_src = var_call_VmLgdKiy6567QWf43xxaq9P4
if isinstance(fund_src, str):
    with open(fund_src,'r',encoding='utf-8') as f:
        fund = json.load(f)
else:
    fund = fund_src
fund_df = pd.DataFrame(fund)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype('int64')

completed_line_kw = re.compile(r'(Construction\s+was\s+completed|Construction\s+completed|Completed\s+Construction|Complete\s+Construction|Construction\s+complete(?:d)?)', re.I)
park_name_kw = re.compile(r'\bpark\b|\bplayground\b|\bbluffs\b|\bskate\b', re.I)

park_completed_2022 = set()

for d in docs:
    lines = [ln.strip() for ln in (d.get('text','') or '').splitlines()]
    for i, ln in enumerate(lines):
        if completed_line_kw.search(ln) and '2022' in ln:
            proj = None
            for j in range(i-1, max(-1, i-60), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                if re.search(r'^(\(cid:|cid:|\u2022|\*|\-|Page \d+ of \d+|Agenda Item)', cand, re.I):
                    continue
                # stop at section headers
                if re.search(r'^(Capital Improvement Projects|Disaster Recovery Projects)\b', cand, re.I):
                    break
                # skip common labels
                if re.search(r'^(Updates:|Project Schedule:|Estimated Schedule:|Project Updates:|Project Description:|DISCUSSION|RECOMMENDED ACTION)$', cand, re.I):
                    continue
                if completed_line_kw.search(cand):
                    continue
                proj = cand
                break
            if proj and park_name_kw.search(proj):
                park_completed_2022.add(proj)

projects = sorted(park_completed_2022)
merged = pd.DataFrame({'Project_Name': projects}).merge(fund_df, on='Project_Name', how='left')

total = int(merged['Amount'].fillna(0).sum())
print('__RESULT__:')
print(json.dumps({'projects': projects, 'total_funding': total, 'n_projects': len(projects)}))"""

env_args = {'var_call_uimwfzwWJBpsV8m3WbZCAK8D': 'file_storage/call_uimwfzwWJBpsV8m3WbZCAK8D.json', 'var_call_VmLgdKiy6567QWf43xxaq9P4': 'file_storage/call_VmLgdKiy6567QWf43xxaq9P4.json', 'var_call_DTXp4U7e3Lx9LTOf7KaJJAqy': {'total_funding_completed_2022_park_projects': 0}, 'var_call_KGK8hJ71LeuUyDRwRNwhztSs': {'projects': [], 'total_funding_completed_2022_park_projects': 0, 'n_projects': 0}, 'var_call_v0H9bZ6QCs7bx9O7WF3WWgck': {'n_docs_with_completed_2022_lines': 1, 'examples': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}]}, 'var_call_VbOaPt4zXglh42XFAPSnBxFO': {'projects': [], 'total': 0, 'n_projects': 0, 'funding_rows': []}, 'var_call_wF0m05kvkqrLIsIwJblP5qn1': {'matches': [{'i': 314, 'before': ['', '(cid:190) Updates:', '', '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.', '', '(cid:190) Project Schedule:', '', '(cid:131) Begin construction: Summer 2023', '(cid:131) Complete Construction: Summer 2023', '', 'Bluffs Park Shade Structure', ''], 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'after': ['', 'filed January 2023', '', 'Page 4 of 6', '']}]}}

exec(code, env_args)

code = """import json, re
import pandas as pd

docs_src = var_call_uimwfzwWJBpsV8m3WbZCAK8D
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

fund_src = var_call_VmLgdKiy6567QWf43xxaq9P4
if isinstance(fund_src, str):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund = json.load(f)
else:
    fund = fund_src
fund_df = pd.DataFrame(fund)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype('int64')

completed_line_kw = re.compile(r'(Construction\s+was\s+completed|Construction\s+completed|Completed\s+Construction|Complete\s+Construction|Construction\s+complete(?:d)?)', re.I)
park_name_kw = re.compile(r'\bpark\b|\bplayground\b|\bbluffs\b|\bskate\b', re.I)

park_completed_2022 = set()

for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if completed_line_kw.search(ln) and '2022' in ln:
            # walk backwards to find a project name line
            proj = None
            for j in range(i-1, max(-1, i-40), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                # skip bullet/metadata lines
                if re.search(r'^(\(cid:|cid:|\u2022|\*|\-|Page \d+ of \d+|Agenda Item|Updates:|Project Schedule:|Estimated Schedule:|Project Updates:|Project Description:|DISCUSSION|RECOMMENDED ACTION)', cand, re.I):
                    continue
                if len(cand) > 140:
                    continue
                # Stop if we encounter another completion line (avoid)
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
print(json.dumps({'projects': projects, 'total': total, 'n_projects': len(projects), 'funding_rows': merged.to_dict(orient='records')}))"""

env_args = {'var_call_uimwfzwWJBpsV8m3WbZCAK8D': 'file_storage/call_uimwfzwWJBpsV8m3WbZCAK8D.json', 'var_call_VmLgdKiy6567QWf43xxaq9P4': 'file_storage/call_VmLgdKiy6567QWf43xxaq9P4.json', 'var_call_DTXp4U7e3Lx9LTOf7KaJJAqy': {'total_funding_completed_2022_park_projects': 0}, 'var_call_KGK8hJ71LeuUyDRwRNwhztSs': {'projects': [], 'total_funding_completed_2022_park_projects': 0, 'n_projects': 0}, 'var_call_v0H9bZ6QCs7bx9O7WF3WWgck': {'n_docs_with_completed_2022_lines': 1, 'examples': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion'}]}}

exec(code, env_args)

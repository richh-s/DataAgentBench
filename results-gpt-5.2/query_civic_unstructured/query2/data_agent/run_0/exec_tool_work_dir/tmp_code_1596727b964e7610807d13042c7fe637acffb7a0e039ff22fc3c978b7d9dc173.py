code = """import json, re
import pandas as pd

# Load civic docs
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

park_name_kw = re.compile(r'\bpark\b|\bplayground\b|\bbluffs\b|\bskate\b', re.I)
completed_line_kw = re.compile(r'(Construction\s+was\s+completed|Construction\s+completed|Completed\s+Construction|Construction\s+complete(?:d)?)\s*[,\:]*\s*(.*)$', re.I)

completed_park_projects = set()

for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        m = completed_line_kw.search(ln)
        if not m:
            continue
        tail = m.group(2).strip()
        if '2022' not in (tail or ''):
            # sometimes year might be on same line with month/year, else skip
            continue
        # Find preceding project name: nearest previous non-empty line not starting with bullet and not generic
        proj = None
        for j in range(i-1, max(-1, i-25), -1):
            cand = lines[j].strip()
            if not cand:
                continue
            if re.search(r'^(\(cid:|cid:|\u2022|\*|\-|Page \d+ of \d+|Agenda Item|Updates:|Project Schedule:|Estimated Schedule:|Project Updates:|Project Description:|DISCUSSION|RECOMMENDED ACTION)', cand, re.I):
                continue
            # likely a project header is title case and short
            if len(cand) > 140:
                continue
            proj = cand
            break
        if proj and park_name_kw.search(proj):
            completed_park_projects.add(proj)

completed_park_projects = sorted(completed_park_projects)
merged = pd.DataFrame({'Project_Name': completed_park_projects}).merge(fund_df, on='Project_Name', how='left')

total = int(merged['Amount'].fillna(0).sum())

result = {
    'projects': completed_park_projects,
    'total_funding_completed_2022_park_projects': total,
    'n_projects': len(completed_park_projects)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uimwfzwWJBpsV8m3WbZCAK8D': 'file_storage/call_uimwfzwWJBpsV8m3WbZCAK8D.json', 'var_call_VmLgdKiy6567QWf43xxaq9P4': 'file_storage/call_VmLgdKiy6567QWf43xxaq9P4.json', 'var_call_DTXp4U7e3Lx9LTOf7KaJJAqy': {'total_funding_completed_2022_park_projects': 0}}

exec(code, env_args)

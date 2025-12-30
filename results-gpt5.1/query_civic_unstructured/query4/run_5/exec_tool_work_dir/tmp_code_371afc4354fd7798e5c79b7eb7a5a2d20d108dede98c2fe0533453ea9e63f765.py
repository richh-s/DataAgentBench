code = """import re, json, pandas as pd
from datetime import datetime

path_docs = var_call_oSRVNiP6QK0tiatt0ypM5tvp
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    current_project = None
    for line in lines:
        if re.search(r'(Project|Improvements|Repairs|Resurfacing|Playground|Park)', line) and len(line.split())<15 and not line.endswith(':'):
            current_project = line.strip()
        m = re.search(r'Begin Construction:\s*([A-Za-z]+\s+\d{4}|\d{4}-[A-Za-z]+|\d{4}-\d{2}|Spring\s+\d{4}|Summer\s+\d{4}|Fall\s+\d{4}|Winter\s+\d{4})', line)
        if m and current_project:
            st = m.group(1)
            projects.append({'Project_Name': current_project, 'st': st})

spring2022_projects = []
for p in projects:
    s = p['st']
    if '2022' not in s:
        continue
    s_lower = s.lower()
    in_spring = False
    if 'spring' in s_lower:
        in_spring = True
    else:
        try:
            dt = datetime.strptime(s, '%B %Y')
            if dt.year==2022 and dt.month in (3,4,5):
                in_spring = True
        except Exception:
            pass
        if re.match(r'2022-(03|04|05)', s):
            in_spring = True
    if in_spring:
        spring2022_projects.append(p['Project_Name'])

spring2022_projects = sorted(set(spring2022_projects))

path_fund = var_call_C88uUTNl2sPl2nMMxlV9aSoG
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

mask = fund_df['Project_Name'].isin(spring2022_projects)
sel = fund_df[mask]

result = {
  'spring2022_projects': spring2022_projects,
  'count_projects_with_funding': int(sel['Project_Name'].nunique()),
  'total_funding_for_those_projects': int(sel['Amount'].sum())
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oSRVNiP6QK0tiatt0ypM5tvp': 'file_storage/call_oSRVNiP6QK0tiatt0ypM5tvp.json', 'var_call_C88uUTNl2sPl2nMMxlV9aSoG': 'file_storage/call_C88uUTNl2sPl2nMMxlV9aSoG.json'}

exec(code, env_args)

code = """import re, json, pandas as pd
from pathlib import Path

civic_path = Path(var_call_SJyeZJgkApZqW009gFshmGKM)
with civic_path.open() as f:
    civic_docs = json.load(f)
texts = '\n'.join(d['text'] for d in civic_docs)

lines = [l.strip() for l in texts.split('\n') if l.strip()]

spring_patterns = [
    re.compile(r'Begin Construction: Spring 2022', re.I),
    re.compile(r'Start(?:s|ing)? .*Spring 2022', re.I)
]

projects_spring_2022 = set()

for i,l in enumerate(lines):
    if any(p.search(l) for p in spring_patterns):
        for j in range(max(0, i-5), i):
            cand = lines[j].strip()
            if len(cand.split()) > 2 and not cand.endswith(':'):
                projects_spring_2022.add(cand)

for i,l in enumerate(lines):
    if '2022-Spring' in l or 'Spring, 2022' in l:
        for j in range(max(0, i-5), i):
            cand = lines[j].strip()
            if len(cand.split()) > 2 and not cand.endswith(':'):
                projects_spring_2022.add(cand)

funding_path = Path(var_call_NhoGkN6DuiUmv7zca0nMHRqZ)
with funding_path.open() as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

matched = fund_df[fund_df['Project_Name'].isin(projects_spring_2022)]

result = {
    'projects_spring_2022_from_docs': sorted(projects_spring_2022),
    'matched_projects': matched['Project_Name'].tolist(),
    'count_started_spring_2022': int(matched['Project_Name'].nunique()),
    'total_funding_started_spring_2022': int(matched['Amount'].sum())
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_SJyeZJgkApZqW009gFshmGKM': 'file_storage/call_SJyeZJgkApZqW009gFshmGKM.json', 'var_call_NhoGkN6DuiUmv7zca0nMHRqZ': 'file_storage/call_NhoGkN6DuiUmv7zca0nMHRqZ.json'}

exec(code, env_args)

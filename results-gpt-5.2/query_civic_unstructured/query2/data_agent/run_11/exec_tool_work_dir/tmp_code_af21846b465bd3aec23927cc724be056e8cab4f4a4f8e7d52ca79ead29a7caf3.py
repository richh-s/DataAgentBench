code = """import json
import pandas as pd
import re

path_docs = var_call_TUyzQDUuBNfMgCrDpx3Q4u3H
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Use only documents mentioning 2022 to reduce noise
filtered_docs = [d for d in docs if '2022' in (d.get('text') or '')]

# Candidate park-related completed-in-2022 projects from text: find lines 'Construction was completed ... 2022' and look back for nearest title containing Park
projects = set()
for d in filtered_docs:
    lines = [ln.strip() for ln in (d.get('text') or '').splitlines()]
    for idx, ln in enumerate(lines):
        if re.search(r'Construction was completed', ln, re.I) and '2022' in ln:
            # look back up to 5 lines for a project name
            for back in range(1, 8):
                if idx-back < 0:
                    break
                cand = lines[idx-back].strip()
                if cand and ':' not in cand and len(cand.split())>=2 and re.search(r'\bpark\b', cand, re.I):
                    projects.add(cand)
                    break

completed_projects = pd.DataFrame({'Project_Name': sorted(projects)})

path_fund = var_call_Jmi8UhdfHAynqpxuKZ7QYJhT
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])

merged = completed_projects.merge(fund_df, on='Project_Name', how='left')
merged['Total_Amount'] = merged['Total_Amount'].fillna(0)

total = int(merged['Total_Amount'].sum())

out = {'total_funding_completed_2022_park_related': total, 'projects': merged.to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YVr6YsGg98GUbY989wj39zDB': ['Funding'], 'var_call_44cSXvBgDbGLbNPd4odSmpfZ': ['civic_docs'], 'var_call_TUyzQDUuBNfMgCrDpx3Q4u3H': 'file_storage/call_TUyzQDUuBNfMgCrDpx3Q4u3H.json', 'var_call_Jmi8UhdfHAynqpxuKZ7QYJhT': 'file_storage/call_Jmi8UhdfHAynqpxuKZ7QYJhT.json', 'var_call_57OCdCDHjEqIiHyAkAgVDFue': {'path': 'file_storage/call_TUyzQDUuBNfMgCrDpx3Q4u3H.json'}}

exec(code, env_args)

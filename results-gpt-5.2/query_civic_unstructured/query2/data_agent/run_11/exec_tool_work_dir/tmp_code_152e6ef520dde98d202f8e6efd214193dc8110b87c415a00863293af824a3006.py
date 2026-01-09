code = """import json, re
import pandas as pd

# load docs with 2022 mention
path_docs = var_call_mOKxHE05TXkEHHGnnt4Yx65a
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

park_completed_2022 = set()
for d in docs:
    text = d.get('text') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'Construction was completed', ln, re.I) and re.search(r'\b2022\b', ln):
            # find nearest previous non-empty line that is likely project title
            for j in range(i-1, max(-1, i-15), -1):
                cand = lines[j]
                if not cand:
                    continue
                if ':' in cand:
                    continue
                if cand.lower().startswith(('(cid', 'updates', 'project schedule', 'project description', 'page', 'agenda item')):
                    continue
                if len(cand.split()) < 2:
                    continue
                # park-related check on candidate or nearby context
                context = ' '.join(lines[max(0,j-2):i+1])
                if re.search(r'\bpark\b', context, re.I):
                    park_completed_2022.add(cand)
                    break

completed_df = pd.DataFrame({'Project_Name': sorted(park_completed_2022)})

# load funding totals
path_fund = var_call_Jmi8UhdfHAynqpxuKZ7QYJhT
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])

merged = completed_df.merge(fund_df, on='Project_Name', how='left')
merged['Total_Amount'] = merged['Total_Amount'].fillna(0)

total = int(merged['Total_Amount'].sum())

out = {'total': total, 'projects': merged.to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YVr6YsGg98GUbY989wj39zDB': ['Funding'], 'var_call_44cSXvBgDbGLbNPd4odSmpfZ': ['civic_docs'], 'var_call_TUyzQDUuBNfMgCrDpx3Q4u3H': 'file_storage/call_TUyzQDUuBNfMgCrDpx3Q4u3H.json', 'var_call_Jmi8UhdfHAynqpxuKZ7QYJhT': 'file_storage/call_Jmi8UhdfHAynqpxuKZ7QYJhT.json', 'var_call_57OCdCDHjEqIiHyAkAgVDFue': {'path': 'file_storage/call_TUyzQDUuBNfMgCrDpx3Q4u3H.json'}, 'var_call_6NCPYwYlD3EbD0pv9R7J5NMR': {'total_funding_completed_2022_park_related': 0, 'projects': []}, 'var_call_mOKxHE05TXkEHHGnnt4Yx65a': 'file_storage/call_mOKxHE05TXkEHHGnnt4Yx65a.json'}

exec(code, env_args)

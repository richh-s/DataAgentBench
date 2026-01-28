code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
with open(var_call_pDCBP2lAa5ZriS39FUTvYSPn, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

lines = [l.strip() for l in full_text.split('\n') if l.strip()]
projects = []
keywords = ['Project', 'Improvements', 'Repairs', 'Park', 'Facility', 'Road', 'Playground', 'Warning', 'Study', 'Canyon', 'Bridge', 'Drain', 'Culvert', 'Slope', 'Walkway', 'Signal', 'Median', 'Resurfacing']
for i, line in enumerate(lines):
    if len(line.split()) < 3:
        continue
    if any(k in line for k in keywords):
        st = None
        for j in range(i, min(i+15, len(lines))):
            m = re.search(r'Begin Construction:\s*([A-Za-z0-9 ,\-]+)', lines[j])
            if m:
                st = m.group(1)
                break
        if st:
            projects.append({'Project_Name': line, 'st': st})

spring_keywords = ['2022-Spring', '2022-March', '2022-April', '2022-May', 'March 2022', 'April 2022', 'May 2022']

spring_projects = [p for p in projects if any(sk in p['st'] for sk in spring_keywords)]

with open(var_call_kGwPCFQiYyETkI14DWsnKys2, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

sp_df = pd.DataFrame(spring_projects)
if not sp_df.empty:
    merged = sp_df.merge(fund_df, on='Project_Name', how='left')
    count_projects = int(merged.shape[0])
    total_funding = int(merged['Amount'].fillna(0).sum())
else:
    count_projects = 0
    total_funding = 0

result = {'projects_started_spring_2022': count_projects, 'total_funding_spring_2022': total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pDCBP2lAa5ZriS39FUTvYSPn': 'file_storage/call_pDCBP2lAa5ZriS39FUTvYSPn.json', 'var_call_kGwPCFQiYyETkI14DWsnKys2': 'file_storage/call_kGwPCFQiYyETkI14DWsnKys2.json'}

exec(code, env_args)

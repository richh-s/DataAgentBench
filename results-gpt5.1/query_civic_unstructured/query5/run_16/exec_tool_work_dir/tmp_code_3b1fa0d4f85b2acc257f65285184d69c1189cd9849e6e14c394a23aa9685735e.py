code = """import re, json, pandas as pd
path_docs = var_call_jieMGSj2N30Wp7FXYKYwFCCX
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = ' '.join(d['text'] for d in docs)
lines = [l.strip() for l in texts.split('\n') if l.strip()]
project_lines = []
for l in lines:
    if re.search(r'Project', l) or re.search(r'Improvements', l) or re.search(r'Repairs', l) or re.search(r'Resurfacing', l):
        project_lines.append(l)
path_fund = var_call_wkX3iZgNC5r1EdEixeWcjshU
with open(path_fund, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
disaster_mask = fund_df['Project_Name'].str.contains('FEMA', case=False, na=False) | fund_df['Project_Name'].str.contains('CalOES', case=False, na=False) | fund_df['Project_Name'].str.contains('CalJPIA', case=False, na=False) | fund_df['Project_Name'].str.contains('Disaster', case=False, na=False) | fund_df['Project_Name'].str.contains('Recovery', case=False, na=False)
start_2022_mask = fund_df['Project_Name'].str.contains('2022', na=False)
target_df = fund_df[disaster_mask & start_2022_mask].copy()
if target_df.empty:
    total = 0
else:
    target_df['Amount'] = pd.to_numeric(target_df['Amount'], errors='coerce').fillna(0)
    total = int(target_df['Amount'].sum())
result = {"total_funding_disaster_2022": total}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jieMGSj2N30Wp7FXYKYwFCCX': 'file_storage/call_jieMGSj2N30Wp7FXYKYwFCCX.json', 'var_call_wkX3iZgNC5r1EdEixeWcjshU': 'file_storage/call_wkX3iZgNC5r1EdEixeWcjshU.json'}

exec(code, env_args)

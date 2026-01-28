code = """import re, json, pandas as pd
path_civic = var_call_U7kOMfpDIhawztaDfw2UtvCq
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)
path_funding = var_call_432j1WT3jZgqIFOaNmGsA3A5
with open(path_funding, 'r') as f:
    funding = json.load(f)
texts = ' '.join(d.get('text','') for d in civic_docs)
fund_df = pd.DataFrame(funding)
fund_df['is_disaster_name'] = fund_df['Project_Name'].str.contains('(FEMA', case=False, regex=False) | fund_df['Project_Name'].str.contains('CalOES', case=False, regex=False) | fund_df['Project_Name'].str.contains('CalJPIA', case=False, regex=False)
start_2022_projects = set()
for pname in fund_df.loc[fund_df['is_disaster_name'], 'Project_Name']:
    if not isinstance(pname, str):
        continue
    pattern = re.escape(pname[:40])
    for m in re.finditer(pattern, texts):
        window = texts[max(0, m.start()-100): m.end()+100]
        if '2022' in window:
            start_2022_projects.add(pname)
            break
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'])
mask = fund_df['Project_Name'].isin(start_2022_projects)
total_funding = float(fund_df.loc[mask, 'Amount'].sum())
result = {"total_funding_2022_disaster_projects": total_funding, "projects": sorted(list(start_2022_projects))}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_U7kOMfpDIhawztaDfw2UtvCq': 'file_storage/call_U7kOMfpDIhawztaDfw2UtvCq.json', 'var_call_432j1WT3jZgqIFOaNmGsA3A5': 'file_storage/call_432j1WT3jZgqIFOaNmGsA3A5.json'}

exec(code, env_args)

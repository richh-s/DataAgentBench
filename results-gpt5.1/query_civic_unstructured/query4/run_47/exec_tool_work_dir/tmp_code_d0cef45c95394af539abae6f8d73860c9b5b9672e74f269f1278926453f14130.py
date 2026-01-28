code = """import re, json, pandas as pd

path_civic = var_call_pHnQz3v6mGoOrgx80X96CuAx
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]

projects = []
for text in texts:
    for line in text.split('\n'):
        s = line.strip()
        if not s:
            continue
        if ('Project' in s or 'Road' in s or 'Park' in s or 'Beach' in s or 'PCH' in s or 'Canyon' in s or 'Drain' in s or 'Water' in s or 'Warning' in s or 'Playground' in s or 'Bridge' in s):
            projects.append(s)

projects = list(dict.fromkeys(projects))

proj_info = {}
for text in texts:
    lines = text.split('\n')
    for i, line in enumerate(lines):
        name = line.strip()
        if name in projects:
            window = '\n'.join(lines[i:i+10])
            m = re.search(r'(Begin Construction|Start|Advertise):\s*(Spring 2022|2022 Spring|March 2022|April 2022|May 2022)', window, re.IGNORECASE)
            if m:
                proj_info[name] = 'Spring 2022'

spring22_projects = list(proj_info.keys())

path_fund = var_call_mH9K6jK11i7vw86LBTw7QrHm
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

matched = fund_df[fund_df['Project_Name'].isin(spring22_projects)].copy()

if matched.empty:
    rows = []
    for pn in spring22_projects:
        for _, row in fund_df.iterrows():
            if pn.lower() in row['Project_Name'].lower() or row['Project_Name'].lower() in pn.lower():
                rows.append(row)
    if rows:
        matched = pd.DataFrame(rows).drop_duplicates(subset=['Funding_ID'])

count_projects = int(matched['Project_Name'].nunique()) if not matched.empty else 0
total_funding = int(matched['Amount'].sum()) if not matched.empty else 0

result = {"projects_started_spring_2022": count_projects, "total_funding_spring_2022": total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pHnQz3v6mGoOrgx80X96CuAx': 'file_storage/call_pHnQz3v6mGoOrgx80X96CuAx.json', 'var_call_mH9K6jK11i7vw86LBTw7QrHm': 'file_storage/call_mH9K6jK11i7vw86LBTw7QrHm.json'}

exec(code, env_args)

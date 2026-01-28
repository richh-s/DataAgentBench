code = """import json
import pandas as pd
import re
with open(var_call_kmRIS19tRbLjbUjv7A8Phvxr, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_NtTvOxLuB398M5hJv6km8pV3, 'r', encoding='utf-8') as f:
    funding = json.load(f)
project_start_names = set()
for doc in docs:
    found = re.findall(r'([A-Za-z0-9 ,&/\'".\-]+)\n\s*(Begin Construction|Advertise|Start|Complete Design|Final Design)[^a-zA-Z0-9]*[:\-]?\s*(March|April|May)\s*2022', doc['text'], re.I)
    for item in found:
        proj_name = item[0].strip()
        project_start_names.add(proj_name)
funding_df = pd.DataFrame(funding)
started_projects = []
total_funding = 0
for proj_name in project_start_names:
    matched = funding_df[funding_df['Project_Name'].str.contains(proj_name[:12], case=False, na=False)]
    if len(matched):
        amt = matched['Amount'].astype(int).sum()
        total_funding += amt
        started_projects.append({'Project_Name': proj_name, 'Funding': int(amt)})
result = {'Spring_2022_Project_Count': len(started_projects), 'Total_Funding': total_funding, 'Projects': started_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kmRIS19tRbLjbUjv7A8Phvxr': 'file_storage/call_kmRIS19tRbLjbUjv7A8Phvxr.json', 'var_call_NtTvOxLuB398M5hJv6km8pV3': 'file_storage/call_NtTvOxLuB398M5hJv6km8pV3.json'}

exec(code, env_args)

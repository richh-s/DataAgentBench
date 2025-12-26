code = """import json
import pandas as pd
import re
with open(var_call_kmRIS19tRbLjbUjv7A8Phvxr, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_NtTvOxLuB398M5hJv6km8pV3, 'r', encoding='utf-8') as f:
    funding = json.load(f)
project_start_names = set()
for doc in docs:
    lines = doc['text'].split('\n')
    for i, line in enumerate(lines):
        if re.search(r'Project Schedule|Estimated Schedule|Updates|Description', line, re.I):
            desc = "\n".join(lines[i:i+10])
            found = re.findall(r'(Begin Construction|Advertise|Start|Complete Design|Final Design|Project start)[^a-zA-Z0-9]*[:\-]?\s*([A-Za-z]+)\s*(\d{4})', desc, re.I)
            for item in found:
                event, month, year = item
                if year == '2022' and month.strip().lower() in ['march','april','may']:
                    name = None
                    for j in range(i-1,max(i-10,0),-1):
                        candidate = lines[j].strip()
                        if candidate and re.search(r'(Project|Improvements|Repair|Study|Facility|Slope|Park|Road|Drainage|Retaining Wall|Walkway|Structure)', candidate, re.I):
                            name = candidate
                            break
                    if not name:
                        for j in range(i-1,max(i-10,0),-1):
                            if lines[j].strip():
                                name = lines[j].strip()
                                break
                    if name:
                        project_start_names.add(name)
funding_df = pd.DataFrame(funding)
started_projects = []
total_funding = 0
for proj_name in project_start_names:
    matched = funding_df[funding_df['Project_Name'].str.contains(proj_name[:15],case=False,na=False)]
    if len(matched):
        amt = matched['Amount'].astype(int).sum()
        total_funding += amt
        started_projects.append({'Project_Name': proj_name, 'Funding': int(amt)})
result = {'Spring_2022_Project_Count': len(started_projects), 'Total_Funding': total_funding, 'Projects': started_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kmRIS19tRbLjbUjv7A8Phvxr': 'file_storage/call_kmRIS19tRbLjbUjv7A8Phvxr.json', 'var_call_NtTvOxLuB398M5hJv6km8pV3': 'file_storage/call_NtTvOxLuB398M5hJv6km8pV3.json'}

exec(code, env_args)

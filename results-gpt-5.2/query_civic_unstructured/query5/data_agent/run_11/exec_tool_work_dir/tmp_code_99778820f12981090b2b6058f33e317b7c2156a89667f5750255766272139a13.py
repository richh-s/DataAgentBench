code = """import json
import pandas as pd
import re

with open(var_call_ivRvrB6C6c4E1YIc1nGaYvPo, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

with open(var_call_AkQRhbxir44oE575dYS4n4Rj, 'r') as f:
    docs = json.load(f)

projects = set()

begin_pat = re.compile('Begin\\s+Construction\\s*:\\s*([^\\n\\r]+)', re.IGNORECASE)
header_pat = re.compile('^\\s*([A-Za-z0-9][A-Za-z0-9&/\\-\\(\\)\\.,\\s]{3,})\\s*$', re.MULTILINE)

for d in docs:
    text = d.get('text','')
    if 'disaster recovery projects' not in text.lower():
        continue
    lines = text.splitlines()
    current_project = None
    in_disaster = False
    for line in lines:
        if re.search('Disaster\\s+Recovery\\s+Projects', line, re.IGNORECASE):
            in_disaster = True
            current_project = None
            continue
        if in_disaster and re.search('Capital\\s+Improvement\\s+Projects', line, re.IGNORECASE):
            in_disaster = False
            current_project = None
            continue
        if not in_disaster:
            continue

        m = header_pat.match(line)
        if m:
            name = m.group(1).strip()
            lowname = name.lower()
            if ('updates' in lowname) or ('project schedule' in lowname) or ('estimated schedule' in lowname) or ('project description' in lowname) or ('page' in lowname) or ('agenda item' in lowname):
                continue
            current_project = name
            continue

        bm = begin_pat.search(line)
        if bm and current_project:
            if '2022' in bm.group(1):
                projects.add(current_project)

# sum funding
total = 0
missing = []
for p in sorted(projects):
    if p in fund_map:
        total += int(fund_map[p])
    else:
        missing.append(p)

out = {
    'projects_started_2022_disaster': sorted(projects),
    'project_count': len(projects),
    'total_funding': total,
    'missing_in_funding_table': missing
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_yAUEJ8JKx4IeDyLqvdXX7Jdg': ['Funding'], 'var_call_R0TM1H3XPtIHjyIdLKkamUlz': ['civic_docs'], 'var_call_ivRvrB6C6c4E1YIc1nGaYvPo': 'file_storage/call_ivRvrB6C6c4E1YIc1nGaYvPo.json', 'var_call_AkQRhbxir44oE575dYS4n4Rj': 'file_storage/call_AkQRhbxir44oE575dYS4n4Rj.json'}

exec(code, env_args)

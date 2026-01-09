code = """import json, re
import pandas as pd

# load funding per project
with open(var_call_ivRvrB6C6c4E1YIc1nGaYvPo, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# load docs
with open(var_call_AkQRhbxir44oE575dYS4n4Rj, 'r') as f:
    docs = json.load(f)

projects = set()

begin_pat = re.compile(r"Begin\s+Construction\s*:\s*([^\n\r]+)", re.IGNORECASE)
header_pat = re.compile(r"^\s*([A-Za-z0-9][A-Za-z0-9&/\-\(\)\.,\s]{3,})\s*$")

for d in docs:
    text = d.get('text','')
    if 'disaster recovery projects' not in text.lower():
        continue
    lines = text.splitlines()
    current_project = None
    in_disaster = False
    for line in lines:
        if re.search(r"Disaster\s+Recovery\s+Projects", line, re.IGNORECASE):
            in_disaster = True
            current_project = None
            continue
        if in_disaster and re.search(r"Capital\s+Improvement\s+Projects", line, re.IGNORECASE):
            in_disaster = False
            current_project = None
            continue
        if not in_disaster:
            continue

        m = header_pat.match(line)
        if m:
            name = m.group(1).strip()
            if any(kw in name.lower() for kw in ['updates', 'project schedule', 'estimated schedule', 'project description', 'page', 'agenda item']):
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
    amt = fund_map.get(p)
    if amt is None:
        missing.append(p)
    else:
        total += int(amt)

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

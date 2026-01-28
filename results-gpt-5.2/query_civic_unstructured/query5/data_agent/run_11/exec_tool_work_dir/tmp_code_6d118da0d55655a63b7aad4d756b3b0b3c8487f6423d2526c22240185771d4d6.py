code = """import json, re
import pandas as pd

# load funding per project
path = var_call_ivRvrB6C6c4E1YIc1nGaYvPo
with open(path, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# load docs
doc_path = var_call_AkQRhbxir44oE575dYS4n4Rj
with open(doc_path, 'r') as f:
    docs = json.load(f)

# extract disaster recovery section project names with Begin/Start in 2022
projects = set()

begin_pat = re.compile(r'Begin\s+Construction\s*:\s*([^\n\r]+)', re.IGNORECASE)
# project header lines: not bullet, not empty
header_pat = re.compile(r'^\s*([A-Za-z0-9][A-Za-z0-9&/\-\(\)\'\.,\s]{3,})\s*$')

for d in docs:
    text = d.get('text','')
    # focus on Disaster Recovery Projects section if present
    low = text.lower()
    if 'disaster recovery projects' not in low:
        continue
    # split lines
    lines = text.splitlines()
    current_project = None
    in_disaster = False
    for line in lines:
        l = line.strip()
        if re.search(r'Disaster\s+Recovery\s+Projects', line, re.IGNORECASE):
            in_disaster = True
            current_project = None
            continue
        if in_disaster and re.search(r'Capital\s+Improvement\s+Projects', line, re.IGNORECASE):
            # if it switches back, stop disaster section
            in_disaster = False
            current_project = None
            continue
        if not in_disaster:
            continue
        # detect project header
        m = header_pat.match(line)
        if m:
            name = m.group(1).strip()
            # filter out obvious non-project labels
            if any(kw.lower() in name.lower() for kw in ['updates', 'project schedule', 'estimated schedule', 'project description', 'page', 'agenda item']):
                continue
            current_project = name
            continue
        # capture begin construction lines
        bm = begin_pat.search(line)
        if bm and current_project:
            val = bm.group(1)
            if '2022' in val:
                projects.add(current_project)

# compute total funding for those projects
total = 0
missing = []
for p in sorted(projects):
    amt = fund_map.get(p)
    if amt is None:
        missing.append(p)
        continue
    total += amt

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

code = """import json, re, pandas as pd
from collections import defaultdict

path = var_call_K3KXjQh9w3HEgCDVXJEEb6a0
with open(path, 'r') as f:
    records = json.load(f)

def extract_field(text, field):
    m = re.search(field + r"\s*:\s*([^,;]+)", text)
    return m.group(1).strip() if m else None

citing_assignee_cpcs = defaultdict(set)

for rec in records:
    info = rec.get('Patents_info','') or ''
    citation = rec.get('citation','') or ''
    cpc_raw = rec.get('cpc','') or ''
    assignee = extract_field(info, 'assignee_harmonized')
    if not assignee or assignee.upper() == 'UNIV CALIFORNIA':
        continue
    if 'UNIV CALIFORNIA' not in citation.upper():
        continue
    try:
        cpc_list = json.loads(cpc_raw)
        for entry in cpc_list:
            code = entry.get('code')
            if code:
                primary = code.split('/')[0]  # primary subclass like A61P43
                citing_assignee_cpcs[assignee].add(primary)
    except Exception:
        continue

rows = []
for assignee, codes in citing_assignee_cpcs.items():
    for code in codes:
        rows.append({'assignee': assignee, 'cpc_primary': code})

result = json.dumps(rows)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_K3KXjQh9w3HEgCDVXJEEb6a0': 'file_storage/call_K3KXjQh9w3HEgCDVXJEEb6a0.json', 'var_call_s79vsoBXvvq8h7VP5lebbykk': ['cpc_definition']}

exec(code, env_args)

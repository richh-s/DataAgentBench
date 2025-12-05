code = """import json, re, pandas as pd
from pathlib import Path

path = Path(var_call_tIG3ikT6XSN8iFYcew9K0o1H)
rows = json.loads(path.read_text())

uc_pub_nums = set()
for r in rows:
    m = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', r['Patents_info'])
    if m:
        uc_pub_nums.add(m.group(1))

citing = []
for r in rows:
    cits = json.loads(r['citation']) if r['citation'] else []
    for c in cits:
        pn = c.get('publication_number','')
        if pn in uc_pub_nums:
            citing.append(r)
            break

pubs = []
for r in citing:
    m = re.search(r'owned by ([^,]+)|assigned to ([^,]+)|is owned by ([^,]+)|holds the .* patent filing .* is (?:owned by|assigned to) ([^,]+)', r['Patents_info'])
    assignee = None
    if m:
        assignee = next((g for g in m.groups() if g), None)
    if not assignee:
        m2 = re.search(r'is owned by ([^,]+)', r['Patents_info'])
        assignee = m2.group(1) if m2 else 'UNKNOWN'
    if assignee == 'UNIV CALIFORNIA':
        continue
    cpcs = [e['code'] for e in json.loads(r['cpc'])] if r['cpc'] else []
    pubs.append({'assignee': assignee, 'cpc_codes': sorted(set(cpcs))})

uniq_cpc = sorted({c for p in pubs for c in p['cpc_codes']})

result = {'pubs': pubs, 'cpc_codes': uniq_cpc}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rOH1fvrOQvwxXi9hckgeykfm': [], 'var_call_tIG3ikT6XSN8iFYcew9K0o1H': 'file_storage/call_tIG3ikT6XSN8iFYcew9K0o1H.json'}

exec(code, env_args)

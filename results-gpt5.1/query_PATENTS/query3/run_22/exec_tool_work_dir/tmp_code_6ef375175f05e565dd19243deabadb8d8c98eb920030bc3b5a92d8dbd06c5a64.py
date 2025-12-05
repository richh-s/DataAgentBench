code = """import json, re, pandas as pd
from collections import defaultdict

# load full publication records
data_path = var_call_hNRNBrmaOApqE5tdVYtDesCO
with open(data_path, 'r') as f:
    pubs = json.load(f)

# helper to extract field from Patents_info
assignee_re = re.compile(r"assignee_harmonized: ([^;]+)")
pubnum_re = re.compile(r"pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")

uc_pubnums = set()
for rec in pubs:
    txt = rec.get('Patents_info','')
    if 'UNIV CALIFORNIA' in txt:
        m = pubnum_re.search(txt)
        if m:
            uc_pubnums.add(m.group(1))

# map cited publication_number -> list of citing assignees
cited_to_assignees = defaultdict(set)

for rec in pubs:
    txt = rec.get('Patents_info','')
    m = assignee_re.search(txt)
    assignee = m.group(1).strip() if m else None
    if not assignee or assignee == 'UNIV CALIFORNIA':
        continue
    cits = rec.get('citation')
    if not cits:
        continue
    try:
        cit_list = json.loads(cits)
    except Exception:
        continue
    for c in cit_list:
        pn = c.get('publication_number')
        if pn in uc_pubnums:
            cited_to_assignees[pn].add(assignee)

# collect CPC codes for those UC patents
uc_cpc_codes = set()
for rec in pubs:
    txt = rec.get('Patents_info','')
    if 'UNIV CALIFORNIA' not in txt:
        continue
    m = pubnum_re.search(txt)
    if not m or m.group(1) not in cited_to_assignees:
        continue
    cpc_raw = rec.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code')
        if code:
            main = code.split('/')[0]
            uc_cpc_codes.add(main)

result = {
    'assignees': sorted({a for s in cited_to_assignees.values() for a in s}),
    'cpc_prefixes': sorted(uc_cpc_codes)
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_ZBI9ZXoZLND1G2qDMJQYdqJw': [], 'var_call_fZDuaKrInpBzwUf1065tfuCD': ['cpc_definition'], 'var_call_28iB90Doj8fvuirwzsyMQi1v': [], 'var_call_hNRNBrmaOApqE5tdVYtDesCO': 'file_storage/call_hNRNBrmaOApqE5tdVYtDesCO.json'}

exec(code, env_args)

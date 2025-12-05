code = """import json, re, os, pandas as pd
from collections import defaultdict

path = var_call_GcgdKa1X4HhkIjOrceK8ChVB
with open(path, 'r') as f:
    uc_records = json.load(f)

# Build index of publication_number -> assignee and cpc codes
pubnum_to_assignee = {}
pubnum_to_cpc = {}

for rec in uc_records:
    info = rec.get('Patents_info','')
    # extract publication_number like XX-########-X? using pattern from examples
    m = re.search(r'pub(?:lication)?\. number ([A-Z]{2}-[0-9]{7,}-[A-Z0-9]+)', info)
    if not m:
        m = re.search(r'publication number ([A-Z]{2}-[0-9]{7,}-[A-Z0-9]+)', info)
    pubnum = m.group(1) if m else None
    # extract assignee_harmonized textual name
    m2 = re.search(r'assigned to ([^,.]+)', info)
    if not m2:
        m2 = re.search(r'owned by ([^,.]+)', info)
    if not m2:
        m2 = re.search(r'holds the .* patent filing .* is (?:owned by|assigned to) ([^,.]+)', info)
    assignee = m2.group(1).strip() if m2 else None
    if pubnum:
        pubnum_to_assignee[pubnum] = assignee or ''
        # parse CPC JSON-like
        cpc_raw = rec.get('cpc') or '[]'
        try:
            cpc_list = json.loads(cpc_raw)
        except Exception:
            cpc_list = []
        codes = [c.get('code') for c in cpc_list if isinstance(c, dict) and c.get('code')]
        pubnum_to_cpc[pubnum] = codes

# Now find all records (any assignee) that cite these pub numbers
uc_pubnums = set(pubnum_to_cpc.keys())

# Need all publications to search citations
# we'll query in chunks is not possible here; assume entire table manageable? can't, no db here.

result = {
  'uc_pubnums_count': len(uc_pubnums),
  'sample_uc_pubnums': list(sorted(uc_pubnums))[:20]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Ijko1UaGGrO3rtkNna7l73Xh': [], 'var_call_UHxHWy8PsHjioiUEVUN1Ygcf': ['cpc_definition'], 'var_call_GcgdKa1X4HhkIjOrceK8ChVB': 'file_storage/call_GcgdKa1X4HhkIjOrceK8ChVB.json'}

exec(code, env_args)

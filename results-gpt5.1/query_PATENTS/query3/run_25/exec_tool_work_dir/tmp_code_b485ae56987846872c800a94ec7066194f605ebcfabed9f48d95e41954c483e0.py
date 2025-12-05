code = """import json, re, pandas as pd
from collections import defaultdict

path = var_call_r9o3TYrRDVmSSaniDTMva2bM
with open(path, 'r') as f:
    data = json.load(f)

# Build mapping: cited publication_number -> set of CPC primary subclasses from UC patents
# Extract UC publication numbers from Patents_info, map their primary CPC subclasses
uc_pub_to_primary_cpc = {}
for rec in data:
    info = rec.get('Patents_info','')
    m = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', info)
    if not m:
        continue
    pubnum = m.group(1)
    cpc_raw = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    # primary CPC subclasses: take codes where first==true OR just first code
    prim_codes = [c['code'] for c in cpcs if c.get('first')]
    if not prim_codes and cpcs:
        prim_codes = [cpcs[0].get('code')]
    # reduce to subclasses (up to first digit group after /), but we'll keep full code; subclass meaning up to group, but CPCDefinition table matches full symbols
    uc_pub_to_primary_cpc[pubnum] = prim_codes

# Now find all records where citations include any of these UC publication numbers; but our citation field for UC patents references others, not cited-by.
# We actually need the reverse: publications whose citations include patents assigned to UC, i.e., Patents_info contains assignee != UC but their citation list contains a pub number that we know is UC.

# So first get set of UC publication numbers from above mapping
uc_pub_set = set(uc_pub_to_primary_cpc.keys())

# Load all publications to search citing ones
# We don't have them all yet; will handle in DB query later, just pass UC pub numbers & CPC codes now
result = {
    'uc_publications': sorted(list(uc_pub_set))[:200],
    'uc_pub_to_primary_cpc_example': {k: uc_pub_to_primary_cpc[k] for k in list(uc_pub_to_primary_cpc)[:20]}
}

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_r9o3TYrRDVmSSaniDTMva2bM': 'file_storage/call_r9o3TYrRDVmSSaniDTMva2bM.json'}

exec(code, env_args)

code = """import json, re, pandas as pd
from collections import defaultdict

path = var_call_zw2OkQi2sQ2HRBVNRq9luScX
with open(path, 'r') as f:
    data = json.load(f)

# Build map from cited publication_number -> set of CPC codes of UC patents
cited_to_uc_cpcs = defaultdict(set)

pubnum_re = re.compile(r"pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")

for rec in data:
    info = rec.get('Patents_info','')
    if 'UNIV CALIFORNIA' not in info:
        continue
    m = pubnum_re.search(info)
    if not m:
        continue
    pubnum = m.group(1)
    try:
        cpcs = json.loads(rec.get('cpc') or '[]')
    except Exception:
        continue
    codes = {c.get('code') for c in cpcs if isinstance(c, dict) and c.get('code')}
    for code in codes:
        cited_to_uc_cpcs[pubnum].add(code)

# Now scan all publications to find those citing these UC pub numbers
assignee_re = re.compile(r"assignee_harmonized: ([^,.;]+)")

assignee_to_cpc = defaultdict(set)

for rec in data:
    info = rec.get('Patents_info','')
    m = assignee_re.search(info)
    if not m:
        continue
    assignee = m.group(1).strip()
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    try:
        cites = json.loads(rec.get('citation') or '[]')
    except Exception:
        continue
    cited_pubnums = {c.get('publication_number') for c in cites if isinstance(c, dict) and c.get('publication_number')}
    overlap = cited_pubnums & cited_to_uc_cpcs.keys()
    if not overlap:
        continue
    # collect all CPC codes associated with those UC citations
    for pub in overlap:
        assignee_to_cpc[assignee].update(cited_to_uc_cpcs[pub])

# Get unique CPC codes
all_cpc_codes = sorted({code for codes in assignee_to_cpc.values() for code in codes})

result = {
    'assignee_to_cpc': {k: sorted(v) for k,v in assignee_to_cpc.items()},
    'all_cpc_codes': all_cpc_codes
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_kQYnU7tJHqBn36sSfz6vzpXt': [], 'var_call_zw2OkQi2sQ2HRBVNRq9luScX': 'file_storage/call_zw2OkQi2sQ2HRBVNRq9luScX.json'}

exec(code, env_args)

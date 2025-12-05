code = """import json, re, pandas as pd
from collections import defaultdict

# Load full result from file
path = var_call_1snbLZrwqw5zwPruiTtkkfkD
with open(path, 'r') as f:
    pubs = json.load(f)

# Build map from cited publication_number -> set of citing assignees and their CPC codes
cited_to_assignees = defaultdict(lambda: {"assignees": set(), "cpcs": set()})

for rec in pubs:
    info = rec.get('Patents_info','')
    m = re.search(r'assignee_harmonized: ([^;,]+)', info)
    if not m:
        # fallback: sometimes phrased as "is owned by X" or "is assigned to X"
        m2 = re.search(r'is owned by ([^.,]+)', info)
        m3 = re.search(r'is assigned to ([^.,]+)', info)
        assignee = (m2 or m3).group(1).strip() if (m2 or m3) else None
    else:
        assignee = m.group(1).strip()
    
    if not assignee or 'UNIV CALIFORNIA' in assignee:
        continue

    # parse CPC list
    cpc_raw = rec.get('cpc') or '[]'
    try:
        cpcs = [e.get('code') for e in json.loads(cpc_raw) if isinstance(e, dict) and e.get('code')]
    except Exception:
        cpcs = []

    # citations
    cit_raw = rec.get('citation') or '[]'
    try:
        cits = json.loads(cit_raw)
    except Exception:
        cits = []

    for c in cits:
        if not isinstance(c, dict):
            continue
        pubnum = c.get('publication_number')
        if not pubnum:
            continue
        key = pubnum.strip()
        cited_to_assignees[key]['assignees'].add(assignee)
        for code in cpcs:
            cited_to_assignees[key]['cpcs'].add(code)

# We don't actually know which cited publication_numbers are UNIV CALIFORNIA; the DB lacks assignee for cited docs.
# Without a linkage table, we cannot reliably filter to "patents assigned to UNIV CALIFORNIA".

result = {
  'num_cited_pubnums': len(cited_to_assignees),
  'sample': list(sorted(cited_to_assignees.items()))[:5]
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8dKSIr5pS0lAe6Xpngm79Q4C': [], 'var_call_1snbLZrwqw5zwPruiTtkkfkD': 'file_storage/call_1snbLZrwqw5zwPruiTtkkfkD.json'}

exec(code, env_args)

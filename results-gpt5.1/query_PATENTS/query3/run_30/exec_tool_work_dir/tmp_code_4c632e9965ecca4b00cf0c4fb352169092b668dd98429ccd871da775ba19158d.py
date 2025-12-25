code = """import json, pandas as pd, re
from collections import defaultdict

path = var_call_YjZBvAwQe3rgx01BT4bHfuzM
with open(path, 'r') as f:
    data = json.load(f)

# Build map from publication_number -> (assignee, cpc list)
patent_map = {}
for row in data:
    info = row.get('Patents_info','')
    cpc_raw = row.get('cpc','[]')
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        cpc_list = []
    # extract publication_number and assignee_harmonized from Patents_info
    pub_match = re.search(r'pub\.? number ([A-Z0-9\-]+)', info)
    if not pub_match:
        pub_match = re.search(r'publication number ([A-Z0-9\-]+)', info)
    pub_no = pub_match.group(1) if pub_match else None
    assignee_match = re.search(r'assigned to ([A-Z0-9\s]+?) and has', info)
    if not assignee_match:
        assignee_match = re.search(r'owned by ([A-Z0-9\s]+?) and has', info)
    if not assignee_match:
        assignee_match = re.search(r'holds the .* filing .*?, with pub\. number', info)
    assignee = assignee_match.group(1).strip() if assignee_match and 'holds' not in assignee_match.group(0) else 'UNIV CALIFORNIA'
    if pub_no:
        patent_map[pub_no] = {'assignee': assignee, 'cpc_codes': [c.get('code') for c in cpc_list if isinstance(c, dict) and c.get('first')]}

# Now, find citing patents (any assignee) that cite these UNIV CALIFORNIA patents

# First, build set of UC publication numbers
uc_pubs = set(patent_map.keys())

# We need to scan entire publicationinfo to find citations; assume this subset is whole DB for this exercise
citing_assignee_to_cpc = defaultdict(set)

for row in data:
    info = row.get('Patents_info','')
    citation_raw = row.get('citation','[]')
    try:
        cites = json.loads(citation_raw)
    except Exception:
        cites = []
    # assignee of this citing patent
    assignee_match = re.search(r'assigned to ([A-Z0-9\s]+?) and has', info)
    if not assignee_match:
        assignee_match = re.search(r'owned by ([A-Z0-9\s]+?) and has', info)
    assignee = assignee_match.group(1).strip() if assignee_match else None
    if not assignee or assignee == 'UNIV CALIFORNIA':
        continue
    # this patent's CPC first codes
    cpc_raw = row.get('cpc','[]')
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        cpc_list = []
    first_codes = [c.get('code') for c in cpc_list if isinstance(c, dict) and c.get('first')]
    if not first_codes:
        continue
    # check citations
    cites_uc = False
    for c in cites:
        if not isinstance(c, dict):
            continue
        pub_no = c.get('publication_number')
        if pub_no in uc_pubs:
            cites_uc = True
            break
    if cites_uc:
        for code in first_codes:
            citing_assignee_to_cpc[assignee].add(code)

result = {k: sorted(list(v)) for k,v in citing_assignee_to_cpc.items()}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mbacTag8rIrHZj5GUEha5jXN': [], 'var_call_YjZBvAwQe3rgx01BT4bHfuzM': 'file_storage/call_YjZBvAwQe3rgx01BT4bHfuzM.json'}

exec(code, env_args)

code = """import json, re, pandas as pd
from collections import defaultdict

# load full result
path = var_call_B4KXSGXZWYvvHW4m0vfpK9Fy
with open(path, 'r') as f:
    data = json.load(f)

# helper to extract assignee and publication number from Patents_info
assignee_re = re.compile(r'assigned to ([^.,]+)|owned by ([^.,]+)|holds the [^,]+, with', re.IGNORECASE)
pubnum_re = re.compile(r'pub(?:lication)?\. number ([A-Z0-9\-]+)', re.IGNORECASE)

records = []
for row in data:
    info = row.get('Patents_info','')
    m_pub = pubnum_re.search(info)
    if not m_pub:
        continue
    pubnum = m_pub.group(1)
    m_ass = assignee_re.search(info)
    assignee = None
    if m_ass:
        assignee = m_ass.group(1) or m_ass.group(2) or 'UNIV CALIFORNIA'
    else:
        if 'UNIV CALIFORNIA' in info:
            assignee = 'UNIV CALIFORNIA'
    cits = json.loads(row.get('citation','[]')) if row.get('citation') else []
    for c in cits:
        cited_pub = c.get('publication_number')
        if cited_pub:
            records.append({'citing_pubnum': pubnum, 'citing_assignee': assignee, 'cited_pubnum': cited_pub})

# now we need to know which of the cited_pubnum are UNIV CALIFORNIA patents

# get all patents to map pubnum -> assignee + cpc
all_rows = data
pub_assignee = {}
pub_cpc = {}

for row in all_rows:
    info = row.get('Patents_info','')
    m_pub = pubnum_re.search(info)
    if not m_pub:
        continue
    pubnum = m_pub.group(1)
    m_ass = assignee_re.search(info)
    assignee = None
    if m_ass:
        assignee = m_ass.group(1) or m_ass.group(2) or 'UNIV CALIFORNIA'
    else:
        if 'UNIV CALIFORNIA' in info:
            assignee = 'UNIV CALIFORNIA'
    pub_assignee[pubnum] = assignee
    cpc_list = []
    if row.get('cpc'):
        try:
            cpc_list = [e['code'] for e in json.loads(row['cpc'])]
        except Exception:
            cpc_list = []
    pub_cpc[pubnum] = cpc_list

filtered = []
for r in records:
    cited_assignee = pub_assignee.get(r['cited_pubnum'])
    if cited_assignee == 'UNIV CALIFORNIA' and r['citing_assignee'] and r['citing_assignee'].upper() != 'UNIV CALIFORNIA':
        cpc_codes = pub_cpc.get(r['cited_pubnum'], [])
        filtered.append({'citing_assignee': r['citing_assignee'], 'cited_pubnum': r['cited_pubnum'], 'cpc_codes': cpc_codes})

# collect unique CPC primary subclasses (take first four chars before slash as subclass, e.g., C12Q)
assignee_to_cpc = defaultdict(set)
for rec in filtered:
    for code in rec['cpc_codes']:
        main = code.split('/')[0]
        assignee_to_cpc[rec['citing_assignee']].add(main)

# prepare list of unique cpc symbols to look up
all_cpc_symbols = sorted({c for s in assignee_to_cpc.values() for c in s})

result = {
    'assignee_to_cpc': {k: sorted(list(v)) for k, v in assignee_to_cpc.items()},
    'cpc_symbols': all_cpc_symbols
}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_AbPT7Pv5fvctnS4fLEe123DK': [], 'var_call_B4KXSGXZWYvvHW4m0vfpK9Fy': 'file_storage/call_B4KXSGXZWYvvHW4m0vfpK9Fy.json'}

exec(code, env_args)

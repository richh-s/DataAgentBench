code = """import json, re, pandas as pd
from collections import defaultdict

# Load full publicationinfo data from file
path = var_call_xckr1i1D5fEFUTr8EWe3CbOa
with open(path, 'r') as f:
    pubs = json.load(f)

# Helper to get assignee and publication number from Patents_info
assignee_re = re.compile(r"owned by ([A-Z0-9 &.-]+)|holds the [A-Z]{2} patent application.*? is (?:owned by|belonging to) ([A-Z0-9 &.-]+)|is assigned to ([A-Z0-9 &.-]+)|is belonging to ([A-Z0-9 &.-]+)|holds the [A-Z]{2} patent filing .*? is (?:owned by|belonging to) ([A-Z0-9 &.-]+)|holds the .*? application .*? is (?:owned by|belonging to) ([A-Z0-9 &.-]+)|is owned by ([A-Z0-9 &.-]+)|holds the .*? patent filing .*? owned by ([A-Z0-9 &.-]+)")
pubnum_re = re.compile(r"pub(?:lication)?(?: no\.| number)? ([A-Z0-9-]+)")

pubnum_to_assignee = {}
for rec in pubs:
    info = rec.get('Patents_info','') or ''
    m_pub = pubnum_re.search(info)
    pubnum = m_pub.group(1) if m_pub else None
    m_a = assignee_re.search(info)
    assignee = None
    if m_a:
        for g in m_a.groups():
            if g:
                assignee = g.strip()
                break
    if pubnum and assignee:
        pubnum_to_assignee[pubnum] = assignee

# Identify publications assigned to UNIV CALIFORNIA
uc_pubnums = set(pn for pn, a in pubnum_to_assignee.items() if a == 'UNIV CALIFORNIA')

# Build mapping from cited pubnum to list of citing pub records
cited_to_citers = defaultdict(list)
for rec in pubs:
    cstr = rec.get('citation') or '[]'
    try:
        cites = json.loads(cstr)
    except Exception:
        continue
    for c in cites:
        pn = c.get('publication_number')
        if pn:
            cited_to_citers[pn].append(rec)

# Find citations where the cited patent is UNIV CALIFORNIA
citing_records = []
for uc_pn in uc_pubnums:
    for citer in cited_to_citers.get(uc_pn, []):
        citing_records.append(citer)

# Deduplicate citing records
seen_ids = set()
unique_citers = []
for rec in citing_records:
    key = rec['Patents_info']
    if key not in seen_ids:
        seen_ids.add(key)
        unique_citers.append(rec)

# For each citing record, get assignee and its CPC codes (primary subclasses: first=true & inventive=true)
rows = []
for rec in unique_citers:
    info = rec.get('Patents_info','')
    m_a = assignee_re.search(info)
    assignee = None
    if m_a:
        for g in m_a.groups():
            if g:
                assignee = g.strip()
                break
    if not assignee or assignee == 'UNIV CALIFORNIA':
        continue
    cpc_raw = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    primary_codes = sorted({e['code'] for e in cpcs if e.get('first') and e.get('inventive')})
    if not primary_codes:
        continue
    for code in primary_codes:
        rows.append({'assignee': assignee, 'cpc_code': code})

# Aggregate unique assignee-CPC combinations
if not rows:
    result = []
else:
    df = pd.DataFrame(rows).drop_duplicates().reset_index(drop=True)
    result = df.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rZyI0PYPFhMBk1ZnKKGsrI0i': [], 'var_call_QW69BrUPfp9UBdp1tq3BXWz6': 'file_storage/call_QW69BrUPfp9UBdp1tq3BXWz6.json', 'var_call_kll6HsC5D4gul1A3oekIQJSE': 'file_storage/call_kll6HsC5D4gul1A3oekIQJSE.json', 'var_call_xckr1i1D5fEFUTr8EWe3CbOa': 'file_storage/call_xckr1i1D5fEFUTr8EWe3CbOa.json'}

exec(code, env_args)

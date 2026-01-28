code = """import json
import re

# Load the publication_database query result
path = var_call_5Sz553TW5TdZm9NFNJo3EnYY
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

pubno_to_assignee = {}

def extract_pubno(s):
    if not s:
        return None
    # common pattern like US-11081687-B2 or JP-2000012031-A
    m = re.search(r"\b[A-Z]{2}-[0-9]{4,}[A-Z0-9-]*\b", s)
    if m:
        return m.group(0)
    # fallback: look for 'publication number' phrase
    m = re.search(r"publication number\s*([A-Z0-9-]+)", s, re.I)
    if m:
        return m.group(1)
    return None

def extract_assignee(s):
    if not s:
        return None
    s = s.strip()
    # Try patterns
    m = re.match(r'^([A-Z0-9 &.,\-]{3,}?)\s+holds\b', s)
    if m:
        return m.group(1).strip().upper()
    m = re.search(r'Assigned to\s+([^,\(\.]+)', s, re.I)
    if m:
        return m.group(1).strip().upper()
    m = re.search(r'Assignee[:\s]+([^,\(\.]+)', s, re.I)
    if m:
        return m.group(1).strip().upper()
    # fallback: take leading all-caps sequence
    m = re.match(r'^([A-Z][A-Z0-9 &.,\-]{2,})', s)
    if m:
        return m.group(1).strip().upper()
    return s.upper()

for rec in data:
    info = rec.get('Patents_info') or ''
    pubno = extract_pubno(info)
    assignee = extract_assignee(info)
    if pubno:
        pubno_to_assignee[pubno] = assignee

# Identify publication numbers assigned to Univ California
uc_pubnos = set()
for pub, asg in pubno_to_assignee.items():
    if asg and 'CALIFORNIA' in asg and (('UNIV' in asg) or ('UNIVERSITY' in asg) or ('REGENTS' in asg)):
        uc_pubnos.add(pub)

# Now find citing records that cite any of these uc_pubnos
pairs = set()
for rec in data:
    citations_raw = rec.get('citation') or '[]'
    try:
        citations = json.loads(citations_raw)
    except Exception:
        # try to fix single quotes
        try:
            citations = json.loads(citations_raw.replace("'", '"'))
        except Exception:
            citations = []
    cited_pubnos = set()
    for c in citations:
        pn = c.get('publication_number') if isinstance(c, dict) else None
        if pn:
            cited_pubnos.add(pn)
    if not (cited_pubnos & uc_pubnos):
        continue
    # parse citing assignee
    citing_assignee = extract_assignee(rec.get('Patents_info',''))
    # skip if citing assignee is UC
    if citing_assignee and 'CALIFORNIA' in citing_assignee and (('UNIV' in citing_assignee) or ('UNIVERSITY' in citing_assignee) or ('REGENTS' in citing_assignee)):
        continue
    # parse primary cpc
    cpc_raw = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        try:
            cpcs = json.loads(cpc_raw.replace("'", '"'))
        except Exception:
            cpcs = []
    primary_code = None
    for item in cpcs:
        if isinstance(item, dict) and item.get('first'):
            primary_code = item.get('code')
            break
    if not primary_code and cpcs:
        # fallback to first code
        if isinstance(cpcs[0], dict):
            primary_code = cpcs[0].get('code')
    if citing_assignee and primary_code:
        pairs.add((citing_assignee, primary_code))

# Prepare result list
result = []
for asg, code in sorted(pairs):
    result.append({'assignee': asg, 'cpc_code': code})

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_5Sz553TW5TdZm9NFNJo3EnYY': 'file_storage/call_5Sz553TW5TdZm9NFNJo3EnYY.json'}

exec(code, env_args)

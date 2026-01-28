code = """import json, re
path = var_call_F0o6KLAYCTaTzUnkOyFIfKph
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

pubnum_re = re.compile(r'[A-Z]{2,}-[0-9]{4,}[0-9A-Z\-]*')

def extract_assignee(s):
    if not s:
        return None
    s = s.strip()
    m = re.search(r'owned by\s+([^,\.]+)', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'is owned by\s+([^,\.]+)', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'held by\s+([^,\.]+)', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'([^,\.]+?)\s+holds the', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'([^,\.]+?)\s+has pub', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    if ',' in s:
        return s.split(',')[0].strip()
    return ' '.join(s.split()[:6])

def is_univ_california(name):
    if not name:
        return False
    up = name.upper()
    return ('CALIFORNIA' in up) and (('UNIV' in up) or ('UNIVERSITY' in up))

# Build pubnum -> info mapping
pub_map = {}
for row in data:
    info = row.get('Patents_info') or ''
    assignee = extract_assignee(info)
    # find all pubnum-like tokens in info
    matches = pubnum_re.findall(info)
    # parse primary cpc codes
    cpc_field = row.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        cpcs = []
    primary_codes = [e.get('code') for e in cpcs if isinstance(e, dict) and e.get('first') and e.get('code')]
    primary_codes = sorted(list(set(primary_codes)))
    for m in matches:
        pub_map[m] = {'assignee': assignee, 'primary_codes': primary_codes, 'rowid': row.get('rowid')}

# Identify target publication numbers assigned to Univ California
target_pubnums = {p for p,info in pub_map.items() if is_univ_california(info.get('assignee'))}

citing_map = {}
for row in data:
    info = row.get('Patents_info') or ''
    citing_assignee = extract_assignee(info) or 'UNKNOWN'
    # parse citations
    citation_field = row.get('citation') or '[]'
    try:
        citations = json.loads(citation_field)
    except Exception:
        citations = []
    codes = set()
    cited_any = False
    for c in citations:
        cited_pub = c.get('publication_number')
        if not cited_pub:
            continue
        if cited_pub in target_pubnums:
            cited_any = True
            pcs = pub_map.get(cited_pub, {}).get('primary_codes', [])
            for pc in pcs:
                if pc:
                    codes.add(pc)
    if cited_any:
        if is_univ_california(citing_assignee):
            continue
        if citing_assignee not in citing_map:
            citing_map[citing_assignee] = set()
        citing_map[citing_assignee].update(codes)

unique_codes = sorted(list({c for codes in citing_map.values() for c in codes}))
result = {'citing_map': {k: sorted(list(v)) for k,v in citing_map.items()}, 'unique_codes': unique_codes}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QrKpS3xCrEvOFTzyHkiOaGa7': ['publicationinfo'], 'var_call_04o2xQiS5aWuOHXcmBa2upJ6': ['cpc_definition'], 'var_call_iFNFnXpgt1jRdEhcOq4ig4jD': 'file_storage/call_iFNFnXpgt1jRdEhcOq4ig4jD.json', 'var_call_F0o6KLAYCTaTzUnkOyFIfKph': 'file_storage/call_F0o6KLAYCTaTzUnkOyFIfKph.json', 'var_call_euL4YTFiEWaffgYDXkUUpE6y': {'citing_map': {}, 'unique_codes': []}, 'var_call_TN169ZanZUXhtwpDfJvr6vx6': 'file_storage/call_TN169ZanZUXhtwpDfJvr6vx6.json'}

exec(code, env_args)

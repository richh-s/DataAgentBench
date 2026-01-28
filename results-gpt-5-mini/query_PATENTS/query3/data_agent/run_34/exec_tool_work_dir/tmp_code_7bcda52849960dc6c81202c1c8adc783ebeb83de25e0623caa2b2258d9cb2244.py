code = """import json, re

# Load full publicationinfo JSON from storage
path = var_call_F0o6KLAYCTaTzUnkOyFIfKph
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Helper functions
pubnum_re = re.compile(r'[A-Z]{2,}-[0-9]{4,}[0-9A-Z\-]*')

def extract_pubnum(s):
    if not s:
        return None
    matches = pubnum_re.findall(s)
    if not matches:
        return None
    # choose longest match
    matches = sorted(matches, key=len, reverse=True)
    return matches[0]


def extract_assignee(s):
    if not s:
        return None
    s = s.strip()
    # try common patterns
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
    # fallback: try start until first comma
    if ',' in s:
        return s.split(',')[0].strip()
    # else take first 6 words as heuristic
    return ' '.join(s.split()[:6])


def is_univ_california(name):
    if not name:
        return False
    up = name.upper()
    return ('CALIFORNIA' in up) and (('UNIV' in up) or ('UNIVERSITY' in up))

# Build mapping of publication number -> info
pub_map = {}
for row in data:
    info = row.get('Patents_info') or ''
    pubnum = extract_pubnum(info)
    assignee = extract_assignee(info)
    # parse cpc primary codes
    cpc_field = row.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        cpcs = []
    primary_codes = []
    for e in cpcs:
        try:
            if e.get('first'):
                code = e.get('code')
                if code:
                    primary_codes.append(code)
        except Exception:
            pass
    if pubnum:
        pub_map[pubnum] = {
            'assignee': assignee,
            'rowid': row.get('rowid'),
            'primary_codes': sorted(list(set(primary_codes)))
        }

# Identify target pubnums assigned to Univ California
target_pubnums = {p for p,info in pub_map.items() if is_univ_california(info.get('assignee'))}

# For each publication, inspect its citations to see if it cites any target pubnums
citing_map = {}  # assignee -> set of cited primary codes
for row in data:
    info = row.get('Patents_info') or ''
    citing_assignee = extract_assignee(info)
    citation_field = row.get('citation') or '[]'
    try:
        citations = json.loads(citation_field)
    except Exception:
        citations = []
    cited_target_found = False
    codes = set()
    for c in citations:
        cited_pub = c.get('publication_number')
        if not cited_pub:
            continue
        if cited_pub in target_pubnums:
            cited_target_found = True
            # get primary codes from target pub
            pcs = pub_map.get(cited_pub, {}).get('primary_codes', [])
            for pc in pcs:
                codes.add(pc)
    if cited_target_found:
        if is_univ_california(citing_assignee):
            # skip citing by Univ California itself
            continue
        if not citing_assignee:
            citing_assignee = 'UNKNOWN'
        if citing_assignee not in citing_map:
            citing_map[citing_assignee] = set()
        citing_map[citing_assignee].update(codes)

# Collect unique codes
unique_codes = sorted(list({c for codes in citing_map.values() for c in codes if c}))

result = {
    'citing_map': {k: sorted(list(v)) for k,v in citing_map.items()},
    'unique_codes': unique_codes
}

# Print result as JSON string per required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QrKpS3xCrEvOFTzyHkiOaGa7': ['publicationinfo'], 'var_call_04o2xQiS5aWuOHXcmBa2upJ6': ['cpc_definition'], 'var_call_iFNFnXpgt1jRdEhcOq4ig4jD': 'file_storage/call_iFNFnXpgt1jRdEhcOq4ig4jD.json', 'var_call_F0o6KLAYCTaTzUnkOyFIfKph': 'file_storage/call_F0o6KLAYCTaTzUnkOyFIfKph.json'}

exec(code, env_args)

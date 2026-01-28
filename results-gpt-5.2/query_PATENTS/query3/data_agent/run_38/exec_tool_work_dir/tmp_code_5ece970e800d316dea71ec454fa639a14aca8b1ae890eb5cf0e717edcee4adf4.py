code = """import json, re

# Load uc-assignee publications to get publication numbers
uc_rows = var_call_HPGrAYsdLHl5CfJGN6CGzNQN
if isinstance(uc_rows, str):
    with open(uc_rows,'r',encoding='utf-8') as f:
        uc_rows = json.load(f)

pub_re = re.compile(r'pub\. number\s+([^\s\.]+)')

def get_pub(patents_info:str):
    if not patents_info:
        return None
    m = pub_re.search(patents_info)
    return m.group(1) if m else None

uc_pubs = set(filter(None,(get_pub(r.get('Patents_info','')) for r in uc_rows)))

# Load citing rows (all rows with citations)
citing_rows = var_call_oBhzxPHXHfPYMCD0FbUB7c5I
if isinstance(citing_rows, str):
    with open(citing_rows,'r',encoding='utf-8') as f:
        citing_rows = json.load(f)

# extract assignee from Patents_info
assignee_re = re.compile(r'^(.*?)\s+holds\s+the', re.IGNORECASE)
assignee_re2 = re.compile(r'In\s+[A-Z]{2},\s+the\s+.*?\s+is\s+(?:owned by|assigned to)\s+(.*?)\s+and\s+has', re.IGNORECASE)
assignee_re3 = re.compile(r'^(.*?)\s+holds\s+the\s+[A-Z]{2}\s+patent', re.IGNORECASE)

def get_assignee(patents_info:str):
    if not patents_info:
        return None
    for rgx in (assignee_re, assignee_re3):
        m = rgx.search(patents_info)
        if m:
            return m.group(1).strip()
    m = assignee_re2.search(patents_info)
    if m:
        return m.group(1).strip()
    # fallback: first token chunk before 'holds' or 'In '
    return None

# parse citations list and see if any cited pub in uc_pubs
hit_rows = []
for r in citing_rows:
    cit = r.get('citation')
    if not cit:
        continue
    try:
        cit_list = json.loads(cit)
    except Exception:
        continue
    cited_pubs = [c.get('publication_number') for c in cit_list if isinstance(c, dict)]
    if any(p in uc_pubs for p in cited_pubs if p):
        hit_rows.append(r)

# For those hit rows, gather (assignee, primary CPC subclass)
# primary CPC code = entries where first==true, take code; subclass = part before '/' (keep group/subgroup?)
# asked: primary CPC subclasses; interpret as subclass symbol without subgroup: e.g., 'F25B' from 'F25B21/00'
# but request says 'CPC subclass' (A01B, F25B). We'll map to titleFull for that symbol.

subclass_set = set()
pairs = set()

for r in hit_rows:
    assignee = get_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    if assignee.strip().upper() == 'UNIV CALIFORNIA':
        continue
    cpc = r.get('cpc')
    try:
        cpcs = json.loads(cpc) if cpc else []
    except Exception:
        cpcs = []
    primary_codes = [x.get('code') for x in cpcs if isinstance(x, dict) and x.get('first') is True and x.get('code')]
    for code in primary_codes:
        subclass = code.split('/')[0]
        subclass_set.add(subclass)
        pairs.add((assignee, subclass))

print('__RESULT__:')
print(json.dumps({
    'hit_publications_count': len(hit_rows),
    'unique_citing_assignees': len(set(a for a,_ in pairs)),
    'unique_pairs': len(pairs),
    'unique_subclasses': len(subclass_set),
    'pairs_sample': sorted(list(pairs))[:50],
    'subclasses': sorted(list(subclass_set))
}))"""

env_args = {'var_call_Tos0p1lnlN2ubDRTAIwKJNro': ['publicationinfo'], 'var_call_ZFmIV1fFavMFSIv2jon6hg0O': ['cpc_definition'], 'var_call_Cp4L2jTAkxznf31PFHsbbte3': [], 'var_call_HPGrAYsdLHl5CfJGN6CGzNQN': 'file_storage/call_HPGrAYsdLHl5CfJGN6CGzNQN.json', 'var_call_8eq7hQAWj63UVf3ywkN7mWF2': {'uc_pub_count': 59, 'sample_uc_pubs': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0']}, 'var_call_oBhzxPHXHfPYMCD0FbUB7c5I': 'file_storage/call_oBhzxPHXHfPYMCD0FbUB7c5I.json'}

exec(code, env_args)

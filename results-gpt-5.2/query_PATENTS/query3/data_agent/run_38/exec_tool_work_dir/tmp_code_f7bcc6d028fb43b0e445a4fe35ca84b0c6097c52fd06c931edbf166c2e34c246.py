code = """import json, re

# Load all rows with citations
all_rows = var_call_oBhzxPHXHfPYMCD0FbUB7c5I
if isinstance(all_rows, str):
    with open(all_rows,'r',encoding='utf-8') as f:
        all_rows = json.load(f)

# UC pubs
uc_rows = var_call_HPGrAYsdLHl5CfJGN6CGzNQN
if isinstance(uc_rows, str):
    with open(uc_rows,'r',encoding='utf-8') as f:
        uc_rows = json.load(f)

pub_re = re.compile(r'pub\. number\s+([^\s\.]+)')

def get_pub(patents_info:str):
    m = pub_re.search(patents_info or '')
    return m.group(1) if m else None
uc_pubs = set(filter(None,(get_pub(r.get('Patents_info','')) for r in uc_rows)))

# assignee extraction patterns
patterns = [
    re.compile(r'^(.*?)\s+holds\s+the', re.IGNORECASE),
    re.compile(r'is held by\s+(.*?)\s+and has', re.IGNORECASE),
    re.compile(r'In\s+[A-Z]{2},\s+the\s+.*?\s+is\s+(?:owned by|assigned to)\s+(.*?)\s+and\s+has', re.IGNORECASE),
    re.compile(r'^(.*?)\s+holds\s+the\s+[A-Z]{2}\s+patent', re.IGNORECASE)
]

def get_assignee(patents_info:str):
    txt = patents_info or ''
    for rgx in patterns:
        m = rgx.search(txt)
        if m:
            return m.group(1).strip()
    return None

pairs=set()
subclasses=set()

for r in all_rows:
    try:
        cit_list=json.loads(r.get('citation') or '[]')
    except Exception:
        continue
    if not any((c.get('publication_number') in uc_pubs) for c in cit_list if isinstance(c,dict)):
        continue
    assignee=get_assignee(r.get('Patents_info',''))
    if not assignee or assignee.strip().upper()=='UNIV CALIFORNIA':
        continue
    try:
        cpcs=json.loads(r.get('cpc') or '[]')
    except Exception:
        cpcs=[]
    primary=[x.get('code') for x in cpcs if isinstance(x,dict) and x.get('first') is True and x.get('code')]
    for code in primary:
        subclass=code.split('/')[0]
        subclasses.add(subclass)
        pairs.add((assignee,subclass))

print('__RESULT__:')
print(json.dumps({'pairs': sorted(list(pairs)), 'subclasses': sorted(list(subclasses))}))"""

env_args = {'var_call_Tos0p1lnlN2ubDRTAIwKJNro': ['publicationinfo'], 'var_call_ZFmIV1fFavMFSIv2jon6hg0O': ['cpc_definition'], 'var_call_Cp4L2jTAkxznf31PFHsbbte3': [], 'var_call_HPGrAYsdLHl5CfJGN6CGzNQN': 'file_storage/call_HPGrAYsdLHl5CfJGN6CGzNQN.json', 'var_call_8eq7hQAWj63UVf3ywkN7mWF2': {'uc_pub_count': 59, 'sample_uc_pubs': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0']}, 'var_call_oBhzxPHXHfPYMCD0FbUB7c5I': 'file_storage/call_oBhzxPHXHfPYMCD0FbUB7c5I.json', 'var_call_5ix4DJMKDrtYm1t2clwL1HDK': {'hit_publications_count': 1, 'unique_citing_assignees': 0, 'unique_pairs': 0, 'unique_subclasses': 0, 'pairs_sample': [], 'subclasses': []}, 'var_call_cHKmOhfiXOsGORlqkNoa92F1': ['The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.'], 'var_call_nzE28pBC1oHzlfRJIQjuTZ39': {'assignee': 'BLOOM ENERGY CORP'}}

exec(code, env_args)

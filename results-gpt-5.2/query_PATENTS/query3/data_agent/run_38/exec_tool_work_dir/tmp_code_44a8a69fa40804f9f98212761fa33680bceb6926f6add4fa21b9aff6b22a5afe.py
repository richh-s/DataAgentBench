code = """import json
hit_rows = var_call_oBhzxPHXHfPYMCD0FbUB7c5I
if isinstance(hit_rows, str):
    with open(hit_rows,'r',encoding='utf-8') as f:
        all_rows = json.load(f)
else:
    all_rows = hit_rows

# reload computed hit rows by reusing stored summary? We'll recompute quickly with uc pubs from prior file
uc_rows = var_call_HPGrAYsdLHl5CfJGN6CGzNQN
if isinstance(uc_rows, str):
    with open(uc_rows,'r',encoding='utf-8') as f:
        uc_rows = json.load(f)

import re
pub_re = re.compile(r'pub\. number\s+([^\s\.]+)')

def get_pub(p):
    m = pub_re.search(p or '')
    return m.group(1) if m else None
uc_pubs = set(filter(None,(get_pub(r.get('Patents_info','')) for r in uc_rows)))

hits=[]
for r in all_rows:
    try:
        cit_list=json.loads(r.get('citation') or '[]')
    except Exception:
        continue
    if any((c.get('publication_number') in uc_pubs) for c in cit_list if isinstance(c,dict)):
        hits.append(r)

# show patents_info of hits
out=[h.get('Patents_info') for h in hits]
print('__RESULT__:')
print(json.dumps(out[:5]))"""

env_args = {'var_call_Tos0p1lnlN2ubDRTAIwKJNro': ['publicationinfo'], 'var_call_ZFmIV1fFavMFSIv2jon6hg0O': ['cpc_definition'], 'var_call_Cp4L2jTAkxznf31PFHsbbte3': [], 'var_call_HPGrAYsdLHl5CfJGN6CGzNQN': 'file_storage/call_HPGrAYsdLHl5CfJGN6CGzNQN.json', 'var_call_8eq7hQAWj63UVf3ywkN7mWF2': {'uc_pub_count': 59, 'sample_uc_pubs': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0']}, 'var_call_oBhzxPHXHfPYMCD0FbUB7c5I': 'file_storage/call_oBhzxPHXHfPYMCD0FbUB7c5I.json', 'var_call_5ix4DJMKDrtYm1t2clwL1HDK': {'hit_publications_count': 1, 'unique_citing_assignees': 0, 'unique_pairs': 0, 'unique_subclasses': 0, 'pairs_sample': [], 'subclasses': []}}

exec(code, env_args)

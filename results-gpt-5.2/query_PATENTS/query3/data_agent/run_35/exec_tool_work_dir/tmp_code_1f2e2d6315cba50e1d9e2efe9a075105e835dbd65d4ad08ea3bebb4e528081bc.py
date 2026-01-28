code = """import json, re, pandas as pd

# load full records
path = var_call_ufsEQoeFmLtnJhEZ82Fctw0q
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

uc_pat_pubs = set()
for r in recs:
    pi = r.get('Patents_info') or ''
    if re.search(r'owned by\s+UNIV\s+CALIFORNIA\b', pi) or re.search(r'owned by\s+UNIVERSITY\s+OF\s+CALIFORNIA\b', pi):
        m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
        if m:
            uc_pat_pubs.add(m.group(1))

# if none found, return empty
result = {"uc_publications_found": sorted(list(uc_pat_pubs))[:50], "count": len(uc_pat_pubs)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2H482CA64rUxdSoVjRJaxcrD': ['publicationinfo'], 'var_call_HO506ZI5IX9dpFemlQpYdkNT': ['cpc_definition'], 'var_call_jWkd0v2qnfrVS2uEDoJTPCEv': [], 'var_call_ufsEQoeFmLtnJhEZ82Fctw0q': 'file_storage/call_ufsEQoeFmLtnJhEZ82Fctw0q.json'}

exec(code, env_args)

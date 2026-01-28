code = """import json
path = var_call_dr8fTvP2uZg23tRiHdmgebAk
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# data is a list of dicts with 'assignee' and 'primary_cpc'
pairs = []
codes = set()
for rec in data:
    assignee = rec.get('assignee')
    code = rec.get('primary_cpc')
    if not assignee or not code:
        continue
    # exclude entries that clearly mention UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    pairs.append({'assignee': assignee, 'primary_cpc': code})
    codes.add(code)
pairs_unique = []
seen = set()
for p in pairs:
    key = (p['assignee'], p['primary_cpc'])
    if key not in seen:
        seen.add(key)
        pairs_unique.append(p)
output = {'pairs': pairs_unique, 'codes': sorted(list(codes))}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_JkzVcUe9mStTDG8g0enUZ82T': 'file_storage/call_JkzVcUe9mStTDG8g0enUZ82T.json', 'var_call_mN0bvvlQgMe2C2VNhr5mLXV6': 'file_storage/call_mN0bvvlQgMe2C2VNhr5mLXV6.json', 'var_call_65VdEqZzcrDGysYV4E5QhCUt': 'file_storage/call_65VdEqZzcrDGysYV4E5QhCUt.json', 'var_call_godfpDa7ee2D983skuWmCPYL': 'file_storage/call_godfpDa7ee2D983skuWmCPYL.json', 'var_call_dr8fTvP2uZg23tRiHdmgebAk': 'file_storage/call_dr8fTvP2uZg23tRiHdmgebAk.json'}

exec(code, env_args)

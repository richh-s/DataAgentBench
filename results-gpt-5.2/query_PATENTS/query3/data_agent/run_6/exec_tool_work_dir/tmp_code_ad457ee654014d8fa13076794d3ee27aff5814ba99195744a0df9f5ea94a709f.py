code = """import json, re, pandas as pd

# load full assignee=UNIV CALIFORNIA records
path = var_call_eiOZ6mu6Fp62QgEmh27Olb79
with open(path, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

# extract UC publication numbers from Patents_info
uc_pubnums = set()
for r in uc_rows:
    pi = r.get('Patents_info') or ''
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
    if m:
        uc_pubnums.add(m.group(1))

# pull potentially citing records by searching citation text for any UC pubnum chunk
# use a coarse substring search on 'UNIV CALIFORNIA' pubnums by their numeric core (reduce query count)
cores = sorted({p.split('-')[1] for p in uc_pubnums if '-' in p})
# if huge, sample; but keep manageable
cores = cores[:200]

# build OR LIKE query
likes = ' OR '.join([f"citation LIKE '%{c}%'" for c in cores])
q = f"SELECT Patents_info, cpc, citation FROM publicationinfo WHERE citation IS NOT NULL AND citation <> '[]' AND ({likes});"
print('__RESULT__:')
print(json.dumps({'uc_pubnums_count': len(uc_pubnums), 'query': q[:5000]}))"""

env_args = {'var_call_iM799Cm624tRs8ZUZbXDWbwz': ['publicationinfo'], 'var_call_rBpbCGpvxezpdzQIOB6hxBNV': ['cpc_definition'], 'var_call_9s7Mnh5BPOggS0UNRTFgPRjn': [], 'var_call_eiOZ6mu6Fp62QgEmh27Olb79': 'file_storage/call_eiOZ6mu6Fp62QgEmh27Olb79.json'}

exec(code, env_args)

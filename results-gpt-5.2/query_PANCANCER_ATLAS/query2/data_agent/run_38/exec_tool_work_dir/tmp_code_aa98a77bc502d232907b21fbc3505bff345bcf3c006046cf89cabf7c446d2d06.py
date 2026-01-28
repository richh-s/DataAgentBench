code = """import pandas as pd, json, re
path = var_call_YQjiLgOo420mmwRTX8CZZdGQ
# load preview file
import os
if isinstance(path, str) and path.endswith('.json') and os.path.exists(path):
    recs = json.load(open(path))
else:
    recs = var_call_YQjiLgOo420mmwRTX8CZZdGQ
cols = list(recs[0].keys())
# find likely cancer type acronym column
candidates = [c for c in cols if 'acronym' in c.lower() or 'cancer' in c.lower() and 'type' in c.lower()]
# also look for project/abbreviation
candidates += [c for c in cols if any(k in c.lower() for k in ['project','disease','tumor_type','cancertype','study'])]
# unique
seen=set(); candidates=[c for c in candidates if not (c in seen or seen.add(c))]
print('__RESULT__:')
print(json.dumps({'n_cols': len(cols), 'candidate_cols': candidates[:50], 'all_cols_first50': cols[:50]}))"""

env_args = {'var_call_5FdTMr2TnI7HrQV4NuZZWaHU': 'file_storage/call_5FdTMr2TnI7HrQV4NuZZWaHU.json', 'var_call_T0FhGr0NsCldbiYeL70Z7PtX': ['clinical_info'], 'var_call_YQjiLgOo420mmwRTX8CZZdGQ': 'file_storage/call_YQjiLgOo420mmwRTX8CZZdGQ.json'}

exec(code, env_args)

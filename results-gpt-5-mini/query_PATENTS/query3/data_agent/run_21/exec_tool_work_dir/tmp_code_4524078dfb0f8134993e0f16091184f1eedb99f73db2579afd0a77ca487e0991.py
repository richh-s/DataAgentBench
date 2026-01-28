code = """import json
cpc_defs = json.load(open(var_call_yibhjuQuYNVfbsvGJV2uRdwv, 'r'))
pairs_data = json.load(open(var_call_HmYwVsetvOZ1SrWOkNrDbW1h, 'r'))['pairs']
# build map symbol->titleFull
mapping = {d['symbol']: d['titleFull'] for d in cpc_defs}
# assemble final list for each pair
results = []
for p in pairs_data:
    code = p['cpc_code']
    title = mapping.get(code, '')
    results.append({'assignee': p['assignee'], 'cpc_code': code, 'titleFull': title})
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_FWaq87obpvltPwUmTRpRaycV': 'file_storage/call_FWaq87obpvltPwUmTRpRaycV.json', 'var_call_xPULEoxuCI0R7gn4s9WmVLxr': 'file_storage/call_xPULEoxuCI0R7gn4s9WmVLxr.json', 'var_call_tgrM8QNXraQ65lKZy8S0oDdF': 'file_storage/call_tgrM8QNXraQ65lKZy8S0oDdF.json', 'var_call_HmYwVsetvOZ1SrWOkNrDbW1h': 'file_storage/call_HmYwVsetvOZ1SrWOkNrDbW1h.json', 'var_call_uwJ71UCjoN6nJceaFvGl4TYY': 'file_storage/call_uwJ71UCjoN6nJceaFvGl4TYY.json', 'var_call_yibhjuQuYNVfbsvGJV2uRdwv': 'file_storage/call_yibhjuQuYNVfbsvGJV2uRdwv.json'}

exec(code, env_args)

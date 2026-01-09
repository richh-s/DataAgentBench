code = """import json, re
raw = var_call_C8L5zhLal1Zk1ENuLjD2VCfK
if isinstance(raw, str):
    with open(raw,'r',encoding='utf-8') as f:
        docs=json.load(f)
else:
    docs=raw

# Find exact lines containing 'Begin Construction: Spring 2022'
out=[]
for d in docs:
    for line in d.get('text','').splitlines():
        if 'Begin Construction' in line and 'Spring 2022' in line:
            out.append({'filename': d.get('filename'), 'line': line})
print('__RESULT__:')
print(json.dumps(out[:50]))"""

env_args = {'var_call_voCW34f5mhpr4lBcDrP0GdJi': ['Funding'], 'var_call_beaAEvwBIwRzy1HcSw5H4XHD': ['civic_docs'], 'var_call_sir3H7yoilAVtxp9uzAjCNCs': 'file_storage/call_sir3H7yoilAVtxp9uzAjCNCs.json', 'var_call_1OKkPLKGhwTNK2ZpwqZXJyH2': {'projects': [], 'count': 0}, 'var_call_C8L5zhLal1Zk1ENuLjD2VCfK': 'file_storage/call_C8L5zhLal1Zk1ENuLjD2VCfK.json', 'var_call_GB4hhkINGJ8gc0CO8aCtTVBu': {'projects': [], 'count': 0}}

exec(code, env_args)

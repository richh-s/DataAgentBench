code = """import json, re
raw = var_call_sir3H7yoilAVtxp9uzAjCNCs
if isinstance(raw, str):
    with open(raw,'r',encoding='utf-8') as f:
        docs=json.load(f)
else:
    docs=raw

# search any 'Spring 2022' occurrences
hits=[]
for d in docs:
    t=d.get('text','')
    if re.search(r'Spring\s+2022', t, flags=re.I):
        # capture some context around first few matches
        for m in re.finditer(r'.{0,80}Spring\s+2022.{0,80}', t, flags=re.I|re.S):
            hits.append({'filename': d.get('filename'), 'context': m.group(0).replace('\n',' ')})
            if len(hits)>=20:
                break
    if len(hits)>=20:
        break
print('__RESULT__:')
print(json.dumps(hits))"""

env_args = {'var_call_voCW34f5mhpr4lBcDrP0GdJi': ['Funding'], 'var_call_beaAEvwBIwRzy1HcSw5H4XHD': ['civic_docs'], 'var_call_sir3H7yoilAVtxp9uzAjCNCs': 'file_storage/call_sir3H7yoilAVtxp9uzAjCNCs.json', 'var_call_1OKkPLKGhwTNK2ZpwqZXJyH2': {'projects': [], 'count': 0}}

exec(code, env_args)

code = """import json
p = var_call_vtSwwwvTau8MPXHdAfFGwNkD
if isinstance(p,str) and p.endswith('.json'):
    with open(p,'r') as f:
        obj = json.load(f)
else:
    obj = p
print('__RESULT__:')
print(json.dumps(obj['query']))"""

env_args = {'var_call_KkYc3f4Uo7DPaLEWKgf8Qy8X': 'file_storage/call_KkYc3f4Uo7DPaLEWKgf8Qy8X.json', 'var_call_rKHS1duJaB92sUCGFoGTg21g': 'file_storage/call_rKHS1duJaB92sUCGFoGTg21g.json', 'var_call_hLBEBSNaiF65beO5tPUloU2C': 'file_storage/call_hLBEBSNaiF65beO5tPUloU2C.json', 'var_call_Mk49FmuluC2X5BxSQDwQxBCT': 'file_storage/call_Mk49FmuluC2X5BxSQDwQxBCT.json', 'var_call_vtSwwwvTau8MPXHdAfFGwNkD': 'file_storage/call_vtSwwwvTau8MPXHdAfFGwNkD.json'}

exec(code, env_args)

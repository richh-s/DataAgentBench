code = """import json
with open(var_call_rKHS1duJaB92sUCGFoGTg21g,'r') as f:
    tables = json.load(f)
# check MRKR
found = [t for t in tables if t=='MRKR']
# find close matches
mr_like = [t for t in tables if t.startswith('MR')][:50]
print('__RESULT__:')
print(json.dumps({'MRKR_in_list': len(found)>0, 'MR_like_sample': mr_like}))"""

env_args = {'var_call_KkYc3f4Uo7DPaLEWKgf8Qy8X': 'file_storage/call_KkYc3f4Uo7DPaLEWKgf8Qy8X.json', 'var_call_rKHS1duJaB92sUCGFoGTg21g': 'file_storage/call_rKHS1duJaB92sUCGFoGTg21g.json', 'var_call_hLBEBSNaiF65beO5tPUloU2C': 'file_storage/call_hLBEBSNaiF65beO5tPUloU2C.json', 'var_call_Mk49FmuluC2X5BxSQDwQxBCT': 'file_storage/call_Mk49FmuluC2X5BxSQDwQxBCT.json', 'var_call_vtSwwwvTau8MPXHdAfFGwNkD': 'file_storage/call_vtSwwwvTau8MPXHdAfFGwNkD.json', 'var_call_gt1wOIQ8kS4o9zuGcnst3gWY': 'file_storage/call_gt1wOIQ8kS4o9zuGcnst3gWY.json', 'var_call_wmHH5j3eINlStuhCjxQhlU8s': {'n_symbols': 86, 'first10': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'has_MRKR': False}}

exec(code, env_args)

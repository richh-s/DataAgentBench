code = """import json, os

clinical_key = 'var_call_2Hbz95VIWvJQczjZECJzyMYV'
mut_key = 'var_call_NbI2VMmvh0BNBWFTgNEKYiPB'

clinical_var = globals().get(clinical_key)
mut_var = globals().get(mut_key)

summary = {}

for name, var in [(clinical_key, clinical_var), (mut_key, mut_var)]:
    info = {}
    info['type'] = type(var).__name__
    if isinstance(var, str) and os.path.exists(var):
        info['is_file'] = True
        try:
            with open(var,'r',encoding='utf-8') as f:
                data = json.load(f)
            info['list_length'] = len(data) if isinstance(data, list) else None
            info['first_keys'] = list(data[0].keys()) if isinstance(data, list) and len(data)>0 and isinstance(data[0], dict) else None
        except Exception as e:
            info['load_error'] = str(e)
    else:
        info['is_file'] = False
        if isinstance(var, list):
            info['list_length'] = len(var)
            info['first_keys'] = list(var[0].keys()) if len(var)>0 and isinstance(var[0], dict) else None
        else:
            info['repr'] = str(var)[:100]
    summary[name] = info

print('__RESULT__:')
print(json.dumps(summary))"""

env_args = {'var_call_euNu3hqX7o5pimk0JDlcvUZn': ['clinical_info'], 'var_call_TT4YmDFu1feeK1YWDQiVcdcZ': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_c48JMfZf7ddnSH9YptwaPZd0': 'file_storage/call_c48JMfZf7ddnSH9YptwaPZd0.json', 'var_call_2Hbz95VIWvJQczjZECJzyMYV': 'file_storage/call_2Hbz95VIWvJQczjZECJzyMYV.json', 'var_call_NbI2VMmvh0BNBWFTgNEKYiPB': 'file_storage/call_NbI2VMmvh0BNBWFTgNEKYiPB.json'}

exec(code, env_args)

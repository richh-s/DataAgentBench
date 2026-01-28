code = """import json
path = var_call_RVR5xX7fhAI9VXGTFOxqHAol
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
codes = data.get('codes', [])
print('__RESULT__:')
print(json.dumps(codes))"""

env_args = {'var_call_JkzVcUe9mStTDG8g0enUZ82T': 'file_storage/call_JkzVcUe9mStTDG8g0enUZ82T.json', 'var_call_mN0bvvlQgMe2C2VNhr5mLXV6': 'file_storage/call_mN0bvvlQgMe2C2VNhr5mLXV6.json', 'var_call_65VdEqZzcrDGysYV4E5QhCUt': 'file_storage/call_65VdEqZzcrDGysYV4E5QhCUt.json', 'var_call_godfpDa7ee2D983skuWmCPYL': 'file_storage/call_godfpDa7ee2D983skuWmCPYL.json', 'var_call_dr8fTvP2uZg23tRiHdmgebAk': 'file_storage/call_dr8fTvP2uZg23tRiHdmgebAk.json', 'var_call_RVR5xX7fhAI9VXGTFOxqHAol': 'file_storage/call_RVR5xX7fhAI9VXGTFOxqHAol.json'}

exec(code, env_args)

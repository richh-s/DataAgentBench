code = """import json
with open(var_call_dVkCoaVyOPrxj2TYNBar3PV2, 'r') as f:
    data = json.load(f)
matched_count = data.get('matched_count', 0)
print("__RESULT__:")
print(json.dumps(matched_count))"""

env_args = {'var_call_TWSODwC5rKyketYdEYUZZUzs': 'file_storage/call_TWSODwC5rKyketYdEYUZZUzs.json', 'var_call_k7B0exd6Wt1c6Oh0vLH2K3QN': ['civic_docs'], 'var_call_j74lAwmE8ofiz9Y8U0ygMnfC': 'file_storage/call_j74lAwmE8ofiz9Y8U0ygMnfC.json', 'var_call_dVkCoaVyOPrxj2TYNBar3PV2': 'file_storage/call_dVkCoaVyOPrxj2TYNBar3PV2.json'}

exec(code, env_args)

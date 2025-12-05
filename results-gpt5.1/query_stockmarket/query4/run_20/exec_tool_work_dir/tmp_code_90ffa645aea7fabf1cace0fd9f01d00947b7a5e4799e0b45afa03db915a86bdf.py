code = """import json
symbols = json.load(open(var_call_zC29esC2DNL0NiWAmbP3eEhQ))
nyse_meta = json.load(open(var_call_KsmRFOpycZDVpj40GiiMLUhF))
nyse_set = {r['Symbol'] for r in nyse_meta}
common = sorted([s for s in symbols if s in nyse_set])
result = json.dumps(common)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_zC29esC2DNL0NiWAmbP3eEhQ': 'file_storage/call_zC29esC2DNL0NiWAmbP3eEhQ.json', 'var_call_KsmRFOpycZDVpj40GiiMLUhF': 'file_storage/call_KsmRFOpycZDVpj40GiiMLUhF.json'}

exec(code, env_args)

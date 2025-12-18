code = """import json

with open(locals()['var_function-call-9397000578558853234'], 'r') as f:
    arca_etf_symbols = json.load(f)

print("__RESULT__:")
print(json.dumps(arca_etf_symbols[:10]))"""

env_args = {'var_function-call-16027928627600003546': 'file_storage/function-call-16027928627600003546.json', 'var_function-call-9397000578558853234': 'file_storage/function-call-9397000578558853234.json'}

exec(code, env_args)

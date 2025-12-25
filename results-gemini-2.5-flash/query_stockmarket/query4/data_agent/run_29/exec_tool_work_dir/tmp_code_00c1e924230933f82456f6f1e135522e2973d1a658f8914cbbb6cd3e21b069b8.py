code = """import json

with open(locals()['var_function-call-3836873403238552655'], 'r') as f:
    symbol_names = json.load(f)

symbols = list(symbol_names.keys())

print("__RESULT__:")
print(json.dumps(symbols))"""

env_args = {'var_function-call-11766224021179762257': 'file_storage/function-call-11766224021179762257.json', 'var_function-call-3836873403238552655': 'file_storage/function-call-3836873403238552655.json'}

exec(code, env_args)

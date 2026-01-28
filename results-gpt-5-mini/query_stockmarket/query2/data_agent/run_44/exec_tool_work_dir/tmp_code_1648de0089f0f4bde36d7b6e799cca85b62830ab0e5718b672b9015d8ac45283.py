code = """import json
path = var_call_RzWEhQLhTSkVNtKtCb8VjS3j
with open(path) as f:
    data = json.load(f)
symbols = [row['Symbol'] for row in data]
print("__RESULT__:")
print(json.dumps(symbols))"""

env_args = {'var_call_RzWEhQLhTSkVNtKtCb8VjS3j': 'file_storage/call_RzWEhQLhTSkVNtKtCb8VjS3j.json'}

exec(code, env_args)

code = """import json

with open(locals()['var_function-call-12486855758920957982'], 'r') as f:
    stocks = json.load(f)

print(f"Number of stocks: {len(stocks)}")
print(f"Sample: {stocks[:5]}")
print("__RESULT__:")
print(json.dumps({"count": len(stocks)}))"""

env_args = {'var_function-call-12486855758920957982': 'file_storage/function-call-12486855758920957982.json'}

exec(code, env_args)

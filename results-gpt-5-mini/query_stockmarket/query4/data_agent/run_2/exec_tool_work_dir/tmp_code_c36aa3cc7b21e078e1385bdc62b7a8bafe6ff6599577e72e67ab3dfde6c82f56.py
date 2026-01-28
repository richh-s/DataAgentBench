code = """import json
path = var_call_PciIwzYCtdu656FXLDAFh82S
with open(path, 'r') as f:
    records = json.load(f)
symbols = [r['Symbol'] for r in records]
res = json.dumps(symbols)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_PciIwzYCtdu656FXLDAFh82S': 'file_storage/call_PciIwzYCtdu656FXLDAFh82S.json'}

exec(code, env_args)

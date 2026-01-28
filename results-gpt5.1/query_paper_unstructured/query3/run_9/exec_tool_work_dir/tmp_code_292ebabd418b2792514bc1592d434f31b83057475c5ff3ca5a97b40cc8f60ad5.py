code = """import json, pandas as pd

sql_path = var_call_ju9InGP20lZd1uAjGF4LYxx9
with open(sql_path, 'r') as f:
    sql_records = json.load(f)

# Inspect keys
keys = sorted({k for rec in sql_records for k in rec.keys()})

print("__RESULT__:")
print(json.dumps(keys))"""

env_args = {'var_call_JrvCkgZlVyQIh8mF21biU9gs': 'file_storage/call_JrvCkgZlVyQIh8mF21biU9gs.json', 'var_call_ju9InGP20lZd1uAjGF4LYxx9': 'file_storage/call_ju9InGP20lZd1uAjGF4LYxx9.json'}

exec(code, env_args)

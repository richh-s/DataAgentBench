code = """import json
path = var_call_GJ65B0zFrs2lMKT5L5Zod9RU
with open(path,'r') as f:
    tables = json.load(f)

etf_path = var_call_4UfIxOFUNz9yoOJgRBfo26dC
with open(etf_path,'r') as f:
    etfs = json.load(f)

etf_set = {e['Symbol'] for e in etfs}
available = sorted(list(etf_set.intersection(tables)))

res = json.dumps({'available_count': len(available)})
print("__RESULT__:")
print(res)"""

env_args = {'var_call_4UfIxOFUNz9yoOJgRBfo26dC': 'file_storage/call_4UfIxOFUNz9yoOJgRBfo26dC.json', 'var_call_wtty6HKUIYHrOzVDWedf3wUK': 'file_storage/call_wtty6HKUIYHrOzVDWedf3wUK.json', 'var_call_GJ65B0zFrs2lMKT5L5Zod9RU': 'file_storage/call_GJ65B0zFrs2lMKT5L5Zod9RU.json'}

exec(code, env_args)

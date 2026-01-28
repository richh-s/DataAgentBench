code = """import json
p1 = var_call_glwAqwUanNo8ExlokGyMH5xr
p2 = var_call_b8L0GzZtBYwGmNoVw96WDvnt

a = json.load(open(p1))
b = json.load(open(p2))

mapping = {item['Symbol']: item.get('Company Description','') for item in a}
tables = set(b)

symbols = [s for s in mapping.keys() if s in tables]

res = {'symbols_considered_count': len(symbols), 'first_20': symbols[:20]}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_glwAqwUanNo8ExlokGyMH5xr': 'file_storage/call_glwAqwUanNo8ExlokGyMH5xr.json', 'var_call_b8L0GzZtBYwGmNoVw96WDvnt': 'file_storage/call_b8L0GzZtBYwGmNoVw96WDvnt.json', 'var_call_3rCgDdperyl00Y2GTbxKWHEa': 'file_storage/call_3rCgDdperyl00Y2GTbxKWHEa.json'}

exec(code, env_args)

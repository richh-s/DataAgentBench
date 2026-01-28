code = """import json
# load variables from previous calls
path_symbols = var_call_7wxjtS5eDBAybdsY4hHUlbkg
with open(path_symbols, 'r') as f:
    symbols = json.load(f)
path_tables = var_call_7LTpHrqwyFIkW2SUcmkW6iZJ
with open(path_tables, 'r') as f:
    tables = json.load(f)
# compute intersection
set_symbols = set(symbols)
set_tables = set(tables)
common = sorted(list(set_symbols & set_tables))
# print result list
print("__RESULT__:")
print(json.dumps(common))"""

env_args = {'var_call_GMErwPiZAV8ACBIMFcLWeylx': 'file_storage/call_GMErwPiZAV8ACBIMFcLWeylx.json', 'var_call_7wxjtS5eDBAybdsY4hHUlbkg': 'file_storage/call_7wxjtS5eDBAybdsY4hHUlbkg.json', 'var_call_7LTpHrqwyFIkW2SUcmkW6iZJ': 'file_storage/call_7LTpHrqwyFIkW2SUcmkW6iZJ.json'}

exec(code, env_args)

code = """import json
path_stockinfo = var_call_30Q4bH3inArkxlM7dvrMi1ha
path_tables = var_call_u7zNvvdRWah3dEIyubxloJSI
with open(path_stockinfo, 'r') as f:
    stockinfo = json.load(f)
with open(path_tables, 'r') as f:
    tables = json.load(f)
symbols = [rec['Symbol'] for rec in stockinfo]
available_symbols = [s for s in symbols if s in tables]
print('__RESULT__:')
print(json.dumps(available_symbols))"""

env_args = {'var_call_30Q4bH3inArkxlM7dvrMi1ha': 'file_storage/call_30Q4bH3inArkxlM7dvrMi1ha.json', 'var_call_u7zNvvdRWah3dEIyubxloJSI': 'file_storage/call_u7zNvvdRWah3dEIyubxloJSI.json'}

exec(code, env_args)

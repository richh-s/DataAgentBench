code = """import json
with open(var_call_wsVInw8eEyMzIoSnAVX55pOn, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_mf8p8wR7qUDwPcMyViiKZp7a, 'r') as f:
    trade_tables = set(json.load(f))
# filter stockinfo to symbols present in trade_tables
rows = []
for rec in stockinfo:
    sym = rec.get('Symbol')
    if sym in trade_tables:
        rows.append({'Symbol': sym, 'Company Description': rec.get('Company Description')})
# output as JSON string
print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_mf8p8wR7qUDwPcMyViiKZp7a': 'file_storage/call_mf8p8wR7qUDwPcMyViiKZp7a.json', 'var_call_wsVInw8eEyMzIoSnAVX55pOn': 'file_storage/call_wsVInw8eEyMzIoSnAVX55pOn.json', 'var_call_atY7Z5oy1ePQMP8fS8SVojO2': {'a': 'ok'}}

exec(code, env_args)

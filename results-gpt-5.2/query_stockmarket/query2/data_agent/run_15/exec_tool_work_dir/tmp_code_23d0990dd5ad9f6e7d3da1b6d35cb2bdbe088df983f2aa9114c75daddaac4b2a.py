code = """import json

with open(var_call_VGVpI3kO5XpwoFYTl8XTVeJE,'r') as f:
    arca = json.load(f)

with open(var_call_tMvtkwNUD4qPnebzX6FZXcPl,'r') as f:
    avail = {r['symbol'] for r in json.load(f)}

syms = sorted({r['Symbol'] for r in arca if r.get('Symbol') in avail})
print('__RESULT__:')
print(json.dumps({'symbols': syms, 'n': len(syms)}))"""

env_args = {'var_call_VGVpI3kO5XpwoFYTl8XTVeJE': 'file_storage/call_VGVpI3kO5XpwoFYTl8XTVeJE.json', 'var_call_JIIwmBkuzTk3s1YN9hLJvjTA': 'file_storage/call_JIIwmBkuzTk3s1YN9hLJvjTA.json', 'var_call_V8MhUQLNeBGUkhoLUHUtY1KW': {'n': 1435}, 'var_call_RwtnADUHw7UHekN3VQmAj6qL': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_tMvtkwNUD4qPnebzX6FZXcPl': 'file_storage/call_tMvtkwNUD4qPnebzX6FZXcPl.json'}

exec(code, env_args)

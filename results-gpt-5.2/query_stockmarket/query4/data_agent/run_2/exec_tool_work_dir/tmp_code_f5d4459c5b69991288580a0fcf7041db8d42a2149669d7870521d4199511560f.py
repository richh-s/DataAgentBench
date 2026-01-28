code = """import json
print('__RESULT__:')
print(json.dumps({'ok': True}))"""

env_args = {'var_call_HA7aZkk6ej0IlGua67UFhxLm': 'file_storage/call_HA7aZkk6ej0IlGua67UFhxLm.json', 'var_call_KS9toGYpPJHCYGzuWhO10tQ3': 'file_storage/call_KS9toGYpPJHCYGzuWhO10tQ3.json', 'var_call_j3Aj5jdNwzAAng2R74eKrFn3': [{'ok': '1'}]}

exec(code, env_args)

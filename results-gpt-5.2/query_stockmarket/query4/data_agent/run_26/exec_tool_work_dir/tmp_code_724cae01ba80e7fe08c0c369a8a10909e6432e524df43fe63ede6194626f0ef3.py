code = """import json
print('__RESULT__:')
print(json.dumps({'a': 1}))"""

env_args = {'var_call_YUklvkNSfsVQgYR1c02Ynr1O': 'file_storage/call_YUklvkNSfsVQgYR1c02Ynr1O.json', 'var_call_JtD0SKI6HkrXBgEo4BnEvRkc': 'file_storage/call_JtD0SKI6HkrXBgEo4BnEvRkc.json'}

exec(code, env_args)

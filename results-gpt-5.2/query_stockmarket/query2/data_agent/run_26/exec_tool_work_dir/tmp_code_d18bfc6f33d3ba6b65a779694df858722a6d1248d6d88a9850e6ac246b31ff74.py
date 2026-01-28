code = """import json
out={'ok': True}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dicekK1CadjdqBVoQN5mEwi3': 'file_storage/call_dicekK1CadjdqBVoQN5mEwi3.json', 'var_call_jSoK13w4Qjxh2skFCII7xkeM': 'file_storage/call_jSoK13w4Qjxh2skFCII7xkeM.json'}

exec(code, env_args)

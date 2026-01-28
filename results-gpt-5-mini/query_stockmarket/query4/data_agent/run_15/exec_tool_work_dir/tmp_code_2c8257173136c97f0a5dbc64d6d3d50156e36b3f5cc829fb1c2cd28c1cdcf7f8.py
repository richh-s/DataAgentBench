code = """import json
with open(var_call_oYATr3lACqKv3d9bwO11EIgq, 'r') as f:
    rows = json.load(f)
symbols = [r['Symbol'] for r in rows]
print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_call_mf8p8wR7qUDwPcMyViiKZp7a': 'file_storage/call_mf8p8wR7qUDwPcMyViiKZp7a.json', 'var_call_wsVInw8eEyMzIoSnAVX55pOn': 'file_storage/call_wsVInw8eEyMzIoSnAVX55pOn.json', 'var_call_atY7Z5oy1ePQMP8fS8SVojO2': {'a': 'ok'}, 'var_call_oYATr3lACqKv3d9bwO11EIgq': 'file_storage/call_oYATr3lACqKv3d9bwO11EIgq.json'}

exec(code, env_args)

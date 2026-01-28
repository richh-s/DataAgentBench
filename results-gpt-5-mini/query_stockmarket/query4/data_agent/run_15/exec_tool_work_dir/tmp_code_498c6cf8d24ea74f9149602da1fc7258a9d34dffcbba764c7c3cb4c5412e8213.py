code = """import json
print('__RESULT__:')
print(json.dumps({'a': 'ok'}))"""

env_args = {'var_call_mf8p8wR7qUDwPcMyViiKZp7a': 'file_storage/call_mf8p8wR7qUDwPcMyViiKZp7a.json', 'var_call_wsVInw8eEyMzIoSnAVX55pOn': 'file_storage/call_wsVInw8eEyMzIoSnAVX55pOn.json'}

exec(code, env_args)

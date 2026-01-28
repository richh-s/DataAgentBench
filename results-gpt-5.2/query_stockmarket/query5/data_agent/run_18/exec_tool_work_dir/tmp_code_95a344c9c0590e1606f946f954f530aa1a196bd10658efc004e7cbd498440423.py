code = """import json
print('__RESULT__:')
print(json.dumps({'x': 1}))"""

env_args = {'var_call_COIkrGN9cWpnuc7Vnq57yeIM': 'file_storage/call_COIkrGN9cWpnuc7Vnq57yeIM.json', 'var_call_CIdqd6spRth4VQvXVr16cRmW': {'n_symbols': 86}, 'var_call_I5zOU2gwHrCtH6ksASeIM4im': 'file_storage/call_I5zOU2gwHrCtH6ksASeIM4im.json'}

exec(code, env_args)

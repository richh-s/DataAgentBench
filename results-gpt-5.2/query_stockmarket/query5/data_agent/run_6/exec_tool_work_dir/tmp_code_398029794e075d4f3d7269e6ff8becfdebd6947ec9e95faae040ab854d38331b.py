code = """import json

# minimal test to ensure printing works
print('__RESULT__:')
print(json.dumps({'ok': True}))"""

env_args = {'var_call_1M2WJBSzBWCBsrqxUcSSQvFy': 'file_storage/call_1M2WJBSzBWCBsrqxUcSSQvFy.json', 'var_call_6zdVBkckwn2R8JwOU8xeyNkR': 'file_storage/call_6zdVBkckwn2R8JwOU8xeyNkR.json', 'var_call_neNIOvU1Qz4tQrb5hXX8vBjb': 'file_storage/call_neNIOvU1Qz4tQrb5hXX8vBjb.json'}

exec(code, env_args)

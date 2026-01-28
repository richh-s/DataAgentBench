code = """import json
print('__RESULT__:')
print(json.dumps({'ok': True}))"""

env_args = {'var_call_lsVzhsWRcJPMqreLutxe9gCr': 'file_storage/call_lsVzhsWRcJPMqreLutxe9gCr.json', 'var_call_sOPO5ItDyEQ2ND9iPkJlrrQb': 'file_storage/call_sOPO5ItDyEQ2ND9iPkJlrrQb.json', 'var_call_i8orDA4VAqo1k3XXAVEWSomT': [{'Symbol': 'SPY'}]}

exec(code, env_args)

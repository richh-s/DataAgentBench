code = """import json
print('__RESULT__:')
print(json.dumps({'a':1}))"""

env_args = {'var_call_7P2pKW2MvdjwPJAT38jWRKoj': 'file_storage/call_7P2pKW2MvdjwPJAT38jWRKoj.json', 'var_call_bmf0BnCD1Y3a4ithfN0awrMh': 'file_storage/call_bmf0BnCD1Y3a4ithfN0awrMh.json', 'var_call_kFjbYZ0s15AJ39Vk9DSBz8tr': [{'Symbol': 'AGMH', 'cnt': '13'}]}

exec(code, env_args)

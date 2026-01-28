code = """import json
s = "ok"
print('__RESULT__:')
print(json.dumps(s))"""

env_args = {'var_call_0cRCwuXzy0ygPKXxZNGk722D': 'file_storage/call_0cRCwuXzy0ygPKXxZNGk722D.json', 'var_call_QmgXm74iO39N022IImWIvqGm': 'file_storage/call_QmgXm74iO39N022IImWIvqGm.json', 'var_call_zTLM20Bmr7M3fKcKo1DvPtSn': [{'n': '2753'}]}

exec(code, env_args)

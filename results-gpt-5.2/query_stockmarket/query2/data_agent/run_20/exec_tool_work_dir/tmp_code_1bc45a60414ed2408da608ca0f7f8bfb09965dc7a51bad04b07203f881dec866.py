code = """import json
print('__RESULT__:')
print(json.dumps({'a':1}))"""

env_args = {'var_call_LB1ZbwPPcY0PzkOXrLj7u8zh': 'file_storage/call_LB1ZbwPPcY0PzkOXrLj7u8zh.json', 'var_call_v7Kx9fKHDfirqP6JfQmY5K9t': 'file_storage/call_v7Kx9fKHDfirqP6JfQmY5K9t.json'}

exec(code, env_args)

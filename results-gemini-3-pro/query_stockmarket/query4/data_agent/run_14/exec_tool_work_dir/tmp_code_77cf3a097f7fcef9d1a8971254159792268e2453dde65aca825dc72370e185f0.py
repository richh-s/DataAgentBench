code = """import json

d1 = '2017-01-01'
d2 = '2017-12-31'

print('__RESULT__:')
print(json.dumps({'d1': d1, 'd2': d2}))"""

env_args = {'var_function-call-2664401347096856404': 'file_storage/function-call-2664401347096856404.json', 'var_function-call-14718190706972975468': 'file_storage/function-call-14718190706972975468.json', 'var_function-call-5783268603279882755': {'count1': 234, 'count2': 2753}, 'var_function-call-5645677206837916636': 'file_storage/function-call-5645677206837916636.json'}

exec(code, env_args)

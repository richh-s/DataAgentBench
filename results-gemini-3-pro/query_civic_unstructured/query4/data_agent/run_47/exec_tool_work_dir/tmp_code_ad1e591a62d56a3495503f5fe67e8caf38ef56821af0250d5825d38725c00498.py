code = """import json
print("__RESULT__:")
print(json.dumps("Hello"))"""

env_args = {'var_function-call-3769111620830882253': 'file_storage/function-call-3769111620830882253.json', 'var_function-call-3769111620830881668': 'file_storage/function-call-3769111620830881668.json'}

exec(code, env_args)

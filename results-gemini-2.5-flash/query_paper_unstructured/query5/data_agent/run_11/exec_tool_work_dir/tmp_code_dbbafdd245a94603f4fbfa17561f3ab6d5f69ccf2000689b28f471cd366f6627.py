code = """import json

with open(locals()['var_function-call-2842283538054183407'], 'r') as f:
    data = json.load(f)

__RESULT__:
print(json.dumps({'type': str(type(data)), 'first_five_elements': data[:5]}))"""

env_args = {'var_function-call-2842283538054183407': 'file_storage/function-call-2842283538054183407.json'}

exec(code, env_args)

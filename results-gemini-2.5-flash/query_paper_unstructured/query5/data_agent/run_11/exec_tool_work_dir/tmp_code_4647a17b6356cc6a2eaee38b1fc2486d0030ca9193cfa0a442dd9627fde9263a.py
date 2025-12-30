code = """import json

content_type = str(type(locals()['var_function-call-2842283538054183407']))
content_value = locals()['var_function-call-2842283538054183407']

__RESULT__:
print(json.dumps({'type': content_type, 'value': content_value}))"""

env_args = {'var_function-call-2842283538054183407': 'file_storage/function-call-2842283538054183407.json'}

exec(code, env_args)

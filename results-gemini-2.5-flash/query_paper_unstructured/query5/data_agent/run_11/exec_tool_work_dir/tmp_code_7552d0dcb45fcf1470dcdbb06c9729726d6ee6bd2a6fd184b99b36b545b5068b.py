code = """import json

__RESULT__:
print(json.dumps(locals()['var_function-call-2842283538054183407']))"""

env_args = {'var_function-call-2842283538054183407': 'file_storage/function-call-2842283538054183407.json'}

exec(code, env_args)

code = """import json
print("__RESULT__:")
print(json.dumps("Hello World"))"""

env_args = {'var_function-call-13812960451374386902': 'file_storage/function-call-13812960451374386902.json', 'var_function-call-8903793629185941567': 'file_storage/function-call-8903793629185941567.json', 'var_function-call-8397726498436877101': 'Test'}

exec(code, env_args)

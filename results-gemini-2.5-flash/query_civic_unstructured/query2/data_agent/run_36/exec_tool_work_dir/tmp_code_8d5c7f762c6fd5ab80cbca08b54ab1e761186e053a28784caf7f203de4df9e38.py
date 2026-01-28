code = """import json
print("__RESULT__:")
print(json.dumps("Test"))"""

env_args = {'var_function-call-13812960451374386902': 'file_storage/function-call-13812960451374386902.json', 'var_function-call-8903793629185941567': 'file_storage/function-call-8903793629185941567.json'}

exec(code, env_args)

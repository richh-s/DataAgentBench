code = """import json
keys = list(locals().keys())
print("__RESULT__:")
print(json.dumps(keys))"""

env_args = {'var_function-call-13379061347181110174': 'file_storage/function-call-13379061347181110174.json', 'var_function-call-6559325847238713717': 'file_storage/function-call-6559325847238713717.json'}

exec(code, env_args)

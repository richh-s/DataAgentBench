code = """import json

query_condition_string = locals()['var_function-call-5588095364749648406']

print("__RESULT__:")
print(json.dumps(query_condition_string))"""

env_args = {'var_function-call-17489811540451064265': 'file_storage/function-call-17489811540451064265.json', 'var_function-call-5588095364749648406': 'file_storage/function-call-5588095364749648406.json'}

exec(code, env_args)

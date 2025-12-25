code = """import json

with open('var_function-call-1113576567256238630', 'r') as f:
    data = json.load(f)

print("__RESULT__:")
print(len(data))"""

env_args = {'var_function-call-1113576567256238630': 'file_storage/function-call-1113576567256238630.json'}

exec(code, env_args)

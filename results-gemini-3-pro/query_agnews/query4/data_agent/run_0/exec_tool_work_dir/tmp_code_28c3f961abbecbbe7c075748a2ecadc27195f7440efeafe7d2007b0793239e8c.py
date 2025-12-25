code = """import json

with open('var_function-call-16217748514118301059.json', 'r') as f:
    metadata = json.load(f)

print("__RESULT__:")
print(len(metadata))"""

env_args = {'var_function-call-16217748514118301059': 'file_storage/function-call-16217748514118301059.json'}

exec(code, env_args)

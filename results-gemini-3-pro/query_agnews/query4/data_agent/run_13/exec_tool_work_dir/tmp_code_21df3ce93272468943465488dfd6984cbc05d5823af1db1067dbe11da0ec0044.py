code = """import json

with open(locals()['var_function-call-517009556635827832'], 'r') as f:
    metadata = json.load(f)

print("__RESULT__:")
print(len(metadata))"""

env_args = {'var_function-call-517009556635827832': 'file_storage/function-call-517009556635827832.json'}

exec(code, env_args)

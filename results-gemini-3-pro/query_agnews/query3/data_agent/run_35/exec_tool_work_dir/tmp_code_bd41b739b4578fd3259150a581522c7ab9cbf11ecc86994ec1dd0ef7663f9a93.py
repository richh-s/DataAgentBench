code = """import json

with open('var_function-call-3785327814520365478.json', 'r') as f:
    metadata = json.load(f)

print(f"__RESULT__:\n{len(metadata)}")"""

env_args = {'var_function-call-3785327814520365478': 'file_storage/function-call-3785327814520365478.json'}

exec(code, env_args)

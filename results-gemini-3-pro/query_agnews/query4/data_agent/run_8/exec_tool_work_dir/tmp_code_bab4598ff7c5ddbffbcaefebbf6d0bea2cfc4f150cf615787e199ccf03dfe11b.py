code = """import json

with open('var_function-call-750385390280883322.json', 'r') as f:
    metadata = json.load(f)

print(f"__RESULT__:\n{len(metadata)}")"""

env_args = {'var_function-call-750385390280883322': 'file_storage/function-call-750385390280883322.json'}

exec(code, env_args)

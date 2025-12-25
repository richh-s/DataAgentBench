code = """import json

with open('var_function-call-7362815310734823686', 'r') as f:
    metadata_records = json.load(f)

print("__RESULT__:")
print(len(metadata_records))"""

env_args = {'var_function-call-7362815310734823686': 'file_storage/function-call-7362815310734823686.json'}

exec(code, env_args)

code = """import json

file_path = locals()['var_function-call-750385390280883322']
with open(file_path, 'r') as f:
    metadata = json.load(f)

# Extract IDs, ensure they are integers
ids = [int(item['article_id']) for item in metadata]

print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_function-call-750385390280883322': 'file_storage/function-call-750385390280883322.json', 'var_function-call-6083932913443130219': 6696}

exec(code, env_args)

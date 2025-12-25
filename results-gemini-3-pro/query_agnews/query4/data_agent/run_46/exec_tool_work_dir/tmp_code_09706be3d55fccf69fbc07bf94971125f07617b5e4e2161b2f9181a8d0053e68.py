code = """import json

# Load the metadata result
with open(locals()['var_function-call-16230520417025150586'], 'r') as f:
    metadata = json.load(f)

# Count
count = len(metadata)
ids = [int(item['article_id']) for item in metadata]
result = {'count': count, 'ids': ids}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16230520417025150586': 'file_storage/function-call-16230520417025150586.json'}

exec(code, env_args)

code = """import json

# Load the metadata result
with open(locals()['var_function-call-16230520417025150586'], 'r') as f:
    metadata = json.load(f)

# Count
count = len(metadata)
ids = [int(item['article_id']) for item in metadata]

print(f"__RESULT__:\n{json.dumps({'count': count, 'ids': ids})}")"""

env_args = {'var_function-call-16230520417025150586': 'file_storage/function-call-16230520417025150586.json'}

exec(code, env_args)

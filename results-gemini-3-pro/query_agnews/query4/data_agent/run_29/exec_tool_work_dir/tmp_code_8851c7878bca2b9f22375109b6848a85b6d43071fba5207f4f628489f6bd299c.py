code = """import json

# Load the result from the previous step
with open(locals()['var_function-call-12409222309987750024'], 'r') as f:
    metadata_records = json.load(f)

# Extract IDs
article_ids = [int(record['article_id']) for record in metadata_records]
print(f"Number of articles in 2015: {len(article_ids)}")

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-12409222309987750024': 'file_storage/function-call-12409222309987750024.json'}

exec(code, env_args)

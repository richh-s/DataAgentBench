code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-17404740365086201769']

# Read the file
with open(file_path, 'r') as f:
    metadata_records = json.load(f)

# Extract article_ids
article_ids = [int(r['article_id']) for r in metadata_records]

print("__RESULT__:")
print(json.dumps({"count": len(article_ids), "sample_ids": article_ids[:10]}))"""

env_args = {'var_function-call-17404740365086201769': 'file_storage/function-call-17404740365086201769.json'}

exec(code, env_args)

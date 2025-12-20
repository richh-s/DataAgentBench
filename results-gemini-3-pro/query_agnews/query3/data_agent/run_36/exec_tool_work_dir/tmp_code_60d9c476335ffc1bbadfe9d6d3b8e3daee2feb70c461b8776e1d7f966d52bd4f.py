code = """import json

# Load the result from the previous tool call
with open(locals()['var_function-call-14838360778106258720'], 'r') as f:
    articles_metadata = json.load(f)

# Extract IDs
article_ids = [entry['article_id'] for entry in articles_metadata]
print("__RESULT__:")
print(json.dumps({"count": len(article_ids), "sample_ids": article_ids[:10]}))"""

env_args = {'var_function-call-14838360778106258720': 'file_storage/function-call-14838360778106258720.json'}

exec(code, env_args)

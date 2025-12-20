code = """import json

# Load the SQL result
with open(locals()['var_function-call-8582204155257448886'], 'r') as f:
    articles_metadata = json.load(f)

# Extract article_ids
article_ids = [item['article_id'] for item in articles_metadata]

print("__RESULT__:")
print(json.dumps({"count": len(article_ids), "ids": article_ids}))"""

env_args = {'var_function-call-8582204155257448886': 'file_storage/function-call-8582204155257448886.json'}

exec(code, env_args)

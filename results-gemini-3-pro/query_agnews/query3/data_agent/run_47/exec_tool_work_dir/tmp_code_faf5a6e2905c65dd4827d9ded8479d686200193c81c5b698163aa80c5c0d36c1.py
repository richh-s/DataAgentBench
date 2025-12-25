code = """import json

# Load the result from the previous query
with open('var_function-call-1050039959698811753.json', 'r') as f:
    metadata = json.load(f)

# Extract article_ids
article_ids = [int(record['article_id']) for record in metadata]

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-886384908282461354': ['authors', 'article_metadata'], 'var_function-call-1050039959698811753': 'file_storage/function-call-1050039959698811753.json'}

exec(code, env_args)

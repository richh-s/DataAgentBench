code = """import json

# Load the result from the previous step
with open(locals()['var_function-call-13553007703269894173'], 'r') as f:
    metadata_records = json.load(f)

# Extract article_ids
article_ids = [int(r['article_id']) for r in metadata_records]

print(f"Total articles in 2015: {len(article_ids)}")
print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-13553007703269894173': 'file_storage/function-call-13553007703269894173.json'}

exec(code, env_args)

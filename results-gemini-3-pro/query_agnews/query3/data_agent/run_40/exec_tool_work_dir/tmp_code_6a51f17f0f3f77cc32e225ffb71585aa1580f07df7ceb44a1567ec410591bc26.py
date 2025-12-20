code = """import json

# Read the result from the previous step
with open(locals()['var_function-call-13727892763181911756'], 'r') as f:
    metadata_records = json.load(f)

# Extract article_ids
article_ids = [r['article_id'] for r in metadata_records]
# Also create a map for later use: article_id -> year
article_year_map = {r['article_id']: int(r['publication_date'][:4]) for r in metadata_records}

print("__RESULT__:")
print(json.dumps({"article_ids": article_ids, "article_year_map": article_year_map}))"""

env_args = {'var_function-call-13727892763181911756': 'file_storage/function-call-13727892763181911756.json'}

exec(code, env_args)

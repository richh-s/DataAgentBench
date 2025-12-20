code = """import json

# Load the result from the previous tool call
with open(locals()['var_function-call-8077609229720510149'], 'r') as f:
    metadata_records = json.load(f)

# Extract article_ids
article_ids = [int(r['article_id']) for r in metadata_records]

print(f"__RESULT__:\nCount: {len(article_ids)}")"""

env_args = {'var_function-call-8077609229720510149': 'file_storage/function-call-8077609229720510149.json'}

exec(code, env_args)

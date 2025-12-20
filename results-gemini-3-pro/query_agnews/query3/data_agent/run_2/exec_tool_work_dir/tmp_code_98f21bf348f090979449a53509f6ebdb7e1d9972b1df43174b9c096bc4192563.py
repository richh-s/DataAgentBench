code = """import json

with open('var_function-call-18399428532014092056', 'r') as f:
    metadata_records = json.load(f)

article_ids = [int(r['article_id']) for r in metadata_records]
print(f"__RESULT__:\n{json.dumps(len(article_ids))}")"""

env_args = {'var_function-call-12102129638019306028': ['authors', 'article_metadata'], 'var_function-call-12102129638019306837': ['articles'], 'var_function-call-18399428532014092056': 'file_storage/function-call-18399428532014092056.json'}

exec(code, env_args)

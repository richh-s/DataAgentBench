code = """import json

with open(locals()['var_function-call-12102332063729111063'], 'r') as f:
    metadata_records = json.load(f)

article_ids = [r['article_id'] for r in metadata_records]
print(f"Count of articles: {len(article_ids)}")
print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-12102332063729111063': 'file_storage/function-call-12102332063729111063.json'}

exec(code, env_args)

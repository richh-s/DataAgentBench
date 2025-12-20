code = """import json

with open('var_function-call-15785121732506884524', 'r') as f:
    metadata_records = json.load(f)

article_ids = [r['article_id'] for r in metadata_records]
print(f"__RESULT__:\n{json.dumps({'count': len(article_ids), 'sample_ids': article_ids[:5]})}")"""

env_args = {'var_function-call-15785121732506884524': 'file_storage/function-call-15785121732506884524.json'}

exec(code, env_args)

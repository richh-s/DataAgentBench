code = """import json

with open(locals()['var_function-call-17075212337781938676'], 'r') as f:
    metadata_records = json.load(f)

article_ids = [int(r['article_id']) for r in metadata_records]
result = {'count': len(article_ids), 'ids_preview': article_ids[:10]}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17075212337781938676': 'file_storage/function-call-17075212337781938676.json'}

exec(code, env_args)

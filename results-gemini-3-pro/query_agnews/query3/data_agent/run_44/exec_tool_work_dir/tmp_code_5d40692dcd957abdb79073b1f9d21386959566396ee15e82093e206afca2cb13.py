code = """import json

with open('var_function-call-12172117661927561958') as f:
    data = json.load(f)

article_ids = [int(item['article_id']) for item in data]
print(f"Total articles: {len(article_ids)}")
print(f"First 10 IDs: {article_ids[:10]}")

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-12172117661927561958': 'file_storage/function-call-12172117661927561958.json'}

exec(code, env_args)

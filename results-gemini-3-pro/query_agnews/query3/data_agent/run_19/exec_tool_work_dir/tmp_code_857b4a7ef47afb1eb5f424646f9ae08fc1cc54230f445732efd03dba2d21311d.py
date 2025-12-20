code = """import json

with open('var_function-call-3309949836529129021.json', 'r') as f:
    data = json.load(f)

article_ids = [int(item['article_id']) for item in data]
count = len(article_ids)

# Create a result dictionary
res = {'count': count, 'ids': article_ids}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-3309949836529129021': 'file_storage/function-call-3309949836529129021.json'}

exec(code, env_args)

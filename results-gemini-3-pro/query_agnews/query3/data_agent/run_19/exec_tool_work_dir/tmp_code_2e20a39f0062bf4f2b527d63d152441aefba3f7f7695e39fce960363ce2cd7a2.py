code = """import json

# Load the result from the previous step
with open('var_function-call-3309949836529129021.json', 'r') as f:
    data = json.load(f)

article_ids = [int(item['article_id']) for item in data]
count = len(article_ids)

print(f"__RESULT__:\n{json.dumps({'count': count, 'ids': article_ids})}")"""

env_args = {'var_function-call-3309949836529129021': 'file_storage/function-call-3309949836529129021.json'}

exec(code, env_args)

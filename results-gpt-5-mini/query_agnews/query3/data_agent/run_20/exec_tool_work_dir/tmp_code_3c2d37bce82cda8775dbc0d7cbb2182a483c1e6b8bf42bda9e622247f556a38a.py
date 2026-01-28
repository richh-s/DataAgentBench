code = """import json
# var_call_U3o8FQVQchz7KL7rLo173iUa is the storage key from the previous query_db call
path = var_call_U3o8FQVQchz7KL7rLo173iUa
with open(path, 'r') as f:
    data = json.load(f)
# extract unique article_ids as ints
ids = sorted({int(item['article_id']) for item in data})
# print in required format
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_U3o8FQVQchz7KL7rLo173iUa': 'file_storage/call_U3o8FQVQchz7KL7rLo173iUa.json'}

exec(code, env_args)

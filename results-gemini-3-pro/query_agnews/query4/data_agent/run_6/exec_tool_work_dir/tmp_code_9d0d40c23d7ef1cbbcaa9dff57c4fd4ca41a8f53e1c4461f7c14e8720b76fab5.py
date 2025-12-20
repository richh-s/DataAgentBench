code = """import json

with open(locals()['var_function-call-15217179502760513550'], 'r') as f:
    data = json.load(f)

ids = [row['article_id'] for row in data]
print(f"Count: {len(ids)}")
print(f"First 10 IDs: {ids[:10]}")
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_function-call-15217179502760513550': 'file_storage/function-call-15217179502760513550.json'}

exec(code, env_args)

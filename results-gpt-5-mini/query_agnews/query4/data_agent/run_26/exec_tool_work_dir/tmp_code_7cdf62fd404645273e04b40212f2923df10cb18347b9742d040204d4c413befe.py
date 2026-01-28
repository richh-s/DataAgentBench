code = """import json
# var_call_bqG3p4Xgp7PyD8VJ6yZy1zuT is a file path to the SQL query result JSON
path = var_call_bqG3p4Xgp7PyD8VJ6yZy1zuT
with open(path, 'r') as f:
    data = json.load(f)
# extract article_ids as integers
ids = sorted({int(item['article_id']) for item in data})
print('__RESULT__:')
print(json.dumps(ids))"""

env_args = {'var_call_OkEHZh9DF3cWuFn5tW0QpXox': ['articles'], 'var_call_bqG3p4Xgp7PyD8VJ6yZy1zuT': 'file_storage/call_bqG3p4Xgp7PyD8VJ6yZy1zuT.json'}

exec(code, env_args)

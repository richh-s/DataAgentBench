code = """import json
# var_call_kO1HUmuJfOqZvh05wh4xaIAu is provided by previous query_db call and contains the path to the full JSON result
path = var_call_kO1HUmuJfOqZvh05wh4xaIAu
with open(path, 'r') as f:
    records = json.load(f)
# extract article_ids as integers
article_ids = [int(r['article_id']) for r in records]
# produce JSON string of list of ids
output = json.dumps(article_ids)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_kO1HUmuJfOqZvh05wh4xaIAu': 'file_storage/call_kO1HUmuJfOqZvh05wh4xaIAu.json'}

exec(code, env_args)

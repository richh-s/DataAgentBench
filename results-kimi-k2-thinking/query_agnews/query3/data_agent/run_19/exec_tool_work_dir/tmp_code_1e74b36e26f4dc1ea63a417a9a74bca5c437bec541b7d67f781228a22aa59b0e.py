code = """import json
metadata_path = var_functions.query_db:2
with open(metadata_path, 'r') as f:
    metadata = json.load(f)
article_ids = [int(item['article_id']) for item in metadata]
print('__RESULT__:')
print(json.dumps(article_ids))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

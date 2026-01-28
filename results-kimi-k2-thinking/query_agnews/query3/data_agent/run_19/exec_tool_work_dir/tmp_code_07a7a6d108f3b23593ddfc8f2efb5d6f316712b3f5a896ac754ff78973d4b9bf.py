code = """import json
metadata_path = locals()['var_functions.query_db:2']
with open(metadata_path, 'r') as f:
    metadata = json.load(f)
article_ids = [int(item['article_id']) for item in metadata]
# Build MongoDB query
query_obj = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids}},
    "projection": {"_id": 0, "article_id": 1, "title": 1, "description": 1}
}
query_str = json.dumps(query_obj)
print('__RESULT__:')
print(json.dumps(query_str))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.execute_python:8': 14860}

exec(code, env_args)

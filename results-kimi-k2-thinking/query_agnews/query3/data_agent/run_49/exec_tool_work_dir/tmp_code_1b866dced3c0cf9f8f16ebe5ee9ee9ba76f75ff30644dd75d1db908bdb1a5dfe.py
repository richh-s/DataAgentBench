code = """import json

# Get the article IDs list again
var_name = 'var_functions.query_db:2'
metadata_path = locals()[var_name]

with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

article_ids = [rec['article_id'] for rec in metadata_records]
print(f"Number of article IDs to query: {len(article_ids)}")

# Create MongoDB query
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1}
}

# Return as JSON string
print('__RESULT__:')
print(json.dumps(mongo_query))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': '14860'}

exec(code, env_args)

code = """import json

# Build a MongoDB query with filter for all article_ids from 2015
# We need to fetch title and description for these articles
query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids_2015}},
    "projection": {"article_id": 1, "title": 1, "description": 1},
    "limit": 30000  # Set a large limit to get all articles
}

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'type': 'str', 'value': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': {'count_2015': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}}

exec(code, env_args)

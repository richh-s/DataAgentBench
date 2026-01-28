code = """import json

file_path = locals()['var_functions.query_db:2']

with open(file_path, 'r') as f:
    metadata_2015 = json.load(f)

article_ids = [int(item['article_id']) for item in metadata_2015]

mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1},
    "limit": 10000
}

print('__RESULT__:')
print(json.dumps(mongo_query))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'total_articles_2015': 6696, 'sample_article_ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}}

exec(code, env_args)

code = """import json
import math

# Read the article IDs again
metadata_path = locals()['var_functions.query_db:2']
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

# Split into batches to avoid hitting query limits
article_ids = [int(item['article_id']) for item in metadata]
batch_size = 1000
batches = [article_ids[i:i + batch_size] for i in range(0, len(article_ids), batch_size)]

# Process first batch
first_batch = batches[0]
query_obj = {
    "collection": "articles",
    "filter": {"article_id": {"$in": first_batch}},
    "projection": {"_id": 0, "article_id": 1, "title": 1, "description": 1}
}
query_str = json.dumps(query_obj)
print('__RESULT__:')
print(json.dumps(query_str))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.execute_python:8': 14860, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'total_articles': 14860, 'articles_per_year': {'2010': 1306, '2011': 1316, '2012': 1355, '2013': 1354, '2014': 1372, '2015': 1357, '2016': 1364, '2017': 1391, '2018': 1351, '2019': 1328, '2020': 1366}}}

exec(code, env_args)

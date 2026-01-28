code = """import json

# Read the metadata file from the previous query
metadata_file = var_functions.query_db:12
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Extract article IDs and create a mapping of article_id to region
article_regions = {}
for item in metadata_2015:
    article_id = int(item['article_id'])
    article_regions[article_id] = item['region']

# Get all article IDs
article_ids = list(article_regions.keys())

print('__RESULT__:')
print(json.dumps({
    'article_count': len(article_ids),
    'sample_article_ids': article_ids[:10],
    'sample_regions': [article_regions[a] for a in article_ids[:10]]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

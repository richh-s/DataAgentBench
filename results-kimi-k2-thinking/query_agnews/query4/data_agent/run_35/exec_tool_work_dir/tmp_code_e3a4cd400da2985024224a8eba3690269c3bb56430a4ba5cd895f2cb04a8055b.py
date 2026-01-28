code = """import json

# Get 2015 metadata
metadata_2015 = locals()['var_functions.query_db:0']
if isinstance(metadata_2015, str) and metadata_2015.endswith('.json'):
    with open(metadata_2015, 'r') as f:
        metadata_2015 = json.load(f)

# Create region lookup and article_id list
region_lookup = {}
for item in metadata_2015:
    article_id = int(item['article_id'])
    region_lookup[article_id] = item['region']

article_ids = list(region_lookup.keys())
article_ids.sort()

# Create batches for MongoDB query (using $in operator)
batch_size = 1000
batches = []
for i in range(0, len(article_ids), batch_size):
    batches.append(article_ids[i:i+batch_size])

result = {
    "total_articles": len(article_ids),
    "number_of_batches": len(batches),
    "first_batch_size": len(batches[0]) if batches else 0,
    "last_article_id": article_ids[-1] if article_ids else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'total_articles_2015': 6696, 'unique_article_ids': 6696, 'sample_article_ids': [13, 18, 26]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 6696, 'min_id': 13, 'max_id': 127570}, 'var_functions.execute_python:14': {'total_articles': 6696, 'number_of_batches': 14, 'batch_size': 500, 'first_batch_sample': [13, 18, 26, 51, 52]}}

exec(code, env_args)

code = """import json

# Get 2015 metadata
metadata_2015 = locals()['var_functions.query_db:0']
if isinstance(metadata_2015, str) and metadata_2015.endswith('.json'):
    with open(metadata_2015, 'r') as f:
        metadata_2015 = json.load(f)

# Create lookup table
region_lookup = {int(item['article_id']): item['region'] for item in metadata_2015}
article_ids = list(region_lookup.keys())

# Split into batches for querying
batch_size = 500
batches = [article_ids[i:i+batch_size] for i in range(0, len(article_ids), batch_size)]

result = {
    "total_articles": len(article_ids),
    "number_of_batches": len(batches),
    "batch_size": batch_size,
    "first_batch_sample": batches[0][:5] if batches else []
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'total_articles_2015': 6696, 'unique_article_ids': 6696, 'sample_article_ids': [13, 18, 26]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 6696, 'min_id': 13, 'max_id': 127570}}

exec(code, env_args)

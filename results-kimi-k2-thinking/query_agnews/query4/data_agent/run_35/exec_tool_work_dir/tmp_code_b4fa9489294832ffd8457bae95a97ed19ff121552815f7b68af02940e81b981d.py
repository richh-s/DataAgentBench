code = """import json

# Access the 2015 metadata
metadata_2015 = locals()['var_functions.query_db:0']
if isinstance(metadata_2015, str) and metadata_2015.endswith('.json'):
    with open(metadata_2015, 'r') as f:
        metadata_2015 = json.load(f)

# Get all article IDs for 2015
article_ids_2015 = [int(item['article_id']) for item in metadata_2015]

result = {
    "total_articles": len(article_ids_2015),
    "min_id": min(article_ids_2015) if article_ids_2015 else None,
    "max_id": max(article_ids_2015) if article_ids_2015 else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'total_articles_2015': 6696, 'unique_article_ids': 6696, 'sample_article_ids': [13, 18, 26]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

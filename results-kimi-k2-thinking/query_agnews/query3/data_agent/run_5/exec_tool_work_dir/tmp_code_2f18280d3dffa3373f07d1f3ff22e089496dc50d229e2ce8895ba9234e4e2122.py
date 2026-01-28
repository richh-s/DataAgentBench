code = """import json

# Load the metadata results from the file
with open('var_functions.query_db:2', 'r') as f:
    metadata_results = json.load(f)

# Get all article_ids
article_ids = [int(item['article_id']) for item in metadata_results]

print('__RESULT__:')
print(json.dumps({
    'total_articles': len(article_ids),
    'first_few': article_ids[:10]
}))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

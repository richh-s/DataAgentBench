code = """import json

# Read the full result from the file
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    europe_articles = json.load(f)

# Extract article IDs
article_ids = [int(article['article_id']) for article in europe_articles]

print('__RESULT__:')
print(json.dumps({
    'total_europe_articles': len(article_ids),
    'sample_articles': article_ids[:10]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json

# Access the file path from storage
file_path = var_functions.query_db:2

# Open and read the data
with open(file_path, 'r') as f:
    metadata = json.load(f)

# Extract article ids as integers
article_ids = [int(record['article_id']) for record in metadata]

# Print number of articles
num_articles = len(article_ids)
print('__RESULT__:')
print(json.dumps({'num_articles': num_articles, 'article_ids': article_ids}))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

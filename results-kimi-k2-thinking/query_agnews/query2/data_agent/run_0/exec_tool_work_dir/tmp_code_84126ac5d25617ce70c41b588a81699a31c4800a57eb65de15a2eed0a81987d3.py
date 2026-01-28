code = """import json

# Access the variable with the file path
data_key = 'var_functions.query_db:2'
file_path = locals()[data_key]

# Read the full result from the file
with open(file_path, 'r') as f:
    articles_metadata = json.load(f)

article_ids = [article['article_id'] for article in articles_metadata]
total_articles = len(article_ids)

print('__RESULT__:')
print(json.dumps({'total_articles': total_articles, 'article_ids': article_ids}))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218', 'name': 'Amy Jones'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

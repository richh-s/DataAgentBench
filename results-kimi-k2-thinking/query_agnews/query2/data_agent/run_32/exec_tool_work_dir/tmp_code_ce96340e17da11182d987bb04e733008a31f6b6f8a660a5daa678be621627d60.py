code = """import json

# Load the metadata results from the file
with open(var_functions.query_db:2, 'r') as f:
    metadata_data = json.load(f)

# Extract article IDs
article_ids = [item['article_id'] for item in metadata_data]

print('__RESULT__:')
print(json.dumps({'article_ids': article_ids, 'total_articles': len(article_ids)}))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218', 'name': 'Amy Jones'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

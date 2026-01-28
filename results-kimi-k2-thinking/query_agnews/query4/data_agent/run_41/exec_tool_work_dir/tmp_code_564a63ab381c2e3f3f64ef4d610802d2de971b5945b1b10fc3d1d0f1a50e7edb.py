code = """import json
# Read the full result from the previous query
result_file = locals()['var_functions.query_db:0']
with open(result_file, 'r') as f:
    metadata_2015 = json.load(f)

# Extract article IDs for 2015
article_ids_2015 = [item['article_id'] for item in metadata_2015]
result = {
    'total_2015_articles': len(article_ids_2015),
    'sample_article_ids': article_ids_2015[:10]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

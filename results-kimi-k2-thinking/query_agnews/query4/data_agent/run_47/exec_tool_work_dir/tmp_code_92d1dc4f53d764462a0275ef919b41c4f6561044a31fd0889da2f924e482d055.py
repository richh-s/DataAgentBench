code = """import json

# Read the full metadata result for 2015 articles
file_path = locals()['var_functions.query_db:0']  # Access via locals()
with open(file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Extract article_ids
article_ids_2015 = [item['article_id'] for item in metadata_2015]

print('__RESULT__:')
print(json.dumps({
    'count': len(article_ids_2015),
    'article_ids': article_ids_2015[:5]  # Just preview a few
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

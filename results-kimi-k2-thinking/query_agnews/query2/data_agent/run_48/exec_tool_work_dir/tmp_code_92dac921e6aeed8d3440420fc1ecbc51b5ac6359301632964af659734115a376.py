code = """import json
# Read the article metadata file
metadata_file = var_functions.query_db:2
with open(metadata_file, 'r') as f:
    metadata = json.load(f)

# Extract article_ids
article_ids = [int(item['article_id']) for item in metadata]
total_articles = len(article_ids)

print('__RESULT__:')
print(json.dumps({"article_ids": article_ids, "total_articles": total_articles}))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218', 'name': 'Amy Jones'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

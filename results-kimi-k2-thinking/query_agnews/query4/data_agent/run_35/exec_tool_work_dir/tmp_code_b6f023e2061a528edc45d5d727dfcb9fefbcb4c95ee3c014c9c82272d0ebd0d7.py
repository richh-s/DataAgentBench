code = """import json

# Access the stored result from previous query
metadata_2015 = locals()['var_functions.query_db:0']

# If it's a file path, read the file
if isinstance(metadata_2015, str) and metadata_2015.endswith('.json'):
    with open(metadata_2015, 'r') as f:
        metadata_2015 = json.load(f)

# Extract article_ids and create region mapping
region_by_article = {}
for item in metadata_2015:
    article_id = int(item['article_id'])
    region_by_article[article_id] = item['region']

article_ids = list(region_by_article.keys())

result = {
    "total_articles_2015": len(metadata_2015),
    "unique_article_ids": len(article_ids),
    "sample_article_ids": article_ids[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

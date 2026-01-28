code = """import json

# Read the JSON file path from storage
file_path = locals()['var_functions.query_db:0']

# Read the JSON file with the metadata results
with open(file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Extract all article IDs from 2015
article_ids_2015 = [item['article_id'] for item in metadata_2015]

# Count total articles in 2015
total_articles = len(article_ids_2015)

print('__RESULT__:')
print(json.dumps({
    "total_articles_2015": total_articles,
    "article_ids_sample": article_ids_2015[:10],
    "article_ids_list": article_ids_2015
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

code = """import json

# Get the file path from storage
file_path = locals()['var_functions.query_db:4']

# Read the full result from the file
with open(file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Extract article IDs
article_ids_2015 = [int(item['article_id']) for item in metadata_2015]

print('__RESULT__:')
print(json.dumps({
    "count": len(article_ids_2015),
    "sample_ids": article_ids_2015[:10],
    "all_ids": article_ids_2015
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

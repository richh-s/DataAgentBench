code = """import json

# Load the metadata results from the file
metadata_path = var_functions.query_db:2
with open(metadata_path, 'r') as f:
    metadata_2015 = json.load(f)

# Extract article IDs
article_ids_2015 = [int(item['article_id']) for item in metadata_2015]

# Print the result in the required format
print('__RESULT__:')
print(json.dumps(article_ids_2015))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

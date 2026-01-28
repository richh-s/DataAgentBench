code = """import json

# Load metadata from file
metadata_file = var_functions.query_db:2
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Extract article IDs
article_ids = [int(item['article_id']) for item in metadata_2015]

# Build MongoDB query for these articles
# MongoDB uses $in operator
import urllib.parse
article_ids_str = json.dumps(article_ids)

# Create the query as a string (will need to use in query_db)
query_str = '{"collection": "articles", "filter": {"article_id": {"$in": ' + article_ids_str + '}}, "projection": {"article_id": 1, "title": 1, "description": 1}}'

print('__RESULT__:')
print(query_str)"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

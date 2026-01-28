code = """import json
# Access the stored variable from locals
metadata_path = str(locals()['var_functions.query_db:2'])

# Load the metadata
with open(metadata_path, 'r') as f:
    metadata_2015 = json.load(f)

# Extract article IDs
article_ids_2015 = [int(item['article_id']) for item in metadata_2015]

# Build MongoDB query
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids_2015}},
    "projection": {"article_id": 1, "title": 1, "description": 1}
}

print('__RESULT__:')
print(json.dumps(mongo_query))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

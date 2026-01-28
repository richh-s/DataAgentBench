code = """import json
# Load the metadata query result from storage
path = var_call_8FxzZo84pzLRYHC44my2FfbI
with open(path, 'r') as f:
    records = json.load(f)
# Extract unique article_ids as integers
ids = sorted({int(r['article_id']) for r in records})
# Build MongoDB query as a JSON string
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1},
    "limit": 0
}
output = json.dumps(mongo_query)
print('__RESULT__:')
print(output)"""

env_args = {'var_call_8FxzZo84pzLRYHC44my2FfbI': 'file_storage/call_8FxzZo84pzLRYHC44my2FfbI.json'}

exec(code, env_args)

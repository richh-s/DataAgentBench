code = """import json
# Load metadata result file
path = var_call_Zvd9beiaubpkKZ7mIFvoQAlQ
with open(path, 'r') as f:
    records = json.load(f)
# Extract unique article_ids as ints
ids = sorted({int(r['article_id']) for r in records})
# Build Mongo query string
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1},
    "limit": len(ids)
}
query_str = json.dumps(mongo_query)
print("__RESULT__:")
print(json.dumps(query_str))"""

env_args = {'var_call_Bl0KkE0hJGL4FcVBoMVc4K5h': ['articles'], 'var_call_Zvd9beiaubpkKZ7mIFvoQAlQ': 'file_storage/call_Zvd9beiaubpkKZ7mIFvoQAlQ.json'}

exec(code, env_args)

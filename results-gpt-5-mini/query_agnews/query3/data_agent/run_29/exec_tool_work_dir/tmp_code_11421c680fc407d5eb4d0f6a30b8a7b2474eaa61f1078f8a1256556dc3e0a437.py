code = """import json
# var_call_GyTzqACDcvIV3zGDKVIrK555 is the storage key containing the file path to the metadata query result
path = var_call_GyTzqACDcvIV3zGDKVIrK555
with open(path, 'r') as f:
    records = json.load(f)
# extract unique article_ids as integers
ids = []
for r in records:
    try:
        ids.append(int(r.get('article_id')))
    except:
        try:
            ids.append(int(r.get('article_id').strip()))
        except:
            pass
ids = sorted(list(set(ids)))
# build MongoDB query JSON string
query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0},
    "limit": 0
}
query_str = json.dumps(query)
print("__RESULT__:")
print(query_str)"""

env_args = {'var_call_GyTzqACDcvIV3zGDKVIrK555': 'file_storage/call_GyTzqACDcvIV3zGDKVIrK555.json'}

exec(code, env_args)

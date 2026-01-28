code = """import json
# var_call_0BWhQ822FlEwjtXW5PCml263 is provided by previous query_db call and contains the path to the full JSON result
path = var_call_0BWhQ822FlEwjtXW5PCml263
with open(path, 'r') as f:
    records = json.load(f)
# extract unique article_ids as ints
ids = sorted({int(rec['article_id']) for rec in records})
# build MongoDB query JSON string
mongo_query = json.dumps({
    "collection": "articles",
    "filter": {"article_id": {"$in": ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1},
    "limit": 0
})

# Output must be a JSON-serializable string
output = {"mongo_query": mongo_query}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_0BWhQ822FlEwjtXW5PCml263': 'file_storage/call_0BWhQ822FlEwjtXW5PCml263.json'}

exec(code, env_args)

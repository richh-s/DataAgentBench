code = """import json
# var_call_ms1IPeXScrnLDnXJ5N74c2Gg is provided in storage and contains the file path to the JSON results
p = var_call_ms1IPeXScrnLDnXJ5N74c2Gg
with open(p, 'r') as f:
    records = json.load(f)
# Extract unique article_ids as integers
ids = sorted({int(r['article_id']) for r in records})
# Build Mongo query dict
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1},
    "limit": 0
}
result_str = json.dumps(mongo_query)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_call_ms1IPeXScrnLDnXJ5N74c2Gg': 'file_storage/call_ms1IPeXScrnLDnXJ5N74c2Gg.json'}

exec(code, env_args)

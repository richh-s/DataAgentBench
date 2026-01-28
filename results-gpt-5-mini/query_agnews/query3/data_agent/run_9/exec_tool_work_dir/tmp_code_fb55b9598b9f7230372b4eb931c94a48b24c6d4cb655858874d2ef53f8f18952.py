code = """import json
# Load the metadata result file path from storage variable
path = var_call_lHFXpsi061JUb8EbGXOJcodE
# Open and load
with open(path, 'r') as f:
    records = json.load(f)
# Extract article_ids as integers, deduplicate
ids = sorted({int(r['article_id']) for r in records})
# Build Mongo query JSON string
query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1},
    "limit": 0
}
query_str = json.dumps(query)
print("__RESULT__:")
print(query_str)"""

env_args = {'var_call_lHFXpsi061JUb8EbGXOJcodE': 'file_storage/call_lHFXpsi061JUb8EbGXOJcodE.json'}

exec(code, env_args)

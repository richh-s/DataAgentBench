code = """import json

# Load the previous result
with open(locals()['var_function-call-3090238535036356339'], 'r') as f:
    metadata_records = json.load(f)

# Extract article IDs
article_ids = [r['article_id'] for r in metadata_records]
# Convert to int if they are strings in the JSON (preview showed strings "13")
article_ids = [int(aid) for aid in article_ids]

print(f"Total articles in 2015: {len(article_ids)}")

# Prepare the MongoDB query
# We need to query the 'articles' collection
# Filter: { article_id: { $in: article_ids } }
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids}}
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-3090238535036356339': 'file_storage/function-call-3090238535036356339.json'}

exec(code, env_args)

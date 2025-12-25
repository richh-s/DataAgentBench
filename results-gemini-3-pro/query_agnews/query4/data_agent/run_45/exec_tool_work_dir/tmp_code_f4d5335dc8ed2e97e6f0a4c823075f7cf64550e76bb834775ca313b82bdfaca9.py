code = """import json

# Read the metadata result
with open('var_function-call-8215058594514075225.json', 'r') as f:
    metadata = json.load(f)

article_ids = [int(item['article_id']) for item in metadata]
print(f"Number of articles in 2015: {len(article_ids)}")

# Construct MongoDB query
# We will use the 'articles_database' and 'articles' collection
# Query: {"article_id": {"$in": article_ids}}
# We need to project fields: article_id, title, description
# Since the list can be long, let's see. If it's < 10000, it's fine.

query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-8215058594514075225': 'file_storage/function-call-8215058594514075225.json'}

exec(code, env_args)

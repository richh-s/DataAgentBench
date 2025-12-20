code = """import json

# Load the SQLite result
with open(locals()['var_function-call-15217179502760513550'], 'r') as f:
    data = json.load(f)

# Extract IDs and convert to int
ids = [int(row['article_id']) for row in data]

# Construct Mongo query
query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": ids}},
    "projection": {"_id": 0, "article_id": 1, "title": 1, "description": 1}
}

print(f"Total IDs: {len(ids)}")
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-15217179502760513550': 'file_storage/function-call-15217179502760513550.json', 'var_function-call-13727430707746249518': 'file_storage/function-call-13727430707746249518.json'}

exec(code, env_args)

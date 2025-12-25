code = """import json

# Load the article_ids
with open(locals()['var_function-call-10354531083663329512'], 'r') as f:
    article_ids = json.load(f)

# Construct Mongo query
query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": article_ids}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-13553007703269894173': 'file_storage/function-call-13553007703269894173.json', 'var_function-call-10354531083663329512': 'file_storage/function-call-10354531083663329512.json'}

exec(code, env_args)

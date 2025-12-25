code = """import json

with open(locals()['var_function-call-4354025683768215761'], 'r') as f:
    ids = json.load(f)

# Construct the Mongo query
query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": ids}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-3168952214730479894': 'file_storage/function-call-3168952214730479894.json', 'var_function-call-4354025683768215761': 'file_storage/function-call-4354025683768215761.json'}

exec(code, env_args)

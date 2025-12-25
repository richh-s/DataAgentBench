code = """import json

file_path = locals()['var_function-call-14238142441611435889']
with open(file_path, 'r') as f:
    data = json.load(f)

article_ids = [int(x) for x in data['article_ids']]

# Construct Mongo query
query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": article_ids}
    },
    "projection": {
        "_id": 0,
        "article_id": 1,
        "title": 1,
        "description": 1
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-17386204446982133767': 'file_storage/function-call-17386204446982133767.json', 'var_function-call-14238142441611435889': 'file_storage/function-call-14238142441611435889.json'}

exec(code, env_args)

code = """import json

with open(locals()['var_function-call-8179185153208761910'], 'r') as f:
    article_ids = json.load(f)

query = json.dumps({"collection": "articles", "filter": {"article_id": {"$in": article_ids}}, "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}})

print("__RESULT__:")
print(query)"""

env_args = {'var_function-call-17178962666327171362': 'file_storage/function-call-17178962666327171362.json', 'var_function-call-8179185153208761910': 'file_storage/function-call-8179185153208761910.json'}

exec(code, env_args)

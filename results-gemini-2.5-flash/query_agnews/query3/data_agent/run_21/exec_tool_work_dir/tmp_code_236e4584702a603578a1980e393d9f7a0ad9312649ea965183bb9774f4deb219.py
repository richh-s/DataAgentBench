code = """import json

with open(locals()['var_function-call-14129203744487139235'], 'r') as f:
    article_ids = json.load(f)

query = {"collection": "articles", "filter": {"article_id": {"$in": article_ids}}, "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}}

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-16393350103042382032': 'file_storage/function-call-16393350103042382032.json', 'var_function-call-14129203744487139235': 'file_storage/function-call-14129203744487139235.json'}

exec(code, env_args)

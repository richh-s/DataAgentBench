code = """import json

article_ids = json.load(open(locals()['var_function-call-602643125818085257']))

# Convert the list of article_ids to integers for MongoDB query
article_ids_int = [int(id) for id in article_ids]

# Construct the MongoDB query as a JSON string
mongo_query = json.dumps({"collection": "articles", "filter": {"article_id": {"$in": article_ids_int}}, "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}})

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-17865766690995657723': 'file_storage/function-call-17865766690995657723.json', 'var_function-call-1237481626713895863': 'file_storage/function-call-1237481626713895863.json', 'var_function-call-602643125818085257': 'file_storage/function-call-602643125818085257.json', 'var_function-call-10478015613867595960': 'file_storage/function-call-10478015613867595960.json'}

exec(code, env_args)

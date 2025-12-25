code = """import json

article_ids = json.load(open(locals()['var_function-call-602643125818085257']))

# Convert the list of article_ids to integers for MongoDB query
article_ids_int = [int(id) for id in article_ids]

query_filter = {"article_id": {"$in": article_ids_int}}

print("__RESULT__:")
print(json.dumps(query_filter))"""

env_args = {'var_function-call-17865766690995657723': 'file_storage/function-call-17865766690995657723.json', 'var_function-call-1237481626713895863': 'file_storage/function-call-1237481626713895863.json', 'var_function-call-602643125818085257': 'file_storage/function-call-602643125818085257.json'}

exec(code, env_args)

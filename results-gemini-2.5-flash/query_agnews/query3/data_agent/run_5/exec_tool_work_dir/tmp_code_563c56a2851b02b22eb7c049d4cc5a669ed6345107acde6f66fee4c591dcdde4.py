code = """import json

# Load article_ids from the previous step
article_ids_str = json.load(open(locals()['var_function-call-602643125818085257']))
article_ids_int = [int(aid) for aid in article_ids_str]

# Construct the full MongoDB query as a Python dictionary
mongo_query_dict = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids_int}},
    "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
}

# Convert the dictionary to a JSON string
mongo_query_json = json.dumps(mongo_query_dict)

print("__RESULT__:")
print(mongo_query_json)"""

env_args = {'var_function-call-17865766690995657723': 'file_storage/function-call-17865766690995657723.json', 'var_function-call-1237481626713895863': 'file_storage/function-call-1237481626713895863.json', 'var_function-call-602643125818085257': 'file_storage/function-call-602643125818085257.json', 'var_function-call-10478015613867595960': 'file_storage/function-call-10478015613867595960.json', 'var_function-call-5871368796247991770': 'file_storage/function-call-5871368796247991770.json', 'var_function-call-7053804959655917203': 'file_storage/function-call-7053804959655917203.json'}

exec(code, env_args)

code = """import json

# Assuming var_function-call-7566576120602219907 contains the list of article_ids
article_ids = locals()['var_function-call-7566576120602219907']

# Construct the MongoDB query with the article_ids list converted to a JSON string
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-13108544427236254645': 'file_storage/function-call-13108544427236254645.json', 'var_function-call-7566576120602219907': 'file_storage/function-call-7566576120602219907.json'}

exec(code, env_args)

code = """import json

article_ids_str = json.load(open(locals()['var_function-call-602643125818085257']))
article_ids_int = [int(aid) for aid in article_ids_str]

mongo_query_filter = json.dumps({"article_id": {"$in": article_ids_int}})

print("__RESULT__:")
print(mongo_query_filter)"""

env_args = {'var_function-call-17865766690995657723': 'file_storage/function-call-17865766690995657723.json', 'var_function-call-1237481626713895863': 'file_storage/function-call-1237481626713895863.json', 'var_function-call-602643125818085257': 'file_storage/function-call-602643125818085257.json', 'var_function-call-10478015613867595960': 'file_storage/function-call-10478015613867595960.json', 'var_function-call-5871368796247991770': 'file_storage/function-call-5871368796247991770.json'}

exec(code, env_args)

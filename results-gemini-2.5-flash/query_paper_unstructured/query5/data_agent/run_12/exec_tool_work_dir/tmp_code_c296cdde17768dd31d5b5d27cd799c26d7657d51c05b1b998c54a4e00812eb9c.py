code = """import json

filenames_list = locals()['var_function-call-6588179796605751218']
query_filter = json.dumps({"filename": {"$in": filenames_list}})

mongo_query = {"collection": "paper_docs", "filter": json.loads(query_filter), "projection": {"filename": 1, "text": 1}}
print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-15052837677645358985': 'file_storage/function-call-15052837677645358985.json', 'var_function-call-17290402157997289971': 'file_storage/function-call-17290402157997289971.json', 'var_function-call-6588179796605751218': 'file_storage/function-call-6588179796605751218.json'}

exec(code, env_args)

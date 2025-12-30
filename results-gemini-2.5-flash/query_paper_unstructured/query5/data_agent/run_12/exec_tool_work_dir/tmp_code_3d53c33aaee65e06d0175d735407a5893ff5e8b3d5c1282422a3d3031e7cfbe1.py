code = """import json

with open(locals()['var_function-call-6588179796605751218'], 'r') as f:
    filenames = json.load(f)

mongo_query_string = json.dumps({"collection": "paper_docs", "filter": {"filename": {"$in": filenames}}, "projection": {"filename": 1, "text": 1}})
print("__RESULT__:")
print(mongo_query_string)"""

env_args = {'var_function-call-15052837677645358985': 'file_storage/function-call-15052837677645358985.json', 'var_function-call-17290402157997289971': 'file_storage/function-call-17290402157997289971.json', 'var_function-call-6588179796605751218': 'file_storage/function-call-6588179796605751218.json', 'var_function-call-13133980189294841151': {'collection': 'paper_docs', 'filter': {'filename': {'$in': 'file_storage/function-call-6588179796605751218.json'}}, 'projection': {'filename': 1, 'text': 1}}, 'var_function-call-15296236495957703649': 'file_storage/function-call-15296236495957703649.json'}

exec(code, env_args)

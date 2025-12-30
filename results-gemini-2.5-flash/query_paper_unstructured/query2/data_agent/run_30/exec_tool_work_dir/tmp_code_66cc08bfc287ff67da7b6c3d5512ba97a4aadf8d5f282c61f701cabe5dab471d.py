code = """import json
with open(locals()['var_function-call-3752941315378179949'], 'r') as f:
    titles = json.load(f)
query_filter = {"filename": {"$in": [title + ".txt" for title in titles]}}
print('__RESULT__:')
print(json.dumps(query_filter))"""

env_args = {'var_function-call-5858147982497012286': 'file_storage/function-call-5858147982497012286.json', 'var_function-call-3752941315378179949': 'file_storage/function-call-3752941315378179949.json'}

exec(code, env_args)

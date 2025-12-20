code = """import json

article_ids_from_storage = json.load(open(locals()['var_function-call-1237481626713895863']))


print("__RESULT__:")
print(json.dumps(article_ids_from_storage))"""

env_args = {'var_function-call-17865766690995657723': 'file_storage/function-call-17865766690995657723.json', 'var_function-call-1237481626713895863': 'file_storage/function-call-1237481626713895863.json'}

exec(code, env_args)

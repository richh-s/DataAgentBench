code = """import json

with open(locals()['var_function-call-10118669966329867769'], 'r') as f:
    data = json.load(f)

ids = data['article_ids']
min_id = min(ids)
max_id = max(ids)
print("__RESULT__:")
print(json.dumps({"min": min_id, "max": max_id, "count": len(ids)}))"""

env_args = {'var_function-call-13078718259946536180': 'file_storage/function-call-13078718259946536180.json', 'var_function-call-10118669966329867769': 'file_storage/function-call-10118669966329867769.json', 'var_function-call-3403215652805393396': 6696}

exec(code, env_args)

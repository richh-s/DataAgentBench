code = """import json

with open(locals()['var_function-call-6674564950342530332'], 'r') as f:
    data = json.load(f)

ids = [int(item['article_id']) for item in data]
print("__RESULT__:")
print(json.dumps({"count": len(ids), "ids": ids[:10], "all_ids": ids}))"""

env_args = {'var_function-call-6674564950342530332': 'file_storage/function-call-6674564950342530332.json'}

exec(code, env_args)

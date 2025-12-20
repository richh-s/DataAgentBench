code = """import json

with open(locals()['var_function-call-2325136846881096984'], 'r') as f:
    data = json.load(f)

ids = data['all_ids']
print("__RESULT__:")
print(json.dumps({"min": min(ids), "max": max(ids), "count": len(ids)}))"""

env_args = {'var_function-call-6674564950342530332': 'file_storage/function-call-6674564950342530332.json', 'var_function-call-2325136846881096984': 'file_storage/function-call-2325136846881096984.json'}

exec(code, env_args)

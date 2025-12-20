code = """import json

with open(locals()['var_function-call-3657157287295125768'], 'r') as f:
    data = json.load(f)

ids = data['ids']
min_id = min(ids)
max_id = max(ids)
count = len(ids)

print("__RESULT__:")
print(json.dumps({"min": min_id, "max": max_id, "count": count}))"""

env_args = {'var_function-call-16230520417025150586': 'file_storage/function-call-16230520417025150586.json', 'var_function-call-3657157287295125768': 'file_storage/function-call-3657157287295125768.json'}

exec(code, env_args)

code = """import json
# var_call_0DRPXBYbhRuzxDy2ieFdONjy is provided by previous query_db call
v = var_call_0DRPXBYbhRuzxDy2ieFdONjy
if isinstance(v, str) and v.endswith('.json'):
    with open(v, 'r') as f:
        data = json.load(f)
else:
    data = v
ids = [int(d['article_id']) for d in data]
ids = sorted(set(ids))
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_0DRPXBYbhRuzxDy2ieFdONjy': 'file_storage/call_0DRPXBYbhRuzxDy2ieFdONjy.json'}

exec(code, env_args)

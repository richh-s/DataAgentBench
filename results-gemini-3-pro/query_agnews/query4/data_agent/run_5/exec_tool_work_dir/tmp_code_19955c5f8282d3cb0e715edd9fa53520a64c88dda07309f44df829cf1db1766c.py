code = """import json

with open(locals()['var_function-call-1474084106243643964'], 'r') as f:
    data = json.load(f)

ids = [row['article_id'] for row in data]
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_function-call-1474084106243643964': 'file_storage/function-call-1474084106243643964.json'}

exec(code, env_args)

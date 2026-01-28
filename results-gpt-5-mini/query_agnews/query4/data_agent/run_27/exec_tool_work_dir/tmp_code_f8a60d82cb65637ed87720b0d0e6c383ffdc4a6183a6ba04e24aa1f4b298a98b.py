code = """import json
path = var_call_omp3ddExYwoslFqB4uKYS5tq
with open(path, 'r') as f:
    data = json.load(f)
ids = [int(item['article_id']) for item in data]
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_omp3ddExYwoslFqB4uKYS5tq': 'file_storage/call_omp3ddExYwoslFqB4uKYS5tq.json'}

exec(code, env_args)

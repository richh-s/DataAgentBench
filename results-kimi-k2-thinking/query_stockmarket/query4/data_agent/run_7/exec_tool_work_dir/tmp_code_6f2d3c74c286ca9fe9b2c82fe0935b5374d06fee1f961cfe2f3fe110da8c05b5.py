code = """import json, os
res = var_functions.query_db:0
if isinstance(res, str) and res.endswith('.json'):
    with open(res, 'r') as f:
        data = json.load(f)
else:
    data = res

type(data), len(data)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

code = """import json, pandas as pd, re
business_file = var_functions.query_db:9
with open(business_file, 'r') as f:
    data = json.load(f)
print('__RESULT__:')
print(json.dumps({'count': len(data), 'sample': data[0] if data else None}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review', 'tip', 'user'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)

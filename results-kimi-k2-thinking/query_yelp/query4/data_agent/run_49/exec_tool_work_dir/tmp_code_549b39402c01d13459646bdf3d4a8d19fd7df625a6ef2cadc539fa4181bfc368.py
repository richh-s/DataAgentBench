code = """import json, pandas as pd
storage_key = 'var_functions.query_db:9'
business_file = locals()[storage_key]
with open(business_file, 'r') as f:
    data = json.load(f)
print('__RESULT__:')
print(json.dumps({'count': len(data), 'first_keys': list(data[0].keys()) if data else []}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review', 'tip', 'user'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)

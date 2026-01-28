code = """import json
with open('/mnt/data/result_query_db_2.json', 'r') as f:
    data = json.load(f)
print('__RESULT__:')
print(json.dumps({'count': len(data), 'sample': data[:3]}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

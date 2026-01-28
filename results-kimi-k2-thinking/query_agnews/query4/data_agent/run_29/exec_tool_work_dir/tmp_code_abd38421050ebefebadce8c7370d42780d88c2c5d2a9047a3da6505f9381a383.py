code = """import json
print('__RESULT__:')
print(json.dumps({'message': 'testing variable access'}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

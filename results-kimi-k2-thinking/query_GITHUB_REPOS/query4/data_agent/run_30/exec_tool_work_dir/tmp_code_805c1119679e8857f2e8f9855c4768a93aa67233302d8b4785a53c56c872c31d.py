code = """import json
storage_key = 'var_functions.query_db:0'
result = locals()[storage_key]
print('__RESULT__:')
print(json.dumps({'type': str(type(result)), 'preview': str(result)[:200]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

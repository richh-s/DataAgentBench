code = """import json
result = var_functions.query_db:2
print('__RESULT__:')
print(json.dumps(str(result)[:200]))"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

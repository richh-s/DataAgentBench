code = """import json
print('Available variables:', list(globals().keys()))
print('__RESULT__:')
print(json.dumps('test'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

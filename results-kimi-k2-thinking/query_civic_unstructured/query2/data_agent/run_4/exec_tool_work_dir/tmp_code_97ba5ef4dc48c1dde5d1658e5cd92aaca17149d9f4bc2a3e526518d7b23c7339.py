code = """import json

# Just check what variables are available
available_vars = list(locals().keys())
print('__RESULT__:')
print(json.dumps(available_vars))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

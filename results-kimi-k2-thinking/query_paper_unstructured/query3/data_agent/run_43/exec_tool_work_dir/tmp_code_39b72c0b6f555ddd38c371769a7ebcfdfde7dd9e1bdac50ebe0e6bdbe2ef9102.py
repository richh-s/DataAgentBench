code = """import json

# Check what variables are available
available_vars = list(locals().keys())
print('__RESULT__:')
print(json.dumps(available_vars))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

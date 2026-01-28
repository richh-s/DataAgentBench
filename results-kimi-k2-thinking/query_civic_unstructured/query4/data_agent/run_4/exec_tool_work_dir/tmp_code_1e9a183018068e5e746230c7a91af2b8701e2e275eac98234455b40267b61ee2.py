code = """import json

# Check what variables are available
available_vars = {}
for name in dir():
    if name.startswith('var_'):
        available_vars[name] = str(type(locals()[name]))

print('__RESULT__:')
print(json.dumps(available_vars))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

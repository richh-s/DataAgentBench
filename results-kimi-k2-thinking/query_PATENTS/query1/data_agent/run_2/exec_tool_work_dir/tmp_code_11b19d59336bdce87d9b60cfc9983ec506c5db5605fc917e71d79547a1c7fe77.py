code = """# First, check what variables are available
print('__RESULT__:')
available_vars = list(locals().keys())
print(json.dumps({'available_keys': available_vars[:50]}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

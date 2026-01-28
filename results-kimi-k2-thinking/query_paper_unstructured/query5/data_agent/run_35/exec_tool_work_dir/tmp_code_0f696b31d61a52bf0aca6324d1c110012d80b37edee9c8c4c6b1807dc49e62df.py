code = """# First check what variables are available in the environment
available_vars = [k for k in locals().keys() if k.startswith('var_')]
print('__RESULT__:')
print(json.dumps({
    'available_vars': available_vars,
    'all_locals_keys': list(locals().keys())[:20]  # Show first 20 keys
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

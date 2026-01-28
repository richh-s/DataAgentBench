code = """# Check what variables are available
available_vars = list(locals().keys())
print('Available variables:')
for v in available_vars:
    print('  ', v)

print('\n__RESULT__:')
print('vars_checked')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

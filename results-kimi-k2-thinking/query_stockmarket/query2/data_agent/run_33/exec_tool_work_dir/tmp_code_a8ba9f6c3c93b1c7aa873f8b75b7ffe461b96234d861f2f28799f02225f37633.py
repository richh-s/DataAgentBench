code = """# Check what's stored in the variable
data = locals()['var_functions.query_db:0']
print('__RESULT__:')
print(type(data).__name__)
print(str(data)[:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

code = """# Check what type of data is stored in the variable
result = locals()['var_functions.query_db:0']

print('__RESULT__:')
print(f"Type: {type(result)}")
print(f"Content preview: {str(result)[:200]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

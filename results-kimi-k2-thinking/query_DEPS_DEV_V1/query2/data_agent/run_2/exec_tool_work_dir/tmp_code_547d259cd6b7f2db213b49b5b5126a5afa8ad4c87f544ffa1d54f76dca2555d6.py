code = """# Access the result from storage
result = locals()['var_functions.query_db:0']
print('__RESULT__:')
print(str(result)[:100] if result else 'No result')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

code = """# Let's check what variables are available in the local scope
temp_keys = [k for k in locals().keys() if 'var_' in k]
print('__RESULT__:')
print(temp_keys)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

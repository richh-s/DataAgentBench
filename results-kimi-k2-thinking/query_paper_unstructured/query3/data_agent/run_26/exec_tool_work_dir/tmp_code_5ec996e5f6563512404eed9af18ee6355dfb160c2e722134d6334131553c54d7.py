code = """# Check what's in the variables
print('__RESULT__:')
print('var_functions.query_db:2'[:100])
print('var_functions.query_db:5'[:100])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """# Check what type of data we have in the result
result = locals()['var_functions.query_db:2']
result_type = type(result).__name__
print('__RESULT__:')
print(result_type)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

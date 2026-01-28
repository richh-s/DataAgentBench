code = """# Check what type of data is stored in the query result
result = var_functions.query_db:0
print('__RESULT__:')
print(type(result).__name__)
print(str(result)[:1000])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs']}

exec(code, env_args)

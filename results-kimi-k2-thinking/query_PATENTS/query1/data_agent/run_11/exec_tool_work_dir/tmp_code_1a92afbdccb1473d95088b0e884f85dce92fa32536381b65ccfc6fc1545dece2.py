code = """result_file = var_functions.query_db:5
print(type(result_file))
print(result_file[:200] if isinstance(result_file, str) else 'Not a string')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

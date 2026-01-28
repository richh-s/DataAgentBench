code = """# Check the variable for query result
path = var_functions.query_db:2
print(type(path))
print(path[:200])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

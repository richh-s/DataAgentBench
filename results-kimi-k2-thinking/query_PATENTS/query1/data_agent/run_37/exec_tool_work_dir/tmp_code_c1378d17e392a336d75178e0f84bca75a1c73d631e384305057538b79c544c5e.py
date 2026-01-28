code = """# First, let's see what the variable contains
print("Variable type:", type(var_functions.query_db:6))
print("Variable value:", var_functions.query_db:6)

# Check if it's a string (file path)
if isinstance(var_functions.query_db:6, str):
    print("It's a file path string")
else:
    print("It's not a string, it might be the actual data")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

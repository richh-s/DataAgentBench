code = """# Check what type of data we have in the result
result_type = type(var_functions.query_db:2).__name__
print(f"Result type: {result_type}")
print(f"Result value: {repr(var_functions.query_db:2)}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

code = """import json

# Check what variables are available
available_vars = [var for var in locals().keys() if var.startswith('var_')]
print("Available variables:", available_vars)

# Try to access the result
if 'var_functions.query_db:0' in locals():
    result_file = locals()['var_functions.query_db:0']
    print(f"Result file path: {result_file}")
else:
    print("var_functions.query_db:0 not found in locals()")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

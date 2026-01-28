code = """import json
import re

# Get the available variables that store our query results
# These are the result keys from previous tool calls
var_keys = [key for key in locals().keys() if key.startswith('var_')]
print("Available result variables:", var_keys)

# Access the actual data from the variables
if 'var_functions.query_db:0' in locals():
    languages_data = locals()['var_functions.query_db:0']
    print(f"Languages data type: {type(languages_data)}")
    print(f"Languages data length: {len(languages_data)}")
else:
    print("var_functions.query_db:0 not found")

if 'var_functions.query_db:2' in locals():
    readme_data = locals()['var_functions.query_db:2']
    print(f"README data type: {type(readme_data)}")
    print(f"README data length: {len(readme_data)}")
else:
    print("var_functions.query_db:2 not found")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

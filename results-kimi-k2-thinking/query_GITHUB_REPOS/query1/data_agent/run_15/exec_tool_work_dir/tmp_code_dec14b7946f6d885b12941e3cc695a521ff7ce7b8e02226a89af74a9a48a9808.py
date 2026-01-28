code = """# Let's check what variables are available in the local scope
import json
import os

# List all variables that start with 'var_'
variables = [name for name in locals().keys() if name.startswith('var_')]
print("Available variables:", variables)

# Let's check if the files exist in the current directory
files = os.listdir('.')
print("Files in current directory:", files[:20])  # Show first 20 files"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

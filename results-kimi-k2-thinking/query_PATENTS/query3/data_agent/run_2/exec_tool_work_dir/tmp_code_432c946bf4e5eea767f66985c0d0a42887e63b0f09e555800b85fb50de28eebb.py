code = """# Let's check what variables are available and find the correct file path
import json
import os

# The key should be in locals()
key_name = 'var_functions.query_db:2'
file_path = locals().get(key_name, None)

print(f"File path from storage: {file_path}")
print(f"File exists: {os.path.exists(file_path) if file_path else 'No file path'}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

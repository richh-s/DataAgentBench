code = """import json
import os

# The result is stored in a file
filepath = 'file_storage/functions.query_db:0.json'
print(f"File exists: {os.path.exists(filepath)}")
print(f"File size: {os.path.getsize(filepath) if os.path.exists(filepath) else 'N/A'}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

code = """import json
import pandas as pd
import re
import os

# Print all available files in the current directory
files = os.listdir('.')
print("Available files:", [f for f in files if 'json' in f])

# Load funding data
funding_path = None
for f in files:
    if 'query_db' in f and '14' in f:
        funding_path = f
        break

print(f"Funding file: {funding_path}")

# Also check the two project document files
project_path = None
project_2022_path = None
for f in files:
    if 'query_db' in f and '2' in f and ':' not in f:
        project_path = f
    elif 'query_db' in f and '16' in f and ':' not in f:
        project_2022_path = f

print(f"All project file: {project_path}")
print(f"2022 project file: {project_2022_path}")

print("__RESULT__:")
print(json.dumps({"funding": funding_path, "projects_all": project_path, "projects_2022": project_2022_path}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)

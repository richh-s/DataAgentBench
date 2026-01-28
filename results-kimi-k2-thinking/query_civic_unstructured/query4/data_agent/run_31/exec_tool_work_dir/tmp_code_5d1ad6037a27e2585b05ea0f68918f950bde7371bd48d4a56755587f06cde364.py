code = """import json, pandas as pd

# Access data using locals()
var_keys = [k for k in locals().keys() if 'query_db' in k]
print("Available query_db variables:", var_keys)

# Try to access funding data
funding_key = None
project_key = None
for k in var_keys:
    if ':14' in k:
        funding_key = k
    elif ':36' in k:
        project_key = k

print("Funding key:", funding_key)
print("Project key:", project_key)

if funding_key and project_key:
    funding_data = locals()[funding_key]
    projects_data = locals()[project_key]
    
    print(f"Funding records: {len(funding_data)}")
    print(f"Project docs: {len(projects_data)}")

print("__RESULT__:")
print(json.dumps({"status": "checked variables"}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:26': {'funding': None, 'projects_all': None, 'projects_2022': None}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)

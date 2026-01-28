code = """import json
import re

# Read the full file from the stored key
import os
with open('func_response.json', 'r') as f:
    resp = json.load(f)
    print("Response keys:", list(resp.keys()))
    file_path_key = 'var_functions.query_db:2'
    file_path = resp.get(file_path_key, '')
    print("File path:", file_path)

# Read the actual file
if file_path and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        full_data = json.load(f)
    print(f"Number of documents: {len(full_data)}")
    if len(full_data) > 0:
        print("First document keys:", list(full_data[0].keys()))
        print("Sample:", full_data[0].get('text', '')[:500])
else:
    print("File not found")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

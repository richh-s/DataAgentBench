code = """import json
import os

# Get the file path from the storage
file_path = '/tmp/tmphn4t1u8a.json'

# Check if file exists
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        civic_docs_result = json.load(f)
    print(f"__RESULT__:")
    print(json.dumps({"count": len(civic_docs_result), "file_exists": True}))
else:
    print(f"__RESULT__:")
    print(json.dumps({"count": 0, "file_exists": False, "error": f"File not found: {file_path}"}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

code = """import json
import os

# Check what's in the variable
file_path = var_functions.query_db__0
print(f"File path: {file_path}")
print(f"File exists: {os.path.exists(file_path)}")

# Read the file
with open(file_path, 'r') as f:
    mongo_results = json.load(f)

print(f"Number of documents retrieved: {len(mongo_results)}")
print("Sample document:")
print(json.dumps(mongo_results[0], indent=2)[:2000])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

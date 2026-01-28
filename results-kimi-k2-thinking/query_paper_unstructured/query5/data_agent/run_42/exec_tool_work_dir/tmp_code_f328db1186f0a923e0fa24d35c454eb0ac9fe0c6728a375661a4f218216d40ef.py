code = """import json
import os

# Read the full result from the file
file_path = var_functions.query_db:0
if isinstance(file_path, str) and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        citations_2020 = json.load(f)
else:
    # If it's already a list, use it directly
    citations_2020 = var_functions.query_db:0

print('__RESULT__:')
print(json.dumps(citations_2020[:5]))  # Print first 5 records to verify"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

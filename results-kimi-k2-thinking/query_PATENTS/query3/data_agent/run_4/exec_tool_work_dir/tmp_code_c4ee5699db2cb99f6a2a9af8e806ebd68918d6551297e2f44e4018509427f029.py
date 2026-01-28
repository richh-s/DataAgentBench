code = """import json
import pandas as pd
import re

# Load the result from the previous query
result_file = var_functions.query_db:2

# Read the JSON file
with open(result_file, 'r') as f:
    data = json.load(f)

# Count UNIV CALIFORNIA patents
uni_california_count = 0
for record in data:
    if 'UNIV CALIFORNIA' in record['Patents_info']:
        uni_california_count += 1

print("__RESULT__:")
print(json.dumps({
    "total_records": len(data),
    "uni_california_records": uni_california_count
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

code = """import json
import pandas as pd
import re

# Load the result from the previous query
result_file = var_functions.query_db:2

print("Loading data from file:", result_file)

# Read the JSON file
with open(result_file, 'r') as f:
    data = json.load(f)

print("Number of records:", len(data))
print("\nFirst record structure:")
print(json.dumps(data[0], indent=2)[:2000])

# Count UNIV CALIFORNIA patents
uni_california_count = 0
for record in data:
    if 'UNIV CALIFORNIA' in record['Patents_info']:
        uni_california_count += 1

print("\nFound", uni_california_count, "UNIV CALIFORNIA patents in sample")
print("Total records:", len(data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

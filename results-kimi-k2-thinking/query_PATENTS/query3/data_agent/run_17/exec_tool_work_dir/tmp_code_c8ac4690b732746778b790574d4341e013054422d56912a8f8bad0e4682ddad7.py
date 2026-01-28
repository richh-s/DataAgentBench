code = """import json
import pandas as pd
from collections import defaultdict

# Read the file path from storage
file_path = locals()['var_functions.query_db:12']
print(f"File path: {file_path}")

# Load the data
with open(file_path, 'r') as f:
    univ_california_patents = json.load(f)

print(f"Total UNIV CALIFORNIA patents: {len(univ_california_patents)}")

# Extract publication numbers of UNIV CALIFORNIA patents
uc_pub_numbers = set()
for patent in univ_california_patents:
    patents_info = patent.get('Patents_info', '')
    # Extract publication number from Patents_info
    if 'pub. number' in patents_info:
        # Look for pattern like "pub. number US-2022074631-A1"
        import re
        match = re.search(r'pub\. number\s+([A-Z]{2}-[^\s]+)', patents_info)
        if match:
            uc_pub_numbers.add(match.group(1))

print(f"Found {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")
print(list(uc_pub_numbers)[:10])  # Show first 10"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

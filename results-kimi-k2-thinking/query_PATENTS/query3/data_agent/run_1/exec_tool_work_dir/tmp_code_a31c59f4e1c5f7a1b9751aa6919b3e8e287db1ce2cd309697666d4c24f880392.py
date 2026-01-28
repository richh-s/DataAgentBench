code = """import json
import re
from collections import defaultdict

# Load the full results from the queries
result_path_1 = var_functions.query_db:5  # General query result
result_path_2 = var_functions.query_db:6  # UNIV CALIFORNIA query result

# Read the full results
with open(result_path_1.replace('"', ''), 'r') as f:
    general_results = json.load(f)

with open(result_path_2.replace('"', ''), 'r') as f:
    uc_results = json.load(f)

print(f"Total patents in database: {len(general_results)}")
print(f"UNIV CALIFORNIA patents found: {len(uc_results)}")

# Check sample data structure
print("\nSample data structure:")
print("Keys in a record:", list(uc_results[0].keys()) if uc_results else "No data")
print("\nSample Patents_info:", uc_results[0]['Patents_info'] if uc_results else "No data")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

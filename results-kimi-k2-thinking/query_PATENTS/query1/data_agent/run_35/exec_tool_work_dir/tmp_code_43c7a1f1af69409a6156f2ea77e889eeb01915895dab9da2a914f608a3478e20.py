code = """import json
import os

# Load the full list of CPC group codes with best year 2022
with open('/tmp/best_2022_groups.json', 'r') as f:
    group_codes = json.load(f)

print(f"Total CPC group codes with best year 2022: {len(group_codes)}")
print("All codes:", group_codes)

print("__RESULT__:")
print(json.dumps(group_codes))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'Processed 2141569 records, years 1837-2024', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'records': 2141569, 'level5_symbols': 677}, 'var_functions.execute_python:22': {'groups': 667, 'years': 186}, 'var_functions.execute_python:26': {'total_groups': 667, 'best_2022_count': 177, 'top_10': ['H01L', 'A61K', 'G06F', 'A61B', 'H04W', 'H04N', 'A61P', 'B32B', 'G01N', 'B29C']}}

exec(code, env_args)

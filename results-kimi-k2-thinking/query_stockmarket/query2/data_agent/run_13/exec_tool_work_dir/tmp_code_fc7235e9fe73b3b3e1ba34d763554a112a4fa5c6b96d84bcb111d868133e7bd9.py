code = """import json
import os

# Read the full list of NYSE Arca ETFs
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    etf_list = json.load(f)

print(f"Total NYSE Arca ETFs found: {len(etf_list)}")
print("__RESULT__:")
print(json.dumps(etf_list[:5]))  # Print first 5 as preview"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

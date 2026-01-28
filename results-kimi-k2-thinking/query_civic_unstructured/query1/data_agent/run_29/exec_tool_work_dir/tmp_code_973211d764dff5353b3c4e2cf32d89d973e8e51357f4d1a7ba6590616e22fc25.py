code = """import json
import pandas as pd
from pathlib import Path

# Read the funding data from the JSON file
funding_file = 'file_storage/functions.query_db:5.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create DataFrame for funding
df_funding = pd.DataFrame(funding_data)

# Convert Amount to int if it isn't already
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Filter for amount > 50000
df_funding_filtered = df_funding[df_funding['Amount'] > 50000]

print('__RESULT__:')
print(json.dumps({
    'total_funding_records': len(df_funding),
    'funding_over_50k': len(df_funding_filtered),
    'sample_projects': df_funding_filtered['Project_Name'].head(10).tolist()
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}}

exec(code, env_args)

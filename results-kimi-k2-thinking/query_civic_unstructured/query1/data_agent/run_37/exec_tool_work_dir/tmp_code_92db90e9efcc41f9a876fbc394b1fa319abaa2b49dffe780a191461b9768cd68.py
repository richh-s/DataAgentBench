code = """import json
import re
import os

# Access the stored results using the storage keys
funding_result_key = 'var_functions.query_db:2'
civic_result_key = 'var_functions.query_db:5'

# Get the actual data from storage
funding_data = globals().get(funding_result_key, [])
civic_docs = globals().get(civic_result_key, [])

print("Funding data type:", type(funding_data))
print("Civic docs type:", type(civic_docs))
print("Funding data length:", len(funding_data) if isinstance(funding_data, list) else 'Not a list')
print("Civic docs length:", len(civic_docs) if isinstance(civic_docs, list) else 'Not a list')

# If data is not directly accessible, check if they're file paths
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print("After loading:")
print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

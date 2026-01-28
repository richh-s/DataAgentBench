code = """import json
import re

# Get the file paths from the storage variables
funding_path = locals()['var_functions.query_db:6']
civic_docs_path = locals()['var_functions.query_db:2']

# Debug: Check what we got
print(f"Funding path: {funding_path}")
print(f"Civic docs path: {civic_docs_path}")

# Load and process the data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_data)} funding records")
print(f"Loaded {len(civic_docs)} civic documents")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

code = """import json
import re

# Get file paths from variables
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

# Load civic documents data
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Load funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# For debugging: show first record of each
print(f"\nFirst funding record: {json.dumps(funding_data[0])}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

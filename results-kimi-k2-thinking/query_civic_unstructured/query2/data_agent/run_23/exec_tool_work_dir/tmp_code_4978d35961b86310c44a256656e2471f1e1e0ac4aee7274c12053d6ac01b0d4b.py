code = """import json
import re
import os

# Read the civic documents data using the correct key
civic_docs_data = locals()['var_functions.query_db:2']
print(f"Civic docs data type: {type(civic_docs_data)}")

# If it's a string (file path), load it
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} civic documents")

# Read the funding data using the correct key
funding_data = locals()['var_functions.query_db:9']
print(f"Funding data type: {type(funding_data)}")

# If it's a string (file path), load it
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

print(f"Loaded {len(funding_data)} funding records")

# Preview first records
if civic_docs_data:
    print(f"First civic doc keys: {list(civic_docs_data[0].keys())}")
    if 'text' in civic_docs_data[0]:
        print(f"First doc text snippet: {civic_docs_data[0]['text'][:300]}")

if funding_data:
    print(f"First funding record: {funding_data[0]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

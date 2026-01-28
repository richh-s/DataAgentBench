code = """import json
import re

# Load funding data
with open('funding_data.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data  
with open('civic_docs_data.json', 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")
print(f"\nFunding data keys: {list(funding_data[0].keys())}")
print(f"Civic docs keys: {list(civic_docs[0].keys())}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

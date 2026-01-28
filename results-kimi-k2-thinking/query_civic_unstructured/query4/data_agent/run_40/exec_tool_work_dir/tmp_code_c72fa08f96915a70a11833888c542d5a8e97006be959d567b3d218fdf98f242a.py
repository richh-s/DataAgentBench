code = """import json
import re
import os

print("Loading data files...")
# Load funding data
with open('/root/shared_data/var_functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data  
with open('/root/shared_data/var_functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

if funding_data:
    keys = list(funding_data[0].keys())
    print("Funding data keys:", keys)
    
if civic_docs:
    keys = list(civic_docs[0].keys())
    print("Civic docs keys:", keys)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

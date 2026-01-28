code = """import json
import re

# Load funding data
with open('var_functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data  
with open('var_functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

if funding_data:
    print("Funding data keys:", list(funding_data[0].keys()))
    
if civic_docs:
    print("Civic docs keys:", list(civic_docs[0].keys()))

# Let's look at some sample data
print("\nSample funding record:", funding_data[0])
print("\nSample civic doc:", civic_docs[0].keys())"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

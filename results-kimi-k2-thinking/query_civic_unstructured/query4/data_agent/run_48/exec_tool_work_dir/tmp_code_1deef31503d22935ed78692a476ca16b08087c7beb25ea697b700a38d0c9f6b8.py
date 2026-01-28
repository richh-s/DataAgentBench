code = """import json
import os

# Read the full civic documents data
with open('var_functions.query_db:6', 'r') as f:
    civic_docs = json.load(f)

# Read the full funding data  
with open('var_functions.query_db:8', 'r') as f:
    funding_data = json.load(f)

print("Data loaded successfully")
print(f"Civic docs count: {len(civic_docs)}")
print(f"Funding records count: {len(funding_data)}")
print("\nFirst few civic docs:")
for i, doc in enumerate(civic_docs[:2]):
    print(f"Doc {i}: {doc.get('filename', 'No filename')}")
    print(f"Text preview: {doc.get('text', '')[:200]}...")
    print()

print("First few funding records:")
for rec in funding_data[:5]:
    print(rec)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

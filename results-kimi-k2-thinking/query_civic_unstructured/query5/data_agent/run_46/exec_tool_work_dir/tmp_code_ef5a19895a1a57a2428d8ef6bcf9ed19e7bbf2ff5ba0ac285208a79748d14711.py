code = """import json
import re
import os

# Read the civic documents from the file
civic_docs_file = 'var_functions.query_db:5.json'
if os.path.exists(civic_docs_file):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    print(f"File not found: {civic_docs_file}")
    civic_docs = []

# Read the funding data from the file
funding_file = 'var_functions.query_db:2.json'
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    print(f"File not found: {funding_file}")
    funding_data = []

print(f"Number of civic documents: {len(civic_docs)}")
print(f"Number of funding records: {len(funding_data)}")

if civic_docs:
    print("First civic document keys:", list(civic_docs[0].keys()))
if funding_data:
    print("First funding record keys:", list(funding_data[0].keys()))
    
print("\nData successfully loaded!")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

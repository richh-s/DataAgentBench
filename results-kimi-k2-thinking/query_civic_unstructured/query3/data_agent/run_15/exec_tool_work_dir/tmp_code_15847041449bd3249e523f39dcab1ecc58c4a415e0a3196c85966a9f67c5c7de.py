code = """import pandas as pd
import json
import os

# Load funding data
funding_path = 'var_functions.query_db:0'
print('Loading funding data from:', funding_path)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Funding records loaded:', len(funding_data))

# Load civic documents data
civic_path = 'var_functions.query_db:2'
print('Loading civic documents from:', civic_path)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Civic documents loaded:', len(civic_docs))

# Check first few records
print('\nFirst 3 funding records:')
for i, record in enumerate(funding_data[:3]):
    print(i, record)

print('\nFirst civic doc preview:')
print(civic_docs[0]['filename'])
print(civic_docs[0]['text'][:200])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

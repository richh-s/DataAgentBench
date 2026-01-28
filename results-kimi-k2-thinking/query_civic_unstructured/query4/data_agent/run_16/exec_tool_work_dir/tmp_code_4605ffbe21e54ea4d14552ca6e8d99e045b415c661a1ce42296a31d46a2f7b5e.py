code = """import json
import re
import os

# Load civic docs data
civic_file = "/tmp/tmp7q6r1zwh.json"
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data  
funding_file = "/tmp/tmptf8vwxq6.json"
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Loaded data:')
print(f'  Civic documents: {len(civic_docs)}')
print(f'  Funding records: {len(funding_data)}')

# Show first 3 funding records
print('\nFirst 3 funding records:')
for i, record in enumerate(funding_data[:3]):
    print(f'  {i+1}. {record}')

# Show first civic doc snippet
print('\nFirst civic doc snippet:')
print(json.dumps(civic_docs[0], indent=2)[:1000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

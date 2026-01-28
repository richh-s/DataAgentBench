code = """import json
import re

# Get the stored variables
funding_data = var_functions_query_db_5
civic_docs_data = var_functions_query_db_8

# Analyze funding data
print('FUNDING DATA INFO:')
print(f'Type: {type(funding_data)}')
print(f'Count: {len(funding_data)}')

# Look for patterns in project names
print('\nSample project names:')
for record in funding_data[:10]:
    print(f"  - {record['Project_Name']}")

print('\nSample funding amounts:')
for record in funding_data[:10]:
    print(f"  - {record['Amount']}")

# Analyze civic docs data
print('\n\nCIVIC DOCS INFO:')
print(f'Type: {type(civic_docs_data)}')
print(f'Count: {len(civic_docs_data)}')

# Check structure
first_doc = civic_docs_data[0]
print(f'Keys in first doc: {list(first_doc.keys())}')

# Sample text structure
sample_text = first_doc['text']
print(f'\nSample text length: {len(sample_text)}')
print(f'First 300 chars: {sample_text[:300]}')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

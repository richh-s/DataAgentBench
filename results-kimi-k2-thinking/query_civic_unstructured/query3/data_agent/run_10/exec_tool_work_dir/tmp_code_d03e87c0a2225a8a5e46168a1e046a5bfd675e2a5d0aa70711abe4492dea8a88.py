code = """import json
import re

# Check what variables are available
vars_list = list(locals().keys())
print('Available variables:', [v for v in vars_list if 'query_db' in v])

# Find and load the funding data
funding_key = [k for k in vars_list if 'query_db:0' in k][0]
civic_key = [k for k in vars_list if 'query_db:4' in k][0]

funding_data = locals()[funding_key]
civic_data = locals()[civic_key]

print('\nFunding data type:', type(funding_data))
print('Civic data type:', type(civic_data))

# If it's a string (file path), load it
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)
if isinstance(civic_data, str):
    with open(civic_data, 'r') as f:
        civic_data = json.load(f)

print('\nAfter loading:')
print('Funding records:', len(funding_data))
print('Civic docs:', len(civic_data))

# Find emergency/FEMA projects
matches = []
for record in funding_data:
    name = record['Project_Name'].lower()
    if 'emergency' in name or 'fema' in name:
        matches.append(record)

print('\nDirect matches:', len(matches))
result = json.dumps(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

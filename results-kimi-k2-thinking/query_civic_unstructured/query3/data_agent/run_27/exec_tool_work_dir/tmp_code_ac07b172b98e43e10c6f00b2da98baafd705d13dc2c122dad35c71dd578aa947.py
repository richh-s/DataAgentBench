code = """import json
import re

# Read funding data
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic documents data (filtered for emergency/FEMA)
civic_file = locals()['var_functions.query_db:10']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents with emergency/FEMA:', len(civic_data))

# Display first few records of each
print('\nFirst 3 funding records:')
for i, rec in enumerate(funding_data[:3]):
    print(f"{i+1}. {rec}")

print('\nFirst civic document preview:')
print(civic_data[0]['text'][:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.execute_python:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

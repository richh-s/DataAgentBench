code = """import json
import re

# Get the file paths
funding_file = locals()['var_functions.query_db:5']
civic_file = locals()['var_functions.query_db:2']

print('Funding file path:', str(funding_file)[:100])
print('Civic file path:', str(civic_file)[:100])

# Load data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded funding records:', len(funding_data))
print('Loaded civic documents:', len(civic_docs))

# Quick validation
if funding_data:
    print('First funding record:', json.dumps(funding_data[0]))
if civic_docs:
    print('First civic doc filename:', civic_docs[0].get('filename'))

print('Data loading complete')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

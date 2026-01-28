code = """import json
import os

# Get the correct file paths from storage
funding_file = 'file_storage/functions.query_db:2/result.json'
civic_file = 'file_storage/functions.query_db:5/result.json'

print('Checking file paths...')
print('Funding file exists:', os.path.exists(funding_file))
print('Civic file exists:', os.path.exists(civic_file))

# Load the data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)
    print('Funding data loaded:', len(funding_data), 'records')

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)
    print('Civic docs loaded:', len(civic_docs), 'documents')

# Now proceed with analysis..."""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

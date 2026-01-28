code = """import json
import os

# Check what variables are available
available_vars = [v for v in dir() if v.startswith('var_')]
print('Available variables:', available_vars)

# Let's check if we can access the funding and civic docs data directly
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:1

print('Funding file path type:', type(funding_file))
print('Civic file path type:', type(civic_file))

# Try to read the data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('Funding records:', len(funding_data))
print('Civic docs:', len(civic_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)

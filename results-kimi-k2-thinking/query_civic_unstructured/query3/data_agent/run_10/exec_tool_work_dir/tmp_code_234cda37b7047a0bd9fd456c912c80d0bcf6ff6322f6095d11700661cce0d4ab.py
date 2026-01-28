code = """import sys
import json

# First, let's see what variables are available
available_vars = list(globals().keys())
print('Available global variables:', available_vars[:20])

# Look for our specific variables
funding_var = [var for var in available_vars if 'query_db:0' in var]
civic_var = [var for var in available_vars if 'query_db:4' in var]

print('Funding variable name:', funding_var)
print('Civic variable name:', civic_var)

if funding_var:
    funding_data = globals()[funding_var[0]]
    print('\nFunding data type:', type(funding_data))
    if isinstance(funding_data, list):
        print('Funding records count:', len(funding_data))
        print('Sample funding records:')
        for i, record in enumerate(funding_data[:3]):
            print(f"  {i+1}. {record}")
    else:
        print('Funding data (string/preview):', str(funding_data)[:300])

if civic_var:
    civic_data = globals()[civic_var[0]]
    print('\nCivic data type:', type(civic_data))
    if isinstance(civic_data, list):
        print('Civic docs count:', len(civic_data))
        print('Sample civic docs:')
        for i, doc in enumerate(civic_data[:2]):
            print(f"  Doc {i+1}: {doc.get('filename', 'Unknown')}")
    else:
        print('Civic data (string/preview):', str(civic_data)[:300])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

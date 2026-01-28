code = """import json
import os

# Check what storage variables are available
storage_vars = [k for k in globals().keys() if k.startswith('var_functions')]
print('Available storage variables:', storage_vars)

# Access funding data
funding_var = 'var_functions.query_db:46'
if funding_var in globals():
    funding_path = globals()[funding_var]
    print('Funding path:', funding_path)
    if os.path.exists(funding_path):
        with open(funding_path, 'r') as f:
            funding_data = json.load(f)
        print('Loaded funding data:', len(funding_data), 'records')
    else:
        print('Funding file not found')
        funding_data = []
else:
    print('Funding variable not found')
    funding_data = []

# Access civic data
civic_var = 'var_functions.query_db:5'
if civic_var in globals():
    civic_path = globals()[civic_var]
    print('Civic path:', civic_path)
    if os.path.exists(civic_path):
        with open(civic_path, 'r') as f:
            civic_docs = json.load(f)
        print('Loaded civic docs:', len(civic_docs), 'documents')
    else:
        print('Civic file not found')
        civic_docs = []
else:
    print('Civic variable not found')
    civic_docs = []"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)

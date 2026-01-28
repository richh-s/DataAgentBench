code = """import json, pandas as pd, re
from datetime import datetime

# Access the stored data
civic_docs_data = locals()['var_functions.query_db:0']
funding_data = locals()['var_functions.query_db:1']

# Load data if it's file paths, or use directly if it's already loaded
def load_data(var):
    if isinstance(var, str) and '/tmp/' in var:
        with open(var, 'r') as f:
            return json.load(f)
    else:
        return var

# Load the actual data
civic_docs = load_data(civic_docs_data)
funding_records = load_data(funding_data)

print('Loaded data shapes:')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Show first record of each for verification
print('First civic doc keys:', list(civic_docs[0].keys()))
print('First funding record:', funding_records[0])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)

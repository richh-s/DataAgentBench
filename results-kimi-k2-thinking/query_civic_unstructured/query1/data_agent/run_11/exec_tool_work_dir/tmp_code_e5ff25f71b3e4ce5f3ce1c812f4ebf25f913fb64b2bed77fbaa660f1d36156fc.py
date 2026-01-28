code = """import json
import os

# Check what variables are available
available_vars = [var_name for var_name in locals().keys() if var_name.startswith('var_')]
print('Available variables:', available_vars)

# Read the civic docs data
civic_docs_path = 'var_functions.query_db:0'
funding_data_path = 'var_functions.query_db:2'

civic_docs = []
funding_data = []

if os.path.exists(civic_docs_path):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)

if os.path.exists(funding_data_path):
    with open(funding_data_path, 'r') as f:
        funding_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'civic_docs_sample': civic_docs[0] if civic_docs else None,
    'funding_data_count': len(funding_data),
    'funding_data_sample': funding_data[0] if funding_data else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

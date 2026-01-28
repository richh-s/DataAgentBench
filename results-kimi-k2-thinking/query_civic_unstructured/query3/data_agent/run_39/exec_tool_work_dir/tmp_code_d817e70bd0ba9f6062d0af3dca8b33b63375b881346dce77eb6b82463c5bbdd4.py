code = """import json
import re

# Load the data from storage
rv1 = locals()['var_functions.query_db:0']
r2 = locals()['var_functions.query_db:2']

print('First variable type:', type(rv1))
print('Second variable type:', type(r2))

# Load data
civic_docs = rv1 if isinstance(rv1, list) else json.load(open(rv1))
funding_data = r2 if isinstance(r2, list) else json.load(open(r2))

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_data), 'funding records')

# Show structure
print('First civic doc keys:', list(civic_docs[0].keys()) if civic_docs else 'No docs')
print('Sample funding record:', funding_data[0] if funding_data else 'No funding')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

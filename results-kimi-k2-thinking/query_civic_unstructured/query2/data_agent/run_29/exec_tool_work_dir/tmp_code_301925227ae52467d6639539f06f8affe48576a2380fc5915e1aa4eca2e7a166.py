code = """import json, re, sys

# Check what variables are available
available_vars = [var for var in locals().keys() if var.startswith('var_')]
print('Available variables:', available_vars, file=sys.stderr)

# Try to access the query results
civic_docs_var = locals().get('var_functions.query_db:2', [])
funding_var = locals().get('var_functions.query_db:16', [])

print(f'Civic docs type: {type(civic_docs_var)}', file=sys.stderr)
print(f'Funding type: {type(funding_var)}', file=sys.stderr)

# The results are likely already loaded as Python objects
civic_docs = civic_docs_var if isinstance(civic_docs_var, list) else []
funding_data = funding_var if isinstance(funding_var, list) else []

print(f'Civic docs count: {len(civic_docs)}', file=sys.stderr)
print(f'Funding records count: {len(funding_data)}', file=sys.stderr)

if civic_docs and funding_data:
    print('Both datasets loaded successfully', file=sys.stderr)
else:
    print('Failed to load one or both datasets', file=sys.stderr)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:30': []}

exec(code, env_args)

code = """import json

# Try to load the data from the storage variables
# The storage keys should be available as variables

try:
    funding_data = var_functions_query_db_2
    print('Funding data loaded directly')
except:
    print('Could not load funding data directly')
    funding_data = []

try:
    civic_docs = var_functions_query_db_6
    print('Civic docs loaded directly')
except:
    print('Could not load civic docs directly')
    civic_docs = []

print(f'Funding records: {len(funding_data)}')
print(f'Civic documents: {len(civic_docs)}')

# Let's also check what's available in the local scope
print('Available variables:', list(locals().keys()))

# Create simple test result
result = {'test': True, 'funding_count': len(funding_data), 'civic_count': len(civic_docs)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

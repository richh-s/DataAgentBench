code = """import json

# Access stored data
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:12']

print('Documents loaded:', len(civic_docs) if isinstance(civic_docs, list) else 'Not a list')
print('Funding records:', len(funding_data) if isinstance(funding_data, list) else 'Not a list')

# Show sample of data structure
if civic_docs:
    print('Sample civic doc keys:', list(civic_docs[0].keys()) if civic_docs else 'No data')
    
if funding_data:
    print('Sample funding record:', funding_data[0] if funding_data else 'No data')

print('__RESULT__:')
print(json.dumps({'status': 'loaded', 'civic_count': len(civic_docs), 'funding_count': len(funding_data)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

code = """# Let's access the data from the storage variable directly
# The file path was provided in the previous message

file_path = '/tmp/tmp3s5v9f5z.json'
print('File path:', file_path)

# Try to open and read the file
try:
    with open(file_path, 'r') as f:
        data = json.load(f)
    print('Successfully loaded data')
    print('Number of records:', len(data))
    
    # Show first record
    if data:
        print('First record keys:', list(data[0].keys()))
        print('Sample publication_date:', data[0].get('publication_date'))
        print('Sample cpc (first 200 chars):', str(data[0].get('cpc', ''))[:200])
    
    # Save to a simpler variable name for next steps
    publications = data
    
    result = {
        'success': True,
        'count': len(publications),
        'sample_keys': list(publications[0].keys()) if publications else []
    }
    
except Exception as e:
    print('Error loading file:', e)
    result = {'success': False, 'error': str(e)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

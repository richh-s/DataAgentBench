code = """import sys
print('Python version:', sys.version)
print('Available variables:')
for key in dir():
    if key.startswith('var_'):
        print(key, type(eval(key)), type(eval(key)).__name__)

print('\nChecking for funding and civic data...')

# Check for funding data
if 'var_functions.query_db:5' in dir():
    funding_data = locals()['var_functions.query_db:5']
    print('Funding data found')
    if isinstance(funding_data, str) and '.json' in funding_data:
        print('Funding data is stored at:', funding_data)
    else:
        print('Funding data is in memory, length:', len(str(funding_data)))

# Check for civic data  
if 'var_functions.query_db:2' in dir():
    civic_data = locals()['var_functions.query_db:2']
    print('Civic data found')
    if isinstance(civic_data, str) and '.json' in civic_data:
        print('Civic data is stored at:', civic_data)
    else:
        print('Civic data is in memory, length:', len(str(civic_data)))

print('__RESULT__:')
print('{"status": "diagnostic complete"}')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

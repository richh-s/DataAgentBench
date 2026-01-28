code = """import json

data_key = 'var_functions.query_db:2'
print('Checking locals() for key:', data_key)
print('Available keys containing "query":', [k for k in locals().keys() if 'query' in str(k)])

if data_key in locals():
    data = locals()[data_key]
    print('\nSuccess! Found data. Type:', type(data))
    if isinstance(data, list):
        print('Length:', len(data))
        if len(data) > 0:
            print('\nFirst record:')
            rec = data[0]
            print('Keys:', list(rec.keys()))
            print('Patents_info:', rec['Patents_info'])
    
    print('\n__RESULT__:')
    print('Found %d records' % len(data))
else:
    print('\n__RESULT__:')
    print('Key not found in locals()')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

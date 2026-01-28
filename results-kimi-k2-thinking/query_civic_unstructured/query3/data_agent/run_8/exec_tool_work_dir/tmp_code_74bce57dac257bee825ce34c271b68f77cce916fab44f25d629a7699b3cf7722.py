code = """import json

# Check what's in the storage variables
print('__RESULT__:')
print(json.dumps({
    'funding_storage_key': 'var_functions.query_db:5',
    'civic_docs_storage_key': 'var_functions.query_db:8'
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

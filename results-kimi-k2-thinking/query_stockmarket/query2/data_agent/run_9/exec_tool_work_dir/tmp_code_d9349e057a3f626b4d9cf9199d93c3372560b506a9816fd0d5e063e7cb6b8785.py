code = """import json

# Define the keys
nyse_arca_key = 'var_functions.query_db:0'
list_db_key = 'var_functions.list_db:2'

# Load the data from storage
with open(locals()[nyse_arca_key], 'r') as f:
    nyse_arca_etfs = json.load(f)

with open(locals()[list_db_key], 'r') as f:
    available_tickers = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'nyse_arca_etfs_count': len(nyse_arca_etfs),
    'available_tickers_count': len(available_tickers),
    'sample_etfs': nyse_arca_etfs[:5],
    'sample_tickers': available_tickers[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:12': {'file1': 'file_storage/functions.query_db:0.json', 'file2': 'file_storage/functions.list_db:2.json'}}

exec(code, env_args)

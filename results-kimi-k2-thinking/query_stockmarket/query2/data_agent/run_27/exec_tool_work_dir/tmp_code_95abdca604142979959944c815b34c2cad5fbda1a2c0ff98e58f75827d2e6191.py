code = """import json

# Get the list of NYSE Arca ETF symbols
nyse_arca_data = locals()['var_functions.query_db:0']
if isinstance(nyse_arca_data, str):
    with open(nyse_arca_data, 'r') as f:
        nyse_arca_data = json.load(f)

nyse_arca_etfs = [item['Symbol'] for item in nyse_arca_data]

# For debugging, let's start with a smaller subset first
# We'll process in chunks to avoid timeout
subset_etfs = nyse_arca_etfs[:50]  # Start with first 50 ETFs

print('__RESULT__:')
print(json.dumps(subset_etfs))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.list_db:11': 'file_storage/functions.list_db:11.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)

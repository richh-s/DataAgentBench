code = """import json
import os

# Get the file path from the query result
nasdaq_cap_file_path = locals()['var_functions.query_db:0']

# Read the file
if os.path.exists(nasdaq_cap_file_path):
    with open(nasdaq_cap_file_path, 'r') as f:
        nasdaq_cap_stocks = json.load(f)
    
    # Extract symbols
    nasdaq_cap_symbols = [stock['Symbol'] for stock in nasdaq_cap_stocks]
    
    print('__RESULT__:')
    print(json.dumps({
        'file_path': nasdaq_cap_file_path,
        'count': len(nasdaq_cap_symbols),
        'symbols_sample': nasdaq_cap_symbols[:20]
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'error': f'File not found: {nasdaq_cap_file_path}'
    }))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': 'file_storage/functions.list_db:4.json'}

exec(code, env_args)

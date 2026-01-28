code = """import json
import os

# Get the file path from the storage variable
file_path = var_functions.query_db_2

# Check if file exists and read it
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        nasdaq_capital_companies = json.load(f)
    
    print('__RESULT__:')
    print(json.dumps({
        'count': len(nasdaq_capital_companies),
        'first_five_symbols': [company['Symbol'] for company in nasdaq_capital_companies[:5]]
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'File not found'}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

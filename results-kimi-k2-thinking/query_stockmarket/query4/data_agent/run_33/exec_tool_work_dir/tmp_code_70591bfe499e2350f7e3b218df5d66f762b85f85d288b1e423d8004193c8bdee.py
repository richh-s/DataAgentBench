code = """import json
import pandas as pd

# Access the stored results
stockinfo_data = locals()['var_functions.query_db:0']

# If it's a file path, read it
if isinstance(stockinfo_data, str):
    with open(stockinfo_data, 'r') as f:
        stockinfo_data = json.load(f)

# Create a mapping of symbol to company description for NYSE stocks
nyse_companies = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
nyse_symbols = list(nyse_companies.keys())

print('__RESULT__:')
print(json.dumps({
    'status': 'ready',
    'symbol_count': len(nyse_symbols),
    'first_10_symbols': nyse_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'total_stocktrade_tables': 2753, 'available_for_analysis': 234, 'sample_stocks': ['SJT', 'LHC', 'GOL', 'RMT', 'NFH', 'NNI', 'HIO', 'OCFT', 'MLI', 'PNM']}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)

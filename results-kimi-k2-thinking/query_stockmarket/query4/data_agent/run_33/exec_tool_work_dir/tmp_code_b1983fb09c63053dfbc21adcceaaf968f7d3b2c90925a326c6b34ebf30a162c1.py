code = """import json

# Access the stored results
stockinfo_data = locals()['var_functions.query_db:0']
stocktrade_tables = locals()['var_functions.list_db:2']

# If they're strings (file paths), read them
if isinstance(stockinfo_data, str):
    with open(stockinfo_data, 'r') as f:
        stockinfo_data = json.load(f)
        
if isinstance(stocktrade_tables, str):
    with open(stocktrade_tables, 'r') as f:
        stocktrade_tables = json.load(f)

# Create a mapping of symbol to company description for NYSE stocks
nyse_companies = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# All NYSE symbols have tables in the stocktrade database
nyse_symbols = list(nyse_companies.keys())

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(nyse_symbols),
    'symbols': nyse_symbols,
    'companies': nyse_companies
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'total_stocktrade_tables': 2753, 'available_for_analysis': 234, 'sample_stocks': ['SJT', 'LHC', 'GOL', 'RMT', 'NFH', 'NNI', 'HIO', 'OCFT', 'MLI', 'PNM']}}

exec(code, env_args)

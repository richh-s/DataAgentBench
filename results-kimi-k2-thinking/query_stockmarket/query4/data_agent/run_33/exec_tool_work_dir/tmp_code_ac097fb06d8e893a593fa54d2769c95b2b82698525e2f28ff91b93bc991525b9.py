code = """import json

# Get the NYSE symbols and company names from stored data
stockinfo_data = locals()['var_functions.query_db:0']

if isinstance(stockinfo_data, str):
    with open(stockinfo_data, 'r') as f:
        stockinfo_data = json.load(f)

nyse_companies = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
nyse_symbols = list(nyse_companies.keys())

# Process first 20 symbols as a test batch
batch1 = nyse_symbols[:20]

print('__RESULT__:')
print(json.dumps({
    'batch_size': len(batch1),
    'symbols': batch1
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'total_stocktrade_tables': 2753, 'available_for_analysis': 234, 'sample_stocks': ['SJT', 'LHC', 'GOL', 'RMT', 'NFH', 'NNI', 'HIO', 'OCFT', 'MLI', 'PNM']}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'status': 'ready', 'symbol_count': 234, 'first_10_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

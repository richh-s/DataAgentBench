code = """import json

# Read the NYSE non-ETF stocks data
nyse_file = 'file_storage/functions.query_db:12.json'
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Get all available symbols from stocktrade database
stocktrade_symbols = locals()['var_functions.list_db:6']
if isinstance(stocktrade_symbols, str) and stocktrade_symbols.endswith('.json'):
    with open(stocktrade_symbols, 'r') as f:
        stocktrade_symbols = json.load(f)

# Find intersection
nyse_symbols = {stock['Symbol'] for stock in nyse_stocks}
available_symbols = set(stocktrade_symbols)
valid_symbols = nyse_symbols.intersection(available_symbols)

print('__RESULT__:')
print(json.dumps({
    'nyse_count': len(nyse_symbols),
    'available_count': len(available_symbols),
    'valid_count': len(valid_symbols),
    'first_valid': list(valid_symbols)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'error': "[Errno 2] No such file or directory: 'var_functions.list_db:6'", 'success': False}, 'var_functions.execute_python:20': {'count': 234, 'first_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_companies': ['Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)

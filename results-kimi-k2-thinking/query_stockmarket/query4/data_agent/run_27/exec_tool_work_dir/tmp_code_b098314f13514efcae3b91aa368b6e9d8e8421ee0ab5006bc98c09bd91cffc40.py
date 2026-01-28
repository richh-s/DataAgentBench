code = """import json

# Read both file paths
nyse_file = locals()['var_functions.query_db:12']
trade_file = locals()['var_functions.list_db:18']

with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

with open(trade_file, 'r') as f:
    all_symbols = json.load(f)

# Extract NYSE symbols
nyse_symbols = {stock['Symbol'] for stock in nyse_stocks}

# Find intersection with available trade data
available_nyse_symbols = nyse_symbols.intersection(all_symbols)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_stocks),
    'total_trade_symbols': len(all_symbols),
    'available_nyse_symbols': len(available_nyse_symbols),
    'sample_symbols': list(available_nyse_symbols)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'stock_count': 234, 'sample_stocks': [['AEFC', 'Aegon Funding'], ['AIN', 'Albany International'], ['AIV', 'Apartment Investment and Management'], ['AIZP', 'Assurant,'], ['AJRD', 'Aerojet Rocketdyne Holdings,'], ['AL', 'Air Lease'], ['AMN', 'AMN Healthcare Services'], ['AMP', 'Ameriprise Financial,'], ['AMT', 'American Tower'], ['ARD', 'Ardagh Group S.A.']]}, 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json'}

exec(code, env_args)

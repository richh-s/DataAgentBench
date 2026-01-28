code = """import json

# Get stored results
nyse_stocks_result = locals()['var_functions.query_db:0']
trade_tables_result = locals()['var_functions.list_db:12']

# Load data
if isinstance(nyse_stocks_result, str) and '.json' in nyse_stocks_result:
    with open(nyse_stocks_result, 'r') as f:
        nyse_stocks = json.load(f)
else:
    nyse_stocks = nyse_stocks_result

if isinstance(trade_tables_result, str) and '.json' in trade_tables_result:
    with open(trade_tables_result, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = trade_tables_result

# Create symbol to company mapping
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

# Initialize results tracking
stock_performance = []
tested_count = 0
no_data_count = 0

# Process first 20 symbols to test
first_20_symbols = list(symbol_to_company.keys())[:20]

print('__RESULT__:')
print(json.dumps({
    'message': 'Testing data access for first 20 symbols',
    'symbols': first_20_symbols
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['A', 'AA', 'AAL', 'AAN'], 'var_functions.execute_python:10': {'total_stocks': 234, 'sample': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.']]}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:16': {'nyse_stock_count': 234, 'available_in_trade_count': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.execute_python:18': {'test_symbols': ['AEFC', 'AIN', 'AIV']}, 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'High': '47.54999923706055', 'Low': '46.400001525878906', 'Close': '47.150001525878906', 'Adj Close': '45.33499526977539', 'Volume': '98300'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'High': '48.34999847412109', 'Low': '47.150001525878906', 'Close': '48.150001525878906', 'Adj Close': '46.2964973449707', 'Volume': '161000'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'High': '48.04999923706055', 'Low': '47.04999923706055', 'Close': '47.75', 'Adj Close': '45.91189193725586', 'Volume': '132300'}, {'Date': '2017-01-06', 'Open': '47.75', 'High': '47.79999923706055', 'Low': '46.5', 'Close': '46.59999847412109', 'Adj Close': '44.8061637878418', 'Volume': '107000'}, {'Date': '2017-01-09', 'Open': '46.5', 'High': '46.5', 'Low': '45.45000076293945', 'Close': '45.54999923706055', 'Adj Close': '43.79658126831055', 'Volume': '187100'}], 'var_functions.execute_python:24': {'total_symbols': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)

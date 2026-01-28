code = """import json

# Get stored results using locals()
nyse_stocks_result = locals()['var_functions.query_db:0']
trade_tables_result = locals()['var_functions.list_db:12']

# Load data from files if needed
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

# Check which symbols exist in trade database
nyse_symbols = list(symbol_to_company.keys())
available_symbols = [s for s in nyse_symbols if s in trade_tables]

# Print results
print('__RESULT__:')
print(json.dumps({
    'nyse_stock_count': len(nyse_symbols),
    'available_in_trade_count': len(available_symbols),
    'sample': available_symbols[:5]
 }))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['A', 'AA', 'AAL', 'AAN'], 'var_functions.execute_python:10': {'total_stocks': 234, 'sample': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.']]}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json'}

exec(code, env_args)

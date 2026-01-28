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

# Create mapping
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

# Test with first 3 symbols
test_symbols = list(symbol_to_company.keys())[:3]
print('__RESULT__:')
print(json.dumps({'test_symbols': test_symbols}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['A', 'AA', 'AAL', 'AAN'], 'var_functions.execute_python:10': {'total_stocks': 234, 'sample': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.']]}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:16': {'nyse_stock_count': 234, 'available_in_trade_count': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}}

exec(code, env_args)

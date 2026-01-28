code = """import json
import os

# Access the stored variables
nyse_stocks_result = var_functions.query_db:0
trade_tables_result = var_functions.list_db:12

# Load NYSE stocks data
if isinstance(nyse_stocks_result, str) and nyse_stocks_result.endswith('.json'):
    with open(nyse_stocks_result, 'r') as f:
        nyse_stocks = json.load(f)
else:
    nyse_stocks = nyse_stocks_result

# Get list of trading tables
if isinstance(trade_tables_result, str) and trade_tables_result.endswith('.json'):
    with open(trade_tables_result, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = trade_tables_result

# Create mapping of symbol to company description
symbol_to_company = {}
for stock in nyse_stocks:
    symbol = stock.get('Symbol')
    company = stock.get('Company Description', '')
    if symbol:
        symbol_to_company[symbol] = company

# Filter for NYSE stocks that exist in trade database
available_symbols = []
for symbol in symbol_to_company.keys():
    if symbol in trade_tables:
        available_symbols.append(symbol)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_stocks),
    'available_in_trade_db': len(available_symbols),
    'sample_symbols': available_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['A', 'AA', 'AAL', 'AAN'], 'var_functions.execute_python:10': {'total_stocks': 234, 'sample': [['AEFC', 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'], ['AIN', 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'], ['AIV', 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.']]}, 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json'}

exec(code, env_args)

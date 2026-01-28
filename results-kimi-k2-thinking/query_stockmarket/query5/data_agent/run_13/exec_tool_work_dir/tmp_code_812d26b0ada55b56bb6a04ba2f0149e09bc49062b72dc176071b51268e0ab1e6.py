code = """import json
import os

# Load the symbols from stockinfo_database
stockinfo_path = locals()['var_functions.query_db:0']
with open(stockinfo_path, 'r') as f:
    stock_records = json.load(f)

# Load the list of tables from stocktrade_database
stocktrade_path = locals()['var_functions.list_db:5']
with open(stocktrade_path, 'r') as f:
    trade_tables = json.load(f)

# Create mapping of symbol to company description
symbol_to_company = {record['Symbol']: record['Company Description'] for record in stock_records}

# Get all NASDAQ Capital Market symbols
capital_market_symbols = [record['Symbol'] for record in stock_records]

# Filter symbols that exist in stocktrade_database
available_symbols = [sym for sym in capital_market_symbols if sym in trade_tables]

print("__RESULT__:")
print(json.dumps({
    'total_nasdaq_capital_symbols': len(capital_market_symbols),
    'available_in_trade_db': len(available_symbols),
    'sample_symbols': available_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)

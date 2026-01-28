code = """import json
import os

# Load all the necessary data
stockinfo_path = locals()['var_functions.query_db:0']
stocktrade_paths = locals()['var_functions.list_db:5']

with open(stockinfo_path, 'r') as f:
    stock_records = json.load(f)

with open(stocktrade_paths, 'r') as f:
    trade_tables = json.load(f)

# Create mapping
symbol_to_company = {record['Symbol']: record['Company Description'] for record in stock_records}
nasdaq_capital_symbols = [record['Symbol'] for record in stock_records]

# Check which symbols exist in trade database
available_symbols = [sym for sym in nasdaq_capital_symbols if sym in trade_tables]

print("__RESULT__:")
print(json.dumps({
    'total_symbols_to_process': len(available_symbols),
    'first_20_symbols': available_symbols[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nasdaq_capital_symbols': 86, 'available_in_trade_db': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:10': {'symbol': 'AGMH', 'total_days': 252, 'high_vol_days': 13}}

exec(code, env_args)

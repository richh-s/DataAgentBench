code = """import json, os

# Access the stored results
symbols_file = locals()['var_functions.query_db:0']
trade_tables_file = locals()['var_functions.list_db:2']

# Load the data
with open(symbols_file, 'r') as f:
    symbols_data = json.load(f)

with open(trade_tables_file, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols and company names
symbol_info = {rec['Symbol']: rec['Company Description'] for rec in symbols_data}

# Find common symbols
common_symbols = [s for s in symbol_info.keys() if s in trade_tables]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_non_etf': len(symbol_info),
    'present_in_trade_db': len(common_symbols),
    'sample_symbols': common_symbols[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)

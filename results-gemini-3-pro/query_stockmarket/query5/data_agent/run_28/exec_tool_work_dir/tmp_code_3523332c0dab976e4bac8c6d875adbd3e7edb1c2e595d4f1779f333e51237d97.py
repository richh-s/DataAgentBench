code = """import json

# Get file paths from variables
stock_info_path = locals()['var_function-call-17865422632145074530']
trade_tables_path = locals()['var_function-call-14843570023963042041']

# Load symbols from stockinfo
with open(stock_info_path, 'r') as f:
    stock_info = json.load(f)

# Extract symbols
nasdaq_capital_symbols = {item['Symbol'] for item in stock_info}

# Load tables from stocktrade_database
with open(trade_tables_path, 'r') as f:
    trade_tables = set(json.load(f))

# Find intersection
valid_symbols = list(nasdaq_capital_symbols.intersection(trade_tables))

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols[:50]}))"""

env_args = {'var_function-call-17865422632145074530': 'file_storage/function-call-17865422632145074530.json', 'var_function-call-14843570023963042041': 'file_storage/function-call-14843570023963042041.json'}

exec(code, env_args)

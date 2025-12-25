code = """import json

# Load symbols from stockinfo
with open('var_function-call-17865422632145074530.json', 'r') as f:
    stock_info = json.load(f)

# Extract symbols
nasdaq_capital_symbols = {item['Symbol'] for item in stock_info}

# Load tables from stocktrade_database
with open('var_function-call-14843570023963042041.json', 'r') as f:
    trade_tables = set(json.load(f))

# Find intersection
valid_symbols = list(nasdaq_capital_symbols.intersection(trade_tables))

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols[:50]})) # Preview 50 symbols"""

env_args = {'var_function-call-17865422632145074530': 'file_storage/function-call-17865422632145074530.json', 'var_function-call-14843570023963042041': 'file_storage/function-call-14843570023963042041.json'}

exec(code, env_args)

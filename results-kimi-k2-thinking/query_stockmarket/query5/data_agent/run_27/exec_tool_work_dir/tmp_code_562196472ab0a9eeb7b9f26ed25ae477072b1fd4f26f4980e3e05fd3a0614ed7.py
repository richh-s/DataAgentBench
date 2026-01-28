code = """import json

# Read the full NASDAQ Capital Market stocks from the file
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

print("Total NASDAQ Capital Market stocks:", len(nasdaq_capital_stocks))
symbols = [stock['Symbol'] for stock in nasdaq_capital_stocks]
print("First 20 symbols:", symbols[:20])

# Also read the list of all tickers from stocktrade_database
result_file2 = var_functions.list_db:8
with open(result_file2, 'r') as f:
    all_trade_stocks = json.load(f)

print("Total stocks in trade database:", len(all_trade_stocks))
print("First 20 trade stocks:", all_trade_stocks[:20])

# Find intersection
nasdaq_cap_symbols = set(symbols)
trade_symbols = set(all_trade_stocks)
common_symbols = nasdaq_cap_symbols.intersection(trade_symbols)
print("NASDAQ Capital stocks with trade data:", len(common_symbols))
print("Sample:", list(common_symbols)[:10])
print("__RESULT__:")
print(json.dumps(list(common_symbols)[:50]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.list_db:7': ['stockinfo'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)

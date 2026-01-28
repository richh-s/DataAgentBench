code = """import json

# Get NASDAQ Capital Market tickers from stockinfo_database
stockinfo_file = locals()['var_functions.query_db:4']
with open(stockinfo_file.replace('"', ''), 'r') as f:
    nasdaq_cap_stocks = json.load(f)

# Get all available ticker tables from stocktrade_database
trade_tables_file = locals()['var_functions.list_db:8']
with open(trade_tables_file.replace('"', ''), 'r') as f:
    all_trade_tables = json.load(f)

# Extract ticker symbols from NASDAQ Capital Market stocks
nasdaq_cap_tickers = [stock['Symbol'] for stock in nasdaq_cap_stocks]

print(f"NASDAQ Capital Market tickers: {len(nasdaq_cap_tickers)}")
print(f"Available trade tables: {len(all_trade_tables)}")

# Find intersection
available_nasdaq_cap = list(set(nasdaq_cap_tickers) & set(all_trade_tables))
print(f"Available NASDAQ Capital Market stocks with trade data: {len(available_nasdaq_cap)}")
print("Sample:", available_nasdaq_cap[:10])"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)

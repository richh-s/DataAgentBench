code = """import json

# Read NYSE stocks
with open('var_query_db', 'r') as f:
    nyse_stocks = json.load(f)

# Read available tables (tickers)
with open('var_list_db', 'r') as f:
    available_tickers = json.load(f)

print(f"NYSE non-ETF stocks: {len(nyse_stocks)}")
print(f"Available tickers in stocktrade_database: {len(available_tickers)}")

# Find intersection
nyse_symbols = {stock['Symbol'] for stock in nyse_stocks}
available_set = set(available_tickers)
common_stocks = nyse_symbols.intersection(available_set)

print(f"Common stocks (NYSE stocks with price data): {len(common_stocks)}")

# Show first 10 common stocks
print("\nFirst 10 common stocks:")
for i, symbol in enumerate(list(common_stocks)[:10]):
    desc = next(stock['Company Description'] for stock in nyse_stocks if stock['Symbol'] == symbol)
    print(f"  {i+1}. {symbol}: {desc[:60]}...")

# Store results for next steps
print("\n---BEGIN JSON OUTPUT---")
print(json.dumps({
    'nyse_count': len(nyse_stocks),
    'available_count': len(available_tickers),
    'common_count': len(common_stocks),
    'common_stocks': list(common_stocks)[:50]  # Just a sample for now
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)

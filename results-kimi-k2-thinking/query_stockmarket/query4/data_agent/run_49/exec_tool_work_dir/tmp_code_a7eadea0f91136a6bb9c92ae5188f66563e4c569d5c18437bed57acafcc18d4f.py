code = """import json

# Read the list of NYSE non-ETF stocks from the previous query
with open('var_functions.query_db:0', 'r') as f:
    nyse_stocks = json.load(f)

print(f"Total NYSE non-ETF stocks found: {len(nyse_stocks)}")

# Print first few to verify
print("First 5 stocks:")
for stock in nyse_stocks[:5]:
    print(f"  {stock['Symbol']}: {stock['Company Description']}")

# Convert to dictionary for easy lookup
stock_info_dict = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
print(f"\nCreated lookup dictionary with {len(stock_info_dict)} entries")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

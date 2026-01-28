code = """import json, os

# Read the ETF symbols from the stored result file
result_file = locals()['var_functions.query_db:0']
with open(result_file, 'r') as f:
    etf_symbols = json.load(f)

# Extract just the symbols as a list
symbols = [item['Symbol'] for item in etf_symbols]
print(f"Found {len(symbols)} NYSE Arca ETFs")
print("Sample symbols:", symbols[:10])

# Now we need to check each symbol's price data in 2015
# For each table (symbol), we need to check if Adjusted Close > 200 at any point in 2015
# This requires querying the stocktrade_database for each symbol"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

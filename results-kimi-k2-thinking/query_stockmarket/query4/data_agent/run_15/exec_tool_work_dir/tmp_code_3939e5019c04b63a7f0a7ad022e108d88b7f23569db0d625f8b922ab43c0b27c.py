code = """import json

# Load the query result from the first database
result_file = locals()['var_functions.query_db:0']
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

print(f"Number of NYSE non-ETF stocks: {len(nyse_stocks)}")
print("First 5 stocks:")
for stock in nyse_stocks[:5]:
    print(f"  {stock['Symbol']}: {stock['Company Description']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

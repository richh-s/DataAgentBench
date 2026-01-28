code = """import json

# Access the result using locals() to handle the colon in the variable name
result_file = locals()['var_functions.query_db:8']

# Read the NYSE non-ETF stocks from the query result
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]
print("Total NYSE non-ETF symbols:", len(nyse_symbols))
print("First 10 symbols:", nyse_symbols[:10])"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['stockinfo'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

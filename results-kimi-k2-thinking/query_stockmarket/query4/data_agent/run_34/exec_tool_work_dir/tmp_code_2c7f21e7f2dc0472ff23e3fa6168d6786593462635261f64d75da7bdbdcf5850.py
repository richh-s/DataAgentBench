code = """import json
import os

# Read the NYSE non-ETF stocks from the query result
result_file = var_functions.query_db:8
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]
print(f"Total NYSE non-ETF symbols: {len(nyse_symbols)}")
print(f"First 10 symbols: {nyse_symbols[:10]}")"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['stockinfo'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

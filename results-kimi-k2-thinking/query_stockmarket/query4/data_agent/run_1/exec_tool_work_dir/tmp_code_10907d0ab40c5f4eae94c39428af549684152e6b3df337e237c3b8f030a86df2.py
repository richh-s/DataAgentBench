code = """import json
import pandas as pd

# Access the result from storage
nyse_non_etf_stocks = locals()['var_functions.query_db:0']
    
print(f"Number of NYSE non-ETF stocks: {len(nyse_non_etf_stocks)}")
print("First few examples:")
for i, stock in enumerate(nyse_non_etf_stocks[:5]):
    print(f"{i+1}. {stock['Symbol']}: {stock['Company Description']}")
print("Ready to proceed to check trading data for 2017.")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

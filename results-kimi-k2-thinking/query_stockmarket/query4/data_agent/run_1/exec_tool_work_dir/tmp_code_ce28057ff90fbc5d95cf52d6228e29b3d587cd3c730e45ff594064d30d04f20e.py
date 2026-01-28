code = """import json
import os

# The variable contains the file path to the JSON file
file_path = var_functions.query_db:0
print(f"File path: {file_path}")
print(f"File exists: {os.path.exists(file_path)}")

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        nyse_non_etf_stocks = json.load(f)
    
    print(f"Number of NYSE non-ETF stocks: {len(nyse_non_etf_stocks)}")
    print("First few examples:")
    for i, stock in enumerate(nyse_non_etf_stocks[:5]):
        print(f"{i+1}. {stock['Symbol']}: {stock['Company Description']}")
else:
    print("File not found")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

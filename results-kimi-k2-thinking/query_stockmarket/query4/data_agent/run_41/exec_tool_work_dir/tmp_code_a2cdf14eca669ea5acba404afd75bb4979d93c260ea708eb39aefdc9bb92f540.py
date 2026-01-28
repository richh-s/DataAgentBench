code = """import json

# Read the file path from the variable
file_path = var_functions.query_db:0

print("File path:", file_path)

# Read the full data from the file
with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

print(f"Number of NYSE non-ETF stocks: {len(nyse_stocks)}")
print("First few stocks:", nyse_stocks[:5])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)

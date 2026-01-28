code = """import json
import pandas as pd

# Read the NYSE non-ETF stocks from the file
with open('/tmp/tmp_result_3b40c1cb.json', 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols
symbols = [stock['Symbol'] for stock in nyse_stocks]
print(f"Total NYSE non-ETF stocks: {len(symbols)}")
print("First 10 symbols:", symbols[:10])

# Store the symbols list
result = {"symbols": symbols, "count": len(symbols)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)

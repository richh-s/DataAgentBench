code = """import json

# Read the NYSE non-ETF stocks data
with open('/var_functions.query_db:10.json', 'r') as f:
    nyse_stocks = json.load(f)

print("Number of NYSE non-ETF stocks:", len(nyse_stocks))
print("Sample stocks:", nyse_stocks[:5])

# Store the symbols in a list
symbols = [stock['Symbol'] for stock in nyse_stocks]
print("\nTotal symbols:", len(symbols))

# Check unique symbols (case-sensitive)
unique_symbols = list(set(symbols))
print("Unique symbols:", len(unique_symbols))

# Output the result
result = json.dumps({'total_stocks': len(nyse_stocks), 'sample_stocks': nyse_stocks[:5], 'symbols': symbols[:20]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'Listing Exchange': 'A', 'count': '28'}, {'Listing Exchange': 'N', 'count': '234'}, {'Listing Exchange': 'P', 'count': '1444'}, {'Listing Exchange': 'Q', 'count': '710'}, {'Listing Exchange': 'Z', 'count': '336'}], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

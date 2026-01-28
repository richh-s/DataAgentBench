code = """import json

# First, let's load our data properly
# Get the file path for NYSE Arca ETFs
nyse_arca_file = var_functions.query_db_26
print(f"NYSE Arca ETFs file: {nyse_arca_file}")

# Read the file
with open(nyse_arca_file, 'r') as f:
    nyse_arca_etfs = json.load(f)

# Extract symbols
nyse_arca_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]
print(f"Total NYSE Arca ETFs: {len(nyse_arca_symbols)}")
print(f"First 10: {nyse_arca_symbols[:10]}")

# Now get available tickers from stocktrade database
available_tickers_file = var_functions.list_db_1
print(f"Available tickers file: {available_tickers_file}")

with open(available_tickers_file, 'r') as f:
    available_tickers = json.load(f)

print(f"Total available tickers: {len(available_tickers)}")
print(f"First 10: {available_tickers[:10]}")

# Find intersection
common_symbols = set(nyse_arca_symbols).intersection(set(available_tickers))
common_list = sorted(list(common_symbols))

print(f"NYSE Arca ETFs with price data: {len(common_list)}")
print(f"First 10: {common_list[:10]}")

# Store results for next step
result = {
    'common_etfs': common_list,
    'count': len(common_list)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.list_db:1': 'file_storage/functions.list_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'check_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'max_price': '125.2300033569336'}], 'var_functions.query_db:30': [{'max_price': '121.58584594726562'}], 'var_functions.query_db:32': [{'max_price': '27.289674758911133'}]}

exec(code, env_args)

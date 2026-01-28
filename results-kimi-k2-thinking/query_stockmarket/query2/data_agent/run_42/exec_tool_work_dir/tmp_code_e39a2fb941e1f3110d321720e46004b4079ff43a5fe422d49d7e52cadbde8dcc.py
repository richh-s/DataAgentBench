code = """# Access the stored results
nyse_arca_etfs = var_functions.query_db_4  # This should be the list of NYSE Arca ETFs
available_tickers = var_functions.list_db_1  # This should be the list of all ticker tables

# Debug: Check what type and length these are
print(f"nyse_arca_etfs type: {type(nyse_arca_etfs)}")
print(f"available_tickers type: {type(available_tickers)}")

# If the data was in file paths, read them
import json
import pandas as pd

# Handle nyse_arca_etfs
if isinstance(nyse_arca_etfs, str) and nyse_arca_etfs.endswith('.json'):
    with open(nyse_arca_etfs, 'r') as f:
        nyse_arca_etfs = json.load(f)

# Handle available_tickers  
if isinstance(available_tickers, str) and available_tickers.endswith('.json'):
    with open(available_tickers, 'r') as f:
        available_tickers = json.load(f)

print(f"Loaded {len(nyse_arca_etfs)} NYSE Arca ETFs")
print(f"Found {len(available_tickers)} total tickers in stocktrade database")
print(f"First few NYSE Arca ETFs: {[etf['Symbol'] for etf in nyse_arca_etfs[:5]]}")
print(f"First few available tickers: {available_tickers[:5]}")

# Convert to sets for easier comparison
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}
available_symbols = set(available_tickers)

# Find ETFs that exist in both databases
common_etfs = nyse_arca_symbols.intersection(available_symbols)
print(f"Found {len(common_etfs)} NYSE Arca ETFs with price data available")

# Store the common ETFs list for next step
result = {
    'common_etfs': sorted(list(common_etfs)),
    'total_common': len(common_etfs)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.list_db:1': 'file_storage/functions.list_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

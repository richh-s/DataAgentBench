code = """# Access the stored results with correct keys
import json

# NYSE Arca ETFs from query
nyse_arca_etfs = var_functions.query_db_4
# Available tickers from stocktrade database
available_tickers = var_functions.list_db_1

print(f"Type of nyse_arca_etfs: {type(nyse_arca_etfs)}")
print(f"Type of available_tickers: {type(available_tickers)}")

# If results are file paths, read them
if isinstance(nyse_arca_etfs, str) and '.json' in nyse_arca_etfs:
    with open(nyse_arca_etfs, 'r') as f:
        nyse_arca_etfs = json.load(f)
        
if isinstance(available_tickers, str) and '.json' in available_tickers:
    with open(available_tickers, 'r') as f:
        available_tickers = json.load(f)

# Extract symbols
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}
available_symbols = set(available_tickers)

common_etfs = nyse_arca_symbols.intersection(available_symbols)

print('__RESULT__:')
print(json.dumps({
    'common_etfs': sorted(list(common_etfs)),
    'count': len(common_etfs)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.list_db:1': 'file_storage/functions.list_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)

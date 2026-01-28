code = """import json

# Access the stored results using the correct keys
nyse_arca_result = var_functions.query_db_4
tickers_result = var_functions.list_db_1

print(f"NYSE Arca result type: {type(nyse_arca_result)}")
print(f"Tickers result type: {type(tickers_result)}")

# If results are file paths, read them
if isinstance(nyse_arca_result, str) and '.json' in nyse_arca_result:
    with open(nyse_arca_result, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = nyse_arca_result

if isinstance(tickers_result, str) and '.json' in tickers_result:
    with open(tickers_result, 'r') as f:
        available_tickers = json.load(f)
else:
    available_tickers = tickers_result

print(f"Loaded {len(nyse_arca_etfs)} NYSE Arca ETFs")
print(f"Found {len(available_tickers)} total tickers")

# Extract symbols and find intersection
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}
available_symbols = set(available_tickers)

common_etfs = nyse_arca_symbols.intersection(available_symbols)
common_list = sorted(list(common_etfs))

print(f"Found {len(common_list)} NYSE Arca ETFs with price data available")

print('__RESULT__:')
print(json.dumps({
    'common_etfs': common_list,
    'count': len(common_list)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.list_db:1': 'file_storage/functions.list_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'check_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

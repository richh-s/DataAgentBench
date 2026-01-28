code = """import json

# Get the results from storage using the provided keys
etf_result = locals()['var_functions.query_db:0']
tables_result = locals()['var_functions.list_db:2']

# Parse the results if they are file paths or already JSON
if isinstance(etf_result, str) and etf_result.endswith('.json'):
    with open(etf_result, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = etf_result

if isinstance(tables_result, str) and tables_result.endswith('.json'):
    with open(tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = tables_result

# Extract ticker symbols from the ETF list
etf_symbols = [etf['Symbol'] for etf in nyse_arca_etfs]

# Find which ETFs have price data tables
available_etfs = [symbol for symbol in etf_symbols if symbol in all_tables]

print("__RESULT__:")
print(json.dumps({
    "total_nyse_arca_etfs": len(etf_symbols),
    "available_in_stocktrade": len(available_etfs),
    "sample_available": available_etfs[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)

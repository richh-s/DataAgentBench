code = """import json
import pandas as pd

# Read the list of NYSE Arca ETFs
with open(var_functions.query_db:0, 'r') as f:
    nyse_arca_etfs = json.load(f)

# Read the list of all tables in stocktrade database
with open(var_functions.list_db:2, 'r') as f:
    all_tables = json.load(f)

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

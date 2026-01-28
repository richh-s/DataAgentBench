code = """# Read the list of NYSE Arca ETF symbols
import json

# Get the file path from storage
symbols_file = locals()['var_functions.execute_python:5']
print(f"Reading symbols from: {symbols_file}")

with open(symbols_file, 'r') as f:
    all_symbols = json.load(f)

print(f"Total symbols available in stocktrade_database: {len(all_symbols)}")
print(f"Sample: {all_symbols[:10]}")

# These are all the symbols in the DuckDB database. We need to filter for NYSE Arca ETFs.
# Let's get only the NYSE Arca ETF symbols
nysearca_etf_file = locals()['var_functions.query_db:2']
print(f"Reading NYSE Arca ETFs from: {nysearca_etf_file}")

with open(nysearca_etf_file, 'r') as f:
    nysearca_etfs = json.load(f)

nysearca_symbols = [etf['Symbol'] for etf in nysearca_etfs]
print(f"Total NYSE Arca ETFs: {len(nysearca_symbols)}")
print(f"Sample: {nysearca_symbols[:10]}")

# Find intersection with available symbols in DuckDB
available_nysearca_etfs = [sym for sym in nysearca_symbols if sym in all_symbols]
print(f"Available NYSE Arca ETFs in DuckDB: {len(available_nysearca_etfs)}")
print(f"Sample: {available_nysearca_etfs[:10]}")

# Save this list for the next step
result = json.dumps(available_nysearca_etfs)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)

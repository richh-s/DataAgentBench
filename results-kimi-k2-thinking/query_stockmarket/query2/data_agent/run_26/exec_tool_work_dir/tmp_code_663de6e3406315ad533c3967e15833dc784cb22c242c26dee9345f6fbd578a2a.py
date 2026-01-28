code = """import json

# Load NYSE Arca ETFs (from the query result stored in var_functions.query_db:16)
nyse_arca_etfs = var_functions.query_db_16

# Extract just the symbols
nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}

print(f"Total NYSE Arca ETFs found: {len(nyse_arca_symbols)}")
print(f"Sample symbols: {list(nyse_arca_symbols)[:10]}")

# Load available tables from stocktrade_database (from var_functions.list_db:18)
trade_tables = var_functions.list_db_18

# Find intersection
common_symbols = nyse_arca_symbols.intersection(trade_tables)

print(f"\nNYSE Arca ETFs with price data: {len(common_symbols)}")
print(f"Sample common symbols: {list(common_symbols)[:10]}")

# Save common symbols for next step
print("__RESULT__:")
print(json.dumps({"common_symbols": sorted(list(common_symbols))}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': {'status': 'checked'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}], 'var_functions.query_db:24': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}]}

exec(code, env_args)

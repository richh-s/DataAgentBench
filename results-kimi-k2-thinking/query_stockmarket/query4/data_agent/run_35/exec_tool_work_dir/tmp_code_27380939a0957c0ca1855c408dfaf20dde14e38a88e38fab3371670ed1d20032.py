code = """import json
import os

# Load the stockinfo results - this should be a file path
stockinfo_path = locals().get('var_functions.query_db:0', '')
if stockinfo_path and os.path.exists(stockinfo_path):
    with open(stockinfo_path, 'r') as f:
        stockinfo_data = json.load(f)
else:
    # If it's not a path but the actual data
    stockinfo_data = locals().get('var_functions.query_db:0', [])

# Load the list of tables from stocktrade database
tables_path = locals().get('var_functions.list_db:2', '')
if tables_path and os.path.exists(tables_path):
    with open(tables_path, 'r') as f:
        tables_data = json.load(f)
else:
    tables_data = locals().get('var_functions.list_db:2', [])

print(f"Stockinfo records: {len(stockinfo_data) if isinstance(stockinfo_data, list) else 'Not a list'}")
print(f"Tables in stocktrade: {len(tables_data) if isinstance(tables_data, list) else 'Not a list'}")

# Show sample data
if isinstance(stockinfo_data, list) and stockinfo_data:
    print(f"Sample stockinfo: {stockinfo_data[0]}")
    
if isinstance(tables_data, list) and tables_data:
    print(f"Sample tables: {tables_data[:5]}")

# Count NYSE non-ETF stocks
nyse_stocks = stockinfo_data if isinstance(stockinfo_data, list) else []
print(f"NYSE non-ETF stocks: {len(nyse_stocks)}")

# Show a few symbols
if nyse_stocks:
    symbols = [stock['Symbol'] for stock in nyse_stocks[:10]]
    print(f"Sample symbols: {symbols}")

# Check how many of these have tables
if isinstance(tables_data, list):
    symbols_set = set([stock['Symbol'] for stock in nyse_stocks])
    existing_tables = [sym for sym in symbols_set if sym in tables_data]
    print(f"Stocks with trade data: {len(existing_tables)}")
    print(f"Sample existing: {existing_tables[:5]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)

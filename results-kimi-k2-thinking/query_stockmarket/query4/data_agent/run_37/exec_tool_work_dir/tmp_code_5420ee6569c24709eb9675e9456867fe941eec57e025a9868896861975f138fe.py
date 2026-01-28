code = """# Access the variables correctly using locals()
import json

# Get file paths from storage
stockinfo_file = locals()['var_functions.query_db:2']
trade_tables_file = locals()['var_functions.list_db:5']

print(f"Stockinfo file path: {stockinfo_file}")
print(f"Trade tables file path: {trade_tables_file}")

# Load and analyze the data
with open(stockinfo_file, 'r') as f:
    stockinfo_data = json.load(f)

with open(trade_tables_file, 'r') as f:
    trade_tables = json.load(f)

print(f"Total NYSE non-ETF stocks in stockinfo: {len(stockinfo_data)}")
print(f"First stock: {stockinfo_data[0]}")

# Extract symbols
symbols = [stock['Symbol'] for stock in stockinfo_data]
print(f"First 5 symbols: {symbols[:5]}")

# Find available tables
available_symbols = list(set(symbols) & set(trade_tables))
print(f"Total available symbols with trade data: {len(available_symbols)}")
print(f"First 10 available: {available_symbols[:10]}")

result = {
    'stockinfo_count': len(stockinfo_data),
    'trade_tables_count': len(trade_tables),
    'available_symbols_count': len(available_symbols),
    'sample_available': available_symbols[:20]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Load the stockinfo query result from the file path
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    stockinfo_data = json.load(f)

# Create DataFrame from the stockinfo data
df_stockinfo = pd.DataFrame(stockinfo_data)
print(f"Total NYSE non-ETF stocks found: {len(df_stockinfo)}")
print(f"First few symbols: {df_stockinfo['Symbol'].head().tolist()}")

# Get list of symbols from stockinfo
symbols = df_stockinfo['Symbol'].tolist()

# Load the stocktrade database tables list from the file path
with open(var_functions.list_db:5, 'r') as f:
    trade_tables = json.load(f)

print(f"Total tables in stocktrade_database: {len(trade_tables)}")
print(f"First few tables: {trade_tables[:5]}")

# Find intersection - NYSE stocks that have trade data
available_symbols = list(set(symbols) & set(trade_tables))
print(f"Number of NYSE non-ETF stocks with available trade data: {len(available_symbols)}")
print(f"Sample available symbols: {available_symbols[:10]}")

# Count how many of these we need to process
result_summary = {
    'total_nyse_stocks': len(df_stockinfo),
    'available_symbols_count': len(available_symbols),
    'first_20_symbols': available_symbols[:20]
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Load the stockinfo query result
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    stockinfo_data = json.load(f)

# Create DataFrame
df_stockinfo = pd.DataFrame(stockinfo_data)
print(f"Total NYSE non-ETF stocks found: {len(df_stockinfo)}")
print(f"First few rows: {df_stockinfo.head()}")

# Get list of symbols
symbols = df_stockinfo['Symbol'].tolist()
print(f"First 10 symbols: {symbols[:10]}")

# Load the stocktrade database tables list
trade_tables_file = var_functions.list_db:5
with open(trade_tables_file, 'r') as f:
    trade_tables = json.load(f)

print(f"Total tables in stocktrade_database: {len(trade_tables)}")
print(f"First 10 tables: {trade_tables[:10]}")

# Find intersection of symbols and available tables
available_symbols = list(set(symbols) & set(trade_tables))
print(f"Number of NYSE non-ETF stocks with trade data: {len(available_symbols)}")
print(f"First 10 available symbols: {available_symbols[:10]}")

# Prepare the data for next steps
result = {
    'total_nyse_stocks': len(df_stockinfo),
    'available_symbols': available_symbols,
    'stockinfo_df': df_stockinfo.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)

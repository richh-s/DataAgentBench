code = """import json
import pandas as pd

# Load the full result from the file
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)
print(f"Data shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Unique indices: {df['Index'].nunique()}")
print(f"Date range: from {df['Date'].min()} to {df['Date'].max()}")
print(f"Unique indices: {df['Index'].unique()}")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])
print('\nData types after conversion:')
print(df.dtypes)

# Preview the data
print('\nFirst 5 rows:')
print(df.head())

print('__RESULT__:')
print('Successfully loaded and processed data')"""

env_args = {'var_functions.list_db:0': ['index_trade'], 'var_functions.list_db:2': ['index_info'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

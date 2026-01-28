code = """import json
import pandas as pd
from datetime import datetime

# Load the big data file which contains all index price data
file_path = var_functions.query_db:8  # This is a string path to the JSON file

# Read the full data
with open(file_path, 'r') as f:
    all_trades = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(all_trades)
print(f"Total records loaded: {len(df)}")

# Show unique indices
indices = df['Index'].unique()
print(f"Unique indices: {indices}")

# Convert Date and CloseUSD to proper types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_datetime(df['CloseUSD'])

print("\nDate range:", df['Date'].min(), "to", df['Date'].max())
print("\nSample data:")
print(df.head())

print('__RESULT__:')
print('Data loaded successfully')"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

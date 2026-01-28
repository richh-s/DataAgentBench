code = """import json
import pandas as pd
from datetime import datetime

# Get the data file path
data_file = var_functions.query_db:8

# Read the full data
with open(data_file, 'r') as f:
    all_trades = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(all_trades)
print('Total records: ' + str(len(df)))

# Show unique indices
unique_indices = df['Index'].unique()
print('Unique indices: ' + str(unique_indices))

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

print('Date range: ' + str(df['Date'].min()) + ' to ' + str(df['Date'].max()))
print('Sample:')
print(df.head())

result = 'Data loaded successfully'
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

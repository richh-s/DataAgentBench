code = """import json
import pandas as pd
import numpy as np

# Get the file path from storage
file_path = locals()['var_functions.query_db:8']

# Read the data
with open(file_path, 'r') as f:
    all_trades = json.load(f)

# Create DataFrame
df = pd.DataFrame(all_trades)

# Convert data types with explicit format
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter data from 2000 onwards
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

output = {
    'total_records': len(df_2000),
    'unique_indices': sorted(df_2000['Index'].unique().tolist()),
    'date_min': str(df_2000['Date'].min()),
    'date_max': str(df_2000['Date'].max())
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

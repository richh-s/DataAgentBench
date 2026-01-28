code = """import json
import os

# Check the type and access the data
file_path = var_functions.query_db:10

# Check if it's a file path string or direct data
if isinstance(file_path, str) and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    # It's direct data
    data = file_path

import pandas as pd

# Create DataFrame
df = pd.DataFrame(data)

# Convert Open and Close to numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Determine up days (Close > Open) and down days (Close < Open)
df['is_up_day'] = df['Close'] > df['Open']
df['is_down_day'] = df['Close'] < df['Open']

# Group by index and count up/down days for 2018
summary = df.groupby('Index').agg({
    'is_up_day': 'sum',
    'is_down_day': 'sum',
    'Date': 'count'
}).reset_index()

summary.columns = ['Index', 'Up_Days', 'Down_Days', 'Total_Days']

# Find indices with more up days than down days
positive_indices = summary[summary['Up_Days'] > summary['Down_Days']]

# Create result with properly formatted JSON
result = {
    'analysis': summary.to_dict('records'),
    'indices_with_more_up_days': positive_indices['Index'].tolist()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'GSPTSE'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

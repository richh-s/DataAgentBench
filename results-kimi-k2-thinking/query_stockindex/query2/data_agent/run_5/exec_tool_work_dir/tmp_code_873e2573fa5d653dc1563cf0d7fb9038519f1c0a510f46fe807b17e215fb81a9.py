code = """import json
import pandas as pd

# Load the trade data for North American indices
trade_data_file = locals()['var_functions.query_db:14']

with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Open and Close to numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Determine up/down days
df['is_up_day'] = df['Close'] > df['Open']
df['is_down_day'] = df['Close'] < df['Open']

# Count up and down days for each index in 2018
up_down_counts = df.groupby('Index').agg({
    'is_up_day': 'sum',
    'is_down_day': 'sum'
}).reset_index()

# Add total days for reference
up_down_counts['total_days'] = up_down_counts['is_up_day'] + up_down_counts['is_down_day']

# Filter indices with more up days than down days
up_more_than_down = up_down_counts[up_down_counts['is_up_day'] > up_down_counts['is_down_day']]

print('__RESULT__:')
print(up_more_than_down.to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'trade_columns': ['Index', 'Date', 'Open', 'Close'], 'trade_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII'], 'north_american_exchanges': ['New York Stock Exchange', 'NASDAQ', 'Toronto Stock Exchange']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

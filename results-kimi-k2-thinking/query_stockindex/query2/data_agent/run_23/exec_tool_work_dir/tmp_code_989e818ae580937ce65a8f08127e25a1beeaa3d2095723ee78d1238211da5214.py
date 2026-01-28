code = """import json
import pandas as pd

# Load all available indices and their 2018 data
file_path = var_functions.query_db:6
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame and filter for 2018
df = pd.DataFrame(trade_data)
df['Date'] = pd.to_datetime(df['Date'])
df_2018 = df[(df['Date'] >= '2018-01-01') & (df['Date'] <= '2018-12-31')].copy()

# Convert numeric columns
df_2018['Open'] = pd.to_numeric(df_2018['Open'])
df_2018['Close'] = pd.to_numeric(df_2018['Close'])

# Get unique indices
all_indices = df_2018['Index'].unique()

# Define North American indices based on common symbols
na_indices_list = [
    'DJI', 'DJX', 'DIA', 'SPX', 'GSPC', 'SPY', 'IXIC', 'COMP', 
    'GSPTSE', 'RUT', 'NYA', 'XAX', 'VIX'
]

# Also check for indices containing these patterns
na_patterns = ['^DJ', '^GS', '^IX', 'TSX', 'RUT', 'NYSE', 'NASDAQ', 'S&P']

na_indices = []
for idx in all_indices:
    # Check if it's in the direct list
    in_direct_list = idx in na_indices_list
    
    # Check if it contains NA patterns
    has_pattern = False
    for pattern in na_patterns:
        if pattern in idx.upper():
            has_pattern = True
            break
    
    # Check for exchange suffixes that indicate North America
    has_na_suffix = any(suffix in idx for suffix in ['.TO', '.VT', '.CN'])
    
    if in_direct_list or has_pattern or has_na_suffix:
        na_indices.append(idx)

# Process each NA index and count up/down days
results = []

for index in na_indices:
    index_data = df_2018[df_2018['Index'] == index]
    if len(index_data) > 0:
        up_days = int((index_data['Close'] > index_data['Open']).sum())
        down_days = int((index_data['Close'] < index_data['Open']).sum())
        flat_days = int((index_data['Close'] == index_data['Open']).sum())
        
        results.append({
            'index_symbol': index,
            'up_days': up_days,
            'down_days': down_days,
            'flat_days': flat_days,
            'total_days': len(index_data),
            'more_up_than_down': up_days > down_days
        })

# Print results
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}]}

exec(code, env_args)

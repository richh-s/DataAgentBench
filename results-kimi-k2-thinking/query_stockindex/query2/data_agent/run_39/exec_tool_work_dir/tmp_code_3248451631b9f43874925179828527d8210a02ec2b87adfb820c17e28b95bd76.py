code = """import json
import pandas as pd

# Get the file path from storage
file_path = locals()['var_functions.query_db:10']

# Read the data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert string numbers to float
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Determine up/down days (Close > Open for up day)
df['is_up_day'] = df['Close'] > df['Open']
df['is_down_day'] = df['Close'] < df['Open']

# Count by index
results = []
for index in df['Index'].unique():
    index_data = df[df['Index'] == index]
    up_days = index_data['is_up_day'].sum()
    down_days = index_data['is_down_day'].sum()
    
    results.append({
        'Index': index,
        'Up_days': int(up_days),
        'Down_days': int(down_days),
        'More_up_than_down': bool(up_days > down_days)
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.execute_python:8': {'north_american_exchanges': ['New York Stock Exchange', 'NASDAQ', 'Toronto Stock Exchange'], 'exchange_to_indices': {'New York Stock Exchange': ['NYA'], 'NASDAQ': ['IXIC'], 'Toronto Stock Exchange': ['GSPTSE']}}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

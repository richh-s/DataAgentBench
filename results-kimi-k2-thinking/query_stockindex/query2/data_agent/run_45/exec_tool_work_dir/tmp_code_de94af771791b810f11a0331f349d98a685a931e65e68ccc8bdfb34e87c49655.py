code = """import json
import pandas as pd
from collections import defaultdict

# Get the file path from previous query
result_file = locals()['var_functions.query_db:24']

# Read and parse the JSON data
with open(result_file, 'r') as f:
    content = f.read()
    
# Parse as JSON array
data = json.loads(content)

# Create DataFrame
df = pd.DataFrame(data)

# Convert Open and Close to numeric
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Remove any rows with missing values
df = df.dropna(subset=['Open', 'Close'])

# Determine up days (Close > Open) and down days (Close < Open)
# Ignore flat days where Close == Open
df['is_up_day'] = df['Close'] > df['Open']
df['is_down_day'] = df['Close'] < df['Open']

# Group by index and count up vs down days
results = {}
for index_name in sorted(df['Index'].unique()):
    index_data = df[df['Index'] == index_name]
    up_days = index_data['is_up_day'].sum()
    down_days = index_data['is_down_day'].sum()
    total_days = len(index_data)
    
    results[index_name] = {
        'up_days': int(up_days),
        'down_days': int(down_days),
        'total_trading_days': int(total_days),
        'up_more_than_down': bool(up_days > down_days)
    }

# Find which North American indices had more up days than down days
north_american_winners = []
for idx, data in results.items():
    if data['up_more_than_down']:
        north_american_winners.append(idx)

# Create final output
output = {
    'analysis_results': results,
    'north_american_indices_with_more_up_days': sorted(north_american_winners),
    'count_of_winners': len(north_american_winners)
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:9': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['index_info'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': [{'Index': 'IXIC', 'Date': '2018-01-02 00:00:00', 'Open': '6937.649902', 'Close': '7006.899902'}, {'Index': 'IXIC', 'Date': '2018-01-04 00:00:00', 'Open': '7089.5', 'Close': '7077.910156'}, {'Index': 'IXIC', 'Date': '2018-01-08 00:00:00', 'Open': '7135.379883', 'Close': '7157.390137'}, {'Index': 'IXIC', 'Date': '2018-01-11 00:00:00', 'Open': '7168.72998', 'Close': '7211.779785'}, {'Index': 'IXIC', 'Date': '2018-01-17 00:00:00', 'Open': '7257.77002', 'Close': '7298.279785'}], 'var_functions.query_db:30': [{'total_records': '86', 'Index': 'GSPTSE', 'records_per_index': '86'}, {'total_records': '78', 'Index': 'NYA', 'records_per_index': '78'}, {'total_records': '75', 'Index': 'IXIC', 'records_per_index': '75'}], 'var_functions.execute_python:40': {'preview': '[\n  {\n    "Index": "NYA",\n    "Date": "2018-01-09 00:00:00",\n    "Open": "13123.83008",\n    "Close": "13120.83984"\n  },\n  {\n    "Index": "NYA",\n    "Date": "2018-01-16 00:00:00",\n    "Open": "13343.82031",\n    "Close": "13246.86035"\n  },\n  {\n    "Index": "NYA",\n    "Date": "2018-01-18 00:00:00",\n    "Open": "13341.75977",\n    "Close": "13315.91016"\n  },\n  {\n    "Index": "NYA",\n    "Date": "2018-01-22 00:00:00",\n    "Open": "13388.32031",\n    "Close": "13470.37012"\n  },\n  {\n    "Index": "NYA",\n  '}}

exec(code, env_args)

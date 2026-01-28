code = """import json
import pandas as pd
from datetime import datetime

# Load the data from the file
file_path = var_functions.query_db_24
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Parse dates - handle multiple formats
def parse_date(date_str):
    formats = [
        '%Y-%m-%d 00:00:00',
        '%d %b %Y, 00:00',
        '%d %B %Y at 12:00 AM'
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            continue
    return None

df['Date_parsed'] = df['Date'].apply(parse_date)
df['Year'] = df['Date_parsed'].dt.year

# Filter for 2018 data
df_2018 = df[df['Year'] == 2018].copy()

# Calculate up vs down days
df_2018['Up_Day'] = df_2018['Close'] > df_2018['Open']
df_2018['Down_Day'] = df_2018['Close'] < df_2018['Open']

# Count by index
results = []
for index in df_2018['Index'].unique():
    index_data = df_2018[df_2018['Index'] == index]
    up_days = index_data['Up_Day'].sum()
    down_days = index_data['Down_Day'].sum()
    total_days = len(index_data)
    
    results.append({
        'Index': index,
        'Up_Days': int(up_days),
        'Down_Days': int(down_days),
        'Total_Days': int(total_days)
    })

# Filter indices with more up days than down days
up_more_than_down = [r for r in results if r['Up_Days'] > r['Down_Days']]

# Format output
output = {
    'all_indices': results,
    'indices_with_more_up_days': up_more_than_down
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:36': 42}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime

# Load the data
file_path = locals()['var_functions.query_db:24']
with open(file_path, 'r') as f:
    all_data = json.load(f)

print('Total records loaded: ' + str(len(all_data)))

# Filter for 2020 onwards
filtered_data = []
for record in all_data:
    date_str = record['Date']
    try:
        # Try to extract year from various formats
        if any(x in date_str for x in ['2020', '2021', '2022', '2023', '2024', '2025']):
            filtered_data.append(record)
    except:
        continue

print('Records from 2020 onwards: ' + str(len(filtered_data)))

# Convert to DataFrame
df = pd.DataFrame(filtered_data)

# Get unique indices
indices = df['Index'].unique().tolist()
print('Indices found: ' + str(indices))

# Calculate intraday volatility for each record
def calc_volatility(record):
    try:
        open_price = float(record['Open'])
        high_price = float(record['High'])
        low_price = float(record['Low'])
        if open_price > 0:
            return (high_price - low_price) / open_price
        return 0
    except:
        return None

# Calculate average volatility per index
volatility_by_index = {}
for index in indices:
    index_data = df[df['Index'] == index]
    volatilities = [calc_volatility(record) for _, record in index_data.iterrows() if calc_volatility(record) is not None]
    if volatilities:
        avg_volatility = sum(volatilities) / len(volatilities)
        volatility_by_index[index] = avg_volatility

print('Average volatility by index: ' + str(volatility_by_index))

# Find index with highest volatility
if volatility_by_index:
    highest_index = max(volatility_by_index, key=volatility_by_index.get)
    highest_vol = volatility_by_index[highest_index]
    print('Index with highest volatility: ' + str(highest_index) + ' (' + str(highest_vol) + ')')

print('\n__RESULT__:')
print(json.dumps({'status': 'completed', 'analysis': volatility_by_index}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:20': {'status': 'checking variables'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)

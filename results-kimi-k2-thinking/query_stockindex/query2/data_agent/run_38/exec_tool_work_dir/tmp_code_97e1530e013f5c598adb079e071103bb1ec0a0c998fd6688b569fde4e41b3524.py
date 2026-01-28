code = """import json
import pandas as pd

# Get the file path for the query results
file_path = var_functions.query_db:12

# Load the data
data = pd.read_json(file_path)

# Convert Open and Close to float
data['Open'] = data['Open'].astype(float)
data['Close'] = data['Close'].astype(float)

# Filter for 2018 dates (check if '2018' is in the date string)
data_2018 = data[data['Date'].str.contains('2018')].copy()

# Determine if each day is up (Close > Open) or down (Close < Open)
# Ignore flat days (Close == Open)
data_2018['is_up'] = data_2018['Close'] > data_2018['Open']
data_2018['is_down'] = data_2018['Close'] < data_2018['Open']

# Group by index and count up/down days
results = []
for idx in data_2018['Index'].unique():
    idx_data = data_2018[data_2018['Index'] == idx]
    up_days = idx_data['is_up'].sum()
    down_days = idx_data['is_down'].sum()
    total_days = len(idx_data)
    
    results.append({
        'Index': idx,
        'Up_Days': int(up_days),
        'Down_Days': int(down_days),
        'Total_Days': int(total_days),
        'More_Up_Than_Down': up_days > down_days
    })

# Convert to JSON string for output
result_json = json.dumps(results)

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:7': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

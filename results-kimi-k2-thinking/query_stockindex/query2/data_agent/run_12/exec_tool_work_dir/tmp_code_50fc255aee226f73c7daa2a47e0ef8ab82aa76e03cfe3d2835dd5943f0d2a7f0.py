code = """import json
import pandas as pd

# Get the data from previous query using locals() to handle the colon in variable name
var_name = 'var_functions.query_db:8'
result_data = locals()[var_name]

# If it's a file path, read it
if isinstance(result_data, str):
    with open(result_data, 'r') as f:
        data = json.load(f)
else:
    data = result_data

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Date strings to datetime and extract year
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

# Filter for 2018
df_2018 = df[df['Year'] == 2018].copy()

# Convert price columns from string to float
df_2018['Open'] = pd.to_numeric(df_2018['Open'])
df_2018['Close'] = pd.to_numeric(df_2018['Close'])

# Determine up days vs down days
df_2018['is_up_day'] = df_2018['Close'] > df_2018['Open']
df_2018['is_down_day'] = df_2018['Close'] < df_2018['Open']

# Group by index and count up/down days
results = []
for index_name in df_2018['Index'].unique():
    index_data = df_2018[df_2018['Index'] == index_name]
    up_days = index_data['is_up_day'].sum()
    down_days = index_data['is_down_day'].sum()
    results.append({
        'Index': index_name,
        'Up_Days': int(up_days),
        'Down_Days': int(down_days),
        'Net_Days': int(up_days - down_days)
    })

# Filter indices with more up days than down days
positive_indices = [r for r in results if r['Net_Days'] > 0]

print('__RESULT__:')
print(json.dumps(positive_indices))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Load the data from the file
file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Date to datetime and Open/Close to float
df['Date'] = pd.to_datetime(df['Date'])
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Filter for 2018
df_2018 = df[(df['Date'] >= '2018-01-01') & (df['Date'] <= '2018-12-31')]

# Calculate up days (Close > Open) and down days (Close < Open) for each index
results = []
for index in df_2018['Index'].unique():
    idx_data = df_2018[df_2018['Index'] == index]
    up_days = (idx_data['Close'] > idx_data['Open']).sum()
    down_days = (idx_data['Close'] < idx_data['Open']).sum()
    flat_days = (idx_data['Close'] == idx_data['Open']).sum()
    
    results.append({
        'Index': index,
        'Up_Days': int(up_days),
        'Down_Days': int(down_days),
        'Flat_Days': int(flat_days),
        'Total_Days': len(idx_data),
        'More_Up_Than_Down': bool(up_days > down_days)
    })

results_df = pd.DataFrame(results)
print('__RESULT__:')
print(results_df.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

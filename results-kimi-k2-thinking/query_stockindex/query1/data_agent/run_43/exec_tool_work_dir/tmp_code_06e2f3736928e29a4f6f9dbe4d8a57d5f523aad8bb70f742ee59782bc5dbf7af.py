code = """import json
import pandas as pd
from datetime import datetime

# Load data
fp = locals()['var_functions.query_db:24']
with open(fp, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Function to check if year is 2020 or later
def check_year(date_str):
    if '2020' in date_str or '2021' in date_str or '2022' in date_str or '2023' in date_str:
        return True
    return False

# Filter data
filtered = [row for row in data if check_year(row['Date'])]
filtered_df = pd.DataFrame(filtered)

# Calculate volatility
results = {}
for index in filtered_df['Index'].unique():
    idx_data = filtered_df[filtered_df['Index'] == index]
    vols = []
    for _, row in idx_data.iterrows():
        try:
            o = float(row['Open'])
            h = float(row['High'])
            l = float(row['Low'])
            if o > 0:
                vols.append((h - l) / o)
        except:
            pass
    if vols:
        results[index] = sum(vols) / len(vols)

# Find max
max_idx = max(results, key=results.get)
output = {
    'volatilities': results,
    'highest': max_idx,
    'highest_value': results[max_idx]
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:20': {'status': 'checking variables'}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)

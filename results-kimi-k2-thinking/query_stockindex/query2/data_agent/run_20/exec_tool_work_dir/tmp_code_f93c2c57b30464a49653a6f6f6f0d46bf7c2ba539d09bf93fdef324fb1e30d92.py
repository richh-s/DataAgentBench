code = """import json
import pandas as pd

# Load the data from the file
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Clean and convert data types
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)
df['Date'] = pd.to_datetime(df['Date'])

# Determine if each day was up or down
df['Direction'] = 'Flat'
df.loc[df['Close'] > df['Open'], 'Direction'] = 'Up'
df.loc[df['Close'] < df['Open'], 'Direction'] = 'Down'

# Group by index and count up/down days
counts = df.groupby(['Index', 'Direction']).size().unstack(fill_value=0)

# Ensure all columns exist
for col in ['Up', 'Down', 'Flat']:
    if col not in counts.columns:
        counts[col] = 0

# Calculate total days and difference
counts['Total'] = counts['Up'] + counts['Down'] + counts['Flat']
counts['Up_Down_Diff'] = counts['Up'] - counts['Down']

# Filter for indices with more up days than down days
result = counts[counts['Up_Down_Diff'] > 0]

# Prepare output
output = {}
for idx in result.index:
    output[idx] = {
        'Up': int(result.loc[idx, 'Up']),
        'Down': int(result.loc[idx, 'Down']),
        'Flat': int(result.loc[idx, 'Flat']),
        'Total': int(result.loc[idx, 'Total']),
        'Up_Down_Diff': int(result.loc[idx, 'Up_Down_Diff'])
    }

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_records': 240, 'sample_records': [{'Index': 'GSPTSE', 'Date': '2018-01-03 00:00:00', 'Open': '16336.7002', 'Close': '16371.59961'}, {'Index': 'GSPTSE', 'Date': '2018-01-05 00:00:00', 'Open': '16362.59961', 'Close': '16349.40039'}, {'Index': 'GSPTSE', 'Date': '2018-01-08 00:00:00', 'Open': '16355.40039', 'Close': '16317.7002'}]}}

exec(code, env_args)

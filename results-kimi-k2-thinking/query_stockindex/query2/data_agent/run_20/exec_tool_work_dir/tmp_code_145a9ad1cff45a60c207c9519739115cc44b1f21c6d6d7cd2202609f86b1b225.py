code = """import json
import pandas as pd

# Read the full data from the file
file_path = var_functions.query_db:8
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = var_functions.query_db:8

# Create DataFrame
df = pd.DataFrame(data)

# Convert string numbers to float
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)
df['Date'] = pd.to_datetime(df['Date'])

# Determine up vs down days
df['Direction'] = df.apply(lambda row: 'Up' if row['Close'] > row['Open'] else ('Down' if row['Close'] < row['Open'] else 'Flat'), axis=1)

# Group by index and count
grouped = df.groupby(['Index', 'Direction']).size().unstack(fill_value=0)

if 'Flat' not in grouped.columns:
    grouped['Flat'] = 0

# Calculate total days and differences
grouped['Total'] = grouped['Up'] + grouped['Down'] + grouped['Flat']
grouped['Up_Down_Diff'] = grouped['Up'] - grouped['Down']

# Filter for indices with more up days than down days
result = grouped[grouped['Up_Down_Diff'] > 0]

# Convert to simple dict for JSON output
output = result[['Up', 'Down', 'Flat', 'Total', 'Up_Down_Diff']].to_dict('index')

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

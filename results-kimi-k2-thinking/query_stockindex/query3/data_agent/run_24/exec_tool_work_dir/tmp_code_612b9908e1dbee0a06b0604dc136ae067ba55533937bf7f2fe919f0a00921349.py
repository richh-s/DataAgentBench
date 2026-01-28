code = """import json
import pandas as pd

# Get trade data from storage
trade_data = locals().get('var_functions.query_db:8')

# If it's a string path, read the file
if isinstance(trade_data, str):
    with open(trade_data, 'r') as f:
        trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter data from 2000 onwards
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

# Define index to country mapping based on geographic knowledge
index_country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'IXIC': 'USA',
    'NYA': 'USA',
    'N100': 'Netherlands',
    'NSEI': 'India',
    'TWII': 'Taiwan',
    'GSPTSE': 'Canada',
    'J203.JO': 'South Africa',
    'SSMI': 'Switzerland'
}

# Add country info
df_2000['Country'] = df_2000['Index'].map(index_country_map)

print('__RESULT__:')
print(f"Records from 2000 onwards: {len(df_2000):,}")
print(f"Available indices: {sorted(df_2000['Index'].unique())}")
print(f"Countries represented: {sorted(df_2000['Country'].unique())}")

# Summary by index
summary = df_2000.groupby(['Index', 'Country']).agg({
    'Date': ['min', 'max', 'count'],
    'CloseUSD': ['first', 'last']
}).round(2)

summary.columns = ['Start_Date', 'End_Date', 'Days', 'First_Price', 'Last_Price']
summary = summary.reset_index()

print("\nSummary by Index:")
print(summary.to_string(index=False))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

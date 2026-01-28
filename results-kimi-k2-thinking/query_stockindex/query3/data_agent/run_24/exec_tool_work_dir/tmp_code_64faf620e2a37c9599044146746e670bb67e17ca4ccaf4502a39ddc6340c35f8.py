code = """import json
import pandas as pd

# Load the trade data
with open('/tmp/tmph0a3z5vq.json', 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Define index to exchange/country mapping
index_mapping = {
    'N225': {'Exchange': 'Tokyo Stock Exchange', 'Country': 'Japan'},
    'HSI': {'Exchange': 'Hong Kong Stock Exchange', 'Country': 'Hong Kong'},
    '000001.SS': {'Exchange': 'Shanghai Stock Exchange', 'Country': 'China'},
    'GDAXI': {'Exchange': 'Frankfurt Stock Exchange', 'Country': 'Germany'},
    'IXIC': {'Exchange': 'NASDAQ', 'Country': 'USA'},
    'NYA': {'Exchange': 'New York Stock Exchange', 'Country': 'USA'},
    'N100': {'Exchange': 'Euronext', 'Country': 'Netherlands/Europe'},
    'NSEI': {'Exchange': 'National Stock Exchange of India', 'Country': 'India'},
    'TWII': {'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan'},
    '399001.SZ': {'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China'},
    'GSPTSE': {'Exchange': 'Toronto Stock Exchange', 'Country': 'Canada'},
    'J203.JO': {'Exchange': 'Johannesburg Stock Exchange', 'Country': 'South Africa'},
    'SSMI': {'Exchange': 'SIX Swiss Exchange', 'Country': 'Switzerland'}
}

# Filter data from 2000 onwards and add exchange info
df_2000 = df[df['Date'] >= '2000-01-01'].copy()
df_2000['Exchange'] = df_2000['Index'].map(lambda x: index_mapping.get(x, {}).get('Exchange', 'Unknown'))
df_2000['Country'] = df_2000['Index'].map(lambda x: index_mapping.get(x, {}).get('Country', 'Unknown'))

print('__RESULT__:')
print(f"Data from 2000 onwards: {len(df_2000)} records")
print(f"Indices available: {df_2000['Index'].nunique()}")
print(f"Countries: {df_2000['Country'].unique()}")"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

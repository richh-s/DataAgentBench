code = """import json
import pandas as pd
from pathlib import Path

# Get the result from the previous query - it's stored in a variable
# The result is the file path as a string
result_from_storage = var_functions.query_db:8

# Read the JSON file
if isinstance(result_from_storage, str) and Path(result_from_storage).exists():
    with open(result_from_storage, 'r') as f:
        trade_data = json.load(f)
else:
    # If it's not a file path, it might be the data directly
    trade_data = result_from_storage

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
    'N100': {'Exchange': 'Euronext', 'Country': 'Netherlands'},
    'NSEI': {'Exchange': 'National Stock Exchange of India', 'Country': 'India'},
    'TWII': {'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan'},
    '399001.SZ': {'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China'},
    'GSPTSE': {'Exchange': 'Toronto Stock Exchange', 'Country': 'Canada'},
    'J203.JO': {'Exchange': 'Johannesburg Stock Exchange', 'Country': 'South Africa'},
    'SSMI': {'Exchange': 'SIX Swiss Exchange', 'Country': 'Switzerland'}
}

# Add country info
df['Country'] = df['Index'].map(lambda x: index_mapping.get(x, {}).get('Country', 'Unknown'))

# Filter data from 2000 onwards
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

# Group by Index and Country to see available data
grouped = df_2000.groupby(['Index', 'Country']).agg({
    'Date': ['min', 'max', 'count']
}).round(2)

grouped.columns = ['First_Date', 'Last_Date', 'Days_Count']
grouped = grouped.reset_index()

print('__RESULT__:')
print(grouped.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime

# Load the data from the file
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime and Adj Close to float
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = df['Adj Close'].astype(float)

# Map index symbols to exchanges/countries
index_to_exchange = {
    'N225': {'exchange': 'Tokyo Stock Exchange', 'country': 'Japan', 'region': 'Asia'},
    'HSI': {'exchange': 'Hong Kong Stock Exchange', 'country': 'Hong Kong', 'region': 'Asia'},
    '000001.SS': {'exchange': 'Shanghai Stock Exchange', 'country': 'China', 'region': 'Asia'},
    '399001.SZ': {'exchange': 'Shenzhen Stock Exchange', 'country': 'China', 'region': 'Asia'},
    'GDAXI': {'exchange': 'Frankfurt Stock Exchange', 'country': 'Germany', 'region': 'Europe'},
    'GSPTSE': {'exchange': 'Toronto Stock Exchange', 'country': 'Canada', 'region': 'North America'},
    'IXIC': {'exchange': 'NASDAQ', 'country': 'United States', 'region': 'North America'},
    'J203.JO': {'exchange': 'Johannesburg Stock Exchange', 'country': 'South Africa', 'region': 'Africa'},
    'N100': {'exchange': 'Euronext', 'country': 'Netherlands/Europe', 'region': 'Europe'},
    'NSEI': {'exchange': 'National Stock Exchange of India', 'country': 'India', 'region': 'Asia'},
    'NYA': {'exchange': 'New York Stock Exchange', 'country': 'United States', 'region': 'North America'},
    'SSMI': {'exchange': 'SIX Swiss Exchange', 'country': 'Switzerland', 'region': 'Europe'},
    'TWII': {'exchange': 'Taiwan Stock Exchange', 'country': 'Taiwan', 'region': 'Asia'}
}

# Add exchange and country info to the dataframe
df['Exchange'] = df['Index'].map({k: v['exchange'] for k, v in index_to_exchange.items()})
df['Country'] = df['Index'].map({k: v['country'] for k, v in index_to_exchange.items()})

# Show sample data
print('__RESULT__:')
print(df[['Index', 'Date', 'Adj Close', 'Country']].head().to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

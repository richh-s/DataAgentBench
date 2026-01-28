code = """import json

# Load the complete dataset
import json
import pandas as pd

# Read the data from the file
data_file = locals()['var_functions.query_db:12']

# Load the JSON data
if isinstance(data_file, str) and data_file.endswith('.json'):
    with open(data_file, 'r') as f:
        trade_data = json.load(f)
else:
    trade_data = data_file

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['Open'] = pd.to_numeric(df['Open'])
df['High'] = pd.to_numeric(df['High'])
df['Low'] = pd.to_numeric(df['Low'])

# Calculate intraday volatility for each day
df['Intraday_Volatility'] = (df['High'] - df['Low']) / df['Open']

# Group by index and calculate average volatility since 2020
avg_volatility = df.groupby('Index')['Intraday_Volatility'].mean().reset_index()

# Add exchange names for better readability
index_to_exchange = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'TWII': 'Taiwan Stock Exchange'
}

avg_volatility['Exchange'] = avg_volatility['Index'].map(index_to_exchange)
avg_volatility = avg_volatility.sort_values('Intraday_Volatility', ascending=False)

# Get the index with highest average volatility
highest_volatility = avg_volatility.iloc[0]

# Prepare results
result = {
    "highest_volatility_index": highest_volatility['Index'],
    "exchange": highest_volatility['Exchange'],
    "avg_intraday_volatility": float(highest_volatility['Intraday_Volatility']),
    "all_indices_volatility": avg_volatility.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_functions.execute_python:10': [{'exchange': 'Tokyo Stock Exchange', 'index_symbol': 'N225', 'status': 'Available'}, {'exchange': 'Hong Kong Stock Exchange', 'index_symbol': 'HSI', 'status': 'Available'}, {'exchange': 'Shanghai Stock Exchange', 'index_symbol': '000001.SS', 'status': 'Available'}, {'exchange': 'Shenzhen Stock Exchange', 'index_symbol': '399001.SZ', 'status': 'Available'}, {'exchange': 'National Stock Exchange of India', 'index_symbol': 'NSEI', 'status': 'Available'}, {'exchange': 'Korea Exchange', 'index_symbol': 'KS11', 'status': 'Not in dataset'}, {'exchange': 'Taiwan Stock Exchange', 'index_symbol': 'TWII', 'status': 'Available'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

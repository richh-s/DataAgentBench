code = """import json
import pandas as pd

# Access the full trade data from file path
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Access the index info data
index_info = locals()['var_functions.query_db:2']

# Convert to DataFrames
df_trade = pd.DataFrame(trade_data)
df_info = pd.DataFrame(index_info)

# Calculate intraday volatility for each trading day
df_trade['Open'] = pd.to_numeric(df_trade['Open'])
df_trade['High'] = pd.to_numeric(df_trade['High'])
df_trade['Low'] = pd.to_numeric(df_trade['Low'])

df_trade['intraday_volatility'] = (df_trade['High'] - df_trade['Low']) / df_trade['Open']

# Map exchanges to their corresponding index symbols
exchange_to_index = {
    'Tokyo Stock Exchange': 'N225',
    'Hong Kong Stock Exchange': 'HSI',
    'Shanghai Stock Exchange': '000001.SS',
    'Shenzhen Stock Exchange': '399001.SZ',
    'National Stock Exchange of India': 'NSEI',
    'Korea Exchange': '^KS11',  # Note: May need to check actual symbol
    'Taiwan Stock Exchange': 'TWII'
}

# Identify Asian exchanges based on the hint
asian_exchanges = []
for exch in df_info['Exchange']:
    if any(geo in exch.lower() for geo in ['tokyo', 'hong kong', 'shanghai', 'shenzhen', 'india', 'korea', 'taiwan', 'japan', 'singapore']):
        asian_exchanges.append(exch)

# Filter for Asian indices
asian_indices = []
for exch in asian_exchanges:
    if exch in exchange_to_index:
        asian_indices.append(exchange_to_index[exch])

# Add more Asian indices based on the symbols we found
asian_indices.extend(['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII'])

# Filter the trade data for Asian indices
df_asian = df_trade[df_trade['Index'].isin(asian_indices)]

# Group by index and calculate average intraday volatility
result = df_asian.groupby('Index')['intraday_volatility'].mean().reset_index()

# Sort by highest volatility
result_sorted = result.sort_values('intraday_volatility', ascending=False)

output = {
    'asian_indices_found': asian_indices,
    'asian_trade_count': len(df_asian),
    'volatility_by_index': result_sorted.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

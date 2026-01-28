code = """import json
import pandas as pd

# Access the data
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

index_info = locals()['var_functions.query_db:2']

df_trade = pd.DataFrame(trade_data)
df_info = pd.DataFrame(index_info)

# Ensure numeric columns are properly typed
df_trade['Open'] = pd.to_numeric(df_trade['Open'])
df_trade['High'] = pd.to_numeric(df_trade['High'])
df_trade['Low'] = pd.to_numeric(df_trade['Low'])

# Calculate intraday volatility
df_trade['intraday_volatility'] = (df_trade['High'] - df_trade['Low']) / df_trade['Open']

# Filter for 2020 and later
df_trade['Date'] = pd.to_datetime(df_trade['Date'])
df_2020 = df_trade[df_trade['Date'] >= '2020-01-01']

# Define Asian indices based on the data we have
asian_indices = ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII']

# Filter for Asian indices
df_asian = df_2020[df_2020['Index'].isin(asian_indices)]

# Calculate average intraday volatility per index
result = df_asian.groupby('Index').agg({
    'intraday_volatility': ['mean', 'count']
}).round(8)

result.columns = ['avg_volatility', 'trading_days']
result = result.reset_index().sort_values('avg_volatility', ascending=False)

# Get full results
full_results = result.to_dict('records')

# Find the highest
highest_volatility = result.iloc[0]

output = {
    'leading_index': highest_volatility['Index'],
    'avg_intraday_volatility': float(highest_volatility['avg_volatility']),
    'trading_days': int(highest_volatility['trading_days']),
    'all_asian_indices_results': full_results
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'asian_indices_found': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', '^KS11', 'TWII', 'N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII'], 'asian_trade_count': 20187, 'volatility_by_index': [{'Index': '399001.SZ', 'intraday_volatility': 0.020202435308195838}, {'Index': '000001.SS', 'intraday_volatility': 0.017311424071026715}, {'Index': 'NSEI', 'intraday_volatility': 0.01585173971531031}, {'Index': 'HSI', 'intraday_volatility': 0.013823046802453519}, {'Index': 'TWII', 'intraday_volatility': 0.013488352260842065}, {'Index': 'N225', 'intraday_volatility': 0.008720764073041308}]}}

exec(code, env_args)

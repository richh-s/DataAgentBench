code = """import json
import pandas as pd
from datetime import datetime

# Load the data from the file
file_path = locals()['var_functions.query_db:6']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
# Convert all values to proper numeric types
for record in trade_data:
    record['Date'] = datetime.strptime(record['Date'].split()[0], '%Y-%m-%d').date()
    record['Open'] = float(record['Open'])
    record['High'] = float(record['High'])
    record['Low'] = float(record['Low'])
    record['Close'] = float(record['Close'])

df = pd.DataFrame(trade_data)

# Filter for Asian indices
asian_indices = ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII']
df_asia = df[df['Index'].isin(asian_indices)].copy()

# Calculate intraday volatility for each day
df_asia['intraday_volatility'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Calculate average intraday volatility per index since 2020
avg_volatility = df_asia.groupby('Index')['intraday_volatility'].mean().reset_index()
avg_volatility = avg_volatility.sort_values('intraday_volatility', ascending=False)

result = avg_volatility.to_dict('records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}

exec(code, env_args)

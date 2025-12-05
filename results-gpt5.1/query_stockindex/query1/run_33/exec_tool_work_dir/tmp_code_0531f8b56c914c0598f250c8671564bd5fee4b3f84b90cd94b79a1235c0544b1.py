code = """import json, pandas as pd
from datetime import datetime

# Load full trade data from file
with open(var_call_oUavX7ykSXVd7pt28FM1X09u, 'r') as f:
    data = json.load(f)

trade_df = pd.DataFrame(data)

# Clean and normalize columns
trade_df['Open'] = pd.to_numeric(trade_df['Open'], errors='coerce')
trade_df['High'] = pd.to_numeric(trade_df['High'], errors='coerce')
trade_df['Low'] = pd.to_numeric(trade_df['Low'], errors='coerce')

# Parse the various date string formats
trade_df['Date'] = pd.to_datetime(trade_df['Date'], errors='coerce')

# Filter since 2020-01-01
trade_df = trade_df[trade_df['Date'] >= pd.Timestamp('2020-01-01')]

# Map indices to regions using domain knowledge
asia_indices = {
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'N225': 'Tokyo Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'TWII': 'Taiwan Stock Exchange',
    'KS11': 'Korea Exchange'
}

trade_df_asia = trade_df[trade_df['Index'].isin(asia_indices.keys())].copy()

# Compute intraday volatility (High - Low) / Open
trade_df_asia = trade_df_asia[trade_df_asia['Open'] > 0]
trade_df_asia['intraday_vol'] = (trade_df_asia['High'] - trade_df_asia['Low']) / trade_df_asia['Open']

# Average by index
avg_vol = trade_df_asia.groupby('Index')['intraday_vol'].mean().reset_index()

# Find index with highest average volatility
if not avg_vol.empty:
    max_row = avg_vol.loc[avg_vol['intraday_vol'].idxmax()]
    result = {
        'Index': max_row['Index'],
        'AverageIntradayVolatility': float(max_row['intraday_vol'])
    }
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oWV03ChsvThKWLjKF3JC3xKR': ['index_info'], 'var_call_l5p1YsdUlaNTgOy4n8m9mNbJ': ['index_trade'], 'var_call_EyLOaz541pgDHfNfBLhfAS5P': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_pC3hFoG5KhDQ7JJ8WvLJi9Pp': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_oUavX7ykSXVd7pt28FM1X09u': 'file_storage/call_oUavX7ykSXVd7pt28FM1X09u.json'}

exec(code, env_args)

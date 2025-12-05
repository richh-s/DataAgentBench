code = """import json, pandas as pd
from datetime import datetime

# Load full index_trade data from file
with open(var_call_rYblDTOc7AOP3mEYg2zvTnmL, 'r') as f:
    index_trade_data = json.load(f)

trade_df = pd.DataFrame(index_trade_data)

# Normalize column types
for col in ['Open', 'High', 'Low', 'Close']:
    trade_df[col] = pd.to_numeric(trade_df[col], errors='coerce')

# Parse dates and filter since 2020-01-01
trade_df['Date_parsed'] = pd.to_datetime(trade_df['Date'], errors='coerce')
trade_df = trade_df[trade_df['Date_parsed'] >= pd.Timestamp('2020-01-01')]

# Map indices to regions (Asia vs others) using knowledge of major indices
asia_indices = set([
    'N225',  # Nikkei 225 - Tokyo
    'HSI',   # Hang Seng - Hong Kong
    '000001.SS', # SSE Composite - Shanghai
    '399001.SZ', # SZSE Component - Shenzhen
    '399006.SZ', # ChiNext - Shenzhen
    '^BSESN',    # Sensex - India BSE
    '^NSEI',     # Nifty 50 - India NSE
    '^KS11',     # KOSPI - Korea Exchange
    '^TWII',     # TAIEX - Taiwan
    '^STI',      # Straits Times - Singapore (if present)
])

trade_df = trade_df[trade_df['Index'].isin(asia_indices)]

# Compute intraday volatility per day
trade_df['Vol'] = (trade_df['High'] - trade_df['Low']) / trade_df['Open']
trade_df = trade_df[trade_df['Vol'].notna() & (trade_df['Vol'] > 0)]

# Average by index
avg_vol = trade_df.groupby('Index')['Vol'].mean().reset_index()

# Get index with highest average volatility
idxmax = avg_vol['Vol'].idxmax()
result_row = avg_vol.loc[idxmax]
result = {
    'Index': result_row['Index'],
    'AverageIntradayVolatility': float(result_row['Vol'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QHKlwJvWVNB23cxXXmeF7fJD': ['index_info'], 'var_call_sjJr9CYZeY6km71EE0ulsc54': ['index_trade'], 'var_call_jHrFPYH82QtxHPhsw2rAJIME': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_rYblDTOc7AOP3mEYg2zvTnmL': 'file_storage/call_rYblDTOc7AOP3mEYg2zvTnmL.json'}

exec(code, env_args)

code = """import json, pandas as pd
from pathlib import Path

# Load full index_trade data from file
path = Path(var_call_TuPIfaXK8ha9JSHxeUCL0S5j)
with path.open() as f:
    index_trade = json.load(f)

trade_df = pd.DataFrame(index_trade)

# Ensure numeric types
for col in ['Open','High','Low']:
    trade_df[col] = pd.to_numeric(trade_df[col], errors='coerce')

# Filter dates since 2020-01-01 (Date is string; parse to datetime first)
trade_df['Date_dt'] = pd.to_datetime(trade_df['Date'], errors='coerce')
trade_df = trade_df[trade_df['Date_dt'] >= pd.Timestamp('2020-01-01')]

# Compute intraday volatility
trade_df = trade_df[trade_df['Open'] > 0]
trade_df['intraday_vol'] = (trade_df['High'] - trade_df['Low']) / trade_df['Open']

# Map indices to regions using geographic knowledge; restrict to Asia
asia_indices = {
    'N225': 'Tokyo Stock Exchange',                 # Japan
    'HSI': 'Hong Kong Stock Exchange',              # Hong Kong
    '000001.SS': 'Shanghai Stock Exchange',         # China
    '399001.SZ': 'Shenzhen Stock Exchange',         # China
    '399006.SZ': 'Shenzhen Stock Exchange',         # China (ChiNext)
    '^BSESN': 'Bombay Stock Exchange',              # India (not in metadata but Asia)
    '^NSEI': 'National Stock Exchange of India',    # India
    '^KS11': 'Korea Exchange',                      # South Korea (KOSPI)
    '^TWII': 'Taiwan Stock Exchange',               # Taiwan
}

asia_df = trade_df[trade_df['Index'].isin(asia_indices.keys())].copy()

# Compute average intraday volatility per index since 2020
avg_vol = asia_df.groupby('Index')['intraday_vol'].mean().dropna()

if avg_vol.empty:
    result = {'index': None, 'average_intraday_volatility': None}
else:
    top_index = avg_vol.idxmax()
    result = {
        'index': top_index,
        'average_intraday_volatility': float(avg_vol.loc[top_index])
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_WsfVhzuhcW0cp3IxlXX4mCXU': ['index_info'], 'var_call_F1Bpya0J8wMzxm2cBXSM04yz': ['index_trade'], 'var_call_k2u4XTr0m7IWxqWvpohAtAvS': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_TuPIfaXK8ha9JSHxeUCL0S5j': 'file_storage/call_TuPIfaXK8ha9JSHxeUCL0S5j.json'}

exec(code, env_args)

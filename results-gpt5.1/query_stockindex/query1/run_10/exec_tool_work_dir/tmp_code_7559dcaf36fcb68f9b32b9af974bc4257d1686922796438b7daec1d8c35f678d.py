code = """import json, pandas as pd, os

# Load full index_trade data from file
path = var_call_LNJh3TGFLLwzW9rrIPPOzxoF
with open(path, 'r') as f:
    index_trade = json.load(f)

# Create DataFrame
trade_df = pd.DataFrame(index_trade)

# Ensure numeric types
for col in ['Open','High','Low']:
    trade_df[col] = pd.to_numeric(trade_df[col], errors='coerce')

# Filter from 2020-01-01 onward; Date is string but query already filtered, so skip

# Compute intraday volatility
trade_df['vol'] = (trade_df['High'] - trade_df['Low']) / trade_df['Open']
trade_df = trade_df.dropna(subset=['vol'])

# Map index to region using known correspondences for Asia
asia_indices = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    '399006.SZ': 'Shenzhen Stock Exchange',
    '^NSEI': 'National Stock Exchange of India',
    'KS11': 'Korea Exchange',
    '^TWII': 'Taiwan Stock Exchange'
}

trade_df_asia = trade_df[trade_df['Index'].isin(asia_indices.keys())]

# Average intraday volatility per index since 2020
avg_vol = trade_df_asia.groupby('Index')['vol'].mean().sort_values(ascending=False)

result = {
    'ranking': avg_vol.to_dict(),
    'top_index': avg_vol.index[0] if len(avg_vol)>0 else None,
    'top_avg_vol': float(avg_vol.iloc[0]) if len(avg_vol)>0 else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_x80BfxhIPZgjyYQ5M9tnBvHJ': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_LNJh3TGFLLwzW9rrIPPOzxoF': 'file_storage/call_LNJh3TGFLLwzW9rrIPPOzxoF.json'}

exec(code, env_args)

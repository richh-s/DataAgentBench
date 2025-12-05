code = """import json, pandas as pd

# Load full index_trade data from file
with open(var_call_Zl80WbLeCKpev2iwonzqWWM1, 'r') as f:
    trade_data = json.load(f)

trade_df = pd.DataFrame(trade_data)

# Ensure numeric types
for col in ['Open', 'High', 'Low']:
    trade_df[col] = pd.to_numeric(trade_df[col], errors='coerce')

# Filter dates from 2020-01-01 onward.
# Date formats are messy strings, so parse to datetime first.
trade_df['Date_parsed'] = pd.to_datetime(trade_df['Date'], errors='coerce')
trade_df = trade_df[trade_df['Date_parsed'] >= pd.Timestamp('2020-01-01')]

# Compute intraday volatility (High - Low) / Open
trade_df['vol'] = (trade_df['High'] - trade_df['Low']) / trade_df['Open']

# Map indices to regions (Asia focus).
# Based on typical major indices present in such datasets.
asia_indices = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    '^NSEI': 'National Stock Exchange of India',
    '^KS11': 'Korea Exchange',
    '^TWII': 'Taiwan Stock Exchange'
}

asia_df = trade_df[trade_df['Index'].isin(asia_indices.keys())].copy()

# Average intraday volatility per index
avg_vol = asia_df.groupby('Index')['vol'].mean().dropna().sort_values(ascending=False)

if avg_vol.empty:
    result = {'error': 'No Asia indices found in dataset for period since 2020-01-01'}
else:
    top_index = avg_vol.index[0]
    result = {
        'top_asia_index': top_index,
        'average_intraday_volatility': float(avg_vol.iloc[0]),
        'all_asia_indices_ranked': avg_vol.reset_index().to_dict(orient='records')
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_SPHgKFW0bBM5SifntaP0s0V3': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_Zl80WbLeCKpev2iwonzqWWM1': 'file_storage/call_Zl80WbLeCKpev2iwonzqWWM1.json'}

exec(code, env_args)

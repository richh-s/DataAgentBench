code = """import json, pandas as pd
from datetime import datetime

path = var_call_NLAQPQgWqTZNMalmXhW14gPG
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# normalize date formats and filter since 2020-01-01
parsed_dates = pd.to_datetime(df['Date'], errors='coerce')
mask = parsed_dates >= pd.Timestamp('2020-01-01')
df = df[mask].copy()

# convert numeric columns
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# drop rows with missing needed data or nonpositive open
df = df.dropna(subset=['Open','High','Low'])
df = df[df['Open'] > 0]

# identify Asia indices based on known symbols
asia_indices = {
    'N225',   # Nikkei 225 - Tokyo Stock Exchange, Japan
    'HSI',    # Hang Seng Index - Hong Kong Stock Exchange
    '000001.SS', # SSE Composite - Shanghai
    '399001.SZ', # Shenzhen Component
    '^NSEI',  # Nifty 50 - National Stock Exchange of India
    '^KS11',  # KOSPI - Korea Exchange
    '^TWII',  # TAIEX - Taiwan Stock Exchange
}

asia_df = df[df['Index'].isin(asia_indices)].copy()

asia_df['intraday_vol'] = (asia_df['High'] - asia_df['Low']) / asia_df['Open']

result = asia_df.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False).reset_index()

top_index = None
if not result.empty:
    row = result.iloc[0]
    top_index = {
        'Index': row['Index'],
        'AverageIntradayVolatility': float(row['intraday_vol'])
    }

out = {
    'ranking': result.to_dict(orient='records'),
    'top_index': top_index
}

res_json = json.dumps(out)
print('__RESULT__:')
print(res_json)"""

env_args = {'var_call_cue9qG4PtnKYtI5WMhk6oWIr': ['index_info'], 'var_call_KiBmtZXlbbbbffd4Y9uAHFBU': ['index_trade'], 'var_call_IEukTxqLnb4JMXFgfrz6kwUd': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_NLAQPQgWqTZNMalmXhW14gPG': 'file_storage/call_NLAQPQgWqTZNMalmXhW14gPG.json'}

exec(code, env_args)

code = """import json, pandas as pd
from datetime import datetime
import re

# Load large json file
path = var_call_04n4MEp3D6qfAqznGNDmKV8e
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# parse dates robustly
# pandas to_datetime can handle multiple formats
# remove 'at' timezone-like text if present
s = df['Date'].astype(str).str.replace(' at 12:00 AM','', regex=False)
dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
df['dt'] = dt

df = df[df['dt'] >= pd.Timestamp('2020-01-01')].copy()

# numeric conversion
for c in ['Open','High','Low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df = df.dropna(subset=['Open','High','Low','Index'])
df = df[df['Open'] != 0]

df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# Define Asia indices set based on known symbols in dataset
asia_indices = {'HSI':'Hang Seng Index (Hong Kong)',
                'N225':'Nikkei 225 (Japan)',
                'NSEI':'NIFTY 50 (India)',
                '000001.SS':'SSE Composite (China - Shanghai)',
                '399001.SZ':'SZSE Component (China - Shenzhen)',
                'TWII':'Taiwan Weighted (Taiwan)'}

asia_df = df[df['Index'].isin(asia_indices.keys())]

agg = asia_df.groupby('Index').agg(avg_intraday_volatility=('intraday_vol','mean'), n_days=('intraday_vol','size'))
agg = agg.sort_values('avg_intraday_volatility', ascending=False)

winner = agg.iloc[0]
winner_index = agg.index[0]

result = {
    'winner_index': winner_index,
    'winner_name': asia_indices[winner_index],
    'avg_intraday_volatility': float(winner['avg_intraday_volatility']),
    'n_days': int(winner['n_days']),
    'ranking': [{
        'Index': idx,
        'Name': asia_indices[idx],
        'avg_intraday_volatility': float(row['avg_intraday_volatility']),
        'n_days': int(row['n_days'])
    } for idx, row in agg.reset_index().set_index('Index').iterrows()]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Fa2AWoBJYBnro3c61gl88UYl': ['index_info'], 'var_call_RpZpAbuvLjydPIILq2WIyHQQ': ['index_trade'], 'var_call_NejJybl8a2moL6E1vGBoEhM6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_Qz7QhsmdQMyuX6fipgwHx0GF': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_q0tPjRe8Ncon3hAJPBU7qSoj': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_xwbyqBGH8PVaTnuJwbrvd0H6': {'indices': ['J203.JO', 'IXIC', 'HSI', 'N225', 'GSPTSE', 'NSEI', 'GDAXI', 'NYA', 'N100', '399001.SZ', '000001.SS', 'SSMI', 'TWII']}, 'var_call_04n4MEp3D6qfAqznGNDmKV8e': 'file_storage/call_04n4MEp3D6qfAqznGNDmKV8e.json'}

exec(code, env_args)

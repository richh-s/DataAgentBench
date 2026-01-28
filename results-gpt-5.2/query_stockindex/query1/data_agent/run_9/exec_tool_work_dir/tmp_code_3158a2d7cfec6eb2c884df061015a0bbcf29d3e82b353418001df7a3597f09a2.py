code = """import json, pandas as pd
from datetime import datetime

# load records
path = var_call_qsHzVnotW0e8p1IzDdk6MhmM
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# parse date: take first 10 chars (YYYY-MM-DD) for 2020+ rows
# ensure filter since 2020-01-01
s = df['Date'].astype(str).str.slice(0,10)
df['date'] = pd.to_datetime(s, errors='coerce')
df = df[df['date'] >= pd.Timestamp('2020-01-01')].copy()
for c in ['Open','High','Low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')
df = df.dropna(subset=['Open','High','Low'])
df = df[df['Open'] != 0]

df['intraday_vol'] = (df['High'] - df['Low'])/df['Open']

# Asia indices in dataset by symbol knowledge
asia = {
    'N225': 'Japan (Tokyo Stock Exchange) Nikkei 225',
    'HSI': 'Hong Kong (Hong Kong Stock Exchange) Hang Seng Index',
    'TWII': 'Taiwan (Taiwan Stock Exchange) TAIEX',
    '000001.SS': 'China (Shanghai Stock Exchange) SSE Composite',
    '399001.SZ': 'China (Shenzhen Stock Exchange) SZSE Component',
    'NSEI': 'India (NSE) Nifty 50'
}

dfa = df[df['Index'].isin(list(asia.keys()))].copy()
res = dfa.groupby('Index').intraday_vol.mean().sort_values(ascending=False)

winner = res.index[0]
answer = {
    'winner_index': winner,
    'winner_description': asia[winner],
    'avg_intraday_volatility': float(res.iloc[0]),
    'ranking': [{'Index': idx, 'avg_intraday_volatility': float(val)} for idx, val in res.items()]
}

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_bNUhopqG20lyGwO3fZMO5NSb': ['index_info'], 'var_call_mDu2xmPZGDNg27pMZjqDYhEI': ['index_trade'], 'var_call_YQxLL6rf0qDcANtIHDkzoJX3': [{'Index': 'NYA', 'n': '13947'}, {'Index': 'N225', 'n': '13874'}, {'Index': 'IXIC', 'n': '12690'}, {'Index': 'GSPTSE', 'n': '10526'}, {'Index': 'HSI', 'n': '8492'}, {'Index': 'GDAXI', 'n': '8438'}, {'Index': 'SSMI', 'n': '7671'}, {'Index': 'TWII', 'n': '5869'}, {'Index': '000001.SS', 'n': '5791'}, {'Index': '399001.SZ', 'n': '5760'}, {'Index': 'N100', 'n': '5474'}, {'Index': 'NSEI', 'n': '3346'}, {'Index': 'J203.JO', 'n': '2346'}], 'var_call_JsXKI4wlb58llDhseHiO0MhK': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_qsHzVnotW0e8p1IzDdk6MhmM': 'file_storage/call_qsHzVnotW0e8p1IzDdk6MhmM.json'}

exec(code, env_args)

code = """import json, pandas as pd
from datetime import datetime

path = var_call_cLoBv1BgypDqCZBURBXMXw2T
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize date strings and filter since 2020-01-01

def parse_date(s):
    for fmt in ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    return None

df['Date_parsed'] = df['Date'].apply(parse_date)
df = df[df['Date_parsed'] >= datetime(2020,1,1)]

# Convert numeric columns
for col in ['Open','High','Low','Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Compute intraday volatility
valid = df[df['Open']>0].copy()
valid['vol'] = (valid['High'] - valid['Low']) / valid['Open']

avg_vol = valid.groupby('Index')['vol'].mean().reset_index()

# Map Asia indices based on known major exchanges
asia_indices = {
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'N225': 'Tokyo Stock Exchange',
    '^NSEI': 'National Stock Exchange of India',
    '^KS11': 'Korea Exchange',
    '^TWII': 'Taiwan Stock Exchange'
}

avg_vol_asia = avg_vol[avg_vol['Index'].isin(asia_indices.keys())].copy()

if avg_vol_asia.empty:
    result = {'index': None, 'average_intraday_volatility': None}
else:
    row = avg_vol_asia.sort_values('vol', ascending=False).iloc[0]
    result = {
        'index': row['Index'],
        'average_intraday_volatility': float(row['vol'])
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_IbpLP4hJc0fri83Ex9qyvxSF': ['index_info'], 'var_call_BHg7T67fyrby5IfQ3lViG44u': ['index_trade'], 'var_call_UvZd2rWEYLZh1hqkyyiyBADa': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_cLoBv1BgypDqCZBURBXMXw2T': 'file_storage/call_cLoBv1BgypDqCZBURBXMXw2T.json'}

exec(code, env_args)

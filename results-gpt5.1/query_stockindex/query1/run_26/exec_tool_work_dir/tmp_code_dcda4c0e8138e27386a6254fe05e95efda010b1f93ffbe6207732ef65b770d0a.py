code = """import json, pandas as pd
from datetime import datetime

path = var_call_DyWXOWcCvhYbKkTCfA6sdZz8
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# parse dates robustly and filter from 2020-01-01
def parse_date(x):
    for fmt in ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)
df = df[df['Date_parsed'] >= pd.Timestamp('2020-01-01')]

# compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# map Asia indices: N225 (Tokyo), HSI (HK), 000001.SS (Shanghai), 399001.SZ (Shenzhen), NSEI (India), TWII (Taiwan), KRX main? but index list has none for Korea
asia_indices = ['N225','HSI','000001.SS','399001.SZ','NSEI','TWII']

res = df[df['Index'].isin(asia_indices)].groupby('Index')['vol'].mean().sort_values(ascending=False)

result = {
    'avg_intraday_vol_by_index': res.to_dict(),
    'max_index': res.index[0] if len(res)>0 else None,
    'max_vol': float(res.iloc[0]) if len(res)>0 else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_N0nsyA30EKz5OjJaE2jn7aX6': ['index_info'], 'var_call_F2LZ24CELTo77bqFFHtPvSJG': ['index_trade'], 'var_call_zUlHwA9z6YmdDqqi6iFCSiR2': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_8I2W8bATa8NYvwuM7qERdb3H': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_call_DyWXOWcCvhYbKkTCfA6sdZz8': 'file_storage/call_DyWXOWcCvhYbKkTCfA6sdZz8.json'}

exec(code, env_args)

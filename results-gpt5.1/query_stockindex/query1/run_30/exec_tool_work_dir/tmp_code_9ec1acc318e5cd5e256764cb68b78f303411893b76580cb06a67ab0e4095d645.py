code = """import json, pandas as pd
from datetime import datetime

path = var_call_FeiZqorwlf55qV6UsGSn19zp
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# normalize dates with multiple formats
formats = [
    '%Y-%m-%d',
    '%d %b %Y, %H:%M',
    '%B %d, %Y at %I:%M %p'
]

def parse_date(x):
    for fmt in formats:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].astype(str).apply(parse_date)

filt = df['Date_parsed'] >= pd.Timestamp('2020-01-01')
post2020 = df[filt].copy()

post2020['vol'] = (post2020['High'] - post2020['Low']) / post2020['Open']
res = post2020.groupby('Index')['vol'].mean().sort_values(ascending=False)

result = res.reset_index().to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result) )"""

env_args = {'var_call_QFA8KcUU2y29NZNQXoS3MQKB': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_ifvuWTY5fXORmQWli5WvOBiN': ['index_info'], 'var_call_FeiZqorwlf55qV6UsGSn19zp': 'file_storage/call_FeiZqorwlf55qV6UsGSn19zp.json'}

exec(code, env_args)

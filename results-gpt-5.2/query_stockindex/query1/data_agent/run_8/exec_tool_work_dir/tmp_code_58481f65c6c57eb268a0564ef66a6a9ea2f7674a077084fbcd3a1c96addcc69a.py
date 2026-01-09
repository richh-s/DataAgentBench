code = """import json, pandas as pd
from datetime import datetime

# load full trade data
path = var_call_ESY7XYi4HRY2TxhIMqe3mtj8
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# numeric columns may be strings
for c in ['Open','High','Low','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# parse heterogeneous date formats
s = df['Date'].astype(str)
# attempt multiple parses
parsed = pd.to_datetime(s, errors='coerce', utc=False, infer_datetime_format=True)
# second pass with dayfirst for formats like '06 Jan 1987, 00:00'
mask = parsed.isna()
if mask.any():
    parsed2 = pd.to_datetime(s[mask], errors='coerce', dayfirst=True)
    parsed.loc[mask] = parsed2
# third pass for 'January 02, 1987 at 12:00 AM'
mask = parsed.isna()
if mask.any():
    parsed3 = pd.to_datetime(s[mask].str.replace(' at ', ' ', regex=False), errors='coerce')
    parsed.loc[mask] = parsed3

df['Date_parsed'] = parsed

df = df[df['Date_parsed'].notna()].copy()
df = df[df['Date_parsed'] >= pd.Timestamp('2020-01-01')]

# compute intraday volatility
vol = (df['High'] - df['Low']) / df['Open']
df['intraday_vol'] = vol
# keep valid
df = df[(df['Open']>0) & df['intraday_vol'].notna() & (df['intraday_vol']>=0)]

# define Asia indices list present
asia_indices = {
    'N225': 'Japan (Nikkei 225)',
    'HSI': 'Hong Kong (Hang Seng)',
    '000001.SS': 'China (SSE Composite)',
    '399001.SZ': 'China (SZSE Component)',
    'KS11': 'South Korea (KOSPI)',
    'TWII': 'Taiwan (TAIEX)',
    'BSESN': 'India (SENSEX)',
    'NSEI': 'India (NIFTY 50)',
    'JKSE': 'Indonesia (Jakarta Composite)',
    'KLSE': 'Malaysia (KLCI)',
    'STI': 'Singapore (STI)',
    'SET.BK': 'Thailand (SET)',
    'PSI': 'Philippines (PSEi)',
}

present = set(df['Index'].unique())
use = sorted(list(present.intersection(asia_indices.keys())))

df_asia = df[df['Index'].isin(use)].copy()

avg = df_asia.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)
# also count
cnt = df_asia.groupby('Index')['intraday_vol'].size()

if len(avg)==0:
    out = {'error':'No Asia indices found with data since 2020 in dataset','present_indices_count': int(len(present))}
else:
    top_idx = avg.index[0]
    out = {
        'top_index': top_idx,
        'top_index_name': asia_indices.get(top_idx, top_idx),
        'avg_intraday_volatility': float(avg.iloc[0]),
        'days_used': int(cnt.loc[top_idx]),
        'ranking_top10': [
            {
                'Index': i,
                'Name': asia_indices.get(i,i),
                'avg_intraday_volatility': float(avg.loc[i]),
                'days_used': int(cnt.loc[i])
            }
            for i in avg.head(10).index
        ]
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AdhnfHZv9o7DayNTPgi5XOKu': ['index_info'], 'var_call_dmT7XoQQfmkjeVxZH7lWzTUi': ['index_trade'], 'var_call_7VxAhE6MGeGvrdUwhTuRaGuJ': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_ESY7XYi4HRY2TxhIMqe3mtj8': 'file_storage/call_ESY7XYi4HRY2TxhIMqe3mtj8.json'}

exec(code, env_args)

code = """import json, pandas as pd
from datetime import datetime

# load full data
path = var_call_FvTEXe47HH0NnjMUIyHeTHOa
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)

# parse dates with multiple possible formats
fmts = [
    '%d %b %Y, %H:%M',
    '%B %d, %Y at %I:%M %p',
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%d'
]

def parse_dt(s):
    if s is None:
        return pd.NaT
    s = str(s).strip()
    for fmt in fmts:
        try:
            return pd.Timestamp(datetime.strptime(s, fmt)).normalize()
        except Exception:
            pass
    # last resort: pandas
    try:
        return pd.to_datetime(s, errors='coerce').normalize()
    except Exception:
        return pd.NaT

# numeric
for c in ['open','high','low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df['date'] = df['dt'].map(parse_dt)

df = df[df['date'].notna()]
df = df[df['date'] >= pd.Timestamp('2020-01-01')]

df = df[(df['open']>0) & df['high'].notna() & df['low'].notna()]
df['intraday_vol'] = (df['high'] - df['low']) / df['open']

df = df[df['intraday_vol'].notna() & (df['intraday_vol']>=0)]

# Asia indices list (inferred)
asia = {
    'N225':'Japan (Tokyo) Nikkei 225',
    'HSI':'Hong Kong Hang Seng',
    '000001.SS':'China (Shanghai) SSE Composite',
    '399001.SZ':'China (Shenzhen) SZSE Component',
    'KS11':'South Korea KOSPI',
    'TWII':'Taiwan TAIEX',
    'STI':'Singapore Straits Times',
    'BSESN':'India BSE Sensex',
    'NSEI':'India Nifty 50',
    'JKSE':'Indonesia Jakarta Composite',
    'KLSE':'Malaysia KLCI',
    'PSEI':'Philippines PSEi',
    'SET.BK':'Thailand SET',
}

df_asia = df[df['idx'].isin(asia.keys())].copy()

stats = (df_asia.groupby('idx')
         .agg(avg_intraday_vol=('intraday_vol','mean'), n_days=('intraday_vol','size'))
         .reset_index())

stats = stats[stats['n_days']>=50].sort_values('avg_intraday_vol', ascending=False)

if len(stats)==0:
    out = {'error':'No Asia indices found with >=50 days since 2020 in dataset.'}
else:
    top = stats.iloc[0].to_dict()
    top['exchange_or_desc'] = asia.get(top['idx'])
    top['avg_intraday_vol'] = float(top['avg_intraday_vol'])
    top['n_days'] = int(top['n_days'])
    out = {
        'top_index': top,
        'ranking_top10': [
            {
                'idx': r['idx'],
                'exchange_or_desc': asia.get(r['idx']),
                'avg_intraday_vol': float(r['avg_intraday_vol']),
                'n_days': int(r['n_days'])
            }
            for r in stats.head(10).to_dict(orient='records')
        ]
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3KUGfe30v0OVUjLrYjVlIIqy': ['index_info'], 'var_call_D1sAsydhLjJQJcFMmsmW7tpi': ['index_trade'], 'var_call_u6pcRMnVQIESuizAcSQWZKRM': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_FvTEXe47HH0NnjMUIyHeTHOa': 'file_storage/call_FvTEXe47HH0NnjMUIyHeTHOa.json'}

exec(code, env_args)

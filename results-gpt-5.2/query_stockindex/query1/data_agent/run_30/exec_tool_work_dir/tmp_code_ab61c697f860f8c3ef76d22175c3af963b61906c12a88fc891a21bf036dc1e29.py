code = """import json, pandas as pd, re
from datetime import datetime

path = var_call_xT4NS0g5VB3wi7VNVFi6z0kX
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# coerce numeric
for c in ['op','hi','lo']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# parse multiple date formats
fmts = ['%Y-%m-%d %H:%M:%S', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']

def parse_dt(s):
    if s is None:
        return pd.NaT
    for fmt in fmts:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            pass
    return pd.NaT

df['dt_parsed'] = df['dt'].map(parse_dt)

# filter since 2020
cutoff = pd.Timestamp('2020-01-01')
df = df[df['dt_parsed'] >= cutoff]

# intraday volatility
vol = (df['hi'] - df['lo']) / df['op'].where(df['op'] != 0)
df['vol'] = vol

# average per index
agg = df.groupby('idx').agg(avg_intraday_vol=('vol','mean'), n_days=('vol','count')).reset_index()

# Define Asia indices universe (based on common major indices present in dataset)
asia_indices = {
    'N225': 'Japan (Tokyo) Nikkei 225',
    'HSI': 'Hong Kong Hang Seng Index',
    '000001.SS': 'China (Shanghai) SSE Composite',
    '399001.SZ': 'China (Shenzhen) SZSE Component',
    'KS11': 'South Korea KOSPI',
    'TWII': 'Taiwan Weighted',
    'SENSEX': 'India BSE Sensex',
    '^NSEI': 'India Nifty 50',
    'STI': 'Singapore Straits Times',
    'JKSE': 'Indonesia Jakarta Composite',
    'KLSE': 'Malaysia KLCI',
    'SET.BK': 'Thailand SET',
    'PSEI.PS': 'Philippines PSEi',
    'VNINDEX': 'Vietnam VN-Index',
    'AORD': 'Australia All Ordinaries',
    'NZ50': 'New Zealand NZX 50',
    'NZX50': 'New Zealand NZX 50',
}

agg_asia = agg[agg['idx'].isin(asia_indices.keys())].copy()

# If none matched, fall back to selecting indices likely Asia by code patterns (Chinese tickers, common ones)
if agg_asia.empty:
    patt = re.compile(r'(^0\d{5}\.SS$)|(^3\d{5}\.SZ$)|(\.BK$)|(\.PS$)')
    agg_asia = agg[agg['idx'].map(lambda x: bool(patt.search(str(x))) or str(x) in ['HSI','N225','KS11','TWII','STI','JKSE','KLSE','SENSEX','^NSEI'])].copy()

agg_asia = agg_asia.dropna(subset=['avg_intraday_vol'])
agg_asia = agg_asia.sort_values('avg_intraday_vol', ascending=False)

top = agg_asia.iloc[0].to_dict() if len(agg_asia) else None

out = {
    'top_asia_index': None if top is None else top['idx'],
    'top_asia_index_name': None if top is None else asia_indices.get(top['idx']),
    'avg_intraday_volatility': None if top is None else float(top['avg_intraday_vol']),
    'n_days': None if top is None else int(top['n_days']),
    'top5': [
        {
            'idx': r.idx,
            'name': asia_indices.get(r.idx),
            'avg_intraday_volatility': float(r.avg_intraday_vol),
            'n_days': int(r.n_days)
        }
        for r in agg_asia.head(5).itertuples(index=False)
    ]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_V4ZJME6KWliaM6KjjxZJCZwN': ['index_info'], 'var_call_fF4mabdmKlik54ChHuND5CWE': ['index_trade'], 'var_call_hsMOqVTKIgDKukXmT0nygWz0': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}, {'Date': '02 Feb 1987, 00:00'}, {'Date': '03 Feb 1987, 00:00'}, {'Date': 'February 04, 1987 at 12:00 AM'}, {'Date': 'February 05, 1987 at 12:00 AM'}, {'Date': '06 Feb 1987, 00:00'}, {'Date': '1987-02-09 00:00:00'}, {'Date': '1987-02-10 00:00:00'}, {'Date': '11 Feb 1987, 00:00'}, {'Date': '12 Feb 1987, 00:00'}, {'Date': 'February 13, 1987 at 12:00 AM'}, {'Date': '16 Feb 1987, 00:00'}, {'Date': 'February 17, 1987 at 12:00 AM'}, {'Date': 'February 18, 1987 at 12:00 AM'}, {'Date': '19 Feb 1987, 00:00'}, {'Date': '1987-02-20 00:00:00'}, {'Date': 'February 23, 1987 at 12:00 AM'}, {'Date': '24 Feb 1987, 00:00'}, {'Date': 'February 25, 1987 at 12:00 AM'}, {'Date': '26 Feb 1987, 00:00'}, {'Date': '27 Feb 1987, 00:00'}, {'Date': '1987-03-02 00:00:00'}, {'Date': '1987-03-03 00:00:00'}, {'Date': '1987-03-04 00:00:00'}, {'Date': 'March 05, 1987 at 12:00 AM'}, {'Date': 'March 06, 1987 at 12:00 AM'}, {'Date': '09 Mar 1987, 00:00'}, {'Date': 'March 10, 1987 at 12:00 AM'}, {'Date': '11 Mar 1987, 00:00'}, {'Date': '12 Mar 1987, 00:00'}, {'Date': 'March 13, 1987 at 12:00 AM'}], 'var_call_xT4NS0g5VB3wi7VNVFi6z0kX': 'file_storage/call_xT4NS0g5VB3wi7VNVFi6z0kX.json'}

exec(code, env_args)

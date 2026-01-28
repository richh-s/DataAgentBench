code = """import json, pandas as pd
from datetime import datetime

# load full dataset
path = var_call_52KD3n1PM0mG2e6fq0tCj8Y6
with open(path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# coerce numeric
for c in ['Open','High','Low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

def parse_dt(s):
    if s is None:
        return pd.NaT
    s = str(s)
    # try common formats
    fmts = [
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
        '%d %b %Y, %H:%M',
        '%d %b %Y, %H:%M:%S',
        '%B %d, %Y at %I:%M %p',
        '%b %d, %Y at %I:%M %p'
    ]
    for fmt in fmts:
        try:
            return pd.Timestamp(datetime.strptime(s, fmt)).normalize()
        except Exception:
            pass
    # fallback
    try:
        return pd.to_datetime(s, errors='coerce').normalize()
    except Exception:
        return pd.NaT

df['DateParsed'] = df['Date'].map(parse_dt)
# filter since 2020
cutoff = pd.Timestamp('2020-01-01')
df = df[df['DateParsed'] >= cutoff]
# intraday volatility
vol = (df['High'] - df['Low']) / df['Open'].replace({0: pd.NA})
df['vol'] = vol
agg = df.groupby('Index', dropna=False).agg(avg_intraday_volatility=('vol','mean'), n_days=('vol','count')).reset_index()
agg = agg.dropna(subset=['avg_intraday_volatility'])
agg = agg.sort_values('avg_intraday_volatility', ascending=False)
# Asia indices list (major)
asia = {
    'N225','HSI','000001.SS','399001.SZ','CSI300','000300.SS','KS11','KOSPI','TWII','^TWII','STI','SENSEX','BSESN','NSEI','NIFTY 50','JKSE','KLCI','SETI','VNINDEX','PSEI'
}
agg_asia = agg[agg['Index'].isin(asia)]
# if some asia symbols not matching, try contains patterns typical of Asia tickers
# but keep it simple; if empty, just take overall top and report inability.
if len(agg_asia)==0:
    top = agg.iloc[0].to_dict()
    out = {'top_asia_index': None, 'note':'No Asia indices matched predefined symbol set', 'overall_top': top}
else:
    top = agg_asia.iloc[0].to_dict()
    out = {'top_asia_index': top, 'top5_asia': agg_asia.head(5).to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_IiUhkcTfj4VWsnlLU11c4Q53': ['index_info'], 'var_call_hyqIt5EEq5nSkyq2saXi9Oxi': ['index_trade'], 'var_call_3o1VnOZfnRE0J9q2NIafyeC5': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_52KD3n1PM0mG2e6fq0tCj8Y6': 'file_storage/call_52KD3n1PM0mG2e6fq0tCj8Y6.json'}

exec(code, env_args)

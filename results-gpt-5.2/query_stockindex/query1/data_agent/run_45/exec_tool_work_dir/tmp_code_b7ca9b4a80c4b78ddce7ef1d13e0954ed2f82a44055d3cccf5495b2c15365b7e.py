code = """import json, pandas as pd
from datetime import datetime

# load full dataset
path = var_call_pIK5gECmA2UBWfU0As9mjVYM
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# convert numeric
for c in ['open','high','low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# parse dates robustly
s = df['dt'].astype(str)
# try pandas to_datetime with mixed formats
parsed = pd.to_datetime(s, errors='coerce', infer_datetime_format=True, utc=False)
# for any remaining NaT, try explicit formats
mask = parsed.isna()
if mask.any():
    fmts = [
        '%d %b %Y, %H:%M',
        '%B %d, %Y at %I:%M %p',
        '%Y-%m-%d %H:%M:%S'
    ]
    alt = pd.Series([pd.NaT]*len(df))
    for fmt in fmts:
        m = mask & alt.isna()
        if not m.any():
            continue
        alt.loc[m] = pd.to_datetime(s.loc[m], format=fmt, errors='coerce')
    parsed = parsed.fillna(alt)

df['date'] = parsed

df = df[df['date'].notna()]
# filter since 2020-01-01
cut = pd.Timestamp('2020-01-01')
df = df[df['date']>=cut]

# Asia indices list from available symbols
asia = ['N225','HSI','TWII','000001.SS','399001.SZ','NSEI']
dfa = df[df['idx'].isin(asia)].copy()

# compute intraday volatility
# avoid division by zero
vol = (dfa['high']-dfa['low'])/dfa['open']
dfa['vol'] = vol
# drop invalid
dfa = dfa.replace([float('inf'), float('-inf')], pd.NA)
dfa = dfa[dfa['vol'].notna() & (dfa['open']>0)]

res = dfa.groupby('idx').agg(avg_intraday_vol=('vol','mean'), days=('vol','size'), start=('date','min'), end=('date','max')).reset_index()
res = res.sort_values('avg_intraday_vol', ascending=False)

out = {
    'top_index': None if res.empty else res.iloc[0].to_dict(),
    'all_asia': res.to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_y0HKbKAhF77GmkFg9E0lzhBe': ['index_info'], 'var_call_igWiGqjt2cl3Id8rPjx1OrCe': ['index_trade'], 'var_call_xTgk9D1HBNe4ZeoDfY3f28S6': [{'idx': 'NYA', 'n': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': 'N225', 'n': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': 'IXIC', 'n': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'idx': 'GSPTSE', 'n': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'idx': 'HSI', 'n': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'idx': 'GDAXI', 'n': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'idx': 'SSMI', 'n': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': 'TWII', 'n': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': '000001.SS', 'n': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'idx': '399001.SZ', 'n': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'idx': 'N100', 'n': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'idx': 'NSEI', 'n': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'idx': 'J203.JO', 'n': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}], 'var_call_rUK9IIMctKLp07ifDSnn4fgl': [{'idx': 'HSI', 'dt': '02 Jan 2020, 00:00', 'open': '28249.36914', 'high': '28543.51953', 'low': '28245.9707'}, {'idx': 'HSI', 'dt': 'January 03, 2020 at 12:00 AM', 'open': '28828.35938', 'high': '28883.30078', 'low': '28428.16992'}, {'idx': 'HSI', 'dt': '06 Jan 2020, 00:00', 'open': '28326.5', 'high': '28367.86914', 'low': '28054.28906'}, {'idx': 'HSI', 'dt': '07 Jan 2020, 00:00', 'open': '28352.67969', 'high': '28473.08008', 'low': '28264.07031'}, {'idx': 'HSI', 'dt': '2020-01-08 00:00:00', 'open': '27999.58008', 'high': '28198.60938', 'low': '27857.73047'}], 'var_call_pIK5gECmA2UBWfU0As9mjVYM': 'file_storage/call_pIK5gECmA2UBWfU0As9mjVYM.json'}

exec(code, env_args)

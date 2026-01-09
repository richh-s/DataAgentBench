code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_rHOm4TrqIGEEetEdhkyV2qMP)
recs = json.loads(path.read_text())
df = pd.DataFrame(recs)

# Parse various date formats
s = df['Date'].astype(str)
dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True, utc=False)
# additional attempts for stubborn formats
mask = dt.isna()
if mask.any():
    dt2 = pd.to_datetime(s[mask], errors='coerce', format='%d %b %Y, %H:%M')
    dt.loc[mask] = dt2
mask = dt.isna()
if mask.any():
    dt3 = pd.to_datetime(s[mask], errors='coerce', format='%B %d, %Y at %I:%M %p')
    dt.loc[mask] = dt3

df['dt'] = dt

df = df[df['dt'].notna()].copy()
df = df[df['dt'] >= pd.Timestamp('2020-01-01')].copy()

for c in ['Open','High','Low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')
df = df.dropna(subset=['Open','High','Low'])
df = df[df['Open'] != 0]

df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

a = df.groupby('Index', as_index=False).agg(avg_intraday_vol=('intraday_vol','mean'), n_days=('intraday_vol','size'))

# Asia indices inference set (major Asia index symbols present)
asia_set = {
    'N225', 'HSI', '000001.SS', '399001.SZ', 'CSI300', 'KS11', 'KQ11', 'TWII', 'BSESN', 'NSEI',
    'JKSE', 'KLSE', 'STI', 'SET.BK', 'PSEI', 'VNINDEX', 'TASI.SR', 'TA125.TA', 'BKPS',
    'AORD', 'AXJO', 'NZ50', 'NZ50.NZ'
}

# Keep only indices in asia_set that actually appear
asia = a[a['Index'].isin(set(asia_set))].copy()

# If asia empty, fallback to include all indices and pick those that match common Asia patterns
if asia.empty:
    asia = a[a['Index'].str.contains(r'(^0{3}|\.SS$|\.SZ$|N225|HSI|KS11|KQ11|TWII|BSESN|NSEI|JKSE|STI|SET|PSEI|VN)', regex=True, na=False)].copy()

asia = asia.sort_values(['avg_intraday_vol','n_days'], ascending=[False, False]).reset_index(drop=True)

top = asia.head(1).to_dict(orient='records')
all_asia_top10 = asia.head(10).to_dict(orient='records')

out = {'top': top, 'top10': all_asia_top10}
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_zGJe9SR2VjYq9qd1C29yGH7p': ['index_trade'], 'var_call_q1qe24ABX2KpWwxCpQFUZFDX': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_rHOm4TrqIGEEetEdhkyV2qMP': 'file_storage/call_rHOm4TrqIGEEetEdhkyV2qMP.json'}

exec(code, env_args)

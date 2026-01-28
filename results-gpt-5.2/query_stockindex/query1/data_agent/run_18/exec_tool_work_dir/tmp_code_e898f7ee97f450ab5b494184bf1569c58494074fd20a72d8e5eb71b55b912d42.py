code = """import json, pandas as pd

path = var_call_iOnNTc7gwZcuXS1az2RdAkqz
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for c in ['Open','High','Low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

def parse_date_series(s: pd.Series) -> pd.Series:
    s = s.astype(str)
    # try vectorized multi-format parsing
    out = pd.to_datetime(s, errors='coerce', format='%Y-%m-%d')
    mask = out.isna()
    if mask.any():
        out.loc[mask] = pd.to_datetime(s[mask], errors='coerce', format='%Y-%m-%d %H:%M:%S')
    mask = out.isna()
    if mask.any():
        out.loc[mask] = pd.to_datetime(s[mask], errors='coerce', format='%d %b %Y, %H:%M')
    mask = out.isna()
    if mask.any():
        out.loc[mask] = pd.to_datetime(s[mask], errors='coerce', format='%B %d, %Y at %I:%M %p')
    # final fallback
    mask = out.isna()
    if mask.any():
        out.loc[mask] = pd.to_datetime(s[mask], errors='coerce')
    return out

df['DateParsed'] = parse_date_series(df['Date'])

df = df.dropna(subset=['DateParsed','Open','High','Low'])
df_2020 = df[df['DateParsed'] >= pd.Timestamp('2020-01-01')].copy()
df_2020['intraday_vol'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

avg_all = df_2020.groupby('Index', as_index=False)['intraday_vol'].mean()

# Asia region mapping based on common index symbols present
asia_indices = {
    'N225','TOPX','HSI','000001.SS','399001.SZ','KS11','KQ11','TWII','STI','SENSEX','BSESN','NSEI','JKSE','SET.BK','KLSE','PSEI','VNINDEX','NZ50','AXJO','AORD'
}
# treat Australia/NZ as Asia-Pacific; include here since prompt says Asia region.

avg_asia = avg_all[avg_all['Index'].isin(asia_indices)].copy()
avg_asia = avg_asia.sort_values('intraday_vol', ascending=False)

best = None
if len(avg_asia) > 0:
    best = avg_asia.iloc[0].to_dict()

top10 = avg_asia.head(10).to_dict(orient='records')

result = {
    'best_asia_index': best,
    'top10_asia_avg_intraday_vol': top10,
    'n_rows_2020_plus': int(len(df_2020)),
    'n_indices_total': int(avg_all.shape[0]),
    'n_indices_asia': int(avg_asia.shape[0])
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_call_cILyUoCRiFxUesA7OOxhKzCV': ['index_info'], 'var_call_QXxxsBRMcomOqXFR2YK6kIEH': ['index_trade'], 'var_call_I4DV0gYldWorcOjsx8gH2mse': [], 'var_call_h1PuRmGMGfnjEiUhNiA70v8l': [{'Date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'Date': '2015-01-16 00:00:00', 'n': '11'}, {'Date': '2017-10-12 00:00:00', 'n': '11'}, {'Date': '2017-06-14 00:00:00', 'n': '10'}, {'Date': 'June 19, 2019 at 12:00 AM', 'n': '10'}], 'var_call_QhFax3b0xGOYROG3wsPOWtmj': {'note': 'need full table scan via SQL with no date cast; will query all rows next'}, 'var_call_iOnNTc7gwZcuXS1az2RdAkqz': 'file_storage/call_iOnNTc7gwZcuXS1az2RdAkqz.json'}

exec(code, env_args)

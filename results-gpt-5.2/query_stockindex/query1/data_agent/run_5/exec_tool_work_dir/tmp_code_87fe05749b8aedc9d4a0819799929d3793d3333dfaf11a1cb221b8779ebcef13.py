code = """import json, pandas as pd

path = var_call_0Q1aLCCHLhnDQAr9I8n9pnuf
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
for c in ['open','high','low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df = df.dropna(subset=['open','high','low'])
df = df[df['open'] != 0]
df['intraday_vol'] = (df['high'] - df['low']) / df['open']

out = (df.groupby('idx')
         .agg(avg_intraday_vol=('intraday_vol','mean'), days=('intraday_vol','size'))
         .reset_index()
         .sort_values('avg_intraday_vol', ascending=False))

result = {
    'top_index': out.iloc[0]['idx'] if len(out) else None,
    'top_avg_intraday_vol': float(out.iloc[0]['avg_intraday_vol']) if len(out) else None,
    'ranking': [
        {'index': r.idx, 'avg_intraday_vol': float(r.avg_intraday_vol), 'days': int(r.days)}
        for r in out.itertuples(index=False)
    ]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TNZzkoDMs5rTuyjR5LIAzWOO': ['index_info'], 'var_call_R0rwZxNQSSesR015YCiLaPYb': ['index_trade'], 'var_call_Z3bvjmTwtLAjmyFhPLPbJrjR': [{'idx': 'NYA', 'n': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': 'N225', 'n': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': 'IXIC', 'n': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'idx': 'GSPTSE', 'n': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'idx': 'HSI', 'n': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'idx': 'GDAXI', 'n': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'idx': 'SSMI', 'n': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': 'TWII', 'n': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': '000001.SS', 'n': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'idx': '399001.SZ', 'n': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'idx': 'N100', 'n': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'idx': 'NSEI', 'n': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'idx': 'J203.JO', 'n': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}], 'var_call_ZolA3RJUuWzbnU2A4cmWrcII': {'asia_indices': ['N225', 'HSI', 'TWII', '000001.SS', '399001.SZ', 'NSEI']}, 'var_call_0Q1aLCCHLhnDQAr9I8n9pnuf': 'file_storage/call_0Q1aLCCHLhnDQAr9I8n9pnuf.json'}

exec(code, env_args)

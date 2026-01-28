code = """import json
import pandas as pd
p = var_call_OB6CtypAhUNNBw90diU0nIjS
# p is a path to a JSON file containing a list of records
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
# build DataFrame
df = pd.DataFrame(data)
# keep necessary columns
cols = ['Index','Date','Open','High','Low']
for c in cols:
    if c not in df.columns:
        df[c] = None
# convert numeric columns
for c in ['Open','High','Low']:
    df[c] = pd.to_numeric(df[c], errors='coerce')
# parse dates with multiple formats
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# filter from 2020-01-01
df = df[df['Date_parsed'] >= pd.to_datetime('2020-01-01')].copy()
# compute intraday volatility
# avoid division by zero or missing
df = df[df['Open'].notna() & (df['Open'] != 0) & df['High'].notna() & df['Low'].notna()]
if df.empty:
    result = {'error': 'No valid data on or after 2020-01-01 for selected indices.'}
else:
    df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']
    grp = df.groupby('Index').agg(avg_vol=('intraday_vol','mean'), days=('intraday_vol','count'))
    grp = grp.reset_index()
    # round values for readability
    grp['avg_vol'] = grp['avg_vol'].round(6)
    # find top
    top = grp.loc[grp['avg_vol'].idxmax()].to_dict()
    # prepare by_index list
    by_index = []
    for _, row in grp.sort_values('avg_vol', ascending=False).iterrows():
        by_index.append({'Index': row['Index'], 'avg_vol': float(row['avg_vol']), 'days': int(row['days'])})
    result = {
        'top_index': top['Index'],
        'top_avg_vol': float(round(top['avg_vol'],6)),
        'top_days': int(top['days']),
        'by_index': by_index
    }
# print in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HbHhLUtHACgs6DSJyRFu78w6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_call_OB6CtypAhUNNBw90diU0nIjS': 'file_storage/call_OB6CtypAhUNNBw90diU0nIjS.json'}

exec(code, env_args)

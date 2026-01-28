code = """import json, pandas as pd
from datetime import datetime

# load full trade data
path = var_call_iRrPT696eUNg4CHs1b9xVEVY
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# coerce types
# parse dates with multiple formats
s = df['date_str'].astype(str)
dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
# second pass for remaining using dayfirst
mask = dt.isna()
if mask.any():
    dt2 = pd.to_datetime(s[mask], errors='coerce', dayfirst=True)
    dt.loc[mask] = dt2

df['date'] = dt
# drop unparsed
df = df.dropna(subset=['date'])
# close_usd to numeric
for col in ['close_usd']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df = df.dropna(subset=['close_usd'])

# filter since 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['date'] >= start]

# monthly investment: take last available CloseUSD each month per index
# compute month-end prices
m = df.copy()
m['month'] = m['date'].dt.to_period('M')
# sort then take last row per (idx, month)
m = m.sort_values(['idx','date'])
month_end = m.groupby(['idx','month'], as_index=False).last()[['idx','month','close_usd']]

# compute units bought each month with $1 contribution
month_end = month_end.sort_values(['idx','month'])
month_end['units'] = 1.0 / month_end['close_usd']

# total units and final value
units = month_end.groupby('idx', as_index=False)['units'].sum().rename(columns={'units':'total_units'})
last_price = month_end.groupby('idx', as_index=False).last()[['idx','close_usd']].rename(columns={'close_usd':'final_price'})
contrib = month_end.groupby('idx', as_index=False).size().rename(columns={'size':'n_months'})
res = units.merge(last_price, on='idx').merge(contrib, on='idx')
res['total_contrib'] = res['n_months'] * 1.0
res['final_value'] = res['total_units'] * res['final_price']
res['return_multiple'] = res['final_value'] / res['total_contrib']

# top 5
res_top = res.sort_values('return_multiple', ascending=False).head(5)

out = res_top.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mDw1PeDJjctMJQvNV8fEvDIt': ['index_info'], 'var_call_pxFG50wxbkS7NkR790Pj3f6U': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_xMo6m1gtLRnYmkFh6atDV50O': [{'idx': 'J203.JO', 'sample_date': '01 Apr 2016, 00:00'}, {'idx': 'N225', 'sample_date': '01 Apr 1971, 00:00'}, {'idx': 'GSPTSE', 'sample_date': '01 Apr 1981, 00:00'}, {'idx': 'NSEI', 'sample_date': '01 Apr 2014, 00:00'}, {'idx': 'GDAXI', 'sample_date': '01 Apr 1992, 00:00'}], 'var_call_53Pj6MB9VCiwEG0TdmCYxswY': [{'idx': 'J203.JO', 'min_date_str': '01 Apr 2016, 00:00', 'max_date_str': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'idx': 'N225', 'min_date_str': '01 Apr 1971, 00:00', 'max_date_str': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'idx': 'GSPTSE', 'min_date_str': '01 Apr 1981, 00:00', 'max_date_str': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'idx': 'NSEI', 'min_date_str': '01 Apr 2014, 00:00', 'max_date_str': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'idx': 'GDAXI', 'min_date_str': '01 Apr 1992, 00:00', 'max_date_str': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'idx': 'IXIC', 'min_date_str': '01 Apr 1974, 00:00', 'max_date_str': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'idx': 'HSI', 'min_date_str': '01 Apr 1992, 00:00', 'max_date_str': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'idx': 'NYA', 'min_date_str': '01 Apr 1969, 00:00', 'max_date_str': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'idx': 'N100', 'min_date_str': '01 Apr 2003, 00:00', 'max_date_str': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'idx': '399001.SZ', 'min_date_str': '01 Apr 2004, 00:00', 'max_date_str': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'idx': '000001.SS', 'min_date_str': '01 Apr 2003, 00:00', 'max_date_str': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'idx': 'SSMI', 'min_date_str': '01 Apr 1996, 00:00', 'max_date_str': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'idx': 'TWII', 'min_date_str': '01 Apr 2004, 00:00', 'max_date_str': 'September 30, 2020 at 12:00 AM', 'n': '5869'}], 'var_call_iRrPT696eUNg4CHs1b9xVEVY': 'file_storage/call_iRrPT696eUNg4CHs1b9xVEVY.json'}

exec(code, env_args)

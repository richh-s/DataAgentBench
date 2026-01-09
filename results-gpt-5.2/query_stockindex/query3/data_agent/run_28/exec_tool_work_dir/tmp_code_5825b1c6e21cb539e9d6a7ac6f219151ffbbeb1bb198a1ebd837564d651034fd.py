code = """import json, pandas as pd
from datetime import datetime

# Load trade data
path = var_call_11KL8JFtCoJ6y0Mr6r5YGYvE
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# Ensure numeric
df['close_usd'] = pd.to_numeric(df['close_usd'], errors='coerce')

# Parse mixed date formats
s = df['dt_str'].astype(str)
parsed = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
# Handle formats like '31 Dec 1986, 00:00'
mask = parsed.isna()
if mask.any():
    parsed2 = pd.to_datetime(s[mask], format='%d %b %Y, %H:%M', errors='coerce')
    parsed.loc[mask] = parsed2
mask = parsed.isna()
if mask.any():
    parsed3 = pd.to_datetime(s[mask], format='%B %d, %Y at %I:%M %p', errors='coerce')
    parsed.loc[mask] = parsed3

df['date'] = parsed
# Filter since 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['date'] >= start].dropna(subset=['date','close_usd'])

# Monthly DCA: invest 1 unit on first available trading day each month
# For each index-month pick earliest date
m = df['date'].dt.to_period('M')
df['month'] = m

df = df.sort_values(['idx','date'])
first_in_month = df.groupby(['idx','month'], as_index=False).first()

# Compute units purchased each month with $1 contribution: 1/price
first_in_month['units'] = 1.0 / first_in_month['close_usd']

# Total contributions and final value at last available date
last_price = df.sort_values(['idx','date']).groupby('idx', as_index=False).last()[['idx','close_usd','date']]
last_price = last_price.rename(columns={'close_usd':'last_close_usd','date':'last_date'})

agg = first_in_month.groupby('idx').agg(total_units=('units','sum'), n_months=('units','size')).reset_index()
res = agg.merge(last_price, on='idx', how='inner')
res['total_contrib'] = res['n_months'] * 1.0
res['final_value'] = res['total_units'] * res['last_close_usd']
res['multiple'] = res['final_value'] / res['total_contrib']

# Keep indices with reasonable coverage: at least 12 months since 2000
res = res[res['n_months'] >= 12]
res = res.sort_values('multiple', ascending=False)

top5 = res.head(5)

out = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_uXuq4qv02TuJJavjKbWSQ6G4': ['index_info'], 'var_call_M1WhtKD8xs0zZl3xi1fo04du': ['index_trade'], 'var_call_SEDHzV7YneXG9Z27iO20DeVG': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}, {'Date': '02 Feb 1987, 00:00'}, {'Date': '03 Feb 1987, 00:00'}, {'Date': 'February 04, 1987 at 12:00 AM'}, {'Date': 'February 05, 1987 at 12:00 AM'}, {'Date': '06 Feb 1987, 00:00'}, {'Date': '1987-02-09 00:00:00'}, {'Date': '1987-02-10 00:00:00'}, {'Date': '11 Feb 1987, 00:00'}, {'Date': '12 Feb 1987, 00:00'}, {'Date': 'February 13, 1987 at 12:00 AM'}, {'Date': '16 Feb 1987, 00:00'}, {'Date': 'February 17, 1987 at 12:00 AM'}, {'Date': 'February 18, 1987 at 12:00 AM'}, {'Date': '19 Feb 1987, 00:00'}, {'Date': '1987-02-20 00:00:00'}, {'Date': 'February 23, 1987 at 12:00 AM'}, {'Date': '24 Feb 1987, 00:00'}, {'Date': 'February 25, 1987 at 12:00 AM'}, {'Date': '26 Feb 1987, 00:00'}, {'Date': '27 Feb 1987, 00:00'}, {'Date': '1987-03-02 00:00:00'}, {'Date': '1987-03-03 00:00:00'}, {'Date': '1987-03-04 00:00:00'}, {'Date': 'March 05, 1987 at 12:00 AM'}, {'Date': 'March 06, 1987 at 12:00 AM'}, {'Date': '09 Mar 1987, 00:00'}, {'Date': 'March 10, 1987 at 12:00 AM'}, {'Date': '11 Mar 1987, 00:00'}, {'Date': '12 Mar 1987, 00:00'}, {'Date': 'March 13, 1987 at 12:00 AM'}], 'var_call_11KL8JFtCoJ6y0Mr6r5YGYvE': 'file_storage/call_11KL8JFtCoJ6y0Mr6r5YGYvE.json'}

exec(code, env_args)

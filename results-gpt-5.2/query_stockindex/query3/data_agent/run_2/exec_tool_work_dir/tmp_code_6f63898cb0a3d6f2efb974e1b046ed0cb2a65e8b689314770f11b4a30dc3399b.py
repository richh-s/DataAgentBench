code = """import json, pandas as pd
from datetime import datetime

# load data
path = var_call_VMs9upOC3FtkUv9AeWmASaVZ
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# ensure numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# robust date parsing
s = df['Date'].astype(str)
# normalize common patterns
s = s.str.replace(' at 12:00 AM', '', regex=False)
# try parse
dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
# for any remaining NaT, try a second pass with dayfirst
mask = dt.isna()
if mask.any():
    dt2 = pd.to_datetime(s[mask], errors='coerce', dayfirst=True, infer_datetime_format=True)
    dt.loc[mask] = dt2

df['dt'] = dt

df = df.dropna(subset=['dt','CloseUSD'])
df = df[df['dt'] >= pd.Timestamp('2000-01-01')]

# month end close per index
# use last trading day close in each month
month = df['dt'].dt.to_period('M').dt.to_timestamp()
df['month'] = month

df_sorted = df.sort_values(['Index','dt'])
monthly_close = df_sorted.groupby(['Index','month'], as_index=False).tail(1)[['Index','month','CloseUSD']]

# compute growth factor from first to last month (equivalent to product of monthly returns)
monthly_close = monthly_close.sort_values(['Index','month'])
first_last = monthly_close.groupby('Index').agg(first=('CloseUSD','first'), last=('CloseUSD','last'), n_months=('CloseUSD','size')).reset_index()
first_last['growth_factor'] = first_last['last'] / first_last['first']

# top 5
out = first_last.sort_values('growth_factor', ascending=False).head(5)
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_idocMYDPNBzOs3BZu1QIaATA': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_7gYZlJs80bw859XOXlXbtOM2': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_VMs9upOC3FtkUv9AeWmASaVZ': 'file_storage/call_VMs9upOC3FtkUv9AeWmASaVZ.json'}

exec(code, env_args)

code = """import json, pandas as pd

path = var_call_rqHvRuDwpKtyFL9J5btUXuOf
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates robustly
from datetime import datetime

def parse_date(s):
    for fmt in ['%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p', '%Y-%m-%d %H:%M:%S']:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    raise ValueError(f'No format for {s}')

df['dt'] = df['Date'].apply(parse_date)

# Filter from 2000-01-01
start = datetime(2000,1,1)
df = df[df['dt'] >= start].copy()

# Ensure numeric
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# Monthly investments: first trading day each month per index
df['month'] = df['dt'].dt.to_period('M')
first_per_month = df.sort_values('dt').groupby(['Index','month']).head(1)

# Assume 1000 per month
first_per_month['units'] = 1000.0 / first_per_month['Adj Close']

agg = first_per_month.groupby('Index').agg(total_units=('units','sum'), n_months=('units','size')).reset_index()

# Latest price per index
latest = df.sort_values('dt').groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'latest_price'})

res = agg.merge(latest, on='Index')
res['final_value'] = res['total_units'] * res['latest_price']
res['total_invested'] = res['n_months'] * 1000.0
res['total_return'] = res['final_value'] / res['total_invested'] - 1

res_top5 = res.sort_values('total_return', ascending=False).head(5)

out = res_top5[['Index','total_return']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cx9nXsyOqv0eJYdTSoQhKUEb': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}], 'var_call_U7TB7A9YFvztdK8LP6S0mjwp': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_bD26yEcy1tMtmrgyyYVjHEAn': ['index_info'], 'var_call_J1FVImMusqw1gdgHJ01nG2UE': [{'sample': '07 '}, {'sample': '200'}, {'sample': 'May'}, {'sample': '11 '}, {'sample': '01 '}, {'sample': '23 '}, {'sample': 'Aug'}, {'sample': '196'}, {'sample': 'Jan'}, {'sample': '198'}], 'var_call_GrOvUcaO1PSYKPwnZpfY8bv1': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_rqHvRuDwpKtyFL9J5btUXuOf': 'file_storage/call_rqHvRuDwpKtyFL9J5btUXuOf.json'}

exec(code, env_args)

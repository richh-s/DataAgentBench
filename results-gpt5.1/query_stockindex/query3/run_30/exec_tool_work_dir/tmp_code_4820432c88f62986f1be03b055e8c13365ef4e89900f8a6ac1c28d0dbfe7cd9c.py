code = """import pandas as pd, json
from datetime import datetime

path = var_call_bbyz6LHOIPCRgBq2eWuc6OKq
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# normalize date
def parse_date(s):
    for fmt in ['%d %b %Y, %H:%M', '%d %b %Y, %H:%M', '%d %b %Y, %H:%M', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    try:
        return pd.to_datetime(s, errors='coerce')
    except Exception:
        return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)

# filter from 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['Date_parsed'] >= start]

# ensure numeric CloseUSD
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# monthly DCA: assume invest 1 unit USD each month at first trading day of month per index
# find first trading day per month per index

df['YearMonth'] = df['Date_parsed'].dt.to_period('M')
first_day_idx = df.sort_values(['Index','Date_parsed']).groupby(['Index','YearMonth']).head(1)

# number of units bought each month = 1 / CloseUSD
first_day_idx['units'] = 1.0 / first_day_idx['CloseUSD']

# sum units and take last price per index
units_per_index = first_day_idx.groupby('Index')['units'].sum().reset_index()

last_price = df.sort_values(['Index','Date_parsed']).groupby('Index').tail(1)[['Index','CloseUSD']]
last_price = last_price.rename(columns={'CloseUSD':'last_CloseUSD'})

res = pd.merge(units_per_index, last_price, on='Index')
res['final_value'] = res['units'] * res['last_CloseUSD']
res = res.sort_values('final_value', ascending=False).head(5)

result = res[['Index','final_value']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mzRE8aq6TOn47pFH13gs2dn1': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_BW1KgHwQWYLtK2zP6lxmu3bJ': [{'Index': 'J203.JO'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_bbyz6LHOIPCRgBq2eWuc6OKq': 'file_storage/call_bbyz6LHOIPCRgBq2eWuc6OKq.json'}

exec(code, env_args)

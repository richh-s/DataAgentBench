code = """import pandas as pd, json
from datetime import datetime

# load full large result
import os, json as jsonlib
path = var_call_TTlJdNUIarL3rqnWcnV9duZQ
with open(path, 'r') as f:
    data = jsonlib.load(f)

df = pd.DataFrame(data)

# normalize date
def parse_date(s):
    for fmt in ["%d %b %Y, %H:%M", "%B %d, %Y at %I:%M %p", "%Y-%m-%d"]:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date'] = df['Date'].apply(parse_date)

# filter from 2000-01-01
start = datetime(2000,1,1)
df = df[df['Date']>=start]

# ensure numeric
for col in ['Adj Close','CloseUSD']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# create year-month for monthly investing
df['ym'] = df['Date'].dt.to_period('M')

# assume invest 1 unit of currency each month, using first available trading day of month
first_month_day = df.sort_values('Date').groupby(['Index','ym']).first().reset_index()

# compute units bought per month based on CloseUSD
first_month_day['units'] = 1.0 / first_month_day['CloseUSD']

# total units and final value per index
latest = df.sort_values('Date').groupby('Index').tail(1)[['Index','CloseUSD']].set_index('Index')
agg = first_month_day.groupby('Index')['units'].sum().to_frame('total_units')
res = agg.join(latest, how='inner')
res['final_value'] = res['total_units'] * res['CloseUSD']

# pick top 5 indices
top5 = res.sort_values('final_value', ascending=False).head(5)

result = top5.reset_index().to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uLUpe9RbaKA2HlPynXLvNPHw': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}], 'var_call_TTlJdNUIarL3rqnWcnV9duZQ': 'file_storage/call_TTlJdNUIarL3rqnWcnV9duZQ.json'}

exec(code, env_args)

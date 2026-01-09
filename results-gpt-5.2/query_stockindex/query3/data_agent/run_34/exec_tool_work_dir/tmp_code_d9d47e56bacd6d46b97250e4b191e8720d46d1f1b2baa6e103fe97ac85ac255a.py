code = """import json, pandas as pd
from datetime import datetime

path = var_call_dpuvcPccQaymeGPOROpcMOiA
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# parse dates in two known formats
s = df['Date'].astype(str)
dt1 = pd.to_datetime(s, format='%d %b %Y, %H:%M', errors='coerce')
dt2 = pd.to_datetime(s, format='%B %d, %Y at %I:%M %p', errors='coerce')
df['dt'] = dt1.fillna(dt2)
df = df.dropna(subset=['dt'])

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# monthly contribution simulation: invest 1 unit USD on first trading day of each month
# shares bought = 1 / CloseUSD
# final value = total shares * last CloseUSD; total invested = num_months

df['month'] = df['dt'].dt.to_period('M')
# first trading day per index-month
first = df.sort_values('dt').groupby(['Index','month'], as_index=False).first()[['Index','month','CloseUSD']]
first = first.rename(columns={'CloseUSD':'buy_price'})
shares = first.assign(shares=1.0/first['buy_price']).groupby('Index', as_index=False).agg(months=('shares','size'), total_shares=('shares','sum'))

last = df.sort_values('dt').groupby('Index', as_index=False).last()[['Index','CloseUSD','dt']].rename(columns={'CloseUSD':'last_price','dt':'last_dt'})
res = shares.merge(last, on='Index', how='inner')
res['final_value'] = res['total_shares'] * res['last_price']
res['total_invested'] = res['months'] * 1.0
res['return_multiple'] = res['final_value'] / res['total_invested']
res = res.sort_values('return_multiple', ascending=False)

# top 5
out = res.head(5)[['Index','return_multiple','months','last_dt']]
out['return_multiple'] = out['return_multiple'].round(6)
out['last_dt'] = out['last_dt'].dt.strftime('%Y-%m-%d')

print('__RESULT__:')
print(out.to_json(orient='records'))"""

env_args = {'var_call_I3GA65myriws3fN22g6de269': ['index_info'], 'var_call_vsEUnteGtULYALcrd1eL5dL1': ['index_trade'], 'var_call_PSPcRSNzr4WJP46HFvE1NFxm': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}], 'var_call_dpuvcPccQaymeGPOROpcMOiA': 'file_storage/call_dpuvcPccQaymeGPOROpcMOiA.json'}

exec(code, env_args)

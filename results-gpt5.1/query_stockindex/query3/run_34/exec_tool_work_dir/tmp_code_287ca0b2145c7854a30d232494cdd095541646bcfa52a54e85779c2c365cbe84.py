code = """import pandas as pd, json
import os

file_path = var_call_tTvJMVrHvWF7qSqcNLlYLLQp
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize date formats and filter from 2000-01-01
from datetime import datetime

def parse_date(s):
    for fmt in ['%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p', '%Y-%m-%d']:
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    return None

df['Date_parsed'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['Date_parsed'])

start = datetime(2000,1,1)
monthly = df[df['Date_parsed']>=start].copy()

# Convert CloseUSD to float
monthly['CloseUSD'] = monthly['CloseUSD'].astype(float)

# Take month-end close for each index-month
monthly['year_month'] = monthly['Date_parsed'].dt.to_period('M')
idx = monthly.sort_values('Date_parsed').groupby(['Index','year_month']).tail(1)

# Assume invest 1 USD at each month-end
idx['contribution'] = 1.0

# number of units bought each month
idx['units'] = idx['contribution']/idx['CloseUSD']

# Final price per index (latest CloseUSD available)
latest = monthly.sort_values('Date_parsed').groupby('Index').tail(1)[['Index','CloseUSD']].rename(columns={'CloseUSD':'final_price'})

agg = idx.groupby('Index').agg(total_units=('units','sum'), total_contrib=('contribution','sum')).reset_index()
res = agg.merge(latest, on='Index')
res['final_value'] = res['total_units']*res['final_price']
res['return_multiple'] = res['final_value']/res['total_contrib']

res_top5 = res.sort_values('return_multiple', ascending=False).head(5)[['Index','return_multiple']]

result = res_top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_H1r238jzfjDLlAuq8HAZTAHw': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}], 'var_call_YNd30BkiIAH0CCMVpcuOVIwW': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_tTvJMVrHvWF7qSqcNLlYLLQp': 'file_storage/call_tTvJMVrHvWF7qSqcNLlYLLQp.json'}

exec(code, env_args)

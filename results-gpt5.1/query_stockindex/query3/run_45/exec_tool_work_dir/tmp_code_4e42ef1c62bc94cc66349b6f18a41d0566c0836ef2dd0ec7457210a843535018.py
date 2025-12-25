code = """import json, pandas as pd

file_path = var_call_8RCKuXiq2CzlfbxNiCWEzvEk
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# normalize date
df['Date'] = pd.to_datetime(df['Date'])

# filter from 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# create year-month column
df['ym'] = df['Date'].dt.to_period('M')

# assume monthly investing at last available trading day each month
last_day = df.sort_values(['Index','Date']).groupby(['Index','ym']).tail(1)

# sort for consistent ordering
last_day = last_day.sort_values(['Index','Date'])

# for each index, simulate investing 1 unit of currency per month using CloseUSD
results = []
for idx, grp in last_day.groupby('Index'):
    prices = grp['CloseUSD'].astype(float)
    # number of units bought each month with 1 USD
    units = 1.0 / prices
    total_units = units.sum()
    final_price = prices.iloc[-1]
    final_value = total_units * final_price
    results.append({'Index': idx, 'final_value': float(final_value), 'months': len(prices)})

res_df = pd.DataFrame(results)
res_df = res_df[res_df['months'] >= 12]

top5 = res_df.sort_values('final_value', ascending=False).head(5)

result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kIfssoa90knPgNfkcoZGm0VC': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}], 'var_call_8RCKuXiq2CzlfbxNiCWEzvEk': 'file_storage/call_8RCKuXiq2CzlfbxNiCWEzvEk.json'}

exec(code, env_args)

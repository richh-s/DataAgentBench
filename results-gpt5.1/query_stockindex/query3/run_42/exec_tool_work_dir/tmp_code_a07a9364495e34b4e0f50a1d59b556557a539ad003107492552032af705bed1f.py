code = """import json, pandas as pd, os

path = var_call_3OAeTR0zT2TjCfDp3jjAH48w
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# parse dates more robustly
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# ensure numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

monthly = df.sort_values(['Index','Date']).groupby('Index').resample('M', on='Date').last().reset_index()

results = []
for idx, g in monthly.groupby('Index'):
    g = g.sort_values('Date')
    n_months = g.shape[0]
    if n_months == 0:
        continue
    monthly_units = 1.0 / g['CloseUSD']
    total_units = monthly_units.sum()
    final_price = g['CloseUSD'].iloc[-1]
    final_value = total_units * final_price
    total_invested = n_months * 1.0
    mult = final_value / total_invested
    results.append({'Index': idx, 'n_months': int(n_months), 'multiplier': float(mult)})

res_df = pd.DataFrame(results)
res_df = res_df[res_df['n_months'] >= 12]
res_df = res_df.sort_values('multiplier', ascending=False).head(5)

result = res_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6S7MqV3wrFRgTiOlagvKxj0L': [{'Index': 'J203.JO', 'first_date': '2012-02-08 00:00:00'}, {'Index': 'N225', 'first_date': '2000-01-04 00:00:00'}, {'Index': 'GSPTSE', 'first_date': '2000-01-05 00:00:00'}, {'Index': 'NSEI', 'first_date': '2007-09-25 00:00:00'}, {'Index': 'GDAXI', 'first_date': '2000-01-05 00:00:00'}, {'Index': 'IXIC', 'first_date': '2000-01-06 00:00:00'}, {'Index': 'HSI', 'first_date': '2000-01-14 00:00:00'}, {'Index': 'NYA', 'first_date': '2000-01-03 00:00:00'}, {'Index': '000001.SS', 'first_date': '2000-01-04 00:00:00'}, {'Index': 'SSMI', 'first_date': '2000-01-05 00:00:00'}, {'Index': 'TWII', 'first_date': '2000-01-17 00:00:00'}, {'Index': 'N100', 'first_date': '2000-01-10 00:00:00'}, {'Index': '399001.SZ', 'first_date': '2000-01-05 00:00:00'}], 'var_call_IT1Dx5oyIropEEkWSMvc2Lre': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_WCgoLG7ZlJSkD6XcUpuZwiuX': ['index_info'], 'var_call_3OAeTR0zT2TjCfDp3jjAH48w': 'file_storage/call_3OAeTR0zT2TjCfDp3jjAH48w.json'}

exec(code, env_args)

code = """import json, pandas as pd, os

path = var_call_4wfJrAK3CwF5zrtCqikVocq3
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ensure proper dtypes
# Date may have different formats, let pandas infer and errors coerce
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=False, infer_datetime_format=True)
df = df.dropna(subset=['Date'])

df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Adj Close'])

monthly = df[df['Date']>=pd.Timestamp('2000-01-01')].copy()
monthly['YearMonth'] = monthly['Date'].dt.to_period('M')
last_days = monthly.sort_values('Date').groupby(['Index','YearMonth']).tail(1)

results = []
for idx, group in last_days.groupby('Index'):
    group = group.sort_values('Date')
    prices = group['Adj Close'].values
    if len(prices)==0:
        continue
    units = 1.0 / prices
    total_units = units.sum()
    final_price = df[df['Index']==idx].sort_values('Date')['Adj Close'].iloc[-1]
    final_value = total_units * final_price
    total_invested = float(len(prices))
    results.append({'Index': idx, 'months': int(len(prices)), 'final_value': float(final_value), 'total_invested': total_invested, 'multiple': float(final_value/total_invested)})

res_df = pd.DataFrame(results)
res_df = res_df[res_df['months']>=12]

top5 = res_df.sort_values('multiple', ascending=False).head(5)

result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_gLf2MlplCVu0BzgBt38hPREj': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}], 'var_call_mIUGaKT1kVQDukM45msrOfeE': [], 'var_call_4wfJrAK3CwF5zrtCqikVocq3': 'file_storage/call_4wfJrAK3CwF5zrtCqikVocq3.json'}

exec(code, env_args)

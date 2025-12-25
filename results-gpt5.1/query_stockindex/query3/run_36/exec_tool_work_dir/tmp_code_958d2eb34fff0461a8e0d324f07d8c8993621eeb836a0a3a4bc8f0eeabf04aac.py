code = """import pandas as pd, json

first_dates = pd.DataFrame(var_call_v4PxtGKCojOKYKfWyFONqgoe)
eligible = set(first_dates.loc[pd.to_datetime(first_dates['first_date'], errors='coerce') <= pd.Timestamp('2000-01-31'), 'Index'])

import os, json as js
path = var_call_80r0wJ0C7A5X03y0omvCz3D1
with open(path, 'r') as f:
    data = js.load(f)

trade = pd.DataFrame(data)
trade['Date'] = pd.to_datetime(trade['Date'], errors='coerce')
trade = trade[trade['Date'] >= pd.Timestamp('2000-01-01')]
trade = trade[trade['Index'].isin(eligible)]
trade['Adj Close'] = pd.to_numeric(trade['Adj Close'], errors='coerce')
trade = trade.dropna(subset=['Adj Close'])

trade['year_month'] = trade['Date'].dt.to_period('M')

monthly_last = trade.sort_values(['Index','Date']).groupby(['Index','year_month']).tail(1)

monthly_last['units'] = 1.0 / monthly_last['Adj Close']
monthly_last['cum_units'] = monthly_last.groupby('Index')['units'].cumsum()

final_prices = trade.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']].set_index('Index')['Adj Close']

results = []
for idx, grp in monthly_last.groupby('Index'):
    total_invested = grp.shape[0] * 1.0
    final_price = final_prices.get(idx)
    if pd.isna(final_price):
        continue
    total_units = grp['cum_units'].iloc[-1]
    final_value = total_units * final_price
    results.append({'Index': idx, 'total_invested': total_invested, 'final_value': final_value, 'multiple': final_value/total_invested})

res_df = pd.DataFrame(results).sort_values('multiple', ascending=False).head(5)

print('__RESULT__:')
print(res_df.to_json(orient='records'))"""

env_args = {'var_call_v4PxtGKCojOKYKfWyFONqgoe': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}], 'var_call_80r0wJ0C7A5X03y0omvCz3D1': 'file_storage/call_80r0wJ0C7A5X03y0omvCz3D1.json'}

exec(code, env_args)

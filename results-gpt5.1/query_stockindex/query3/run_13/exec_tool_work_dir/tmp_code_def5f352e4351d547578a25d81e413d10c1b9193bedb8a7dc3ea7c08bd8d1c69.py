code = """import json, pandas as pd

first_dates = pd.DataFrame(var_call_3Y6bMoMBFcVvyJ6ZvVCIxxQB)

# Parse first_date with dayfirst since it's like '01 Apr 2016, 00:00'
first_dates['first_date'] = pd.to_datetime(first_dates['first_date'], dayfirst=True)

# Load full price data
file_path = var_call_zIaVXr5Z4ihq7bF5grl1RnYl
with open(file_path, 'r') as f:
    data = json.load(f)
prices = pd.DataFrame(data)

prices['Adj Close'] = prices['Adj Close'].astype(float)
prices['Date'] = pd.to_datetime(prices['Date'])

monthly_first = prices.sort_values(['Index','Date']).groupby(['Index', prices['Date'].dt.to_period('M')]).head(1)
monthly_first['units'] = 1.0 / monthly_first['Adj Close']

last_price = prices.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'final_price'})

units_sum = monthly_first.groupby('Index')['units'].sum().reset_index()

res = units_sum.merge(last_price, on='Index')

counts = monthly_first.groupby('Index').size().reset_index(name='n_contributions')
res = res.merge(counts, on='Index')

res['total_invested'] = res['n_contributions'] * 1.0
res['return_multiple'] = res['final_value'] = res['units'] * res['final_price'] / res['total_invested']

eligible = first_dates[first_dates['first_date'] <= '2000-01-31']['Index']
res_eligible = res[res['Index'].isin(eligible)]

top5 = res_eligible.sort_values('return_multiple', ascending=False).head(5)

result = top5[['Index','return_multiple']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3Y6bMoMBFcVvyJ6ZvVCIxxQB': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}], 'var_call_zIaVXr5Z4ihq7bF5grl1RnYl': 'file_storage/call_zIaVXr5Z4ihq7bF5grl1RnYl.json', 'var_call_aScodSb4bAdOWNmfrJT8dya4': ['index_info']}

exec(code, env_args)

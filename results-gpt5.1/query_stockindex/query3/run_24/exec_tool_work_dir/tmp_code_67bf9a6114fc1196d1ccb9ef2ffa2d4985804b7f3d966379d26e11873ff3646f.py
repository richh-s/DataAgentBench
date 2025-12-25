code = """import pandas as pd, json
import os

first_dates = pd.DataFrame(var_call_dpoBLmCP6iCaYo89GII36R6J)
path = var_call_x1ESuqQK0mYOX2tphrSaVYvS
full = pd.read_json(path)

full['Date'] = pd.to_datetime(full['Date']).dt.to_period('M')

start = pd.Timestamp('2000-01-01')

monthly = full.groupby(['Index','Date'])['Adj Close'].last().reset_index()

results = []
for idx, g in monthly.groupby('Index'):
    g = g.sort_values('Date')
    # assume invest 1 unit of currency each month, shares = 1 / price
    shares = (1.0 / g['Adj Close']).values
    prices = g['Adj Close'].values
    total_invested = len(g)
    total_shares = shares.sum()
    final_value = total_shares * prices[-1]
    total_return = (final_value - total_invested) / total_invested
    results.append({'Index': idx, 'months': len(g), 'total_return': total_return})

res_df = pd.DataFrame(results)

# keep indices that have data starting in or before Jan 2000
monthly_first = monthly.groupby('Index')['Date'].min().reset_index()
monthly_first['Date_ts'] = monthly_first['Date'].dt.to_timestamp()
eligible = monthly_first[monthly_first['Date_ts'] <= start]['Index']

eligible_res = res_df[res_df['Index'].isin(eligible)]

top5 = eligible_res.sort_values('total_return', ascending=False).head(5)

out = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_dpoBLmCP6iCaYo89GII36R6J': [{'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}], 'var_call_x1ESuqQK0mYOX2tphrSaVYvS': 'file_storage/call_x1ESuqQK0mYOX2tphrSaVYvS.json'}

exec(code, env_args)

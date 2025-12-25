code = """import json, pandas as pd

with open(var_call_iucLrIi0nC2h6lUZYZjEgA3t, 'r') as f:
    data = json.load(f)

prices = pd.DataFrame(data)
prices['Adj Close'] = prices['Adj Close'].astype(float)

# custom date parser to handle inconsistent formats
prices['Date'] = pd.to_datetime(prices['Date'], errors='coerce', dayfirst=False, infer_datetime_format=True)
prices = prices.dropna(subset=['Date'])
prices = prices[prices['Date'] >= '2000-01-01']

prices['YearMonth'] = prices['Date'].dt.to_period('M')
first_monthly = prices.sort_values('Date').groupby(['Index','YearMonth']).first().reset_index()

latest = prices.sort_values('Date').groupby('Index').last().reset_index()[['Index','Adj Close']].rename(columns={'Adj Close':'FinalPrice'})

merged = first_monthly.merge(latest, on='Index', how='left')
merged['UnitsBought'] = 1.0 / merged['Adj Close']
merged['FinalValue'] = merged['UnitsBought'] * merged['FinalPrice']

summary = merged.groupby('Index').agg(
    total_invested=('FinalValue', 'size'),
    final_portfolio=('FinalValue', 'sum')
).reset_index()
summary['total_invested'] = summary['total_invested'].astype(float)
summary['return_multiple'] = summary['final_portfolio'] / summary['total_invested']

Top5 = summary.sort_values('return_multiple', ascending=False).head(5)

print('__RESULT__:')
print(json.dumps(Top5.to_dict(orient='records')))"""

env_args = {'var_call_qeWPkxhYbGpyKv8AEq98ZzMo': [{'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}], 'var_call_iucLrIi0nC2h6lUZYZjEgA3t': 'file_storage/call_iucLrIi0nC2h6lUZYZjEgA3t.json'}

exec(code, env_args)

code = """import pandas as pd, json

# Load the large trade data from file
with open(var_call_myAx42JYi9qdbc60SpUm5vQa, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure types
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# Create year-month for monthly contributions (assume contribution at month-end using last available trading day)
df['year_month'] = df['Date'].dt.to_period('M')

results = []

for idx, g in df.groupby('Index'):
    # Investor invests a fixed amount each month starting from Jan 2000
    monthly = g[(g['Date'] >= '2000-01-01')]
    if monthly.empty:
        continue
    # Get last trading day per month
    month_last = monthly.sort_values('Date').groupby('year_month').tail(1)
    month_last = month_last[month_last['Date'] <= pd.Timestamp('today')]
    if month_last.empty:
        continue
    # Assume $1 invested each month; units bought = 1 / price
    units = (1.0 / month_last['Adj Close']).sum()
    total_invested = len(month_last) * 1.0
    final_price = month_last.iloc[-1]['Adj Close']
    final_value = units * final_price
    ratio = final_value / total_invested
    results.append({'Index': idx, 'contribution_months': len(month_last), 'final_value_per_1usd_monthly': ratio})

res_df = pd.DataFrame(results)
res_top5 = res_df.sort_values('final_value_per_1usd_monthly', ascending=False).head(5)

out = res_top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_5xwZcOJlHJKstdnXls6rAoej': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_myAx42JYi9qdbc60SpUm5vQa': 'file_storage/call_myAx42JYi9qdbc60SpUm5vQa.json', 'var_call_qvL6QyFH5ermhC0avKlGbiBR': ['index_info']}

exec(code, env_args)

code = """import json, pandas as pd
from datetime import datetime

# load full data
with open(var_call_5wVfQ2ltCQjEOyLheSdIoZZF, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ensure proper dtypes
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# construct monthly investment dates: we'll use month-end of each month from Jan 2000 to last date in data.
start = df['Date'].min().to_period('M')
end = df['Date'].max().to_period('M')
months = pd.period_range(start, end, freq='M')

results = []
for idx, g in df.groupby('Index'):
    g = g.sort_values('Date')
    # for each month, pick last available trading day in that month
    g['Month'] = g['Date'].dt.to_period('M')
    monthly = g.groupby('Month').tail(1)
    # require full span from 2000-01 to last month? We'll just use available months from 2000-01 onward
    monthly = monthly[monthly['Month'] >= months[0]]
    if monthly.empty:
        continue
    # assume invest 1 unit of currency each month at that Adj Close price
    monthly = monthly.sort_values('Month')
    invest = 1.0
    units = (invest / monthly['Adj Close']).sum()
    total_invested = invest * len(monthly)
    final_price = monthly.iloc[-1]['Adj Close']
    final_value = units * final_price
    total_return = final_value / total_invested - 1
    results.append({'Index': idx, 'total_return': total_return})

res_df = pd.DataFrame(results).sort_values('total_return', ascending=False).head(5)

# map index to country manually
index_country = {
    'HSI': 'Hong Kong (China)',
    'IXIC': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'NYA': 'United States',
    'N100': 'Eurozone (Europe-wide)',
    '399001.SZ': 'China',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'J203.JO': 'South Africa'
}

res_df['Country'] = res_df['Index'].map(index_country)

answer = res_df.to_dict(orient='records')

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RMvspbk6JU9n0dx7sOaPR9OZ': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}], 'var_call_1yfrm4buKkDWX43EJ82y9DBq': [{'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}], 'var_call_7aa3hAr2FA6OgHnZcFQwHxmf': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_5wVfQ2ltCQjEOyLheSdIoZZF': 'file_storage/call_5wVfQ2ltCQjEOyLheSdIoZZF.json'}

exec(code, env_args)

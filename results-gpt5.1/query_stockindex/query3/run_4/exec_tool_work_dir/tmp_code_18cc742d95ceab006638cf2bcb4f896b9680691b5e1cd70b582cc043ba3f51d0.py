code = """import pandas as pd, json
import os

# Load distinct indices and first dates
indices = pd.DataFrame(var_call_nUeWvG3DW8AQ5HLZGjwj7Fhf)
first_dates = pd.DataFrame(var_call_hhUp30jbOTn8JhqPQ9wlrHFD)

# Load large trade data from file
path = var_call_mfm9P2cGS0RsbaLYUz1pkDoU
with open(path, 'r') as f:
    data = json.load(f)
trades = pd.DataFrame(data)

# Normalize dates to YYYY-MM-DD
trades['Date'] = pd.to_datetime(trades['Date'], errors='coerce')
trades = trades[trades['Date'] >= pd.Timestamp('2000-01-01')]

# Ensure Adj Close numeric
trades['Adj Close'] = pd.to_numeric(trades['Adj Close'], errors='coerce')
trades = trades.dropna(subset=['Adj Close'])

# For monthly investing, take last trading day of each month per index
trades['YearMonth'] = trades['Date'].dt.to_period('M')
monthly = trades.sort_values(['Index','Date']).groupby(['Index','YearMonth']).tail(1)

# Assume investing 1 unit of currency per month; units bought = 1 / price
monthly['units'] = 1.0 / monthly['Adj Close']

# Aggregate units per index and compute final value using last available price
agg = monthly.groupby('Index').agg({'units':'sum'}).reset_index()
last_price = trades.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']].rename(columns={'Adj Close':'final_price'})
res = agg.merge(last_price, on='Index')
res['final_value'] = res['units'] * res['final_price']

# Also compute number of contributions
n_months = monthly.groupby('Index').size().reset_index(name='n_months')
res = res.merge(n_months, on='Index')

# Filter indices that have data since at least 2000-01-01 (they all should after filtering) but ensure reasonable history

# Rank by final_value
res = res.sort_values('final_value', ascending=False).head(5)

result = res.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_nUeWvG3DW8AQ5HLZGjwj7Fhf': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}], 'var_call_hhUp30jbOTn8JhqPQ9wlrHFD': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}], 'var_call_mfm9P2cGS0RsbaLYUz1pkDoU': 'file_storage/call_mfm9P2cGS0RsbaLYUz1pkDoU.json'}

exec(code, env_args)

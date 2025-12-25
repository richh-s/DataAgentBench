code = """import json, pandas as pd

# Load full index trade data
path = var_call_rYrMDPASrALnGuCQ560oKLq0
with open(path, 'r') as f:
    trades = json.load(f)

df = pd.DataFrame(trades)

# Ensure correct types
# Strip time part if present
df['Date'] = df['Date'].str.slice(0,10)
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d').dt.to_period('M')
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# For each index and month, take the last available trading day as the monthly investment date
monthly_prices = df.sort_values(['Index','Date']).groupby(['Index','Date']).tail(1)

# For each index, compute number of months and final price
monthly_prices = monthly_prices.sort_values(['Index','Date'])

results = []
for idx, grp in monthly_prices.groupby('Index'):
    grp = grp.sort_values('Date')
    if grp.empty:
        continue
    units = (1.0 / grp['Adj Close']).sum()
    final_price = grp['Adj Close'].iloc[-1]
    final_value = units * final_price
    results.append({'Index': idx, 'final_value': float(final_value)})

res_df = pd.DataFrame(results)

# Get top 5 indices by final_value
top5 = res_df.sort_values('final_value', ascending=False).head(5)

index_to_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    '^NSEI': 'India',
    '^BSESN': 'India',
    '^GDAXI': 'Germany',
    '^FCHI': 'France',
    '^STOXX50E': 'Eurozone',
    '^GSPC': 'United States',
    '^DJI': 'United States',
    '^IXIC': 'United States',
    '^GSPTSE': 'Canada',
    '^SSMI': 'Switzerland',
    '^KS11': 'South Korea',
    '^TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

top5['Country'] = top5['Index'].map(index_to_country).fillna('Unknown')

answer = top5.to_dict(orient='records')
result = json.dumps(answer)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_rYrMDPASrALnGuCQ560oKLq0': 'file_storage/call_rYrMDPASrALnGuCQ560oKLq0.json', 'var_call_0QEv96KeMTp5a2GhtXR6fS8z': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

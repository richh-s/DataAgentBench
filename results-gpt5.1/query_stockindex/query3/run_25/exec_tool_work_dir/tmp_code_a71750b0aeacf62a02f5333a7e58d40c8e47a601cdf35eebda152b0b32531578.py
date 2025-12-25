code = """import pandas as pd, json, os

path = var_call_vzVXrtubIAyW6UO8uzJYNVOH
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ensure correct dtypes
# coerce errors in datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Adj Close'])

# simulate monthly DCA: invest 1 unit of cash at last trading day of each month per index
results = []
for idx, g in df.groupby('Index'):
    g = g.sort_values('Date')
    # get last trading day of each month
    g['YearMonth'] = g['Date'].dt.to_period('M')
    monthly = g.sort_values('Date').groupby('YearMonth').tail(1)
    if monthly.empty:
        continue
    prices = monthly['Adj Close'].values.astype(float)
    units = 1.0 / prices
    total_units = units.sum()
    total_invested = float(len(prices))
    final_price = float(g['Adj Close'].iloc[-1])
    final_value = total_units * final_price
    total_return = (final_value / total_invested) - 1.0
    results.append({'Index': idx, 'total_return': float(total_return)})

res_df = pd.DataFrame(results)
res_df = res_df.sort_values('total_return', ascending=False).head(5)

country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    '^GSPC': 'United States',
    '^DJI': 'United States',
    '^IXIC': 'United States',
    '^GDAXI': 'Germany',
    '^FTSE': 'United Kingdom',
    '^FCHI': 'France',
    '^STOXX50E': 'Eurozone',
    '^GSPTSE': 'Canada',
    '^BSESN': 'India',
    '^KS11': 'South Korea',
    '^SSMI': 'Switzerland',
    '^TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

res_df['Country'] = res_df['Index'].map(country_map).fillna('Unknown')

answer = res_df.to_dict(orient='records')
answer_json = json.dumps(answer)
print('__RESULT__:')
print(answer_json)"""

env_args = {'var_call_vzVXrtubIAyW6UO8uzJYNVOH': 'file_storage/call_vzVXrtubIAyW6UO8uzJYNVOH.json', 'var_call_Ap9BcvotalzilQW9PQY2UBMG': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

code = """import json, pandas as pd, os

# Load full index_trade data from file
path = var_call_Jsxv4fONkU1tSj83APo0dir1
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure correct dtypes
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# Resample to month-end prices per index
monthly = df.set_index('Date').groupby('Index')['Adj Close'].resample('M').last().reset_index()

# Simulate fixed-dollar monthly contribution using unit-price scaling
# For ranking, it's equivalent to assume investing 1 unit of currency each month:
# contribution_t = 1 / price_t units, portfolio value = sum(1/price_t * last_price)

# For each index, compute final value from regular contributions starting from first available month >=2000
results = []
for idx, grp in monthly.groupby('Index'):
    grp = grp.sort_values('Date')
    # assume invest from first month in 2000 data through last month
    first_price = grp['Adj Close'].iloc[0]
    last_price = grp['Adj Close'].iloc[-1]
    # DCA final value proportional to last_price * sum(1/price_t)
    value = last_price * (1.0 / grp['Adj Close']).sum()
    results.append({'Index': idx, 'dca_value': float(value)})

res_df = pd.DataFrame(results)
res_top5 = res_df.sort_values('dca_value', ascending=False).head(5)

# Map indices to countries manually based on known major indices
country_map = {
    'NYA': 'United States',
    'IXIC': 'United States',
    '^GSPC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N225': 'Japan',
    'GDAXI': 'Germany',
    'N100': 'Eurozone',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

res_top5['Country'] = res_top5['Index'].map(country_map).fillna('Unknown')

answer = res_top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_Wn5xbCOChQMympMxBiTGZEoy': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_Jsxv4fONkU1tSj83APo0dir1': 'file_storage/call_Jsxv4fONkU1tSj83APo0dir1.json', 'var_call_h6qnheSI6UxM9WRSOAcQ8cqz': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

code = """import pandas as pd
import json

# Load the large query result from index_trade (path provided in storage)
path = var_call_2nbhKfAWkCuFMBUpsQiDzrQ5

df = pd.read_json(path)
# Ensure correct types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD','Date'])

# Keep data from 2000-01-01 onwards
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# Determine first trading day price each month for each index
df['ym'] = df['Date'].dt.to_period('M')
first_prices = df.sort_values('Date').groupby(['Index','ym'], as_index=False).first()

# Last available closing price per index
last_price = df.sort_values('Date').groupby('Index', as_index=False).last()[['Index','CloseUSD','Date']]

results = []
for idx, grp in first_prices.groupby('Index'):
    grp = grp.sort_values('ym')
    n_months = len(grp)
    if n_months == 0:
        continue
    # monthly investment of $1
    shares = (1.0 / grp['CloseUSD']).sum()
    lp = last_price[last_price['Index'] == idx]
    if lp.empty:
        continue
    final_price = float(lp['CloseUSD'].iloc[0])
    final_value = shares * final_price
    total_invested = n_months * 1.0
    factor = final_value / total_invested
    results.append({'Index': idx, 'months': int(n_months), 'final_value': float(final_value), 'total_invested': float(total_invested), 'factor': float(factor)})

# Sort by factor (overall return) descending
res_sorted = sorted(results, key=lambda x: x['factor'], reverse=True)
top5 = res_sorted[:5]

# Heuristic mapping from index symbol to country
def map_country(symbol):
    s = symbol.upper()
    if '.SS' in s or s.endswith('.SS') or s.endswith('.SH') or s.endswith('.SZ') or s.startswith('000') or s.startswith('399') or s.startswith('6'):
        return 'China'
    if 'HSI' in s or 'HANG' in s or s.startswith('HK'):
        return 'Hong Kong'
    if 'N225' in s or 'NIKKEI' in s:
        return 'Japan'
    if 'KOSPI' in s or 'KS11' in s:
        return 'South Korea'
    if 'TSX' in s or s.endswith('.TO') or 'GSPTSE' in s:
        return 'Canada'
    if 'DAX' in s or 'GDAXI' in s:
        return 'Germany'
    if 'FTSE' in s or 'LSE' in s:
        return 'United Kingdom'
    if 'SP' in s or 'GSPC' in s or 'S&P' in s or 'INX' in s or 'DJI' in s or 'NASDAQ' in s or 'IXIC' in s:
        return 'United States'
    if 'NSE' in s or 'NIFTY' in s:
        return 'India'
    if 'SMI' in s or 'SIX' in s or 'SWISS' in s:
        return 'Switzerland'
    if 'TW' in s or 'TAI' in s or 'TAIEX' in s or '.TW' in s:
        return 'Taiwan'
    if 'JSE' in s or 'JOH' in s:
        return 'South Africa'
    return 'Unknown'

for d in top5:
    d['country'] = map_country(d['Index'])

# Prepare output
out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mQGpBKUyRPqrKkKLnN53YKk0': ['index_trade'], 'var_call_2nbhKfAWkCuFMBUpsQiDzrQ5': 'file_storage/call_2nbhKfAWkCuFMBUpsQiDzrQ5.json', 'var_call_c6eHGTP79UgbJVFw0qi1ZlAG': ['index_info'], 'var_call_uBloPhRHxhXExSUX346o3xBo': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

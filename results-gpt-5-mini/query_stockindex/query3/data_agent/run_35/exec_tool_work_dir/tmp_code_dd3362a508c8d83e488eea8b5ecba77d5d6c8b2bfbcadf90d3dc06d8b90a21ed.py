code = """import pandas as pd
import json

# Load large query result from file path stored in var_call_kGwrzWbmhSp5hm7IZT9M7c9J
file_path = var_call_kGwrzWbmhSp5hm7IZT9M7c9J
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Keep only relevant columns
df = df[["Index", "Date", "CloseUSD"]]
# Convert types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Parse dates with coercion
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# Drop rows with missing
df = df.dropna(subset=['Date','CloseUSD'])
# Filter from 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# Resample monthly per index using month-end last available price
monthly = df.set_index('Date').groupby('Index').resample('M').last().reset_index()

results = []

# mapping from index to country (inferred)
country_map = {
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'J203.JO': 'South Africa',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands',
    '399001.SZ': 'China'
}

for idx, group in monthly.groupby('Index'):
    group = group.sort_values('Date')
    prices = group['CloseUSD'].values
    dates = group['Date'].values
    if len(prices) < 2:
        continue
    # monthly invest $1 at each month-end price
    shares = 1.0 / prices
    total_shares = shares.sum()
    final_price = prices[-1]
    final_value = total_shares * final_price
    months = len(prices)
    total_contrib = months * 1.0
    multiplier = final_value / total_contrib
    results.append({
        'Index': idx,
        'country': country_map.get(idx, 'Unknown'),
        'months': int(months),
        'multiplier': float(multiplier),
        'final_value': float(final_value)
    })

# Sort by multiplier descending
results_sorted = sorted(results, key=lambda x: x['multiplier'], reverse=True)
# Take top 5
top5 = results_sorted[:5]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_pQ32cIYMR1KqeWvxeS7xTYIX': ['index_trade'], 'var_call_d296t0WMhtxfiQ7FwzNuohSf': [{'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}], 'var_call_flUn2eWzILhsvJKOt2PQqSvk': ['index_info'], 'var_call_qHG5y3e18K0YfrjhOBsmmNR4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_kGwrzWbmhSp5hm7IZT9M7c9J': 'file_storage/call_kGwrzWbmhSp5hm7IZT9M7c9J.json'}

exec(code, env_args)

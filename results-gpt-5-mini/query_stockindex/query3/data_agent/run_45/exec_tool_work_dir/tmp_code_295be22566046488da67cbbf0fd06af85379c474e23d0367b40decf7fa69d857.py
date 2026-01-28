code = """import json
import pandas as pd
from pathlib import Path

# Load the large query result from the storage file
data_file = Path(var_call_kWJzbq09etfC7eMrNrv0lpfJ)
with data_file.open('r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)
# Ensure types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])
# Filter from 2000-01-01 (already done in query, but ensure)
df = df[df['Date'] >= pd.to_datetime('2000-01-01')]

results = []
for idx, g in df.groupby('Index'):
    g = g.sort_values('Date').copy()
    g['year_month'] = g['Date'].dt.to_period('M')
    months = sorted(g['year_month'].unique())
    prices_for_invest = []
    for ym in months:
        month_rows = g[g['year_month'] == ym]
        if month_rows.empty:
            continue
        # use first trading day's CloseUSD in the month
        first_row = month_rows.loc[month_rows['Date'].idxmin()]
        price = first_row['CloseUSD']
        if pd.isna(price) or price <= 0:
            continue
        prices_for_invest.append(price)
    if len(prices_for_invest) == 0:
        continue
    monthly_amount = 1.0
    shares = sum((monthly_amount / p) for p in prices_for_invest)
    last_price = g.loc[g['Date'].idxmax()]['CloseUSD']
    final_value = shares * last_price
    total_invested = monthly_amount * len(prices_for_invest)
    total_return = final_value / total_invested - 1.0
    results.append({
        'Index': idx,
        'months_invested': len(prices_for_invest),
        'total_invested': round(total_invested, 6),
        'final_value': round(final_value, 6),
        'total_return': round(total_return, 6)
    })

# Sort by total_return descending
results_sorted = sorted(results, key=lambda x: x['total_return'], reverse=True)
top5 = results_sorted[:5]

# Map indices to countries (inferred)
mapping = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'N100': 'Netherlands',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

for item in top5:
    item['country'] = mapping.get(item['Index'], 'Unknown')
    # add percent string
    item['total_return_pct'] = f"{item['total_return']*100:.2f}%"

# Prepare JSON-serializable output
out = top5

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_8XkeRr2DirGEFpbJOYe8zHD8': ['index_trade'], 'var_call_Y0m845FrcUHQzkLDTehkjXjY': ['index_info'], 'var_call_kWJzbq09etfC7eMrNrv0lpfJ': 'file_storage/call_kWJzbq09etfC7eMrNrv0lpfJ.json', 'var_call_7K1gOM204DLTilOIyrU65HMG': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_tLNMwg5ugQR2NCIpF3LEc7IQ': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)

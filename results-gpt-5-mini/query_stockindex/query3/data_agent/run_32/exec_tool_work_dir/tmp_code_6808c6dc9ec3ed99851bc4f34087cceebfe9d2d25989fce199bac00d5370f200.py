code = """import pandas as pd
import json
from datetime import datetime
# Load data from storage variable (file path)
fp = var_call_IO52AQhQw2TYVqUmNvSKxH9c
with open(fp, 'r') as f:
    records = json.load(f)

# Convert CloseUSD strings to numeric, Date to datetime carefully
for rec in records:
    # Some CloseUSD may be strings
    try:
        rec['CloseUSD'] = float(rec['CloseUSD'])
    except:
        rec['CloseUSD'] = None

    # Date may be like '2000-01-04 00:00:00'
    try:
        rec['Date'] = pd.to_datetime(rec['Date'])
    except:
        rec['Date'] = None


# Build DataFrame
df = pd.DataFrame(records)
# Drop records with nulls
df = df.dropna(subset=['Date','CloseUSD'])

results = []
indexes = df['Index'].unique()
for idx in indexes:
    dfi = df[df['Index'] == idx].sort_values('Date')
    if dfi.empty:
        continue
    # Create year-month period
    dfi['ym'] = dfi['Date'].dt.to_period('M')
    # Get first trading day per month
    firsts = dfi.loc[dfi.groupby('ym')['Date'].idxmin()].copy()
    firsts = firsts.sort_values('Date')
    n_months = len(firsts)
    if n_months == 0:
        continue
    invest = 1.0  # $1 per month
    units = (invest / firsts['CloseUSD']).sum()
    total_invested = invest * n_months
    last_price = dfi.iloc[-1]['CloseUSD']
    final_value = units * last_price
    multiple = final_value / total_invested
    pct_return = (final_value - total_invested) / total_invested * 100.0
    results.append({
        'Index': idx,
        'n_months': int(n_months),
        'total_invested': round(total_invested,4),
        'final_value': round(final_value,4),
        'multiple': round(multiple,6),
        'pct_return': round(pct_return,2)
    })

# Rank by multiple
results_sorted = sorted(results, key=lambda x: x['multiple'], reverse=True)
top5 = results_sorted[:5]

# Map indices to countries (inferred)
country_map = {
    'J203.JO': 'South Africa',
    'IXIC': 'United States',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'NYA': 'United States',
    'N100': 'Europe (pan-European)',
    '399001.SZ': 'China'
}

for r in top5:
    r['country'] = country_map.get(r['Index'], 'Unknown')

# Prepare JSON string
out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_YVGH4PEjrnftDFNBYmzlcINZ': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_vnEuW1tQhJDbGwzF5MvU95sp': 'file_storage/call_vnEuW1tQhJDbGwzF5MvU95sp.json', 'var_call_IO52AQhQw2TYVqUmNvSKxH9c': 'file_storage/call_IO52AQhQw2TYVqUmNvSKxH9c.json'}

exec(code, env_args)

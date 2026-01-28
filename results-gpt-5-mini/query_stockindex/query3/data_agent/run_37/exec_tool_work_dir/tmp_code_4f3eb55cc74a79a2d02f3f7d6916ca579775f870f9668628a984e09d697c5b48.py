code = """import json
import pandas as pd
from datetime import datetime

# Load the query result from storage
path = var_call_LMuVgejHw98EcMwI0bRRC8Nt
with open(path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Clean and convert types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Robust date parsing
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# drop rows without dates or closeusd
df = df.dropna(subset=['Date', 'CloseUSD']).copy()

indices = df['Index'].unique().tolist()

results = []
for idx in indices:
    dfi = df[df['Index'] == idx].sort_values('Date').copy()
    if dfi.empty:
        continue
    # determine start month (no earlier than 2000-01)
    first_date = dfi['Date'].min()
    start_date = max(pd.Timestamp('2000-01-01'), first_date)
    # months to consider: month starts from start_date's month
    month_starts = pd.date_range(start=start_date.replace(day=1), end=dfi['Date'].max(), freq='MS')
    shares = 0.0
    purchase_dates = []
    for m in month_starts:
        # find rows in same month
        mask = (dfi['Date'].dt.year == m.year) & (dfi['Date'].dt.month == m.month)
        month_rows = dfi[mask]
        if month_rows.empty:
            # no trading in that month for this index
            continue
        # pick the first trading day of the month
        purchase_row = month_rows.sort_values('Date').iloc[0]
        price = purchase_row['CloseUSD']
        if pd.isna(price) or price <= 0:
            continue
        shares += 1.0 / price
        purchase_dates.append(purchase_row['Date'])
    months_invested = len(purchase_dates)
    if months_invested == 0:
        continue
    last_price = dfi['CloseUSD'].dropna().iloc[-1]
    final_value = shares * last_price
    total_invested = months_invested * 1.0
    return_multiple = final_value / total_invested
    results.append({
        'Index': idx,
        'MonthsInvested': int(months_invested),
        'FinalValue_per_$1_monthly_invested': float(final_value),
        'ReturnMultiple': float(return_multiple),
        'LastDate': dfi['Date'].max().strftime('%Y-%m-%d')
    })

# sort by ReturnMultiple
results_sorted = sorted(results, key=lambda x: x['ReturnMultiple'], reverse=True)
# take top 5
top5 = results_sorted[:5]

# map indices to countries (inferred)
country_map = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong (China)',
    'NYA': 'United States',
    'N100': 'Netherlands',
    '399001.SZ': 'China',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

# attach country and round numeric values for readability
for r in top5:
    r['Country'] = country_map.get(r['Index'], 'Unknown')
    r['FinalValue_per_$1_monthly_invested'] = round(r['FinalValue_per_$1_monthly_invested'], 4)
    r['ReturnMultiple'] = round(r['ReturnMultiple'], 4)

output = {'top5': top5}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_IZCMGy5w8j0qD8m6dK3KvI6c': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_LMuVgejHw98EcMwI0bRRC8Nt': 'file_storage/call_LMuVgejHw98EcMwI0bRRC8Nt.json'}

exec(code, env_args)

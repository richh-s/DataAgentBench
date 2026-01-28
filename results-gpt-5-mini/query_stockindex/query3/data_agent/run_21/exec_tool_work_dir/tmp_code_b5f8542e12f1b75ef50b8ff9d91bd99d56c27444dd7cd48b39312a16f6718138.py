code = """import json
import pandas as pd
from datetime import datetime

# Load data from previous tool calls available as variables
# var_call_ZjUxpmH3sKWIFidIJMbvJ3wQ contains the path to the large JSON result
trades_path = var_call_ZjUxpmH3sKWIFidIJMbvJ3wQ
with open(trades_path, 'r') as f:
    trades = json.load(f)

# var_call_fIcoOZHmc6cBdrvJdkHuPJ3e is list of distinct indices
indices_list = var_call_fIcoOZHmc6cBdrvJdkHuPJ3e

# var_call_b0M0hArEXD8qhg6EccAeakGP contains index_info
index_info = var_call_b0M0hArEXD8qhg6EccAeakGP

# Build DataFrame
df = pd.DataFrame(trades)
# Parse types
df['Date'] = pd.to_datetime(df['Date'])
# Convert CloseUSD to float, handle strings
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Mapping of index symbol to country (inferred)
index_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'IXIC': 'United States',
    'NYA': 'United States',
    'N100': 'Europe',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa',
    'NSEI': 'India'
}

results = []
start_period = pd.Period('2000-01', freq='M')

for rec in indices_list:
    idx = rec['Index']
    df_idx = df[df['Index'] == idx].sort_values('Date').copy()
    if df_idx.empty:
        continue
    # only consider data from 2000-01-01 onward
    df_idx = df_idx[df_idx['Date'] >= pd.Timestamp('2000-01-01')]
    if df_idx.empty:
        continue
    # group by year-month period and take first available trading day in each month
    df_idx['ym'] = df_idx['Date'].dt.to_period('M')
    # Keep months from 2000-01 to last available month for this index
    first_month = df_idx['ym'].min()
    last_month = df_idx['ym'].max()
    # Ensure start at 2000-01 or later
    period_range = pd.period_range(max(start_period, first_month), last_month, freq='M')
    # For each period, get the first trading day's close
    monthly_purchases = []
    for p in period_range:
        month_rows = df_idx[df_idx['ym'] == p]
        if month_rows.empty:
            continue
        first_row = month_rows.sort_values('Date').iloc[0]
        close_price = first_row['CloseUSD']
        if pd.isna(close_price) or close_price <= 0:
            continue
        monthly_purchases.append({'date': first_row['Date'], 'price': float(close_price)})
    if len(monthly_purchases) == 0:
        continue
    # Simulate investing 1 USD each month at the recorded price
    units = sum(1.0 / mp['price'] for mp in monthly_purchases)
    total_invested = float(len(monthly_purchases))
    # final value uses the last available CloseUSD for the index
    last_price_row = df_idx.sort_values('Date').iloc[-1]
    last_price = float(last_price_row['CloseUSD'])
    final_value = units * last_price
    multiplier = final_value / total_invested if total_invested>0 else None
    return_pct = multiplier - 1 if multiplier is not None else None
    results.append({
        'Index': idx,
        'Country': index_country.get(idx, None),
        'MonthsInvested': int(total_invested),
        'TotalInvestedUSD': round(total_invested,2),
        'FinalValueUSD': round(final_value,2),
        'Multiplier': round(multiplier,4) if multiplier is not None else None,
        'ReturnPct': round(return_pct*100,2) if return_pct is not None else None
    })

# Sort by Multiplier descending
results_sorted = sorted(results, key=lambda x: (x['Multiplier'] if x['Multiplier'] is not None else -999), reverse=True)

# Take top 5
top5 = results_sorted[:5]

# Prepare output
output = top5

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_fIcoOZHmc6cBdrvJdkHuPJ3e': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_b0M0hArEXD8qhg6EccAeakGP': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_ZjUxpmH3sKWIFidIJMbvJ3wQ': 'file_storage/call_ZjUxpmH3sKWIFidIJMbvJ3wQ.json'}

exec(code, env_args)

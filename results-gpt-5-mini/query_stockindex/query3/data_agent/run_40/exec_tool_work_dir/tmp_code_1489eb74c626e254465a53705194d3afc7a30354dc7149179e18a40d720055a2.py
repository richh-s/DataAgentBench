code = """import json
import pandas as pd
from datetime import datetime

# Load the large index_trade query result from storage file
path = var_call_RgRThaQLhUPRZKl49cR3ifMu
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure proper types
df['Date'] = pd.to_datetime(df['Date'])
# Convert CloseUSD to float (some may be strings)
df['CloseUSD'] = df['CloseUSD'].astype(float)

# List of indices from earlier distinct query
indices = [d['idx'] for d in var_call_eiZyUqUxIyaqc7TpozJAwwzS]

# Manual mapping of index symbol to country (based on known major indices and index_info)
country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Euronext (Europe)',
    'IXIC': 'United States',
    'NYA': 'United States',
    'J203.JO': 'South Africa'
}

results = []
monthly_amount = 100.0  # fixed monthly investment in USD

for idx in indices:
    df_idx = df[df['Index'] == idx].sort_values('Date').reset_index(drop=True)
    if df_idx.empty:
        continue
    # Consider only dates from 2000-01-01
    df_idx = df_idx[df_idx['Date'] >= pd.Timestamp('2000-01-01')]
    if df_idx.empty:
        continue
    # Create periods (year-month) available for this index
    df_idx['period'] = df_idx['Date'].dt.to_period('M')
    periods = sorted(df_idx['period'].unique())

    total_invested = 0.0
    total_shares = 0.0
    months_invested = 0

    for p in periods:
        # pick first trading day in the month
        month_rows = df_idx[df_idx['period'] == p]
        if month_rows.empty:
            continue
        first_row = month_rows.iloc[0]
        price = float(first_row['CloseUSD'])
        if price <= 0 or pd.isna(price):
            continue
        shares_bought = monthly_amount / price
        total_shares += shares_bought
        total_invested += monthly_amount
        months_invested += 1

    # final value at last available close
    final_price = float(df_idx.iloc[-1]['CloseUSD'])
    final_value = total_shares * final_price
    if total_invested == 0:
        multiple = None
        return_pct = None
    else:
        multiple = final_value / total_invested
        return_pct = (final_value - total_invested) / total_invested * 100.0

    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'MonthsInvested': months_invested,
        'TotalInvestedUSD': round(total_invested, 2),
        'FinalValueUSD': round(final_value, 2),
        'Multiple': round(multiple, 4) if multiple is not None else None,
        'ReturnPercent': round(return_pct, 2) if return_pct is not None else None,
        'LastDate': df_idx.iloc[-1]['Date'].strftime('%Y-%m-%d')
    })

# Sort by Multiple descending and pick top 5
results_sorted = sorted([r for r in results if r['Multiple'] is not None], key=lambda x: x['Multiple'], reverse=True)
top5 = results_sorted[:5]

# Prepare output
output = {
    'monthly_investment_usd': monthly_amount,
    'top5_by_total_return': top5
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_4JzeBT6DPmO56hxSAUoAE7W0': ['index_trade'], 'var_call_pWb3LSHcar9KVZNIOMIOp3H2': ['index_info'], 'var_call_eiZyUqUxIyaqc7TpozJAwwzS': [{'idx': 'J203.JO'}, {'idx': 'N225'}, {'idx': 'GSPTSE'}, {'idx': 'NSEI'}, {'idx': 'GDAXI'}, {'idx': 'HSI'}, {'idx': 'NYA'}, {'idx': '000001.SS'}, {'idx': 'SSMI'}, {'idx': 'TWII'}, {'idx': 'N100'}, {'idx': '399001.SZ'}, {'idx': 'IXIC'}], 'var_call_RgRThaQLhUPRZKl49cR3ifMu': 'file_storage/call_RgRThaQLhUPRZKl49cR3ifMu.json', 'var_call_F4Ffn0Ft7Zi375PrIPQfBUwn': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

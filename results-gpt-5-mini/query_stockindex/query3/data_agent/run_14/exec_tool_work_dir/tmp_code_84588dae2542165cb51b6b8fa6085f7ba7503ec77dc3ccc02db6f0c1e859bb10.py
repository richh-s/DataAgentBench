code = """import pandas as pd
import json
from datetime import datetime

# Load data from previous query result file path
path = var_call_cAzhJMG6j7PvYHn4yXzVqKQ4
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Normalize column names
# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Parse dates with pandas
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# Filter for dates from 2000-01-01 onwards
df = df[df['Date_parsed'].notna()]
df = df[df['Date_parsed'] >= pd.Timestamp('2000-01-01')]

# Prepare result container
results = []

# Define mapping of index symbols to countries (inferred)
index_country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GDAXI': 'Germany',
    'NSEI': 'India',
    'J203.JO': 'South Africa',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands (Euronext)'
}

# Compute monthly DCA investing $1 at first trading day of each month for each index
for idx, grp in df.groupby('Index'):
    g = grp.sort_values('Date_parsed').copy()
    # Keep only rows with positive CloseUSD
    g = g[g['CloseUSD'] > 0]
    if g.empty:
        continue
    # Determine first trading day per month: use Year-Month period
    g['year_month'] = g['Date_parsed'].dt.to_period('M')
    first_days = g.loc[g.groupby('year_month')['Date_parsed'].idxmin()]
    # Only consider months from 2000-01 onwards (already filtered)
    # Invest $1 per month on those first trading days
    first_days = first_days.sort_values('Date_parsed')
    # Compute shares accumulated
    first_days['shares'] = 1.0 / first_days['CloseUSD']
    total_shares = first_days['shares'].sum()
    months_invested = len(first_days)
    if months_invested == 0:
        continue
    # Determine last available close price for this index (use latest date in original grp)
    last_price_row = g.loc[g['Date_parsed'].idxmax()]
    last_price = float(last_price_row['CloseUSD'])
    final_value = total_shares * last_price
    invested_amount = float(months_invested) * 1.0
    return_ratio = final_value / invested_amount if invested_amount > 0 else None
    results.append({
        'Index': idx,
        'Country': index_country_map.get(idx, 'Unknown'),
        'MonthsInvested': months_invested,
        'FinalValue': round(final_value, 6),
        'Invested': round(invested_amount, 6),
        'ReturnRatio': round(return_ratio, 6)
    })

# Sort by ReturnRatio descending and pick top 5
results_sorted = sorted(results, key=lambda x: (x['ReturnRatio'] if x['ReturnRatio'] is not None else -999), reverse=True)
top5 = results_sorted[:5]

# Print result as JSON string per required format
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_okGt5idIWo1siSDYc8JssgyE': ['index_trade'], 'var_call_Qvc4LUsFOIcKZFPVWNiGVtot': ['index_info'], 'var_call_cAzhJMG6j7PvYHn4yXzVqKQ4': 'file_storage/call_cAzhJMG6j7PvYHn4yXzVqKQ4.json', 'var_call_Ng4nGyOQYlktMOjm8DzStW5o': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_YxwzToo8MlrBTjBhODPwuBPI': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}]}

exec(code, env_args)

code = """import json
import pandas as pd

# Load the large query result from storage
path = var_call_2XvJwQ5YIyCi64mDOOpYn3EC
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Create DataFrame
df = pd.DataFrame(records)
# Convert types safely
# Some Date entries may have extra spaces; coerce errors
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# Drop rows with invalid dates
df = df.dropna(subset=['Date']).copy()
# CloseUSD may be string; convert to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Filter out invalid prices
df = df[df['CloseUSD'] > 0].copy()

# Determine first trading day of each month for each index
df['YearMonth'] = df['Date'].dt.to_period('M')
# Sort
df = df.sort_values(['Index', 'Date'])
# Get first trading day record per Index-YearMonth
first_of_month = df.groupby(['Index', 'YearMonth'], as_index=False).first()

results = []

# Country mapping for known index symbols
country_map = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    'N100': 'Europe',
    '399001.SZ': 'China',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

# Compute monthly-investment DCA ($1 each month) results per index
for idx, group in first_of_month.groupby('Index'):
    months = group.shape[0]
    if months == 0:
        continue
    # Sum of shares bought with $1 each month at that month's first trading day's CloseUSD
    # Avoid division by zero
    valid_prices = group['CloseUSD'].replace(0, pd.NA).dropna()
    if valid_prices.empty:
        continue
    shares = (1.0 / valid_prices).sum()
    # Last available close price for the index
    last_rows = df[df['Index'] == idx].sort_values('Date', ascending=False)
    if last_rows.empty:
        continue
    last_price = float(last_rows.iloc[0]['CloseUSD'])
    final_value = float(shares) * last_price
    total_invested = float(months)
    return_factor = final_value / total_invested if total_invested > 0 else None
    results.append({
        'Index': idx,
        'MonthsInvested': int(months),
        'FinalValuePerDollarInvested': return_factor,
        'TotalFinalValueFor$1PerMonth': final_value,
        'TotalInvested': total_invested,
        'Country': country_map.get(idx, 'Unknown')
    })

# Sort by FinalValuePerDollarInvested descending and take top 5
results_sorted = sorted(results, key=lambda x: (x['FinalValuePerDollarInvested'] if x['FinalValuePerDollarInvested'] is not None else -999), reverse=True)
top5 = results_sorted[:5]

# Prepare output list with clearer return percentages
output = []
for r in top5:
    factor = r['FinalValuePerDollarInvested']
    pct = None
    if factor is not None:
        pct = (factor - 1.0) * 100.0
    output.append({
        'Index': r['Index'],
        'Country': r['Country'],
        'MonthsInvested': r['MonthsInvested'],
        'TotalInvested_USD': r['TotalInvested'],
        'FinalValue_USD': round(r['TotalFinalValueFor$1PerMonth'], 6),
        'ReturnFactor': round(factor, 6) if factor is not None else None,
        'ReturnPercent': round(pct, 3) if pct is not None else None
    })

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ZemLgHhBzxYaoj8MPVd7iruM': ['index_trade'], 'var_call_PUnGboKVNPJx1KrpDtRsbx0H': ['index_info'], 'var_call_aSALVXASyBmpOYOBIrP3fqOR': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_2XvJwQ5YIyCi64mDOOpYn3EC': 'file_storage/call_2XvJwQ5YIyCi64mDOOpYn3EC.json', 'var_call_v78nxa5wVyIcr3AcFA7KcU7d': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

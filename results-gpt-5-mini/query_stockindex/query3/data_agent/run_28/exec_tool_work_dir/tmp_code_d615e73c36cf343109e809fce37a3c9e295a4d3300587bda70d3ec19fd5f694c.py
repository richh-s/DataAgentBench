code = """import pandas as pd
import json
from pathlib import Path

# Load the large query result from the storage path
data_path = Path(var_call_oHL9xSBTIFUquAhBzK7elqnV)
df = pd.read_json(data_path)

# Prepare dataframe
df['Date'] = pd.to_datetime(df['Date'])
# Ensure CloseUSD is numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Mapping from index symbol to country (inferred from DATABASE DESCRIPTION and hints)
index_country = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Euronext (Europe)',
    '399001.SZ': 'China',
    'NYA': 'United States'
}

monthly_amount = 1.0
results = []

for idx, grp in df.groupby('Index'):
    g = grp.sort_values('Date').reset_index(drop=True)
    # Consider months from 2000-01-01 to last available date for that index
    start = pd.Timestamp('2000-01-01')
    end = g['Date'].max()
    # Create list of month starts
    months = pd.date_range(start=start, end=end, freq='MS')
    shares = 0.0
    months_invested = 0
    for m in months:
        # find first trading day in month m for this index
        month_mask = (g['Date'].dt.year == m.year) & (g['Date'].dt.month == m.month)
        month_rows = g.loc[month_mask]
        if month_rows.empty:
            continue
        first_price = month_rows.sort_values('Date').iloc[0]['CloseUSD']
        if pd.isna(first_price) or first_price <= 0:
            continue
        shares += (monthly_amount / first_price)
        months_invested += 1
    if months_invested == 0:
        continue
    last_price = g.sort_values('Date').iloc[-1]['CloseUSD']
    final_value = shares * last_price
    total_invested = monthly_amount * months_invested
    return_factor = final_value / total_invested if total_invested != 0 else None
    results.append({
        'Index': idx,
        'Country': index_country.get(idx, 'Unknown'),
        'MonthsInvested': months_invested,
        'TotalInvestedUSD': round(total_invested, 2),
        'FinalValueUSD': round(final_value, 2),
        'ReturnFactor': round(return_factor, 4) if return_factor is not None else None,
        'LastDate': end.strftime('%Y-%m-%d')
    })

# Sort by ReturnFactor descending and take top 5
results_sorted = sorted(results, key=lambda x: x['ReturnFactor'] if x['ReturnFactor'] is not None else -999, reverse=True)
top5 = results_sorted[:5]

# Prepare output string
output = json.dumps(top5)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_uQF7MYyQfgPaL1QeoUIrKE9p': ['index_trade'], 'var_call_BDVZfOsHbp6IcQo3Awf1eUwY': ['index_info'], 'var_call_RHAxroMrJkp6tj5KbHnx480S': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_call_ZCWyZBs9aBuYiNvqJjLap6R6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_oHL9xSBTIFUquAhBzK7elqnV': 'file_storage/call_oHL9xSBTIFUquAhBzK7elqnV.json'}

exec(code, env_args)

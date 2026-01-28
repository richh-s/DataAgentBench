code = """import pandas as pd
import json
from datetime import datetime, timedelta

# Load the query result file path from storage variable
records_file = var_call_fejPpg6Kc3uBoA4SGJy38sR4
with open(records_file, 'r') as f:
    records = json.load(f)

# Create DataFrame
df = pd.DataFrame(records)
# Convert types
df['Date'] = pd.to_datetime(df['Date'])
# Convert CloseUSD to float (some values may be strings)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Filter from 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# Prepare list of months from 2000-01 to the latest date in the entire dataset
start_month = pd.Timestamp('2000-01-01')
end_month = df['Date'].max().replace(day=1)
all_month_starts = pd.date_range(start=start_month, end=end_month, freq='MS')

results = []

# Helper to get first trading day in a month for an index
for idx, grp in df.groupby('Index'):
    grp = grp.sort_values('Date')
    last_price = grp['CloseUSD'].iloc[-1]
    if pd.isna(last_price) or last_price <= 0:
        continue
    total_shares = 0.0
    months_invested = 0
    for month_start in all_month_starts:
        month_end = (month_start + pd.offsets.MonthEnd(0)).normalize()
        # find first trading day for this index in this month
        mdf = grp[(grp['Date'] >= month_start) & (grp['Date'] <= month_end)]
        if mdf.empty:
            continue
        purchase_price = mdf.sort_values('Date')['CloseUSD'].iloc[0]
        if pd.isna(purchase_price) or purchase_price <= 0:
            continue
        total_shares += 1.0 / purchase_price  # investing $1 each month
        months_invested += 1
    if months_invested == 0:
        continue
    total_invested = float(months_invested)
    final_value = total_shares * float(last_price)
    multiplier = final_value / total_invested
    results.append({'Index': idx, 'Months': months_invested, 'TotalInvestedUSD': total_invested,
                    'FinalValueUSD': final_value, 'ReturnMultiplier': multiplier})

# Sort by ReturnMultiplier desc and take top 10 for inspection
results = sorted(results, key=lambda x: x['ReturnMultiplier'], reverse=True)

# Map indices to countries (inferred manually)
country_map = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong (China)',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands',
    '399001.SZ': 'China'
}

top5 = results[:5]
# Attach country and format numbers
out = []
for r in top5:
    idx = r['Index']
    country = country_map.get(idx, 'Unknown')
    out.append({'Index': idx,
                'Country': country,
                'MonthsInvested': r['Months'],
                'TotalInvestedUSD': round(r['TotalInvestedUSD'], 2),
                'FinalValueUSD': round(r['FinalValueUSD'], 2),
                'ReturnMultiplier': round(r['ReturnMultiplier'], 4)})

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_wgNlcig1QXhoQl4EiCQcYQOK': ['index_trade'], 'var_call_WMCE0TzqnyFI3tS4NSFdhniV': ['index_info'], 'var_call_SwD1ie6ZflyXNLqHN2FYoxyf': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_fejPpg6Kc3uBoA4SGJy38sR4': 'file_storage/call_fejPpg6Kc3uBoA4SGJy38sR4.json'}

exec(code, env_args)

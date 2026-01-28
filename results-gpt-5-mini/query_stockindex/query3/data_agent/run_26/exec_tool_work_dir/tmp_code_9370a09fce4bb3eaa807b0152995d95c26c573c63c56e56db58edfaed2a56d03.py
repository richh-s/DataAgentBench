code = """import pandas as pd
import json

records_file = var_call_fejPpg6Kc3uBoA4SGJy38sR4
with open(records_file, 'r') as f:
    records = json.load(f)

# Create DataFrame
df = pd.DataFrame(records)
# Convert types robustly
# Some Date values might be in different formats; coerce errors
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# Drop rows with invalid dates
df = df.dropna(subset=['Date']).copy()
# Convert CloseUSD to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Filter from 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# Determine overall last date across all indices
if df.empty:
    results = []
else:
    start_month = pd.Timestamp('2000-01-01')
    # end_month = first day of latest month in dataset
    latest = df['Date'].max()
    end_month = pd.Timestamp(year=latest.year, month=latest.month, day=1)
    all_month_starts = pd.date_range(start=start_month, end=end_month, freq='MS')

    results = []
    for idx, grp in df.groupby('Index'):
        grp = grp.sort_values('Date')
        last_price = grp['CloseUSD'].iloc[-1]
        if pd.isna(last_price) or last_price <= 0:
            continue
        total_shares = 0.0
        months_invested = 0
        for month_start in all_month_starts:
            # month_end inclusive
            month_end = (month_start + pd.offsets.MonthEnd(0))
            mdf = grp[(grp['Date'] >= month_start) & (grp['Date'] <= month_end)]
            if mdf.empty:
                continue
            # first trading day in month
            purchase_price = mdf.sort_values('Date')['CloseUSD'].iloc[0]
            if pd.isna(purchase_price) or purchase_price <= 0:
                continue
            total_shares += 1.0 / float(purchase_price)
            months_invested += 1
        if months_invested == 0:
            continue
        total_invested = float(months_invested)
        final_value = total_shares * float(last_price)
        multiplier = final_value / total_invested
        results.append({'Index': idx, 'Months': months_invested, 'TotalInvestedUSD': total_invested,
                        'FinalValueUSD': final_value, 'ReturnMultiplier': multiplier})

    results = sorted(results, key=lambda x: x['ReturnMultiplier'], reverse=True)

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
    out = []
    for r in top5:
        idx = r['Index']
        country = country_map.get(idx, 'Unknown')
        out.append({'Index': idx,
                    'Country': country,
                    'MonthsInvested': int(r['Months']),
                    'TotalInvestedUSD': round(r['TotalInvestedUSD'], 2),
                    'FinalValueUSD': round(r['FinalValueUSD'], 2),
                    'ReturnMultiplier': round(r['ReturnMultiplier'], 4)})

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_wgNlcig1QXhoQl4EiCQcYQOK': ['index_trade'], 'var_call_WMCE0TzqnyFI3tS4NSFdhniV': ['index_info'], 'var_call_SwD1ie6ZflyXNLqHN2FYoxyf': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_fejPpg6Kc3uBoA4SGJy38sR4': 'file_storage/call_fejPpg6Kc3uBoA4SGJy38sR4.json'}

exec(code, env_args)

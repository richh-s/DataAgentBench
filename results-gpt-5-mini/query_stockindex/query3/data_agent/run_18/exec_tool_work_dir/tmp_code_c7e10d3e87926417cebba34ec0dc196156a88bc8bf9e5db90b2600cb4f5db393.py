code = """import pandas as pd
import json
from datetime import datetime

# Load the large query result from storage variable
data_path = var_call_OZt2fMKH7rQKYB6cMSlbfobK
with open(data_path, 'r') as f:
    records = json.load(f)

# Clean records: ensure CloseUSD numeric and Date parseable
cleaned = []
for r in records:
    try:
        r2 = r.copy()
        # handle CloseUSD that might be numeric strings
        r2['CloseUSD'] = float(r2['CloseUSD'])
        # ensure Date is in ISO format
        # Some dates appear as '2000-01-04 00:00:00' which is parseable
        r2['Date'] = r2['Date']
        cleaned.append(r2)
    except Exception:
        continue


# Create DataFrame
df = pd.DataFrame(cleaned)
# parse dates explicitly
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')

results = []

# Manual mapping from index symbol to country based on common knowledge and index_info table
index_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'TWII': 'Taiwan',
    'GSPTSE': 'Canada',
    'IXIC': 'United States',
    'NYA': 'United States',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'N100': 'Netherlands',
    'J203.JO': 'South Africa'
}

for idx, g in df.groupby('Index'):
    g = g.sort_values('Date')
    if g.empty:
        continue
    # Determine monthly first trading day contributions from Jan 2000
    start = pd.Timestamp('2000-01-01')
    end = g['Date'].max()
    months = pd.date_range(start=start, end=end, freq='MS')
    shares = 0.0
    contributions = 0
    for m in months:
        mask = (g['Date'].dt.year == m.year) & (g['Date'].dt.month == m.month)
        month_rows = g.loc[mask]
        if month_rows.empty:
            continue
        first_row = month_rows.iloc[0]
        price = float(first_row['CloseUSD'])
        if price <= 0:
            continue
        shares += 1.0 / price
        contributions += 1
    if contributions == 0:
        continue
    last_price = float(g.iloc[-1]['CloseUSD'])
    final_value = shares * last_price
    total_invested = contributions * 1.0
    return_ratio = final_value / total_invested
    return_pct = (final_value - total_invested) / total_invested * 100.0
    results.append({
        'Index': idx,
        'Country': index_country.get(idx, 'Unknown'),
        'Contributions': contributions,
        'TotalInvested': round(total_invested, 2),
        'FinalValue': round(final_value, 2),
        'ReturnRatio': round(return_ratio, 4),
        'ReturnPct': round(return_pct, 2),
        'StartDate': str(months[0].date()),
        'EndDate': str(end.date())
    })

results_sorted = sorted(results, key=lambda x: x['ReturnRatio'], reverse=True)
top5 = results_sorted[:5]

output = json.dumps(top5)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_v7BJ9tJ7hTTB6cWd0vc4hzO6': ['index_trade'], 'var_call_chlA51jku008O2mANxOScdNf': ['index_info'], 'var_call_auhpslBzkYLlafHkEDIwQYAP': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_OZt2fMKH7rQKYB6cMSlbfobK': 'file_storage/call_OZt2fMKH7rQKYB6cMSlbfobK.json', 'var_call_Cp0CQdmiIoi9mCVsZz5UaYpt': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

code = """import pandas as pd
import json
from datetime import datetime

# Load large query result from file path variable
data_path = var_call_dYTFhENsVrZTLYQNSV6jvmOa
with open(data_path, 'r') as f:
    records = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(records)
# parse dates
df['Date'] = pd.to_datetime(df['Date'])
# ensure CloseUSD numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

indices = df['Index'].unique().tolist()
results = []

# mapping for country inference for indices
country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)',
    'GSPTSE': 'Canada',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'NSEI': 'India',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands (Euronext)'
}

for idx in indices:
    dfi = df[df['Index']==idx].sort_values('Date').reset_index(drop=True)
    if dfi.empty:
        continue
    # investment months from 2000-01-01 to last date
    start = pd.Timestamp('2000-01-01')
    end = dfi['Date'].max()
    # generate month starts
    months = pd.date_range(start=start, end=end, freq='MS')
    units = 0.0
    months_invested = 0
    for m in months:
        # find first trading day on or after month start
        candidate = dfi[dfi['Date'] >= m]
        if candidate.empty:
            continue
        first_day = candidate.iloc[0]
        price = first_day['CloseUSD']
        if pd.isna(price) or price<=0:
            continue
        units += 1.0 / price
        months_invested += 1
    if months_invested == 0:
        continue
    total_invested = float(months_invested)
    last_price = float(dfi.iloc[-1]['CloseUSD'])
    final_value = units * last_price
    multiple = final_value / total_invested if total_invested>0 else None
    country = country_map.get(idx, 'Unknown')
    results.append({
        'Index': idx,
        'Country': country,
        'MonthsInvested': months_invested,
        'TotalInvestedUSD': round(total_invested,2),
        'FinalValueUSD': round(final_value,6),
        'Multiple': round(multiple,6)
    })

# sort by Multiple descending
results_sorted = sorted(results, key=lambda x: x['Multiple'], reverse=True)
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_An6RZXxLOwnquAunXXHCuFmF': ['index_trade'], 'var_call_MTvXWuXOahMmh1ZGjo6Ia51l': ['index_info'], 'var_call_bt5J2WYSj8vAmkq8Dp9y20wI': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_bkWZw1JO8lfOZ3EZhaoRRoR8': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_dYTFhENsVrZTLYQNSV6jvmOa': 'file_storage/call_dYTFhENsVrZTLYQNSV6jvmOa.json'}

exec(code, env_args)

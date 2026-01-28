code = """import pandas as pd
import json

data_path = var_call_2ELRoIafFP2TQ75FMECZc1ZV
with open(data_path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Parse CloseUSD robustly
df['CloseUSD'] = pd.to_numeric(df.get('CloseUSD', pd.Series()), errors='coerce')
# Parse Date robustly
df['Date'] = pd.to_datetime(df.get('Date', pd.Series()), errors='coerce', infer_datetime_format=True)
# Drop invalid rows
df = df.dropna(subset=['Date', 'CloseUSD']).copy()

# Sort
df = df.sort_values(['Index', 'Date'])
# Month period
df['Month'] = df['Date'].dt.to_period('M')

# For each Index and Month, take the first trading day's row
first_by_month = df.groupby(['Index', 'Month'], sort=False).apply(lambda g: g.loc[g['Date'].idxmin()])
first_by_month = first_by_month.reset_index(drop=True)

# Manual mapping index->country
index_country = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    'IXIC': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Pan-European',
    '399001.SZ': 'China'
}

results = []
for idx, group in first_by_month.groupby('Index'):
    group = group.sort_values('Month')
    months_invested = len(group)
    if months_invested == 0:
        continue
    # $1 invested each month -> shares = 1 / price
    shares = (1.0 / group['CloseUSD']).sum()
    # last available price from full df
    last_row = df[df['Index'] == idx].sort_values('Date').iloc[-1]
    last_price = float(last_row['CloseUSD'])
    final_value = shares * last_price
    total_invested = float(months_invested)
    return_ratio = final_value / total_invested if total_invested > 0 else None
    return_pct = (return_ratio - 1.0) * 100.0 if return_ratio is not None else None
    results.append({
        'Index': idx,
        'Country': index_country.get(idx, 'Unknown'),
        'MonthsInvested': int(months_invested),
        'TotalInvestedUSD': round(total_invested, 2),
        'FinalValueUSD': round(float(final_value), 2),
        'ReturnRatio': round(float(return_ratio), 4) if return_ratio is not None else None,
        'ReturnPercent': round(float(return_pct), 2) if return_pct is not None else None
    })

results_sorted = sorted(results, key=lambda x: x['ReturnRatio'] if x['ReturnRatio'] is not None else -9999, reverse=True)
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_AxRTjoYg0JMUNzQzQsIM6Lpp': ['index_info'], 'var_call_DYOveL0lS4TpewDtqxbDxZ3M': ['index_trade'], 'var_call_8fL9djr8KPhaK62S1pj7ro17': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_2ELRoIafFP2TQ75FMECZc1ZV': 'file_storage/call_2ELRoIafFP2TQ75FMECZc1ZV.json', 'var_call_qQxta7torHjSoSDM4E543xIF': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}]}

exec(code, env_args)

code = """import pandas as pd
import json

# Load the large query result from the provided storage key
path = var_call_CId0SG4v6L1ZeZMvjHKZH4B3
df = pd.read_json(path)

# Ensure correct dtypes
df['Date'] = pd.to_datetime(df['Date'])
# Some CloseUSD may be strings; convert
df['CloseUSD'] = df['CloseUSD'].astype(float)

# Create year-month period for monthly investments
df['ym'] = df['Date'].dt.to_period('M')

# For each Index and month, pick the first trading day's price
df_sorted = df.sort_values(['Index','Date'])
monthly = df_sorted.groupby(['Index','ym']).first().reset_index()[['Index','ym','Date','CloseUSD']]

results = []
# Mapping indices to countries (inferred)
country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'TWII': 'Taiwan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands'
}

for idx, group in monthly.groupby('Index'):
    group = group.sort_values('Date')
    months = len(group)
    if months == 0:
        continue
    # monthly contributions of $1
    # avoid division by zero prices
    group = group[group['CloseUSD'] > 0]
    if len(group) == 0:
        continue
    shares = (1.0 / group['CloseUSD']).sum()
    # last available price for the index
    last_price = df_sorted[df_sorted['Index'] == idx]['CloseUSD'].iloc[-1]
    final_value = shares * last_price
    total_invested = months * 1.0
    return_multiple = final_value / total_invested
    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'MonthsInvested': int(months),
        'TotalInvestedUSD': round(total_invested, 2),
        'FinalValueUSD': round(float(final_value), 2),
        'ReturnMultiple': round(float(return_multiple), 4)
    })

# Sort by return multiple descending and take top 5
results_sorted = sorted(results, key=lambda x: x['ReturnMultiple'], reverse=True)
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_lLPYuBekrI5mryrbcLPpdwCA': ['index_trade'], 'var_call_LK8uxaKNtPj1YZFRC2LAxIuM': ['index_info'], 'var_call_TbSr8xYNOGgSDvKX4jWc5FiR': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_FsxKi1FNztGj1uYegTpdLWXu': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_CId0SG4v6L1ZeZMvjHKZH4B3': 'file_storage/call_CId0SG4v6L1ZeZMvjHKZH4B3.json'}

exec(code, env_args)
